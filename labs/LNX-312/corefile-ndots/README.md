# Lab: a Corefile and the ndots arithmetic

Two files in `$LAB_DIR`, created by `setup`:

1. `Corefile`: the main server block on `.:53` needs `errors`, `health`, `ready`, a `kubernetes cluster.local in-addr.arpa ip6.arpa`
   plugin with `pods insecure` and `fallthrough in-addr.arpa ip6.arpa`, `prometheus :9153`, `forward . /etc/resolv.conf`, `cache 30`, `loop`, `reload`.
   Add a second server block for `corp.example.com:53` that forwards to `10.1.1.53` and `10.1.1.54`, with `cache 30` and `errors`.
2. `answers.yaml`: the number of DNS queries (A only) a successful lookup of `api.example.com` costs for a Pod whose search list is
   `shop.svc.cluster.local svc.cluster.local cluster.local`, in three cases: `ndots5` (default), `fqdn` (written `api.example.com.`) and `ndots2`.

```bash
mkdir -p ~/lab && cd ~/lab && LAB_DIR=$PWD /path/to/repo/labs/LNX-312/corefile-ndots/setup
LAB_DIR=$PWD /path/to/repo/labs/LNX-312/corefile-ndots/check
```

Needs `python3` and `PyYAML`. Reading: [the lesson](lesson:LNX-312-T08), then [the quiz](quiz:LNX-312-T08).
