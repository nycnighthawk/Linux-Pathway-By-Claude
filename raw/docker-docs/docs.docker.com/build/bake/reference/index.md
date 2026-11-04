---
{"title": "Bake file reference", "url": "https://docs.docker.com/build/bake/reference", "retrieved": "2026-11-01", "license": "Apache-2.0"}
---

# Bake file reference {#bake-file-reference pagefind-weight="10"}

------------------------------------------------------------------------

Table of contents

------------------------------------------------------------------------

The Bake file is a file for defining workflows that you run using `docker buildx bake`.

## [File format](#file-format) {#file-format .scroll-mt-20 .flex .items-center .gap-2}

You can define your Bake file in the following file formats:

-   HashiCorp Configuration Language (HCL)
-   JSON
-   YAML (Compose file)

By default, Bake uses the following lookup order to find the configuration file:

1.  `compose.yaml`
2.  `compose.yml`
3.  `docker-compose.yml`
4.  `docker-compose.yaml`
5.  `docker-bake.json`
6.  `docker-bake.hcl`
7.  `docker-bake.override.json`
8.  `docker-bake.override.hcl`

You can specify the file location explicitly using the `--file` flag:

``` {.chroma tabindex="0"}
$ docker buildx bake --file ../docker/bake.hcl --print
```

If you don\'t specify a file explicitly, Bake searches for the file in the current working directory. If more than one Bake file is found, all files are merged into a single definition. Files are merged according to the lookup order. That means that if your project contains both a `compose.yaml` file and a `docker-bake.hcl` file, Bake loads the `compose.yaml` file first, and then the `docker-bake.hcl` file.

If merged files contain duplicate attribute definitions, those definitions are either merged or overridden by the last occurrence, depending on the attribute. The following attributes are overridden by the last occurrence:

-   `target.cache-to`
-   `target.dockerfile-inline`
-   `target.dockerfile`
-   `target.output`
-   `target.platforms`
-   `target.pull`
-   `target.tags`
-   `target.target`

For example, if `compose.yaml` and `docker-bake.hcl` both define the `tags` attribute, the `docker-bake.hcl` is used.

``` {.chroma tabindex="0"}
$ cat compose.yaml
services:
  webapp:
    build:
      context: .
      tags:
        - bar
$ cat docker-bake.hcl
target "webapp" {
  tags = ["foo"]
}
$ docker buildx bake --print webapp
{
  "group": {
    "default": {
      "targets": [
        "webapp"
      ]
    }
  },
  "target": {
    "webapp": {
      "context": ".",
      "dockerfile": "Dockerfile",
      "tags": [
        "foo"
      ]
    }
  }
}
```

All other attributes are merged. For example, if `compose.yaml` and `docker-bake.hcl` both define unique entries for the `labels` attribute, all entries are included. Duplicate entries for the same label are overridden.

``` {.chroma tabindex="0"}
$ cat compose.yaml
services:
  webapp:
    build:
      context: .
      labels: 
        com.example.foo: "foo"
        com.example.name: "Alice"
$ cat docker-bake.hcl
target "webapp" {
  labels = {
    "com.example.bar" = "bar"
    "com.example.name" = "Bob"
  }
}
$ docker buildx bake --print webapp
{
  "group": {
    "default": {
      "targets": [
        "webapp"
      ]
    }
  },
  "target": {
    "webapp": {
      "context": ".",
      "dockerfile": "Dockerfile",
      "labels": {
        "com.example.foo": "foo",
        "com.example.bar": "bar",
        "com.example.name": "Bob"
      }
    }
  }
}
```

## [Syntax](#syntax) {#syntax .scroll-mt-20 .flex .items-center .gap-2}

The Bake file supports the following property types:

-   `target`: build targets
-   `group`: collections of build targets
-   `variable`: build arguments and variables
-   `function`: custom Bake functions

You define properties as hierarchical blocks in the Bake file. You can assign one or more attributes to a property.

The following snippet shows a JSON representation of a simple Bake file. This Bake file defines three properties: a variable, a group, and a target.

``` {.chroma tabindex="0"}
{
  "variable": {
    "TAG": {
      "default": "latest"
    }
  },
  "group": {
    "default": {
      "targets": ["webapp"]
    }
  },
  "target": {
    "webapp": {
      "dockerfile": "Dockerfile",
      "tags": ["docker.io/username/webapp:${TAG}"]
    }
  }
}
```

In the JSON representation of a Bake file, properties are objects, and attributes are values assigned to those objects.

The following example shows the same Bake file in the HCL format:

``` {.chroma tabindex="0"}
variable "TAG" {
  default = "latest"
}

group "default" {
  targets = ["webapp"]
}

target "webapp" {
  dockerfile = "Dockerfile"
  tags = ["docker.io/username/webapp:${TAG}"]
}
```

HCL is the preferred format for Bake files. Aside from syntactic differences, HCL lets you use features that the JSON and YAML formats don\'t support.

The examples in this document use the HCL format.

## [Target](#target) {#target .scroll-mt-20 .flex .items-center .gap-2}

A target reflects a single `docker build` invocation. Consider the following build command:

``` {.chroma tabindex="0"}
$ docker build \
  --file=Dockerfile.webapp \
  --tag=docker.io/username/webapp:latest \
  https://github.com/username/webapp
```

You can express this command in a Bake file as follows:

``` {.chroma tabindex="0"}
target "webapp" {
  dockerfile = "Dockerfile.webapp"
  tags = ["docker.io/username/webapp:latest"]
  context = "https://github.com/username/webapp"
}
```

The following table shows the complete list of attributes that you can assign to a target:

  Name                                              Type      Description
  ------------------------------------------------- --------- ----------------------------------------------------------------------
  [`args`](#targetargs)                             Map       Build arguments
  [`annotations`](#targetannotations)               List      Exporter annotations
  [`attest`](#targetattest)                         List      Build attestations
  [`cache-from`](#targetcache-from)                 List      External cache sources
  [`cache-to`](#targetcache-to)                     List      External cache destinations
  [`call`](#targetcall)                             String    Specify the frontend method to call for the target.
  [`context`](#targetcontext)                       String    Set of files located in the specified path or URL
  [`contexts`](#targetcontexts)                     Map       Additional build contexts
  [`description`](#targetdescription)               String    Description of a target
  [`dockerfile-inline`](#targetdockerfile-inline)   String    Inline Dockerfile string
  [`dockerfile`](#targetdockerfile)                 String    Dockerfile location
  [`entitlements`](#targetentitlements)             List      Permissions that the build process requires to run
  [`extra-hosts`](#targetextra-hosts)               List      Custom host-to-IP mapping
  [`inherits`](#targetinherits)                     List      Inherit attributes from other targets
  [`labels`](#targetlabels)                         Map       Metadata for images
  [`matrix`](#targetmatrix)                         Map       Define a set of variables that forks a target into multiple targets.
  [`name`](#targetname)                             String    Override the target name when using a matrix.
  [`no-cache-filter`](#targetno-cache-filter)       List      Disable build cache for specific stages
  [`no-cache`](#targetno-cache)                     Boolean   Disable build cache completely
  [`output`](#targetoutput)                         List      Output destinations
  [`policy`](#targetpolicy)                         List      Policies to validate build sources and metadata
  [`platforms`](#targetplatforms)                   List      Target platforms
  [`pull`](#targetpull)                             Boolean   Always pull images
  [`resources`](#targetresources)                   Map       Resource limits for build containers
  [`secret`](#targetsecret)                         List      Secrets to expose to the build
  [`shm-size`](#targetshm-size)                     List      Size of `/dev/shm`
  [`ssh`](#targetssh)                               List      SSH agent sockets or keys to expose to the build
  [`tags`](#targettags)                             List      Image names and tags
  [`target`](#targettarget)                         String    Target build stage
  [`ulimits`](#targetulimits)                       List      Ulimit options

### [`target.args`](#targetargs) {#targetargs .scroll-mt-20 .flex .items-center .gap-2}

Use the `args` attribute to define build arguments for the target. This has the same effect as passing a [`--build-arg`](https://docs.docker.com/reference/cli/docker/image/build/#build-arg) flag to the build command.

``` {.chroma tabindex="0"}
target "default" {
  args = {
    VERSION = "0.0.0+unknown"
  }
}
```

You can set `args` attributes to use `null` values. Doing so forces the `target` to use the `ARG` value specified in the Dockerfile.

``` {.chroma tabindex="0"}
variable "GO_VERSION" {
  default = "1.20.3"
}

target "webapp" {
  dockerfile = "webapp.Dockerfile"
  tags = ["docker.io/username/webapp"]
}

target "db" {
  args = {
    GO_VERSION = null
  }
  dockerfile = "db.Dockerfile"
  tags = ["docker.io/username/db"]
}
```

### [`target.annotations`](#targetannotations) {#targetannotations .scroll-mt-20 .flex .items-center .gap-2}

The `annotations` attribute lets you add annotations to images built with bake. The key takes a list of annotations, in the format of `KEY=VALUE`.

``` {.chroma tabindex="0"}
target "default" {
  output = [{ type = "image", name = "foo" }]
  annotations = ["org.opencontainers.image.authors=dvdksn"]
}
```

By default, the annotation is added to image manifests. You can configure the level of the annotations by adding a prefix to the annotation, containing a comma-separated list of all the levels that you want to annotate. The following example adds annotations to both the image index and manifests.

``` {.chroma tabindex="0"}
target "default" {
  output = [
    {
      type = "image"
      name = "foo"
    }
  ]
  annotations = ["index,manifest:org.opencontainers.image.authors=dvdksn"]
}
```

Read about the supported levels in [Specifying annotation levels](https://docs.docker.com/build/building/annotations/#specifying-annotation-levels).

### [`target.attest`](#targetattest) {#targetattest .scroll-mt-20 .flex .items-center .gap-2}

The `attest` attribute lets you apply [build attestations](https://docs.docker.com/build/attestations/) to the target. This attribute accepts the long-form CSV version of attestation parameters.

``` {.chroma tabindex="0"}
target "default" {
  attest = [
    {
      type = "provenance"
      mode = "max"
    },
    {
      type = "sbom"
    }
  ]
}
```

### [`target.cache-from`](#targetcache-from) {#targetcache-from .scroll-mt-20 .flex .items-center .gap-2}

Build cache sources. The builder imports cache from the locations you specify. It uses the [Buildx cache storage backends](https://docs.docker.com/build/cache/backends/), and it works the same way as the [`--cache-from`](https://docs.docker.com/reference/cli/docker/buildx/build/#cache-from) flag. This takes a list value, so you can specify multiple cache sources.

``` {.chroma tabindex="0"}
target "app" {
  cache-from = [
    {
      type = "s3"
      region = "eu-west-1"
      bucket = "mybucket"
    },
    {
      type = "registry"
      ref = "user/repo:cache"
    }
  ]
}
```

### [`target.cache-to`](#targetcache-to) {#targetcache-to .scroll-mt-20 .flex .items-center .gap-2}

Build cache export destinations. The builder exports its build cache to the locations you specify. It uses the [Buildx cache storage backends](https://docs.docker.com/build/cache/backends/), and it works the same way as the [`--cache-to` flag](https://docs.docker.com/reference/cli/docker/buildx/build/#cache-to). This takes a list value, so you can specify multiple cache export targets.

``` {.chroma tabindex="0"}
target "app" {
  cache-to = [
    {
      type = "s3"
      region = "eu-west-1"
      bucket = "mybucket"
    },
    {
      type = "inline"
    }
  ]
}
```

### [`target.call`](#targetcall) {#targetcall .scroll-mt-20 .flex .items-center .gap-2}

Specifies the frontend method to use. Frontend methods let you, for example, execute build checks only, instead of running a build. This is the same as the `--call` flag.

``` {.chroma tabindex="0"}
target "app" {
  call = "check"
}
```

Supported values are:

-   `build` builds the target (default)
-   `check`: evaluates [build checks](https://docs.docker.com/build/checks/) for the target
-   `outline`: displays the target\'s build arguments and their default values if available
-   `targets`: lists all Bake targets in the loaded definition, along with its [description](#targetdescription).

For more information about frontend methods, refer to the CLI reference for [`docker buildx build --call`](https://docs.docker.com/reference/cli/docker/buildx/build/#call).

### [`target.context`](#targetcontext) {#targetcontext .scroll-mt-20 .flex .items-center .gap-2}

Specifies the location of the build context to use for this target. Accepts a URL or a directory path. This is the same as the [build context](https://docs.docker.com/reference/cli/docker/buildx/build/#build-context) positional argument that you pass to the build command.

``` {.chroma tabindex="0"}
target "app" {
  context = "./src/www"
}
```

This resolves to the current working directory (`"."`) by default. Set `BUILDX_BAKE_FILE_RELATIVE_PATHS=1` to resolve local directory paths in `target.context` and `target.contexts` relative to the Bake file that defines each path. Compose files use the first Compose file directory as the base, which matches Compose project directory semantics. Use `cwd://` for paths that should remain relative to the current working directory when this opt-in is enabled.

``` {.chroma tabindex="0"}
$ docker buildx bake --print -f - <<< 'target "default" {}'
[+] Building 0.0s (0/0)
{
  "target": {
    "default": {
      "context": ".",
      "dockerfile": "Dockerfile"
    }
  }
}
```

### [`target.contexts`](#targetcontexts) {#targetcontexts .scroll-mt-20 .flex .items-center .gap-2}

Additional build contexts. This is the same as the [`--build-context` flag](https://docs.docker.com/reference/cli/docker/buildx/build/#build-context). This attribute takes a map, where keys result in named contexts that you can reference in your builds.

You can specify different types of contexts, such local directories, Git URLs, and even other Bake targets. Bake automatically determines the type of a context based on the pattern of the context value.

  Context type      Example
  ----------------- -------------------------------------------
  Container image   `docker-image://alpine@sha256:0123456789`
  Git URL           `https://github.com/user/proj.git`
  HTTP URL          `https://example.com/files`
  Local directory   `../path/to/src`
  Bake target       `target:base`

#### [Pin an image version](#pin-an-image-version) {#pin-an-image-version .scroll-mt-20 .flex .items-center .gap-2}

``` {.chroma tabindex="0"}
# docker-bake.hcl
target "app" {
  contexts = {
    alpine = "docker-image://alpine:3.13"
  }
}
```

``` {.chroma tabindex="0"}
# Dockerfile
FROM alpine
RUN echo "Hello world"
```

#### [Use a local directory](#use-a-local-directory) {#use-a-local-directory .scroll-mt-20 .flex .items-center .gap-2}

``` {.chroma tabindex="0"}
# docker-bake.hcl
target "app" {
  contexts = {
    src = "../path/to/source"
  }
}
```

``` {.chroma tabindex="0"}
# Dockerfile
FROM scratch AS src
FROM golang
COPY --from=src . .
```

#### [Use another target as base](#use-another-target-as-base) {#use-another-target-as-base .scroll-mt-20 .flex .items-center .gap-2}

> Note
>
> You should prefer to use regular multi-stage builds over this option. You can Use this feature when you have multiple Dockerfiles that can\'t be easily merged into one.

``` {.chroma tabindex="0"}
# docker-bake.hcl
target "base" {
  dockerfile = "baseapp.Dockerfile"
}

target "app" {
  contexts = {
    baseapp = "target:base"
  }
}
```

``` {.chroma tabindex="0"}
# Dockerfile
FROM baseapp
RUN echo "Hello world"
```

### [`target.description`](#targetdescription) {#targetdescription .scroll-mt-20 .flex .items-center .gap-2}

Defines a human-readable description for the target, clarifying its purpose or functionality.

``` {.chroma tabindex="0"}
target "lint" {
  description = "Runs golangci-lint to detect style errors"
  args = {
    GOLANGCI_LINT_VERSION = null
  }
  dockerfile = "lint.Dockerfile"
}
```

This attribute is useful when combined with the `docker buildx bake --list=targets` option, providing a more informative output when listing the available build targets in a Bake file.

### [`target.dockerfile-inline`](#targetdockerfile-inline) {#targetdockerfile-inline .scroll-mt-20 .flex .items-center .gap-2}

Uses the string value as an inline Dockerfile for the build target.

``` {.chroma tabindex="0"}
target "default" {
  dockerfile-inline = "FROM alpine\nENTRYPOINT [\"echo\", \"hello\"]"
}
```

The `dockerfile-inline` takes precedence over the `dockerfile` attribute. If you specify both, Bake uses the inline version.

### [`target.dockerfile`](#targetdockerfile) {#targetdockerfile .scroll-mt-20 .flex .items-center .gap-2}

Name of the Dockerfile to use for the build. This is the same as the [`--file` flag](https://docs.docker.com/reference/cli/docker/image/build/#file) for the `docker build` command.

``` {.chroma tabindex="0"}
target "default" {
  dockerfile = "./src/www/Dockerfile"
}
```

Resolves to `"Dockerfile"` by default.

``` {.chroma tabindex="0"}
$ docker buildx bake --print -f - <<< 'target "default" {}'
[+] Building 0.0s (0/0)
{
  "target": {
    "default": {
      "context": ".",
      "dockerfile": "Dockerfile"
    }
  }
}
```

### [`target.entitlements`](#targetentitlements) {#targetentitlements .scroll-mt-20 .flex .items-center .gap-2}

Entitlements are permissions that the build process requires to run.

Currently supported entitlements are:

-   `network.host`: Allows the build to use commands that access the host network. In Dockerfile, use [`RUN --network=host`](https://docs.docker.com/reference/dockerfile/#run---networkhost) to run a command with host network enabled.

-   `security.insecure`: Allows the build to run commands in privileged containers that are not limited by the default security sandbox. Such container may potentially access and modify system resources. In Dockerfile, use [`RUN --security=insecure`](https://docs.docker.com/reference/dockerfile/#run---security) to run a command in a privileged container.

``` {.chroma tabindex="0"}
target "integration-tests" {
  # this target requires privileged containers to run nested containers
  entitlements = ["security.insecure"]
}
```

Entitlements are enabled with a two-step process. First, a target must declare the entitlements it requires. Secondly, when invoking the `bake` command, the user must grant the entitlements by passing the `--allow` flag or confirming the entitlements when prompted in an interactive terminal. This is to ensure that the user is aware of the possibly insecure permissions they are granting to the build process.

### [`target.extra-hosts`](#targetextra-hosts) {#targetextra-hosts .scroll-mt-20 .flex .items-center .gap-2}

Use the `extra-hosts` attribute to define custom host-to-IP mapping for the target. This has the same effect as passing a [`--add-host`](https://docs.docker.com/reference/cli/docker/buildx/build/#add-host) flag to the build command.

``` {.chroma tabindex="0"}
target "default" {
  extra-hosts = {
    my_hostname = "8.8.8.8"
  }
}
```

### [`target.inherits`](#targetinherits) {#targetinherits .scroll-mt-20 .flex .items-center .gap-2}

A target can inherit attributes from other targets. Use `inherits` to reference from one target to another.

In the following example, the `app-dev` target specifies an image name and tag. The `app-release` target uses `inherits` to reuse the tag name.

``` {.chroma tabindex="0"}
variable "TAG" {
  default = "latest"
}

target "app-dev" {
  tags = ["docker.io/username/myapp:${TAG}"]
}

target "app-release" {
  inherits = ["app-dev"]
  platforms = ["linux/amd64", "linux/arm64"]
}
```

The `inherits` attribute is a list, meaning you can reuse attributes from multiple other targets. In the following example, the `app-release` target reuses attributes from both the `app-dev` and `_release` targets.

``` {.chroma tabindex="0"}
target "app-dev" {
  args = {
    GO_VERSION = "1.20"
    BUILDX_EXPERIMENTAL = 1
  }
  tags = ["docker.io/username/myapp"]
  dockerfile = "app.Dockerfile"
  labels = {
    "org.opencontainers.image.source" = "https://github.com/username/myapp"
  }
}

target "_release" {
  args = {
    BUILDKIT_CONTEXT_KEEP_GIT_DIR = 1
    BUILDX_EXPERIMENTAL = 0
  }
}

target "app-release" {
  inherits = ["app-dev", "_release"]
  platforms = ["linux/amd64", "linux/arm64"]
}
```

When inheriting attributes from multiple targets and there\'s a conflict, the target that appears last in the `inherits` list takes precedence. The previous example defines the `BUILDX_EXPERIMENTAL` argument twice for the `app-release` target. It resolves to `0` because the `_release` target appears last in the inheritance chain:

``` {.chroma tabindex="0"}
$ docker buildx bake --print app-release
[+] Building 0.0s (0/0)
{
  "group": {
    "default": {
      "targets": [
        "app-release"
      ]
    }
  },
  "target": {
    "app-release": {
      "context": ".",
      "dockerfile": "app.Dockerfile",
      "args": {
        "BUILDKIT_CONTEXT_KEEP_GIT_DIR": "1",
        "BUILDX_EXPERIMENTAL": "0",
        "GO_VERSION": "1.20"
      },
      "labels": {
        "org.opencontainers.image.source": "https://github.com/username/myapp"
      },
      "tags": [
        "docker.io/username/myapp"
      ],
      "platforms": [
        "linux/amd64",
        "linux/arm64"
      ]
    }
  }
}
```

### [`target.labels`](#targetlabels) {#targetlabels .scroll-mt-20 .flex .items-center .gap-2}

Assigns image labels to the build. This is the same as the `--label` flag for `docker build`.

``` {.chroma tabindex="0"}
target "default" {
  labels = {
    "org.opencontainers.image.source" = "https://github.com/username/myapp"
    "com.docker.image.source.entrypoint" = "Dockerfile"
  }
}
```

It\'s possible to use a `null` value for labels. If you do, the builder uses the label value specified in the Dockerfile.

### [`target.matrix`](#targetmatrix) {#targetmatrix .scroll-mt-20 .flex .items-center .gap-2}

A matrix strategy lets you fork a single target into multiple different variants, based on parameters that you specify. This works in a similar way to \[Matrix strategies for GitHub Actions\]. You can use this to reduce duplication in your bake definition.

The `matrix` attribute is a map of parameter names to lists of values. Bake builds each possible combination of values as a separate target.

Each generated target **must** have a unique name. To specify how target names should resolve, use the `name` attribute.

The following example resolves the `app` target to `app-foo` and `app-bar`. It also uses the matrix value to define the [target build stage](#targettarget).

``` {.chroma tabindex="0"}
target "app" {
  name = "app-${tgt}"
  matrix = {
    tgt = ["foo", "bar"]
  }
  target = tgt
}
```

``` {.chroma tabindex="0"}
$ docker buildx bake --print app
[+] Building 0.0s (0/0)
{
  "group": {
    "app": {
      "targets": [
        "app-foo",
        "app-bar"
      ]
    },
    "default": {
      "targets": [
        "app"
      ]
    }
  },
  "target": {
    "app-bar": {
      "context": ".",
      "dockerfile": "Dockerfile",
      "target": "bar"
    },
    "app-foo": {
      "context": ".",
      "dockerfile": "Dockerfile",
      "target": "foo"
    }
  }
}
```

#### [Multiple axes](#multiple-axes) {#multiple-axes .scroll-mt-20 .flex .items-center .gap-2}

You can specify multiple keys in your matrix to fork a target on multiple axes. When using multiple matrix keys, Bake builds every possible variant.

The following example builds four targets:

-   `app-foo-1-0`
-   `app-foo-2-0`
-   `app-bar-1-0`
-   `app-bar-2-0`

``` {.chroma tabindex="0"}
target "app" {
  name = "app-${tgt}-${replace(version, ".", "-")}"
  matrix = {
    tgt = ["foo", "bar"]
    version = ["1.0", "2.0"]
  }
  target = tgt
  args = {
    VERSION = version
  }
}
```

#### [Multiple values per matrix target](#multiple-values-per-matrix-target) {#multiple-values-per-matrix-target .scroll-mt-20 .flex .items-center .gap-2}

If you want to differentiate the matrix on more than just a single value, you can use maps as matrix values. Bake creates a target for each map, and you can access the nested values using dot notation.

The following example builds two targets:

-   `app-foo-1-0`
-   `app-bar-2-0`

``` {.chroma tabindex="0"}
target "app" {
  name = "app-${item.tgt}-${replace(item.version, ".", "-")}"
  matrix = {
    item = [
      {
        tgt = "foo"
        version = "1.0"
      },
      {
        tgt = "bar"
        version = "2.0"
      }
    ]
  }
  target = item.tgt
  args = {
    VERSION = item.version
  }
}
```

### [`target.name`](#targetname) {#targetname .scroll-mt-20 .flex .items-center .gap-2}

Specify name resolution for targets that use a matrix strategy. The following example resolves the `app` target to `app-foo` and `app-bar`.

``` {.chroma tabindex="0"}
target "app" {
  name = "app-${tgt}"
  matrix = {
    tgt = ["foo", "bar"]
  }
  target = tgt
}
```

### [`target.network`](#targetnetwork) {#targetnetwork .scroll-mt-20 .flex .items-center .gap-2}

Specify the network mode for the whole build request. This will override the default network mode for all the `RUN` instructions in the Dockerfile. Accepted values are `default`, `host`, and `none`.

Usually, a better approach to set the network mode for your build steps is to instead use `RUN --network=<value>` in your Dockerfile. This way, you can set the network mode for individual build steps and everyone building the Dockerfile gets consistent behavior without needing to pass additional flags to the build command.

If you set network mode to `host` in your Bake file, you must also grant `network.host` entitlement when invoking the `bake` command. This is because `host` network mode requires elevated privileges and can be a security risk. You can pass `--allow=network.host` to the `docker buildx bake` command to grant the entitlement, or you can confirm the entitlement when prompted if you are using an interactive terminal.

``` {.chroma tabindex="0"}
target "app" {
  # make sure this build does not access internet
  network = "none"
}
```

### [`target.no-cache-filter`](#targetno-cache-filter) {#targetno-cache-filter .scroll-mt-20 .flex .items-center .gap-2}

Don\'t use build cache for the specified stages. This is the same as the `--no-cache-filter` flag for `docker build`. The following example avoids build cache for the `foo` build stage.

``` {.chroma tabindex="0"}
target "default" {
  no-cache-filter = ["foo"]
}
```

### [`target.no-cache`](#targetno-cache) {#targetno-cache .scroll-mt-20 .flex .items-center .gap-2}

Don\'t use cache when building the image. This is the same as the `--no-cache` flag for `docker build`.

``` {.chroma tabindex="0"}
target "default" {
  no-cache = true
}
```

### [`target.output`](#targetoutput) {#targetoutput .scroll-mt-20 .flex .items-center .gap-2}

Configuration for exporting the build output. This is the same as the [`--output` flag](https://docs.docker.com/reference/cli/docker/buildx/build/#output). The following example configures the target to use a cache-only output,

``` {.chroma tabindex="0"}
target "default" {
  output = [{ type = "cacheonly" }]
}
```

> Note
>
> Local outputs with `mode=delete` require granting `--allow=buildx.local.delete` when invoking `docker buildx bake`.

### [`target.policy`](#targetpolicy) {#targetpolicy .scroll-mt-20 .flex .items-center .gap-2}

Policies to validate build sources and metadata. Each entry uses the same keys as the `--policy` flag for `docker buildx build` (`filename`, `reset`, `disabled`, `strict`, `log-level`). Bake also automatically loads `Dockerfile.rego` alongside the target Dockerfile when present.

``` {.chroma tabindex="0"}
target "default" {
  policy = [
    { filename = "extra.rego" },
  ]
}
```

### [`target.platforms`](#targetplatforms) {#targetplatforms .scroll-mt-20 .flex .items-center .gap-2}

Set target platforms for the build target. This is the same as the [`--platform` flag](https://docs.docker.com/reference/cli/docker/buildx/build/#platform). The following example creates a multi-platform build for three architectures.

``` {.chroma tabindex="0"}
target "default" {
  platforms = ["linux/amd64", "linux/arm64", "linux/arm/v7"]
}
```

### [`target.pull`](#targetpull) {#targetpull .scroll-mt-20 .flex .items-center .gap-2}

Configures whether the builder should attempt to pull images when building the target. This is the same as the `--pull` flag for `docker build`. The following example forces the builder to always pull all images referenced in the build target.

``` {.chroma tabindex="0"}
target "default" {
  pull = true
}
```

### [`target.resources`](#targetresources) {#targetresources .scroll-mt-20 .flex .items-center .gap-2}

Sets cgroup resource limits for the containers that run `RUN` instructions during the build. The supported keys are `memory`, `memory-swap`, `cpu-shares`, `cpu-period`, `cpu-quota`, `cpuset-cpus`, and `cpuset-mems`. These map to the equivalent `docker build` flags and to the [`--resource`](https://docs.docker.com/reference/cli/docker/buildx/build/#resource) flag for `docker buildx build`.

``` {.chroma tabindex="0"}
target "default" {
  resources = {
    memory      = "2g"
    memory-swap = "4g"
    cpu-quota   = 50000
  }
}
```

> Note
>
> These limits require a BuildKit daemon that supports per-step resource limits and only take effect on Linux. They don\'t affect the build cache key.

### [`target.secret`](#targetsecret) {#targetsecret .scroll-mt-20 .flex .items-center .gap-2}

Defines secrets to expose to the build target. This is the same as the [`--secret` flag](https://docs.docker.com/reference/cli/docker/buildx/build/#secret).

``` {.chroma tabindex="0"}
variable "HOME" {
  default = null
}

target "default" {
  secret = [
    {
      type = "env"
      id = "KUBECONFIG"
    },
    {
      type = "file"
      id = "aws"
      src = "${HOME}/.aws/credentials"
    }
  ]
}
```

This lets you [mount the secret](https://docs.docker.com/reference/dockerfile/#run---mounttypesecret) in your Dockerfile.

``` {.chroma tabindex="0"}
RUN --mount=type=secret,id=aws,target=/root/.aws/credentials \
    aws cloudfront create-invalidation ...
RUN --mount=type=secret,id=KUBECONFIG,env=KUBECONFIG \
    helm upgrade --install
```

You can override the source for an existing secret without changing the target\'s secret IDs. The secret must already be declared by the target.

``` {.chroma tabindex="0"}
$ docker buildx bake --set default.secret.aws=env=AWS_CREDENTIALS
$ docker buildx bake --set default.secret.KUBECONFIG=src=/path/to/kubeconfig
```

### [`target.shm-size`](#targetshm-size) {#targetshm-size .scroll-mt-20 .flex .items-center .gap-2}

Sets the size of the shared memory allocated for build containers when using `RUN` instructions.

The format is `<number><unit>`. `number` must be greater than `0`. Unit is optional and can be `b` (bytes), `k` (kilobytes), `m` (megabytes), or `g` (gigabytes). If you omit the unit, the system uses bytes.

This is the same as the `--shm-size` flag for `docker build`.

``` {.chroma tabindex="0"}
target "default" {
  shm-size = "128m"
}
```

> Note
>
> In most cases, it is recommended to let the builder automatically determine the appropriate configurations. Manual adjustments should only be considered when specific performance tuning is required for complex build scenarios.

### [`target.ssh`](#targetssh) {#targetssh .scroll-mt-20 .flex .items-center .gap-2}

Defines SSH agent sockets or keys to expose to the build. This is the same as the [`--ssh` flag](https://docs.docker.com/reference/cli/docker/buildx/build/#ssh). This can be useful if you need to access private repositories during a build.

``` {.chroma tabindex="0"}
target "default" {
  ssh = [{ id = "default" }]
}
```

``` {.chroma tabindex="0"}
FROM alpine
RUN --mount=type=ssh \
    apk add git openssh-client \
    && install -m 0700 -d ~/.ssh \
    && ssh-keyscan github.com >> ~/.ssh/known_hosts \
    && git clone git@github.com:user/my-private-repo.git
```

> Note
>
> When overriding `ssh` from the command line with `--set`, use the inline `id=path` string form rather than the object form shown above, for example `docker buildx bake --set "*.ssh=default=$HOME/.ssh/id_ed25519"`. Separate multiple paths with commas. See [`bake --set`](https://docs.docker.com/reference/cli/docker/buildx/bake/#set) for details.

### [`target.tags`](#targettags) {#targettags .scroll-mt-20 .flex .items-center .gap-2}

Image names and tags to use for the build target. This is the same as the [`--tag` flag](https://docs.docker.com/reference/cli/docker/image/build/#tag).

``` {.chroma tabindex="0"}
target "default" {
  tags = [
    "org/repo:latest",
    "myregistry.azurecr.io/team/image:v1"
  ]
}
```

### [`target.target`](#targettarget) {#targettarget .scroll-mt-20 .flex .items-center .gap-2}

Set the target build stage to build. This is the same as the [`--target` flag](https://docs.docker.com/reference/cli/docker/image/build/#target).

``` {.chroma tabindex="0"}
target "default" {
  target = "binaries"
}
```

### [`target.ulimits`](#targetulimits) {#targetulimits .scroll-mt-20 .flex .items-center .gap-2}

Ulimits overrides the default ulimits of build\'s containers when using `RUN` instructions and are specified with a soft and hard limit as such: `<type>=<soft limit>[:<hard limit>]`, for example:

``` {.chroma tabindex="0"}
target "app" {
  ulimits = [
    "nofile=1024:1024"
  ]
}
```

> Note
>
> If you do not provide a `hard limit`, the `soft limit` is used for both values. If no `ulimits` are set, they are inherited from the default `ulimits` set on the daemon.

> Note
>
> In most cases, it is recommended to let the builder automatically determine the appropriate configurations. Manual adjustments should only be considered when specific performance tuning is required for complex build scenarios.

## [Group](#group) {#group .scroll-mt-20 .flex .items-center .gap-2}

Groups allow you to invoke multiple builds (targets) at once.

``` {.chroma tabindex="0"}
group "default" {
  targets = ["db", "webapp-dev"]
}

target "webapp-dev" {
  dockerfile = "Dockerfile.webapp"
  tags = ["docker.io/username/webapp:latest"]
}

target "db" {
  dockerfile = "Dockerfile.db"
  tags = ["docker.io/username/db"]
}
```

Groups take precedence over targets, if both exist with the same name. The following bake file builds the `default` group. Bake ignores the `default` target.

``` {.chroma tabindex="0"}
target "default" {
  dockerfile-inline = "FROM ubuntu"
}

group "default" {
  targets = ["alpine", "debian"]
}
target "alpine" {
  dockerfile-inline = "FROM alpine"
}
target "debian" {
  dockerfile-inline = "FROM debian"
}
```

## [Variable](#variable) {#variable .scroll-mt-20 .flex .items-center .gap-2}

The HCL file format supports variable block definitions. You can use variables as build arguments in your Dockerfile, or interpolate them in attribute values in your Bake file.

``` {.chroma tabindex="0"}
variable "TAG" {
  type = string
  default = "latest"
  description = "Tag to use for build"
}

target "webapp-dev" {
  dockerfile = "Dockerfile.webapp"
  tags = ["docker.io/username/webapp:${TAG}"]
}
```

You can assign a default value for a variable in the Bake file, or assign a `null` value to it. If you assign a `null` value, Buildx uses the default value from the Dockerfile instead.

You can also add a description of the variable\'s purpose with the `description` field. This attribute is useful when combined with the `docker buildx bake --list=variables` option, providing a more informative output when listing the available variables in a Bake file.

You can override variable defaults set in the Bake file using environment variables. The following example sets the `TAG` variable to `dev`, overriding the default `latest` value shown in the previous example.

``` {.chroma tabindex="0"}
$ TAG=dev docker buildx bake webapp-dev
```

Variables can also be assigned an explicit type. If provided, it will be used to validate the default value (if set), as well as any overrides. This is particularly useful when using complex types which are intended to be overridden. The previous example could be expanded to apply an arbitrary series of tags.

``` {.chroma tabindex="0"}
variable "TAGS" {
  default = ["latest"]
  type = list(string)
}

target "webapp-dev" {
  dockerfile = "Dockerfile.webapp"
  tags = [for tag in TAGS: "docker.io/username/webapp:${tag}"]
}
```

This example shows how to generate three tags without changing the file or using custom functions/parsing:

``` {.chroma tabindex="0"}
$ TAGS=dev,latest,2 docker buildx bake webapp-dev
```

### [Variable typing](#variable-typing) {#variable-typing .scroll-mt-20 .flex .items-center .gap-2}

The following primitive types are available:

-   `string`
-   `number`
-   `bool`

The type is expressed like a keyword; it must be expressed as a literal:

``` {.chroma tabindex="0"}
variable "OK" {
  type = string
}

# cannot be an actual string
variable "BAD" {
  type = "string"
}

# cannot be the result of an expression
variable "ALSO_BAD" {
  type = lower("string")
}
```

Specifying primitive types can be valuable to show intent (especially when a default is not provided), but bake will generally behave as expected without explicit typing.

Complex types are expressed with \"type constructors\"; they are:

-   `tuple([<type>,...])`
-   `list(<type>)`
-   `set(<type>)`
-   `map(<type>)`
-   `object({<attr>=<type>},...})`

The following are examples of each of those, as well as how the (optional) default value would be expressed:

``` {.chroma tabindex="0"}
# structured way to express "1.2.3-alpha"
variable "MY_VERSION" {
  type = tuple([number, number, number, string])
  default = [1, 2, 3, "alpha"]
}

# JDK versions used in a matrix build
variable "JDK_VERSIONS" {
  type = list(number)
  default = [11, 17, 21]
}

# better way to express the previous example; this will also
# enforce set semantics and allow use of set-based functions
variable "JDK_VERSIONS" {
  type = set(number)
  default = [11, 17, 21]
}

# with the help of lookup(), translate a 'feature' to a tag
variable "FEATURE_TO_NAME" {
  type = map(string)
  default = {featureA = "slim", featureB = "tiny"}
}

# map a branch name to a registry location
variable "PUSH_DESTINATION" {
  type = object({branch = string, registry = string})
  default = {branch = "main", registry = "prod-registry.invalid.com"}
}

# make the previous example more useful with composition
variable "PUSH_DESTINATIONS" {
  type = list(object({branch = string, registry = string}))
  default = [
    {branch = "develop", registry = "test-registry.invalid.com"},
    {branch = "main", registry = "prod-registry.invalid.com"},
  ]
}
```

Note that in each example, the default value would be valid even if typing was not present. If typing was omitted, the first three would all be considered `tuple`; you would be restricted to functions that operate on `tuple` and, for example, not be able to add elements. Similarly, the third and fourth would both be considered `object`, with the limits and semantics of that type. In short, in the absence of a type, any value delimited with `[]` is a `tuple` and value delimited with `{}` is an `object`. Explicit typing for complex types not only opens up the ability to use functions applicable to that specialized type, but is also a precondition for providing overrides.

> Note
>
> See [HCL Type Expressions](https://github.com/hashicorp/hcl/tree/main/ext/typeexpr) page for more details.

### [Overriding variables](#overriding-variables) {#overriding-variables .scroll-mt-20 .flex .items-center .gap-2}

As mentioned in the [intro to variables](#variable), primitive types (`string`, `number`, and `bool`) can be overridden without typing and will generally behave as expected. (When explicit typing is not provided, a variable is assumed to be primitive when the default value lacks `{}` or `[]` delimiters; a variable with neither typing nor a default value is treated as `string`.) Naturally, these same overrides can be used alongside explicit typing too; they may help in edge cases where you want `VAR=true` to be a `string`, where without typing, it may be a `string` or a `bool` depending on how/where it\'s used. Overriding a variable with a complex type can only be done when the type is provided. This is still done via environment variables, but the values can be provided via CSV or JSON.

#### [CSV overrides](#csv-overrides) {#csv-overrides .scroll-mt-20 .flex .items-center .gap-2}

This is considered the canonical method and is well suited to interactive usage. It is assumed that `list` and `set` will be the most common complex type, as well as the most common complex type designed to be overridden. Thus, there is full CSV support for `list` and `set` (and `tuple`; despite being considered a structural type, it is more like a collection type in this regard).

There is limited support for `map` and `object` and no support for composite types; for these advanced cases, an alternative mechanism [using JSON](#json-overrides) is available.

#### [JSON overrides](#json-overrides) {#json-overrides .scroll-mt-20 .flex .items-center .gap-2}

Overrides can also be provided via JSON. This is the only method available for providing some complex types and may be convenient if overrides are already JSON (for example, if they come from a JSON API). It can also be used when dealing with values are difficult or impossible to specify using CSV (e.g., values containing quotes or commas). To use JSON, simply append `_JSON` to the variable name. In this contrived example, CSV cannot handle the second value; despite being a supported CSV type, JSON must be used:

``` {.chroma tabindex="0"}
variable "VALS" {
  type = list(string)
  default = ["some", "list"]
}
```

``` {.chroma tabindex="0"}
$ cat data.json
["hello","with,comma","with\"quote"]
$ VALS_JSON=$(< data.json) docker buildx bake

# CSV equivalent, though the second value cannot be expressed at all 
$ VALS='hello,"with""quote"' docker buildx bake
```

This example illustrates some precedence and usage rules:

``` {.chroma tabindex="0"}
variable "FOO" {
  type = string
  default = "foo"
}

variable "FOO_JSON" {
  type = string
  default = "foo"
}
```

The variable `FOO` can *only* be overridden using CSV because `FOO_JSON`, which would typically used for a JSON override, is already a defined variable. Since `FOO_JSON` is an actual variable, setting that environment variable would be expected to a CSV value. A JSON override *is* possible for this variable, using environment variable `FOO_JSON_JSON`.

``` {.chroma tabindex="0"}
# These three are all equivalent, setting variable FOO=bar
$ FOO=bar docker buildx bake <...>
$ FOO='bar' docker buildx bake <...>
$ FOO="bar" docker buildx bake <...>

# Sets *only* variable FOO_JSON; FOO is untouched
$ FOO_JSON=bar docker buildx bake <...>

# This also sets FOO_JSON, but will fail due to not being valid JSON
$ FOO_JSON_JSON=bar docker buildx bake <...>

# These are all equivalent
$ cat data.json
"bar"
$ FOO_JSON_JSON=$(< data.json) docker buildx bake <...>
$ FOO_JSON_JSON='"bar"' docker buildx bake <...>
$ FOO_JSON=bar docker buildx bake <...>

# This results in setting two different variables, both specified as CSV (FOO=bar and FOO_JSON="baz")
$ FOO=bar FOO_JSON='"baz"' docker buildx bake <...>

# These refer to the same variable with FOO_JSON_JSON having precedence and read as JSON (FOO_JSON=baz)
$ FOO_JSON=bar FOO_JSON_JSON='"baz"' docker buildx bake <...>
```

### [Built-in variables](#built-in-variables) {#built-in-variables .scroll-mt-20 .flex .items-center .gap-2}

The following variables are built-ins that you can use with Bake without having to define them.

  Variable                Description
  ----------------------- -------------------------------------------------------------------------------------
  `BAKE_CMD_CONTEXT`      Holds the main context when building using a remote Bake file.
  `BAKE_LOCAL_PLATFORM`   Returns the current platform's default platform specification (e.g. `linux/amd64`).

### [Use environment variable as default](#use-environment-variable-as-default) {#use-environment-variable-as-default .scroll-mt-20 .flex .items-center .gap-2}

If an environment variable exists with the same name as a declared Bake variable, Bake uses that environment variable value instead of the declared default.

To disable this environment-based variable lookup, set `BUILDX_BAKE_DISABLE_VARS_ENV_LOOKUP=1`.

``` {.chroma tabindex="0"}
variable "HOME" {
  default = "/root"
}
```

### [Interpolate variables into attributes](#interpolate-variables-into-attributes) {#interpolate-variables-into-attributes .scroll-mt-20 .flex .items-center .gap-2}

To interpolate a variable into an attribute string value, you must use curly brackets. The following doesn\'t work:

``` {.chroma tabindex="0"}
variable "HOME" {
  default = "$HOME"
}

target "default" {
  ssh = ["default=$HOME/.ssh/id_rsa"]
}
```

Wrap the variable in curly brackets where you want to insert it:

``` {.chroma tabindex="0"}
  variable "HOME" {
    default = "$HOME"
  }

  target "default" {
-   ssh = ["default=$HOME/.ssh/id_rsa"]
+   ssh = ["default=${HOME}/.ssh/id_rsa"]
  }
```

Before you can interpolate a variable into an attribute, first you must declare it in the bake file, as demonstrated in the following example.

``` {.chroma tabindex="0"}
$ cat docker-bake.hcl
target "default" {
  dockerfile-inline = "FROM ${BASE_IMAGE}"
}
$ docker buildx bake
[+] Building 0.0s (0/0)
docker-bake.hcl:2
--------------------
   1 |     target "default" {
   2 | >>>   dockerfile-inline = "FROM ${BASE_IMAGE}"
   3 |     }
   4 |
--------------------
ERROR: docker-bake.hcl:2,31-41: Unknown variable; There is no variable named "BASE_IMAGE"., and 1 other diagnostic(s)
$ cat >> docker-bake.hcl

variable "BASE_IMAGE" {
  default = "alpine"
}

$ docker buildx bake
[+] Building 0.6s (5/5) FINISHED
```

## [Function](#function) {#function .scroll-mt-20 .flex .items-center .gap-2}

A [set of general-purpose functions](https://github.com/docker/buildx/blob/master/docs/bake-stdlib.md) provided by [go-cty](https://github.com/zclconf/go-cty/tree/main/cty/function/stdlib) are available for use in HCL files:

``` {.chroma tabindex="0"}
# docker-bake.hcl
target "webapp-dev" {
  dockerfile = "Dockerfile.webapp"
  tags = ["docker.io/username/webapp:latest"]
  args = {
    buildno = "${add(123, 1)}"
  }
}
```

In addition, [user defined functions](https://github.com/hashicorp/hcl/tree/main/ext/userfunc) are also supported:

``` {.chroma tabindex="0"}
# docker-bake.hcl
function "increment" {
  params = [number]
  result = number + 1
}

target "webapp-dev" {
  dockerfile = "Dockerfile.webapp"
  tags = ["docker.io/username/webapp:latest"]
  args = {
    buildno = "${increment(123)}"
  }
}
```

> Note
>
> See [User defined HCL functions](https://docs.docker.com/build/bake/hcl-funcs/) page for more details.
