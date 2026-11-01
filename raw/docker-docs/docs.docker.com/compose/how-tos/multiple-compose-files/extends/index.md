---
{"title": "Extend your Compose file", "url": "https://docs.docker.com/compose/how-tos/multiple-compose-files/extends/", "retrieved": "2026-11-01", "license": "Apache-2.0"}
---

# Extend your Compose file {#extend-your-compose-file pagefind-weight="10"}

------------------------------------------------------------------------

Table of contents

------------------------------------------------------------------------

Docker Compose\'s [`extends` attribute](https://docs.docker.com/reference/compose-file/services/#extends) lets you share common configurations among different files, or even different projects entirely.

Extending services is useful if you have several services that reuse a common set of configuration options. With `extends` you can define a common set of service options in one place and refer to it from anywhere. You can refer to another Compose file and select a service you want to also use in your own application, with the ability to override some attributes for your own needs.

> Important
>
> When you use multiple Compose files, you must make sure all paths in the files are relative to the base Compose file (i.e. the Compose file in your main-project folder). This is required because extend files need not be valid Compose files. Extend files can contain small fragments of configuration. Tracking which fragment of a service is relative to which path is difficult and confusing, so to keep paths easier to understand, all paths must be defined relative to the base file.

> Note
>
> `extends` is not supported when deploying with `docker stack deploy`. Running `docker stack config` on a Compose file that uses `extends` returns the error: `Configuration contains forbidden properties`.

## [How the `extends` attribute works](#how-the-extends-attribute-works) {#how-the-extends-attribute-works .scroll-mt-20 .flex .items-center .gap-2}

### [Extending services from another file](#extending-services-from-another-file) {#extending-services-from-another-file .scroll-mt-20 .flex .items-center .gap-2}

Take the following example:

``` {.chroma tabindex="0"}
services:
  web:
    extends:
      file: common-services.yml
      service: webapp
```

This instructs Compose to reuse only the properties of the `webapp` service defined in the `common-services.yml` file. The `webapp` service itself is not part of the final project.

If `common-services.yml` looks like this:

``` {.chroma tabindex="0"}
services:
  webapp:
    build: .
    ports:
      - "8000:8000"
    volumes:
      - "/data"
```

You get exactly the same result as if you wrote `compose.yaml` with the same `build`, `ports`, and `volumes` configuration values defined directly under `web`.

To include the service `webapp` in the final project when extending services from another file, you need to explicitly include both services in your current Compose file. For example (this is for illustrative purposes only):

``` {.chroma tabindex="0"}
services:
  web:
    build: ./alpine
    command: echo
    extends:
      file: common-services.yml
      service: webapp
  webapp:
    extends:
      file: common-services.yml
      service: webapp
```

Alternatively, you can use [include](https://docs.docker.com/compose/how-tos/multiple-compose-files/include/).

### [Extending services within the same file](#extending-services-within-the-same-file) {#extending-services-within-the-same-file .scroll-mt-20 .flex .items-center .gap-2}

If you define services in the same Compose file and extend one service from another, both the original service and the extended service will be part of your final configuration. For example:

``` {.chroma tabindex="0"}
services:
  web:
    build: ./alpine
    extends: webapp
  webapp:
    environment:
      - DEBUG=1
```

### [Extending services within the same file and from another file](#extending-services-within-the-same-file-and-from-another-file) {#extending-services-within-the-same-file-and-from-another-file .scroll-mt-20 .flex .items-center .gap-2}

You can go further and define, or re-define, configuration locally in `compose.yaml`:

``` {.chroma tabindex="0"}
services:
  web:
    extends:
      file: common-services.yml
      service: webapp
    environment:
      - DEBUG=1
    cpu_shares: 5

  important_web:
    extends: web
    cpu_shares: 10
```

## [Additional example](#additional-example) {#additional-example .scroll-mt-20 .flex .items-center .gap-2}

Extending an individual service is useful when you have multiple services that have a common configuration. The example below is a Compose app with two services, a web application and a queue worker. Both services use the same codebase and share many configuration options.

The `common.yaml` file defines the common configuration:

``` {.chroma tabindex="0"}
services:
  app:
    build: .
    environment:
      CONFIG_FILE_PATH: /code/config
      API_KEY: xxxyyy
    cpu_shares: 5
```

The `compose.yaml` defines the concrete services which use the common configuration:

``` {.chroma tabindex="0"}
services:
  webapp:
    extends:
      file: common.yaml
      service: app
    command: /code/run_web_app
    ports:
      - 8080:8080
    depends_on:
      - queue
      - db

  queue_worker:
    extends:
      file: common.yaml
      service: app
    command: /code/run_worker
    depends_on:
      - queue
```

## [Relative paths](#relative-paths) {#relative-paths .scroll-mt-20 .flex .items-center .gap-2}

When using `extends` with a `file` attribute which points to another folder, relative paths declared by the service being extended are converted so they still point to the same file when used by the extending service. This is illustrated in the following example:

Base Compose file:

``` {.chroma tabindex="0"}
services:
  webapp:
    image: example
    extends:
      file: ../commons/compose.yaml
      service: base
```

The `commons/compose.yaml` file:

``` {.chroma tabindex="0"}
services:
  base:
    env_file: ./container.env
```

The resulting service refers to the original `container.env` file within the `commons` directory. This can be confirmed with `docker compose config` which inspects the actual model:

``` {.chroma tabindex="0"}
services:
  webapp:
    image: example
    env_file: 
      - ../commons/container.env
```

## [Reference information](#reference-information) {#reference-information .scroll-mt-20 .flex .items-center .gap-2}

-   [`extends`](https://docs.docker.com/reference/compose-file/services/#extends)
