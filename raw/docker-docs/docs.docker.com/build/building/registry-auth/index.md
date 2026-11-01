---
{"title": "Registry authentication", "url": "https://docs.docker.com/build/building/registry-auth/", "retrieved": "2026-11-01", "license": "Apache-2.0"}
---

# Registry authentication {#registry-authentication pagefind-weight="10"}

------------------------------------------------------------------------

Table of contents

------------------------------------------------------------------------

Buildx uses Docker\'s credential configuration to authenticate when pulling images for a build and pushing build results. Sign in to the registry before building:

``` {.chroma tabindex="0"}
$ docker login registry.example.com
```

See the [`docker login` reference](/reference/cli/docker/login/) for credential stores and authentication methods.

## [Select credentials by repository and scope](#select-credentials-by-repository-and-scope) {#select-credentials-by-repository-and-scope .scroll-mt-20 .flex .items-center .gap-2}

Buildx can load separate Docker credential configurations for specific registry repositories and token scopes. Use this when a build needs different credentials for repositories on the same registry, or for pull and push requests.

Store each Docker `config.json` in a directory under `$BUILDX_CONFIG/config/<registry>[/<repository>][@<scope>[,<scope>...]]`. If `BUILDX_CONFIG` isn\'t set, use the [config directory lookup order](https://docs.docker.com/build/building/variables/#buildx_config). Repository paths must match the full repository name. Scopes are registry token actions, such as `pull` and `push`.

For example, the default config directory can contain:

``` {.chroma tabindex="0"}
~/.docker/buildx/config/
└── registry.example.com/
    └── team/
        ├── app@pull/
        │   └── config.json
        └── app@pull,push/
            └── config.json
```

Populate these files with Docker credential configurations. For example, use the Docker CLI\'s `--config` flag to store credentials in the pull config directory:

``` {.chroma tabindex="0"}
$ docker --config \
    ~/.docker/buildx/config/registry.example.com/team/app@pull \
    login registry.example.com
```

Use a different config directory and credentials for the combined `pull,push` scope. Buildx prefers repository-specific matches over registry-wide matches, then prefers the match with more scope actions. Every action in a config\'s directory suffix must be present in the requested scope.

If no alternative matches, Buildx uses the normal Docker credential config. Alternative matching applies when authentication requests contain a single repository scope; requests involving multiple repositories use the normal config.

This is a Buildx-specific compatibility mechanism. Docker commands don\'t automatically select these configs by repository or scope. The `--config` example only chooses where `docker login` stores credentials.
