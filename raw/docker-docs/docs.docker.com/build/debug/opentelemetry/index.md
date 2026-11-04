---
{"title": "OpenTelemetry support", "url": "https://docs.docker.com/build/debug/opentelemetry/", "retrieved": "2026-11-01", "license": "Apache-2.0"}
---

# OpenTelemetry support {#opentelemetry-support pagefind-weight="10"}

------------------------------------------------------------------------

------------------------------------------------------------------------

Both Buildx and BuildKit support [OpenTelemetry](https://opentelemetry.io/).

To capture the trace to [Jaeger](https://github.com/jaegertracing/jaeger), set `JAEGER_TRACE` environment variable to the collection address using a `driver-opt`.

First create a Jaeger container:

``` {.chroma tabindex="0"}
$ docker run -d --name jaeger -p "6831:6831/udp" -p "16686:16686" --restart unless-stopped jaegertracing/all-in-one
```

Then [create a `docker-container` builder](https://docs.docker.com/build/builders/drivers/docker-container/) that will use the Jaeger instance via the `JAEGER_TRACE` environment variable:

``` {.chroma tabindex="0"}
$ docker buildx create --use \
  --name mybuilder \
  --driver docker-container \
  --driver-opt "network=host" \
  --driver-opt "env.JAEGER_TRACE=localhost:6831"
```

Boot and [inspect `mybuilder`](/reference/cli/docker/buildx/inspect/):

``` {.chroma tabindex="0"}
$ docker buildx inspect --bootstrap
```

Buildx commands should be traced at `http://127.0.0.1:16686/`:

![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGZpbGw9ImN1cnJlbnRDb2xvciIgYXJpYS1oaWRkZW49InRydWUiIGRhdGEtc2xvdD0iaWNvbiI+PHBhdGggZmlsbC1ydWxlPSJldmVub2RkIiBkPSJNNS40NyA1LjQ3YS43NS43NS4wIDAxMS4wNi4wTDEyIDEwLjk0bDUuNDctNS40N2EuNzUuNzUuMCAxMTEuMDYgMS4wNkwxMy4wNiAxMmw1LjQ3IDUuNDdhLjc1Ljc1LjAgMTEtMS4wNiAxLjA2TDEyIDEzLjA2bC01LjQ3IDUuNDdhLjc1Ljc1LjAgMDEtMS4wNi0xLjA2TDEwLjk0IDEyIDUuNDcgNi41M2EuNzUuNzUuMCAwMTAtMS4wNnoiIGNsaXAtcnVsZT0iZXZlbm9kZCI+PC9wYXRoPjwvc3ZnPg==)

![OpenTelemetry Buildx Bake](https://docs.docker.com/build/images/opentelemetry.png)
