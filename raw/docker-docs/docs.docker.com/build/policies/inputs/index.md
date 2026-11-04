---
{"title": "Input reference", "url": "https://docs.docker.com/build/policies/inputs/", "retrieved": "2026-11-01", "license": "Apache-2.0"}
---

# Input reference {#input-reference pagefind-weight="10"}

------------------------------------------------------------------------

Table of contents

------------------------------------------------------------------------

When Buildx evaluates policies, it provides information about build inputs through the `input` object. The structure of `input` depends on the type of resource your Dockerfile references.

## [Input types](#input-types) {#input-types .scroll-mt-20 .flex .items-center .gap-2}

Build inputs correspond to Dockerfile instructions:

  Dockerfile instruction                    Input type   Access pattern
  ----------------------------------------- ------------ ----------------
  `FROM alpine:latest`                      Image        `input.image`
  `COPY --from=builder /app /app`           Image        `input.image`
  `ADD https://example.com/file.tar.gz /`   HTTP         `input.http`
  `RUN curl https://example.com/`           HTTP         `input.http`
  `ADD git@github.com:user/repo.git /src`   Git          `input.git`
  Build context (`.`)                       Local        `input.local`

Each input type has specific fields available for policy evaluation.

## [HTTP inputs](#http-inputs) {#http-inputs .scroll-mt-20 .flex .items-center .gap-2}

HTTP inputs represent files downloaded over HTTP or HTTPS using the `ADD` instruction, or requests from `RUN` instructions when BuildKit\'s proxy is enabled. See [Block URLs in build steps](https://docs.docker.com/build/policies/usage/#block-urls-in-build-steps).

### [Example Dockerfile](#example-dockerfile) {#example-dockerfile .scroll-mt-20 .flex .items-center .gap-2}

``` {.chroma tabindex="0"}
FROM alpine
ADD --checksum=sha256:abc123... https://example.com/app.tar.gz /app.tar.gz
```

### [Available fields](#available-fields) {#available-fields .scroll-mt-20 .flex .items-center .gap-2}

#### [`input.http.url`](#inputhttpurl) {#inputhttpurl .scroll-mt-20 .flex .items-center .gap-2}

The complete URL of the resource.

``` {.chroma tabindex="0"}
allow if {
    input.http.url == "https://example.com/app.tar.gz"
}
```

#### [`input.http.schema`](#inputhttpschema) {#inputhttpschema .scroll-mt-20 .flex .items-center .gap-2}

The URL scheme (`http` or `https`).

``` {.chroma tabindex="0"}
# Require HTTPS for all downloads
allow if {
    input.http.schema == "https"
}
```

#### [`input.http.host`](#inputhttphost) {#inputhttphost .scroll-mt-20 .flex .items-center .gap-2}

The hostname from the URL.

``` {.chroma tabindex="0"}
# Allow downloads from approved domains
allow if {
    input.http.host == "cdn.example.com"
}
```

#### [`input.http.path`](#inputhttppath) {#inputhttppath .scroll-mt-20 .flex .items-center .gap-2}

The path component of the URL.

``` {.chroma tabindex="0"}
allow if {
    startswith(input.http.path, "/releases/")
}
```

#### [`input.http.checksum`](#inputhttpchecksum) {#inputhttpchecksum .scroll-mt-20 .flex .items-center .gap-2}

The checksum specified with `ADD --checksum=...`, if present. Empty string if no checksum was provided.

``` {.chroma tabindex="0"}
# Require checksums for all downloads
allow if {
    input.http.checksum != ""
}
```

#### [`input.http.hasAuth`](#inputhttphasauth) {#inputhttphasauth .scroll-mt-20 .flex .items-center .gap-2}

Boolean indicating if the request includes authentication (HTTP basic auth or bearer token).

``` {.chroma tabindex="0"}
# Require authentication for internal servers
allow if {
    input.http.host == "internal.company.com"
    input.http.hasAuth
}
```

## [Image inputs](#image-inputs) {#image-inputs .scroll-mt-20 .flex .items-center .gap-2}

Image inputs represent container images from `FROM` instructions or `COPY --from` references.

### [Example Dockerfile](#example-dockerfile-1) {#example-dockerfile-1 .scroll-mt-20 .flex .items-center .gap-2}

``` {.chroma tabindex="0"}
FROM alpine:3.19@sha256:abc123...
COPY --from=builder:latest /app /app
```

### [Available fields](#available-fields-1) {#available-fields-1 .scroll-mt-20 .flex .items-center .gap-2}

#### [`input.image.ref`](#inputimageref) {#inputimageref .scroll-mt-20 .flex .items-center .gap-2}

The complete image reference as written in the Dockerfile.

``` {.chroma tabindex="0"}
allow if {
    input.image.ref == "alpine:3.19@sha256:abc123..."
}
```

#### [`input.image.host`](#inputimagehost) {#inputimagehost .scroll-mt-20 .flex .items-center .gap-2}

The registry hostname. Docker Hub images use `"docker.io"`.

``` {.chroma tabindex="0"}
# Only allow Docker Hub images
allow if {
    input.image.host == "docker.io"
}

# Only allow images from GitHub Container Registry
allow if {
    input.image.host == "ghcr.io"
}
```

#### [`input.image.repo`](#inputimagerepo) {#inputimagerepo .scroll-mt-20 .flex .items-center .gap-2}

The repository name without the registry host.

``` {.chroma tabindex="0"}
allow if {
    input.image.repo == "library/alpine"
}
```

#### [`input.image.fullRepo`](#inputimagefullrepo) {#inputimagefullrepo .scroll-mt-20 .flex .items-center .gap-2}

The full repository path including registry host.

``` {.chroma tabindex="0"}
allow if {
    input.image.fullRepo == "docker.io/library/alpine"
}
```

#### [`input.image.tag`](#inputimagetag) {#inputimagetag .scroll-mt-20 .flex .items-center .gap-2}

The tag portion of the reference. Empty if using a digest reference.

``` {.chroma tabindex="0"}
# Allow only specific tags
allow if {
    input.image.tag == "3.19"
}
```

#### [`input.image.isCanonical`](#inputimageiscanonical) {#inputimageiscanonical .scroll-mt-20 .flex .items-center .gap-2}

Boolean indicating if the reference uses a digest (`@sha256:...`).

``` {.chroma tabindex="0"}
# Require digest references
allow if {
    input.image.isCanonical
}
```

#### [`input.image.checksum`](#inputimagechecksum) {#inputimagechecksum .scroll-mt-20 .flex .items-center .gap-2}

The SHA256 digest of the image manifest.

``` {.chroma tabindex="0"}
allow if {
    input.image.checksum == "sha256:abc123..."
}
```

#### [`input.image.platform`](#inputimageplatform) {#inputimageplatform .scroll-mt-20 .flex .items-center .gap-2}

The target platform for multi-platform images.

``` {.chroma tabindex="0"}
allow if {
    input.image.platform == "linux/amd64"
}
```

#### [`input.image.os`](#inputimageos) {#inputimageos .scroll-mt-20 .flex .items-center .gap-2}

The operating system from the image configuration.

``` {.chroma tabindex="0"}
allow if {
    input.image.os == "linux"
}
```

#### [`input.image.arch`](#inputimagearch) {#inputimagearch .scroll-mt-20 .flex .items-center .gap-2}

The CPU architecture from the image configuration.

``` {.chroma tabindex="0"}
allow if {
    input.image.arch == "amd64"
}
```

#### [`input.image.hasProvenance`](#inputimagehasprovenance) {#inputimagehasprovenance .scroll-mt-20 .flex .items-center .gap-2}

Boolean indicating if the image has provenance attestations.

``` {.chroma tabindex="0"}
# Require provenance for production images
allow if {
    input.image.hasProvenance
}
```

#### [`input.image.provenance`](#inputimageprovenance) {#inputimageprovenance .scroll-mt-20 .flex .items-center .gap-2}

Metadata parsed from an image\'s SLSA provenance attestation. Buildx supports SLSA v0.2 and v1 predicates. Fields depend on what the attestation records; an absent field isn\'t equivalent to a Boolean value of `false`.

  Field                        Description
  ---------------------------- -------------------------------------------------------------
  `predicateType`              SLSA provenance predicate URI.
  `buildType`                  Identifier for the build process.
  `builderID`                  Builder identifier recorded in the attestation.
  `invocationID`               Identifier for the build invocation.
  `startedOn`, `finishedOn`    Build timestamps in RFC 3339 format.
  `configSource.uri`           URI of the source containing the build definition.
  `configSource.digest`        Map of source digest algorithms to values.
  `configSource.path`          Path to the build definition within the source.
  `frontend`                   BuildKit frontend used for the build.
  `buildArgs`                  Map of build argument names to values.
  `rawArgs`                    Map of frontend arguments, including `build-arg:` prefixes.
  `reproducible`               Whether the attestation declares the build reproducible.
  `hermetic`                   Whether the attestation declares the build hermetic.
  `completeness.parameters`    Whether build parameters are fully recorded.
  `completeness.environment`   Whether the environment is fully recorded (v0.2).
  `completeness.materials`     Whether build dependencies are fully recorded.

For example, require an attestation that declares the build hermetic and records all dependencies:

``` {.chroma tabindex="0"}
allow if {
    input.image.provenance.hermetic == true
    input.image.provenance.completeness.materials == true
}
```

Accessing these fields during policy evaluation resolves the provenance metadata as needed. To inspect it without evaluating a policy, request the fields explicitly:

``` {.chroma tabindex="0"}
$ docker buildx policy eval --print --fields image.provenance \
    docker-image://registry.example.com/team/app:latest
```

These fields describe claims in the attestation. To verify who produced it, also check the image\'s [attestation signatures](#inputimagesignatures).

#### [`input.image.labels`](#inputimagelabels) {#inputimagelabels .scroll-mt-20 .flex .items-center .gap-2}

A map of image labels from the image configuration.

``` {.chroma tabindex="0"}
# Check for specific labels
allow if {
    input.image.labels["org.opencontainers.image.vendor"] == "Example Corp"
}
```

#### [`input.image.signatures`](#inputimagesignatures) {#inputimagesignatures .scroll-mt-20 .flex .items-center .gap-2}

Array of attestation signatures. Each signature in the array has the following fields:

-   `kind`: Signature kind (e.g., `"docker-github-builder"`, `"self-signed"`)
-   `type`: Signature type (e.g., `"bundle-v0.3"`, `"simplesigning-v1"`)
-   `timestamps`: Trusted timestamps from transparency logs
-   `dockerReference`: Docker image reference
-   `isDHI`: Boolean indicating if this is a Docker Hardened Image
-   `signer`: Sigstore certificate details

``` {.chroma tabindex="0"}
# Require at least one signature
allow if {
    count(input.image.signatures) > 0
}
```

For Sigstore signatures, the `signer` object provides detailed certificate information from the signing workflow:

-   `certificateIssuer`: Certificate issuer
-   `subjectAlternativeName`: Subject alternative name from certificate
-   `buildSignerURI`: URI of the build signer
-   `buildSignerDigest`: Digest of the build signer
-   `runnerEnvironment`: CI/CD runner environment
-   `sourceRepositoryURI`: Source repository URL
-   `sourceRepositoryDigest`: Source repository digest
-   `sourceRepositoryRef`: Source repository ref (branch/tag)
-   `sourceRepositoryIdentifier`: Source repository identifier
-   `sourceRepositoryOwnerURI`: Repository owner URI
-   `buildConfigURI`: Build configuration URI
-   `buildTrigger`: What triggered the build
-   `runInvocationURI`: CI/CD run invocation URI

``` {.chroma tabindex="0"}
# Require signatures from GitHub Actions
allow if {
    some sig in input.image.signatures
    sig.signer.runnerEnvironment == "github-hosted"
    startswith(sig.signer.sourceRepositoryURI, "https://github.com/myorg/")
}
```

### [Provenance materials](#provenance-materials) {#provenance-materials .scroll-mt-20 .flex .items-center .gap-2}

`input.image.provenance.materials` contains the build dependencies recorded in an image\'s provenance. Each entry is an input object with the same `image`, `git`, or `http` fields used for direct build inputs.

For example, inspect the Git repository used to build a base image:

``` {.chroma tabindex="0"}
allow if {
    some material in input.image.provenance.materials
    material.git.host == "github.com"
    material.git.remote == "https://github.com/myorg/base.git"
}
```

An image material can have its own `image.provenance.materials` array. Access nested fields to resolve metadata for those dependencies as needed. Buildx supports image, Git, and HTTP material sources; unsupported material URIs are skipped with a warning. Checking a parent image doesn\'t automatically apply your rules to every material. Write explicit conditions for the dependencies you need to validate.

To inspect a nested field without evaluating a policy, use `--fields`:

``` {.chroma tabindex="0"}
$ docker buildx policy eval --print \
    --fields 'image.provenance.materials[0].git.commitChecksum' \
    docker-image://registry.example.com/team/base:latest
```

The example requests Git metadata for the first material. Choose the index and field for the material you want to inspect.

## [Git inputs](#git-inputs) {#git-inputs .scroll-mt-20 .flex .items-center .gap-2}

Git inputs represent Git repositories referenced in `ADD` instructions or used as build context.

### [Example Dockerfile](#example-dockerfile-2) {#example-dockerfile-2 .scroll-mt-20 .flex .items-center .gap-2}

``` {.chroma tabindex="0"}
ADD git@github.com:moby/buildkit.git#v0.12.0 /src
```

### [Available fields](#available-fields-2) {#available-fields-2 .scroll-mt-20 .flex .items-center .gap-2}

#### [`input.git.schema`](#inputgitschema) {#inputgitschema .scroll-mt-20 .flex .items-center .gap-2}

The URL scheme (`https`, `http`, `git`, or `ssh`).

``` {.chroma tabindex="0"}
# Require HTTPS for Git clones
allow if {
    input.git.schema == "https"
}
```

#### [`input.git.host`](#inputgithost) {#inputgithost .scroll-mt-20 .flex .items-center .gap-2}

The Git host (e.g., `github.com`, `gitlab.com`).

``` {.chroma tabindex="0"}
allow if {
    input.git.host == "github.com"
}
```

#### [`input.git.remote`](#inputgitremote) {#inputgitremote .scroll-mt-20 .flex .items-center .gap-2}

The complete Git URL.

``` {.chroma tabindex="0"}
allow if {
    input.git.remote == "https://github.com/moby/buildkit.git"
}
```

#### [`input.git.ref`](#inputgitref) {#inputgitref .scroll-mt-20 .flex .items-center .gap-2}

The Git reference.

``` {.chroma tabindex="0"}
allow if {
    input.git.ref == "refs/heads/master"
}
```

#### [`input.git.tagName`](#inputgittagname) {#inputgittagname .scroll-mt-20 .flex .items-center .gap-2}

The tag name if the reference is a tag.

``` {.chroma tabindex="0"}
# Only allow version tags
allow if {
    regex.match(`^v[0-9]+\.[0-9]+\.[0-9]+$`, input.git.tagName)
}
```

#### [`input.git.branch`](#inputgitbranch) {#inputgitbranch .scroll-mt-20 .flex .items-center .gap-2}

The branch name if the reference is a branch.

``` {.chroma tabindex="0"}
allow if {
    input.git.branch == "main"
}
```

#### [`input.git.subDir`](#inputgitsubdir) {#inputgitsubdir .scroll-mt-20 .flex .items-center .gap-2}

The subdirectory path within the repository, if specified.

``` {.chroma tabindex="0"}
# Ensure clones are from the root
allow if {
    input.git.subDir == ""
}
```

#### [`input.git.isCommitRef`](#inputgitiscommitref) {#inputgitiscommitref .scroll-mt-20 .flex .items-center .gap-2}

Boolean indicating if the reference is a commit SHA (as opposed to a branch or tag name).

``` {.chroma tabindex="0"}
# Require commit SHAs for production
allow if {
    input.env.target == "production"
    input.git.isCommitRef
}
```

#### [`input.git.checksum`](#inputgitchecksum) {#inputgitchecksum .scroll-mt-20 .flex .items-center .gap-2}

The checksum of the Git reference. For commit references and branches, this is the commit hash. For annotated tags, this is the tag object hash.

``` {.chroma tabindex="0"}
allow if {
    input.git.checksum == "abc123..."
}
```

#### [`input.git.commitChecksum`](#inputgitcommitchecksum) {#inputgitcommitchecksum .scroll-mt-20 .flex .items-center .gap-2}

The commit hash that the reference points to. For annotated tags, this differs from `checksum` (which is the tag object hash). For commit references and branches, this is the same as `checksum`.

``` {.chroma tabindex="0"}
allow if {
    input.git.commitChecksum == "abc123..."
}
```

#### [`input.git.isAnnotatedTag`](#inputgitisannotatedtag) {#inputgitisannotatedtag .scroll-mt-20 .flex .items-center .gap-2}

Boolean indicating if the reference is an annotated tag (as opposed to a lightweight tag).

``` {.chroma tabindex="0"}
# Require annotated tags
allow if {
    input.git.tagName != ""
    input.git.isAnnotatedTag
}
```

#### [`input.git.commit`](#inputgitcommit) {#inputgitcommit .scroll-mt-20 .flex .items-center .gap-2}

Object containing commit metadata:

-   `author`: Author name, email, when
-   `committer`: Committer name, email, when
-   `message`: Commit message
-   `pgpSignature`: PGP signature details if signed
-   `sshSignature`: SSH signature details if signed

``` {.chroma tabindex="0"}
# Check commit author
allow if {
    input.git.commit.author.email == "maintainer@example.com"
}
```

#### [`input.git.tag`](#inputgittag) {#inputgittag .scroll-mt-20 .flex .items-center .gap-2}

Object containing tag metadata for annotated tags:

-   `tagger`: Tagger name, email, when
-   `message`: Tag message
-   `pgpSignature`: PGP signature details if signed
-   `sshSignature`: SSH signature details if signed

``` {.chroma tabindex="0"}
# Require signed tags
allow if {
    input.git.tag.pgpSignature != null
}
```

## [Local inputs](#local-inputs) {#local-inputs .scroll-mt-20 .flex .items-center .gap-2}

Local inputs represent the build context directory.

### [Available fields](#available-fields-3) {#available-fields-3 .scroll-mt-20 .flex .items-center .gap-2}

#### [`input.local.name`](#inputlocalname) {#inputlocalname .scroll-mt-20 .flex .items-center .gap-2}

The name or path of the local context.

``` {.chroma tabindex="0"}
allow if {
    input.local.name == "."
}
```

Local inputs are typically less restricted than remote inputs, but you can still write policies to enforce context requirements.

## [Environment fields](#environment-fields) {#environment-fields .scroll-mt-20 .flex .items-center .gap-2}

The `input.env` object provides build configuration information set by user on invoking the build, not specific to a resource type.

### [Available fields](#available-fields-4) {#available-fields-4 .scroll-mt-20 .flex .items-center .gap-2}

#### [`input.env.filename`](#inputenvfilename) {#inputenvfilename .scroll-mt-20 .flex .items-center .gap-2}

The name of the Dockerfile being built.

``` {.chroma tabindex="0"}
# Stricter rules for production Dockerfile
allow if {
    input.env.filename == "Dockerfile"
    input.image.isCanonical
}

# Relaxed rules for development
allow if {
    input.env.filename == "Dockerfile.dev"
}
```

#### [`input.env.target`](#inputenvtarget) {#inputenvtarget .scroll-mt-20 .flex .items-center .gap-2}

The build target from multi-stage builds.

``` {.chroma tabindex="0"}
# Require signing only for release builds
allow if {
    input.env.target == "release"
    input.git.tagName != ""
    verify_git_signature(input.git.tag, "maintainer.asc")
}
```

#### [`input.env.depth`](#inputenvdepth) {#inputenvdepth .scroll-mt-20 .flex .items-center .gap-2}

The input\'s depth in the provenance material tree. A direct build input has depth `0`, its materials have depth `1`, and each nested material increases the depth by one. For example, access `material.env.depth` when iterating over `input.image.provenance.materials`.

#### [`input.env.args`](#inputenvargs) {#inputenvargs .scroll-mt-20 .flex .items-center .gap-2}

Build arguments passed with `--build-arg`. Access specific arguments by key.

``` {.chroma tabindex="0"}
# Check build argument values
allow if {
    input.env.args.ENVIRONMENT == "production"
    input.image.hasProvenance
}
```

## [Next steps](#next-steps) {#next-steps .scroll-mt-20 .flex .items-center .gap-2}

-   See [Built-in functions](https://docs.docker.com/build/policies/built-ins/) for built-in helper functions to check and validate input properties
-   Browse [Example policies](https://docs.docker.com/build/policies/examples/) for common patterns
-   Read about [Rego](https://www.openpolicyagent.org/docs/latest/policy-language/) for advanced policy logic
