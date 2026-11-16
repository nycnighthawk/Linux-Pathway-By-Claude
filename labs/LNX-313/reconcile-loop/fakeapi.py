# SPDX-License-Identifier: MIT
"""A tiny in-memory stand-in for the Kubernetes API, just enough to test a reconciler."""
import copy, itertools

_uid = itertools.count(1)


class FakeAPI:
    def __init__(self):
        self.objects = {}      # (kind, ns, name) -> dict
        self.writes = 0        # creates, updates and deletes performed through the API
        self.external = set()  # an external system the operator manages (uids registered)

    # reads return copies so callers cannot mutate the store by accident
    def get(self, kind, ns, name):
        o = self.objects.get((kind, ns, name))
        return copy.deepcopy(o) if o else None

    def create(self, obj):
        key = (obj["kind"], obj["metadata"]["namespace"], obj["metadata"]["name"])
        if key in self.objects:
            raise KeyError("already exists: %s" % (key,))
        obj = copy.deepcopy(obj)
        obj["metadata"].setdefault("uid", "uid-%d" % next(_uid))
        obj["metadata"].setdefault("generation", 1)
        self.objects[key] = obj
        self.writes += 1
        return copy.deepcopy(obj)

    def update(self, obj):
        """Replace metadata and spec; the status is ignored (use update_status). A spec change bumps generation."""
        key = (obj["kind"], obj["metadata"]["namespace"], obj["metadata"]["name"])
        cur = self.objects[key]
        new = copy.deepcopy(obj)
        new["status"] = cur.get("status", {})
        if new.get("spec") != cur.get("spec"):
            new["metadata"]["generation"] = cur["metadata"].get("generation", 1) + 1
        else:
            new["metadata"]["generation"] = cur["metadata"].get("generation", 1)
        new["metadata"]["uid"] = cur["metadata"]["uid"]
        if "deletionTimestamp" in cur["metadata"]:
            new["metadata"]["deletionTimestamp"] = cur["metadata"]["deletionTimestamp"]
        self.objects[key] = new
        self.writes += 1
        if new["metadata"].get("deletionTimestamp") and not new["metadata"].get("finalizers"):
            self._remove(key)
        return copy.deepcopy(new)

    def update_status(self, obj):
        key = (obj["kind"], obj["metadata"]["namespace"], obj["metadata"]["name"])
        self.objects[key]["status"] = copy.deepcopy(obj.get("status", {}))
        self.writes += 1

    def delete(self, kind, ns, name):
        key = (kind, ns, name)
        o = self.objects.get(key)
        if not o:
            return
        self.writes += 1
        if o["metadata"].get("finalizers"):
            o["metadata"]["deletionTimestamp"] = "now"   # blocked until the finalizers are removed
        else:
            self._remove(key)

    def _remove(self, key):
        uid = self.objects[key]["metadata"]["uid"]
        del self.objects[key]
        for k, v in list(self.objects.items()):          # garbage collection by owner reference
            if any(r.get("uid") == uid for r in v["metadata"].get("ownerReferences", [])):
                self._remove(k)

    def list_owned(self, kind, ns, owner_uid):
        return [copy.deepcopy(v) for (k, n, _), v in self.objects.items()
                if k == kind and n == ns and any(r.get("uid") == owner_uid for r in v["metadata"].get("ownerReferences", []))]
