---
{"title": "Functions", "url": "https://docs.docker.com/build/bake/funcs/", "retrieved": "2026-11-01", "license": "Apache-2.0"}
---

# Functions {#functions pagefind-weight="10"}

------------------------------------------------------------------------

Table of contents

------------------------------------------------------------------------

HCL functions are great for when you need to manipulate values in your build configuration in more complex ways than just concatenation or interpolation.

## [Standard library](#standard-library) {#standard-library .scroll-mt-20 .flex .items-center .gap-2}

Bake ships with built-in support for the [standard library functions](https://docs.docker.com/build/bake/stdlib/).

The following example shows the `add` function:

docker-bake.hcl

``` {.chroma tabindex="0"}
variable "TAG" {
  default = "latest"
}

group "default" {
  targets = ["webapp"]
}

target "webapp" {
  args = {
    buildno = "${add(123, 1)}"
  }
}
```

``` {.chroma tabindex="0"}
$ docker buildx bake --print webapp
```

``` {.chroma tabindex="0"}
{
  "group": {
    "default": {
      "targets": ["webapp"]
    }
  },
  "target": {
    "webapp": {
      "context": ".",
      "dockerfile": "Dockerfile",
      "args": {
        "buildno": "124"
      }
    }
  }
}
```

## [User-defined functions](#user-defined-functions) {#user-defined-functions .scroll-mt-20 .flex .items-center .gap-2}

You can create [user-defined functions](https://github.com/hashicorp/hcl/tree/main/ext/userfunc) that do just what you want, if the built-in standard library functions don\'t meet your needs.

The following example defines an `increment` function.

docker-bake.hcl

``` {.chroma tabindex="0"}
function "increment" {
  params = [number]
  result = number + 1
}

group "default" {
  targets = ["webapp"]
}

target "webapp" {
  args = {
    buildno = "${increment(123)}"
  }
}
```

``` {.chroma tabindex="0"}
$ docker buildx bake --print webapp
```

``` {.chroma tabindex="0"}
{
  "group": {
    "default": {
      "targets": ["webapp"]
    }
  },
  "target": {
    "webapp": {
      "context": ".",
      "dockerfile": "Dockerfile",
      "args": {
        "buildno": "124"
      }
    }
  }
}
```

## [Variables in functions](#variables-in-functions) {#variables-in-functions .scroll-mt-20 .flex .items-center .gap-2}

You can make references to [variables](https://docs.docker.com/build/bake/variables/) and standard library functions inside your functions.

The following example uses a global variable (`REPO`) in a custom function.

docker-bake.hcl

``` {.chroma tabindex="0"}
# docker-bake.hcl
variable "REPO" {
  default = "user/repo"
}

function "tag" {
  params = [tag]
  result = ["${REPO}:${tag}"]
}

target "webapp" {
  tags = tag("v1")
}
```

Printing the Bake file with the `--print` flag shows that the `tag` function uses the value of `REPO` to set the prefix of the tag.

``` {.chroma tabindex="0"}
$ docker buildx bake --print webapp
```

``` {.chroma tabindex="0"}
{
  "group": {
    "default": {
      "targets": ["webapp"]
    }
  },
  "target": {
    "webapp": {
      "context": ".",
      "dockerfile": "Dockerfile",
      "tags": ["user/repo:v1"]
    }
  }
}
```
