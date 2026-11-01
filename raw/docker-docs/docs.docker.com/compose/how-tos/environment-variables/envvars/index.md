---
{"title": "Configure pre-defined environment variables in Docker Compose", "url": "https://docs.docker.com/compose/how-tos/environment-variables/envvars/", "retrieved": "2026-11-01", "license": "Apache-2.0"}
---

# Configure pre-defined environment variables in Docker Compose {#configure-pre-defined-environment-variables-in-docker-compose pagefind-weight="10"}

------------------------------------------------------------------------

Table of contents

------------------------------------------------------------------------

Docker Compose includes several pre-defined environment variables. It also inherits common Docker CLI environment variables, such as `DOCKER_HOST` and `DOCKER_CONTEXT`. See [Docker CLI environment variable reference](/reference/cli/docker/#environment-variables) for details.

This page explains how to set or change the following pre-defined environment variables:

-   `COMPOSE_PROJECT_NAME`
-   `COMPOSE_FILE`
-   `COMPOSE_PROFILES`
-   `COMPOSE_CONVERT_WINDOWS_PATHS`
-   `COMPOSE_PATH_SEPARATOR`
-   `COMPOSE_IGNORE_ORPHANS`
-   `COMPOSE_REMOVE_ORPHANS`
-   `COMPOSE_PARALLEL_LIMIT`
-   `COMPOSE_ANSI`
-   `COMPOSE_STATUS_STDOUT`
-   `COMPOSE_ENV_FILES`
-   `COMPOSE_DISABLE_ENV_FILE`
-   `COMPOSE_MENU`
-   `COMPOSE_EXPERIMENTAL`
-   `COMPOSE_PROGRESS`

## [Methods to override](#methods-to-override) {#methods-to-override .scroll-mt-20 .flex .items-center .gap-2}

  Method                                                                                                                     Description
  -------------------------------------------------------------------------------------------------------------------------- ----------------------------------------------
  [`.env` file](https://docs.docker.com/compose/how-tos/environment-variables/variable-interpolation/)                       Located in the working directory.
  [Shell](https://docs.docker.com/compose/how-tos/environment-variables/variable-interpolation/#substitute-from-the-shell)   Defined in the host operating system shell.
  CLI                                                                                                                        Passed with `--env` or `-e` flag at runtime.

When changing or setting any environment variables, be aware of [Environment variable precedence](https://docs.docker.com/compose/how-tos/environment-variables/envvars-precedence/).

## [Configuration details](#configuration-details) {#configuration-details .scroll-mt-20 .flex .items-center .gap-2}

### [Project and file configuration](#project-and-file-configuration) {#project-and-file-configuration .scroll-mt-20 .flex .items-center .gap-2}

#### [COMPOSE_PROJECT_NAME](#compose_project_name) {#compose_project_name .scroll-mt-20 .flex .items-center .gap-2}

Sets the project name. This value is prepended along with the service name to the container\'s name on startup.

For example, if your project name is `myapp` and it includes two services `db` and `web`, then Compose starts containers named `myapp-db-1` and `myapp-web-1` respectively.

Compose can set the project name in different ways. The level of precedence (from highest to lowest) for each method is as follows:

1.  The `-p` command line flag
2.  `COMPOSE_PROJECT_NAME`
3.  The top-level `name:` variable from the config file (or the last `name:` from a series of config files specified using `-f`)
4.  The `basename` of the project directory containing the config file (or containing the first config file specified using `-f`)
5.  The `basename` of the current directory if no config file is specified

Project names must contain only lowercase letters, decimal digits, dashes, and underscores, and must begin with a lowercase letter or decimal digit. If the `basename` of the project directory or current directory violates this constraint, you must use one of the other mechanisms.

See also [using `-p` to specify a project name](/reference/cli/docker/compose/#use--p-to-specify-a-project-name).

#### [COMPOSE_FILE](#compose_file) {#compose_file .scroll-mt-20 .flex .items-center .gap-2}

Specifies the path to a Compose file. Specifying multiple Compose files is supported.

-   Default behavior: If not provided, Compose looks for a file named `compose.yaml` in the current directory and, if not found, then Compose searches each parent directory recursively until a file by that name is found.
-   When specifying multiple Compose files, the path separators are, by default, on:
    -   Mac and Linux: `:` (colon)

    -   Windows: `;` (semicolon) For example:

        ``` {.chroma tabindex="0"}
        COMPOSE_FILE=compose.yaml:compose.prod.yaml
        ```

    The path separator can also be customized using [`COMPOSE_PATH_SEPARATOR`](#compose_path_separator).

See also [using `-f` to specify name and path of one or more Compose files](/reference/cli/docker/compose/#use--f-to-specify-the-name-and-path-of-one-or-more-compose-files).

#### [COMPOSE_PROFILES](#compose_profiles) {#compose_profiles .scroll-mt-20 .flex .items-center .gap-2}

Specifies one or more profiles to be enabled when `docker compose up` is run.

Services with matching profiles are started as well as any services for which no profile has been defined.

For example, calling `docker compose up` with `COMPOSE_PROFILES=frontend` selects services with the `frontend` profile as well as any services without a profile specified.

If specifying multiple profiles, use a comma as a separator.

The following example enables all services matching both the `frontend` and `debug` profiles and services without a profile.

``` {.chroma tabindex="0"}
COMPOSE_PROFILES=frontend,debug
```

See also [Using profiles with Compose](https://docs.docker.com/compose/how-tos/profiles/) and the [`--profile` command-line option](/reference/cli/docker/compose/#use-profiles-to-enable-optional-services).

#### [COMPOSE_PATH_SEPARATOR](#compose_path_separator) {#compose_path_separator .scroll-mt-20 .flex .items-center .gap-2}

Specifies a different path separator for items listed in `COMPOSE_FILE`.

-   Defaults to:
    -   On macOS and Linux to `:`
    -   On Windows to`;`

#### [COMPOSE_ENV_FILES](#compose_env_files) {#compose_env_files .scroll-mt-20 .flex .items-center .gap-2}

Specifies which environment files Compose should use if `--env-file` isn\'t used.

When using multiple environment files, use a comma as a separator. For example:

``` {.chroma tabindex="0"}
COMPOSE_ENV_FILES=.env.envfile1,.env.envfile2
```

If `COMPOSE_ENV_FILES` is not set, and you don\'t provide `--env-file` in the CLI, Docker Compose uses the default behavior, which is to look for an `.env` file in the project directory.

#### [COMPOSE_DISABLE_ENV_FILE](#compose_disable_env_file) {#compose_disable_env_file .scroll-mt-20 .flex .items-center .gap-2}

Lets you disable the use of the default `.env` file.

-   Supported values:
    -   `true` or `1`, Compose ignores the `.env` file
    -   `false` or `0`, Compose looks for an `.env` file in the project directory
-   Defaults to: `0`

### [Environment handling and container lifecycle](#environment-handling-and-container-lifecycle) {#environment-handling-and-container-lifecycle .scroll-mt-20 .flex .items-center .gap-2}

#### [COMPOSE_CONVERT_WINDOWS_PATHS](#compose_convert_windows_paths) {#compose_convert_windows_paths .scroll-mt-20 .flex .items-center .gap-2}

When enabled, Compose performs path conversion from Windows-style to Unix-style in volume definitions.

-   Supported values:
    -   `true` or `1`, to enable
    -   `false` or `0`, to disable
-   Defaults to: `0`

#### [COMPOSE_IGNORE_ORPHANS](#compose_ignore_orphans) {#compose_ignore_orphans .scroll-mt-20 .flex .items-center .gap-2}

When enabled, Compose doesn\'t try to detect orphaned containers for the project.

-   Supported values:
    -   `true` or `1`, to enable
    -   `false` or `0`, to disable
-   Defaults to: `0`

#### [COMPOSE_REMOVE_ORPHANS](#compose_remove_orphans) {#compose_remove_orphans .scroll-mt-20 .flex .items-center .gap-2}

When enabled, Compose automatically removes orphaned containers when updating a service or stack. Orphaned containers are those that were created by a previous configuration but are no longer defined in the current `compose.yaml` file.

-   Supported values:
    -   `true` or `1`, to enable automatic removal of orphaned containers
    -   `false` or `0`, to disable automatic removal. Compose displays a warning about orphaned containers instead.
-   Defaults to: `0`

#### [COMPOSE_PARALLEL_LIMIT](#compose_parallel_limit) {#compose_parallel_limit .scroll-mt-20 .flex .items-center .gap-2}

Specifies the maximum level of parallelism for concurrent engine calls.

### [Output](#output) {#output .scroll-mt-20 .flex .items-center .gap-2}

#### [COMPOSE_ANSI](#compose_ansi) {#compose_ansi .scroll-mt-20 .flex .items-center .gap-2}

Specifies when to print ANSI control characters.

-   Supported values:
    -   `auto`, Compose detects if TTY mode can be used. Otherwise, use plain text mode
    -   `never`, use plain text mode
    -   `always` or `0`, use TTY mode
-   Defaults to: `auto`

#### [COMPOSE_STATUS_STDOUT](#compose_status_stdout) {#compose_status_stdout .scroll-mt-20 .flex .items-center .gap-2}

When enabled, Compose writes its internal status and progress messages to `stdout` instead of `stderr`. The default value is false to clearly separate the output streams between Compose messages and your container\'s logs.

-   Supported values:
    -   `true` or `1`, to enable
    -   `false` or `0`, to disable
-   Defaults to: `0`

#### [COMPOSE_PROGRESS](#compose_progress) {#compose_progress .scroll-mt-20 .flex .items-center .gap-2}

Requires: Docker Compose [2.36.0](https://github.com/docker/compose/releases/tag/v2.36.0) and later

Defines the type of progress output, if `--progress` isn\'t used.

Supported values are `auto`, `tty`, `plain`, `json`, and `quiet`. Default is `auto`.

### [User experience](#user-experience) {#user-experience .scroll-mt-20 .flex .items-center .gap-2}

#### [COMPOSE_MENU](#compose_menu) {#compose_menu .scroll-mt-20 .flex .items-center .gap-2}

Requires: Docker Compose [2.26.0](https://github.com/docker/compose/releases/tag/v2.26.0) and later

When enabled, Compose displays a navigation menu where you can choose to open the Compose stack in Docker Desktop, switch on [`watch` mode](https://docs.docker.com/compose/how-tos/file-watch/), or use [Docker Debug](/reference/cli/docker/debug/).

-   Supported values:
    -   `true` or `1`, to enable
    -   `false` or `0`, to disable
-   Defaults to: `1` if you obtained Docker Compose through Docker Desktop, otherwise the default is `0`

#### [COMPOSE_EXPERIMENTAL](#compose_experimental) {#compose_experimental .scroll-mt-20 .flex .items-center .gap-2}

Requires: Docker Compose [2.26.0](https://github.com/docker/compose/releases/tag/v2.26.0) and later

This is an opt-out variable. When turned off it deactivates the experimental features.

-   Supported values:
    -   `true` or `1`, to enable
    -   `false` or `0`, to disable
-   Defaults to: `1`

## [Unsupported in Compose V2](#unsupported-in-compose-v2) {#unsupported-in-compose-v2 .scroll-mt-20 .flex .items-center .gap-2}

The following environment variables have no effect in Compose V2.

-   `COMPOSE_API_VERSION` By default the API version is negotiated with the server. Use `DOCKER_API_VERSION`.\
    See the [Docker CLI environment variable reference](/reference/cli/docker/#environment-variables) page.
-   `COMPOSE_HTTP_TIMEOUT`
-   `COMPOSE_TLS_VERSION`
-   `COMPOSE_FORCE_WINDOWS_HOST`
-   `COMPOSE_INTERACTIVE_NO_CLI`
-   `COMPOSE_DOCKER_CLI_BUILD` Use `DOCKER_BUILDKIT` to select between BuildKit and the classic builder. If `DOCKER_BUILDKIT=0` then `docker compose build` uses the classic builder to build images.
