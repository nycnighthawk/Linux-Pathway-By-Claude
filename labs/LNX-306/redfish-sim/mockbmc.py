#!/usr/bin/env python3
# SPDX-License-Identifier: MIT
"""A tiny mock Redfish BMC for the lab. Basic auth, one system, state in state.json."""
import base64, json, os, sys, threading, time
from http.server import BaseHTTPRequestHandler, HTTPServer

USER, PASSWORD = sys.argv[1], sys.argv[2]
STATE = {"PowerState": "On", "Boot": {"BootSourceOverrideTarget": "None", "BootSourceOverrideEnabled": "Disabled"}, "resets": []}
TARGETS = ["None", "Pxe", "Hdd", "Cd", "Diags"]
ENABLED = ["Disabled", "Once", "Continuous"]
RESETS = ["On", "ForceOff", "GracefulShutdown", "ForceRestart", "GracefulRestart", "PushPowerButton"]


def save():
    with open("state.json.tmp", "w") as f:
        json.dump(STATE, f)
    os.replace("state.json.tmp", "state.json")


def system():
    return {"@odata.id": "/redfish/v1/Systems/1", "Id": "1", "Name": "lab-node", "PowerState": STATE["PowerState"],
            "Boot": dict(STATE["Boot"], **{"BootSourceOverrideTarget@Redfish.AllowableValues": TARGETS}),
            "Actions": {"#ComputerSystem.Reset": {"target": "/redfish/v1/Systems/1/Actions/ComputerSystem.Reset",
                                                  "ResetType@Redfish.AllowableValues": RESETS}}}


class H(BaseHTTPRequestHandler):
    def log_message(self, *a):
        pass

    def send(self, code, body=None):
        data = json.dumps(body).encode() if body is not None else b""
        self.send_response(code)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(data)))
        if code == 401:
            self.send_header("WWW-Authenticate", 'Basic realm="redfish"')
        self.end_headers()
        self.wfile.write(data)

    def authed(self):
        h = self.headers.get("Authorization", "")
        if h.startswith("Basic "):
            try:
                return base64.b64decode(h[6:]).decode() == USER + ":" + PASSWORD
            except Exception:
                return False
        return False

    def body(self):
        n = int(self.headers.get("Content-Length") or 0)
        try:
            return json.loads(self.rfile.read(n) or b"{}")
        except ValueError:
            return None

    def do_GET(self):
        p = self.path.rstrip("/")
        if p == "/redfish/v1":  # the service root needs no login, as in the standard
            return self.send(200, {"@odata.id": "/redfish/v1/", "RedfishVersion": "1.15.0", "Systems": {"@odata.id": "/redfish/v1/Systems"}})
        if not self.authed():
            return self.send(401, {"error": "authentication required"})
        if p == "/redfish/v1/Systems":
            return self.send(200, {"Members": [{"@odata.id": "/redfish/v1/Systems/1"}], "Members@odata.count": 1})
        if p == "/redfish/v1/Systems/1":
            return self.send(200, system())
        self.send(404, {"error": "not found"})

    def do_PATCH(self):
        if not self.authed():
            return self.send(401, {"error": "authentication required"})
        if self.path.rstrip("/") != "/redfish/v1/Systems/1":
            return self.send(404, {"error": "not found"})
        b = self.body()
        boot = (b or {}).get("Boot")
        if not isinstance(boot, dict):
            return self.send(400, {"error": "send a JSON body with a Boot object"})
        t, e = boot.get("BootSourceOverrideTarget"), boot.get("BootSourceOverrideEnabled")
        if (t is not None and t not in TARGETS) or (e is not None and e not in ENABLED):
            return self.send(400, {"error": "value not in the allowable list"})
        if t is not None:
            STATE["Boot"]["BootSourceOverrideTarget"] = t
        if e is not None:
            STATE["Boot"]["BootSourceOverrideEnabled"] = e
        save()
        self.send(200, system())

    def do_POST(self):
        if not self.authed():
            return self.send(401, {"error": "authentication required"})
        if self.path.rstrip("/") != "/redfish/v1/Systems/1/Actions/ComputerSystem.Reset":
            return self.send(404, {"error": "not found"})
        b = self.body() or {}
        rt = b.get("ResetType")
        if rt not in RESETS:
            return self.send(400, {"error": "ResetType must be one of the allowable values"})
        if rt == "ForceOff" or rt == "GracefulShutdown":
            STATE["PowerState"] = "Off"
        else:
            STATE["PowerState"] = "On"
        STATE["resets"].append(rt)
        save()
        self.send(204)


def main():
    srv = HTTPServer(("127.0.0.1", 0), H)
    open("bmc.port", "w").write(str(srv.server_port))
    save()
    threading.Timer(600, lambda: os._exit(0)).start()
    srv.serve_forever()


main()
