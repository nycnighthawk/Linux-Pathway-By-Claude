---
{"title": "Bake targets", "url": "https://docs.docker.com/build/bake/targets/", "retrieved": "2026-11-01", "license": "Apache-2.0"}
---

# Bake targets {#bake-targets pagefind-weight="10"}

------------------------------------------------------------------------

Table of contents

------------------------------------------------------------------------

A target in a Bake file represents a build invocation. It holds all the information you would normally pass to a `docker build` command using flags.

docker-bake.hcl

``` {.chroma tabindex="0"}
target "webapp" {
  dockerfile = "webapp.Dockerfile"
  tags = ["docker.io/username/webapp:latest"]
  context = "https://github.com/username/webapp"
}
```

To build a target with Bake, pass name of the target to the `bake` command.

``` {.chroma tabindex="0"}
$ docker buildx bake webapp
```

You can build multiple targets at once by passing multiple target names to the `bake` command.

``` {.chroma tabindex="0"}
$ docker buildx bake webapp api tests
```

## [Default target](#default-target) {#default-target .scroll-mt-20 .flex .items-center .gap-2}

If you don\'t specify a target when running `docker buildx bake`, Bake will build the target named `default`.

docker-bake.hcl

``` {.chroma tabindex="0"}
target "default" {
  dockerfile = "webapp.Dockerfile"
  tags = ["docker.io/username/webapp:latest"]
  context = "https://github.com/username/webapp"
}
```

To build this target, run `docker buildx bake` without any arguments:

``` {.chroma tabindex="0"}
$ docker buildx bake
```

## [Target properties](#target-properties) {#target-properties .scroll-mt-20 .flex .items-center .gap-2}

The properties you can set for a target closely resemble the CLI flags for `docker build`, with a few additional properties that are specific to Bake.

The `dockerfile` property specifies the path to the Dockerfile for a target. If you also set a `context`, the `dockerfile` path resolves relative to that context.

docker-bake.hcl

``` {.chroma tabindex="0"}
target "default" {
  context = "app"
  # resolves to app/src/www/Dockerfile
  dockerfile = "src/www/Dockerfile"
}
```

For all the properties you can set for a target, see the [Bake reference](/build/bake/reference#target).

## [Grouping targets](#grouping-targets) {#grouping-targets .scroll-mt-20 .flex .items-center .gap-2}

You can group targets together using the `group` block. This is useful when you want to build multiple targets at once.

docker-bake.hcl

``` {.chroma tabindex="0"}
group "all" {
  targets = ["webapp", "api", "tests"]
}

target "webapp" {
  dockerfile = "webapp.Dockerfile"
  tags = ["docker.io/username/webapp:latest"]
  context = "https://github.com/username/webapp"
}

target "api" {
  dockerfile = "api.Dockerfile"
  tags = ["docker.io/username/api:latest"]
  context = "https://github.com/username/api"
}

target "tests" {
  dockerfile = "tests.Dockerfile"
  contexts = {
    webapp = "target:webapp"
    api = "target:api"
  }
  output = ["type=local,dest=build/tests"]
  context = "."
}
```

To build all the targets in a group, pass the name of the group to the `bake` command.

``` {.chroma tabindex="0"}
$ docker buildx bake all
```

### [Run tests and lint checks](#run-tests-and-lint-checks) {#run-tests-and-lint-checks .scroll-mt-20 .flex .items-center .gap-2}

Bake targets can run checks without producing an image. For a Go project with a `go.mod` file, source code, and tests, define matching Dockerfile stages:

Dockerfile

``` {.chroma tabindex="0"}
FROM --platform=$BUILDPLATFORM golang:1.26 AS base
WORKDIR /src
COPY . .

FROM base AS test
RUN go test ./...

FROM base AS lint
RUN go vet ./...
```

Map each Bake target to its Dockerfile stage and group the checks:

docker-bake.hcl

``` {.chroma tabindex="0"}
group "validate" {
  targets = ["test", "lint"]
}

target "test" {
  target = "test"
  output = ["type=cacheonly"]
}

target "lint" {
  target = "lint"
  output = ["type=cacheonly"]
}
```

``` {.chroma tabindex="0"}
$ docker buildx bake validate
```

Both checks run concurrently. A failing check causes the command to fail. The `cacheonly` output keeps the build cache without exporting an image.

## [Export build artifacts](#export-build-artifacts) {#export-build-artifacts .scroll-mt-20 .flex .items-center .gap-2}

A target can export files, such as compiled binaries, to your local filesystem. For the Go project in the previous example, append these stages to the Dockerfile:

Dockerfile

``` {.chroma tabindex="0"}
FROM base AS build
ARG TARGETOS
ARG TARGETARCH
ARG BUILD_MODE=release
RUN if [ "$BUILD_MODE" = "debug" ]; then \
      CGO_ENABLED=0 GOOS=$TARGETOS GOARCH=$TARGETARCH go build -gcflags="all=-N -l" -o /out/app .; \
    else \
      CGO_ENABLED=0 GOOS=$TARGETOS GOARCH=$TARGETARCH go build -o /out/app .; \
    fi

FROM scratch AS export
COPY --from=build /out/ /
```

The `scratch` stage contains only the files to export. Add these Bake targets to save the binary locally or build it for multiple platforms:

docker-bake.hcl

``` {.chroma tabindex="0"}
target "bin" {
  target = "export"
  platforms = ["local"]
  output = ["type=local,dest=build/bin"]
}

target "bin-cross" {
  inherits = ["bin"]
  platforms = ["linux/amd64", "linux/arm64"]
}
```

``` {.chroma tabindex="0"}
$ docker buildx bake bin
$ docker buildx bake bin-cross
```

The `bin` target builds for the client\'s platform and writes `build/bin/app`. The `bin-cross` target writes separate `build/bin/linux_amd64/app` and `build/bin/linux_arm64/app` files. See [Inheritance](https://docs.docker.com/build/bake/inheritance/) and [Local and tar exporters](https://docs.docker.com/build/exporters/local-tar/) for reuse and output options.

The base stage uses `BUILDPLATFORM` to run the Go compiler on the builder\'s native platform. `TARGETOS` and `TARGETARCH` select the output platform, so this example cross-compiles without emulation. For other toolchains, see [Multi-platform build strategies](https://docs.docker.com/build/building/multi-platform/#strategies).

## [Pattern matching for targets and groups](#pattern-matching-for-targets-and-groups) {#pattern-matching-for-targets-and-groups .scroll-mt-20 .flex .items-center .gap-2}

Bake supports shell-style wildcard patterns when specifying target or grouped targets. This makes it easier to build multiple targets without listing each one explicitly.

Supported patterns:

-   `*` matches any sequence of characters
-   `?` matches any single character
-   `[abc]` matches any character in brackets

> Note
>
> Always wrap wildcard patterns in quotes. Without quotes, your shell will expand the wildcard to match files in the current directory, causing errors.

Examples:

``` {.chroma tabindex="0"}
# Match all targets starting with 'foo-'
$ docker buildx bake "foo-*"

# Match all targets
$ docker buildx bake "*"

# Matches: foo-baz, foo-caz, foo-daz, etc.
$ docker buildx bake "foo-?az"

# Matches: foo-bar, boo-bar
$ docker buildx bake "[fb]oo-bar"

# Matches: mtx-a-b-d, mtx-a-b-e, mtx-a-b-f
$ docker buildx bake "mtx-a-b-*"
```

You can also combine multiple patterns:

``` {.chroma tabindex="0"}
$ docker buildx bake "foo*" "tests"
```

## [Additional resources](#additional-resources) {#additional-resources .scroll-mt-20 .flex .items-center .gap-2}

Refer to the following pages to learn more about Bake\'s features:

-   Learn how to use [variables](https://docs.docker.com/build/bake/variables/) in Bake to make your build configuration more flexible.
-   Learn how you can use matrices to build multiple images with different configurations in [Matrices](https://docs.docker.com/build/bake/matrices/).
-   Head to the [Bake file reference](/build/bake/reference/) to learn about all the properties you can set in a Bake file, and its syntax.
