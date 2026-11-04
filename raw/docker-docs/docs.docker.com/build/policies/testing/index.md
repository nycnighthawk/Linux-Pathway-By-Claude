---
{"title": "Test build policies", "url": "https://docs.docker.com/build/policies/testing/", "retrieved": "2026-11-01", "license": "Apache-2.0"}
---

# Test build policies {#test-build-policies pagefind-weight="10"}

------------------------------------------------------------------------

Table of contents

------------------------------------------------------------------------

The [`docker buildx policy test`](/reference/cli/docker/buildx/policy/test/) command runs unit tests for build policies using OPA\'s [standard test framework](https://www.openpolicyagent.org/docs/policy-testing).

``` {.chroma tabindex="0"}
$ docker buildx policy test <path>
```

This validates policy logic with mocked inputs.

For testing against real sources (actual image metadata, Git repositories), use [`docker buildx policy eval`](/reference/cli/docker/buildx/policy/eval/) instead. You can use the `eval --print` option to resolve input for a specific source for writing a test case.

## [Basic example](#basic-example) {#basic-example .scroll-mt-20 .flex .items-center .gap-2}

Start with a simple policy that only allows `alpine` images:

Dockerfile.rego

``` {.chroma tabindex="0"}
package docker

default allow = false

allow if {
    input.image.repo == "alpine"
}

decision := {"allow": allow}
```

Create a test file with the `*_test.rego` suffix. Test functions must start with `test_`:

Dockerfile_test.rego

``` {.chroma tabindex="0"}
package docker

test_alpine_allowed if {
    decision.allow with input as {"image": {"repo": "alpine"}}
}

test_ubuntu_denied if {
    not decision.allow with input as {"image": {"repo": "ubuntu"}}
}
```

Run the tests:

``` {.chroma tabindex="0"}
$ docker buildx policy test .
test_alpine_allowed: PASS (allow=true)
test_ubuntu_denied: PASS (allow=false)
```

`PASS` indicates that the tests defined in `Dockerfile_test.rego` executed successfully and all assertions were satisfied.

## [Command options](#command-options) {#command-options .scroll-mt-20 .flex .items-center .gap-2}

Filter tests by name with `--run`:

``` {.chroma tabindex="0"}
$ docker buildx policy test --run alpine .
test_alpine_allowed: PASS (allow=true)
```

Test policies with non-default filenames using `--filename`:

``` {.chroma tabindex="0"}
$ docker buildx policy test --filename app.Dockerfile .
```

This loads `app.Dockerfile.rego` and runs `*_test.rego` files against it.

## [Test output](#test-output) {#test-output .scroll-mt-20 .flex .items-center .gap-2}

Passed tests show the allow status and any deny messages:

``` {.chroma tabindex="0"}
test_alpine_allowed: PASS (allow=true)
test_ubuntu_denied: PASS (allow=false, deny_msg=only alpine images are allowed)
```

Failed tests show input, decision output, and missing fields:

``` {.chroma tabindex="0"}
test_invalid: FAIL (allow=false)
input:
  {
    "image": {}
  }
decision:
  {
    "allow": false,
    "deny_msg": [
      "only alpine images are allowed"
    ]
  }
missing_input: input.image.repo
```

## [Test deny messages](#test-deny-messages) {#test-deny-messages .scroll-mt-20 .flex .items-center .gap-2}

To test custom error messages, capture the full decision result and assert on the `deny_msg` field.

For a policy with deny messages:

Dockerfile.rego

``` {.chroma tabindex="0"}
package docker

default allow = false

allow if {
    input.image.repo == "alpine"
}

deny_msg contains msg if {
    not allow
    msg := "only alpine images are allowed"
}

decision := {"allow": allow, "deny_msg": deny_msg}
```

Test the deny message:

Dockerfile_test.rego

``` {.chroma tabindex="0"}
test_deny_message if {
    result := decision with input as {"image": {"repo": "ubuntu"}}
    not result.allow
    "only alpine images are allowed" in result.deny_msg
}
```

## [Test patterns](#test-patterns) {#test-patterns .scroll-mt-20 .flex .items-center .gap-2}

**Test environment-specific rules:**

``` {.chroma tabindex="0"}
test_production_requires_digest if {
    decision.allow with input as {
        "env": {"target": "production"},
        "image": {"isCanonical": true}
    }
}

test_development_allows_tags if {
    decision.allow with input as {
        "env": {"target": "development"},
        "image": {"isCanonical": false}
    }
}
```

**Test multiple registries:**

``` {.chroma tabindex="0"}
test_dockerhub_allowed if {
    decision.allow with input as {
        "image": {
            "ref": "docker.io/library/alpine",
            "host": "docker.io",
            "repo": "alpine"
        }
    }
}

test_ghcr_allowed if {
    decision.allow with input as {
        "image": {
            "ref": "ghcr.io/myorg/myapp",
            "host": "ghcr.io",
            "repo": "myorg/myapp"
        }
    }
}
```

For available input fields, see the [Input reference](https://docs.docker.com/build/policies/inputs/).

## [Organize test files](#organize-test-files) {#organize-test-files .scroll-mt-20 .flex .items-center .gap-2}

The test runner discovers all `*_test.rego` files recursively:

``` {.chroma tabindex="0"}
build-policies/
├── Dockerfile.rego
├── Dockerfile_test.rego
└── tests/
    ├── registries_test.rego
    ├── signatures_test.rego
    └── environments_test.rego
```

Run all tests:

``` {.chroma tabindex="0"}
$ docker buildx policy test .
```

Or test specific files:

``` {.chroma tabindex="0"}
$ docker buildx policy test tests/registries_test.rego
```
