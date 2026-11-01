---
{"title": "None network driver", "url": "https://docs.docker.com/engine/network/drivers/none/", "retrieved": "2026-11-01", "license": "Apache-2.0"}
---

# None network driver {#none-network-driver pagefind-weight="10"}

------------------------------------------------------------------------

Table of contents

------------------------------------------------------------------------

If you want to completely isolate the networking stack of a container, you can use the `--network none` flag when starting the container. Within the container, only the loopback device is created.

The following example shows the output of `ip link show` in an `alpine` container using the `none` network driver.

``` {.chroma tabindex="0"}
$ docker run --rm --network none alpine:latest ip link show
1: lo: <LOOPBACK,UP,LOWER_UP> mtu 65536 qdisc noqueue state UNKNOWN qlen 1000
    link/loopback 00:00:00:00:00:00 brd 00:00:00:00:00:00
```

No IPv6 loopback address is configured for containers using the `none` driver.

``` {.chroma tabindex="0"}
$ docker run --rm --network none --name no-net-alpine alpine:latest ip addr show
1: lo: <LOOPBACK,UP,LOWER_UP> mtu 65536 qdisc noqueue state UNKNOWN qlen 1000
    link/loopback 00:00:00:00:00:00 brd 00:00:00:00:00:00
    inet 127.0.0.1/8 scope host lo
       valid_lft forever preferred_lft forever
```

## [Next steps](#next-steps) {#next-steps .scroll-mt-20 .flex .items-center .gap-2}

-   Learn about [networking from the container\'s point of view](https://docs.docker.com/engine/network/)
-   Learn about [host networking](https://docs.docker.com/engine/network/drivers/host/)
-   Learn about [bridge networks](https://docs.docker.com/engine/network/drivers/bridge/)
-   Learn about [overlay networks](https://docs.docker.com/engine/network/drivers/overlay/)
-   Learn about [Macvlan networks](https://docs.docker.com/engine/network/drivers/macvlan/)
