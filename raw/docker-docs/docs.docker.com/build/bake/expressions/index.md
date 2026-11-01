---
{"title": "Expression evaluation in Bake", "url": "https://docs.docker.com/build/bake/expressions/", "retrieved": "2026-11-01", "license": "Apache-2.0"}
---

# Expression evaluation in Bake {#expression-evaluation-in-bake pagefind-weight="10"}

------------------------------------------------------------------------

Table of contents

------------------------------------------------------------------------

Bake files in the HCL format support expression evaluation, which lets you perform arithmetic operations, conditionally set values, and more.

## [Arithmetic operations](#arithmetic-operations) {#arithmetic-operations .scroll-mt-20 .flex .items-center .gap-2}

You can perform arithmetic operations in expressions. The following example shows how to multiply two numbers.

docker-bake.hcl

``` {.chroma tabindex="0"}
sum = 7*6

target "default" {
  args = {
    answer = sum
  }
}
```

Printing the Bake file with the `--print` flag shows the evaluated value for the `answer` build argument.

``` {.chroma tabindex="0"}
$ docker buildx bake --print
```

``` {.chroma tabindex="0"}
{
  "target": {
    "default": {
      "context": ".",
      "dockerfile": "Dockerfile",
      "args": {
        "answer": "42"
      }
    }
  }
}
```

## [Ternary operators](#ternary-operators) {#ternary-operators .scroll-mt-20 .flex .items-center .gap-2}

You can use ternary operators to conditionally register a value.

The following example adds a tag only when a variable is not empty, using the built-in `notequal` [function](https://docs.docker.com/build/bake/funcs/).

docker-bake.hcl

``` {.chroma tabindex="0"}
variable "TAG" {}

target "default" {
  context="."
  dockerfile="Dockerfile"
  tags = [
    "my-image:latest",
    notequal("",TAG) ? "my-image:${TAG}": ""
  ]
}
```

In this case, `TAG` is an empty string, so the resulting build configuration only contains the hard-coded `my-image:latest` tag.

``` {.chroma tabindex="0"}
$ docker buildx bake --print
```

``` {.chroma tabindex="0"}
{
  "target": {
    "default": {
      "context": ".",
      "dockerfile": "Dockerfile",
      "tags": ["my-image:latest"]
    }
  }
}
```

## [Expressions with variables](#expressions-with-variables) {#expressions-with-variables .scroll-mt-20 .flex .items-center .gap-2}

You can use expressions with [variables](https://docs.docker.com/build/bake/variables/) to conditionally set values, or to perform arithmetic operations.

The following example uses expressions to set values based on the value of variables. The `v1` build argument is set to \"higher\" if the variable `FOO` is greater than 5, otherwise it is set to \"lower\". The `v2` build argument is set to \"yes\" if the `IS_FOO` variable is true, otherwise it is set to \"no\".

docker-bake.hcl

``` {.chroma tabindex="0"}
variable "FOO" {
  default = 3
}

variable "IS_FOO" {
  default = true
}

target "app" {
  args = {
    v1 = FOO > 5 ? "higher" : "lower"
    v2 = IS_FOO ? "yes" : "no"
  }
}
```

Printing the Bake file with the `--print` flag shows the evaluated values for the `v1` and `v2` build arguments.

``` {.chroma tabindex="0"}
$ docker buildx bake --print app
```

``` {.chroma tabindex="0"}
{
  "group": {
    "default": {
      "targets": ["app"]
    }
  },
  "target": {
    "app": {
      "context": ".",
      "dockerfile": "Dockerfile",
      "args": {
        "v1": "lower",
        "v2": "yes"
      }
    }
  }
}
```
