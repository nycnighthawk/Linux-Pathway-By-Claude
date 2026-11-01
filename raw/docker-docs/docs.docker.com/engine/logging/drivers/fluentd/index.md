---
{"title": "Fluentd logging driver", "url": "https://docs.docker.com/engine/logging/drivers/fluentd/", "retrieved": "2026-11-01", "license": "Apache-2.0"}
---

# Fluentd logging driver {#fluentd-logging-driver pagefind-weight="10"}

------------------------------------------------------------------------

Table of contents

------------------------------------------------------------------------

The `fluentd` logging driver sends container logs to the [Fluentd](https://www.fluentd.org) collector as structured log data. Then, users can use any of the [various output plugins of Fluentd](https://www.fluentd.org/plugins) to write these logs to various destinations.

In addition to the log message itself, the `fluentd` log driver sends the following metadata in the structured log message:

  Field              Description
  ------------------ --------------------------------------------------------------------------------------------------------------------------------------------------------
  `container_id`     The full 64-character container ID.
  `container_name`   The container name at the time it was started. If you use `docker rename` to rename a container, the new name isn\'t reflected in the journal entries.
  `source`           `stdout` or `stderr`
  `log`              The container log

## [Usage](#usage) {#usage .scroll-mt-20 .flex .items-center .gap-2}

Some options are supported by specifying `--log-opt` as many times as needed:

-   `fluentd-address`: specify a socket address to connect to the Fluentd daemon, ex `fluentdhost:24224` or `unix:///path/to/fluentd.sock`.
-   `tag`: specify a tag for Fluentd messages. Supports some Go template markup, ex `{{.ID}}`, `{{.FullID}}` or `{{.Name}}` `docker.{{.ID}}`.

To use the `fluentd` driver as the default logging driver, set the `log-driver` and `log-opt` keys to appropriate values in the `daemon.json` file. For more about configuring Docker using `daemon.json`, see [daemon.json](https://docs.docker.com/reference/cli/dockerd/#daemon-configuration-file).

> Note
>
> If you\'re using Docker Desktop, edit the daemon configuration through the Docker Desktop Dashboard. Open **Settings** and select **Docker Engine**. For details, see [Docker Engine settings](https://docs.docker.com/desktop/settings-and-maintenance/settings/#docker-engine).

The following example sets the log driver to `fluentd` and sets the `fluentd-address` option.

``` {.chroma tabindex="0"}
{
  "log-driver": "fluentd",
  "log-opts": {
    "fluentd-address": "fluentdhost:24224"
  }
}
```

Restart Docker for the changes to take effect.

> Note
>
> `log-opts` configuration options in the `daemon.json` configuration file must be provided as strings. Boolean and numeric values (such as the value for `fluentd-async` or `fluentd-max-retries`) must therefore be enclosed in quotes (`"`).

To set the logging driver for a specific container, pass the `--log-driver` option to `docker run`:

``` {.chroma tabindex="0"}
$ docker run --log-driver=fluentd ...
```

Before using this logging driver, launch a Fluentd daemon. The logging driver connects to this daemon through `localhost:24224` by default. Use the `fluentd-address` option to connect to a different address.

``` {.chroma tabindex="0"}
$ docker run --log-driver=fluentd --log-opt fluentd-address=fluentdhost:24224
```

If container cannot connect to the Fluentd daemon, the container stops immediately unless the `fluentd-async` option is used.

## [Options](#options) {#options .scroll-mt-20 .flex .items-center .gap-2}

Users can use the `--log-opt NAME=VALUE` flag to specify additional Fluentd logging driver options.

### [fluentd-address](#fluentd-address) {#fluentd-address .scroll-mt-20 .flex .items-center .gap-2}

By default, the logging driver connects to `localhost:24224`. Supply the `fluentd-address` option to connect to a different address. `tcp`(default) and `unix` sockets are supported.

``` {.chroma tabindex="0"}
$ docker run --log-driver=fluentd --log-opt fluentd-address=fluentdhost:24224
$ docker run --log-driver=fluentd --log-opt fluentd-address=tcp://fluentdhost:24224
$ docker run --log-driver=fluentd --log-opt fluentd-address=unix:///path/to/fluentd.sock
```

Two of the above specify the same address, because `tcp` is default.

### [tag](#tag) {#tag .scroll-mt-20 .flex .items-center .gap-2}

By default, Docker uses the first 12 characters of the container ID to tag log messages. Refer to the [log tag option documentation](https://docs.docker.com/engine/logging/log_tags/) for customizing the log tag format.

### [labels, labels-regex, env, and env-regex](#labels-labels-regex-env-and-env-regex) {#labels-labels-regex-env-and-env-regex .scroll-mt-20 .flex .items-center .gap-2}

The `labels` and `env` options each take a comma-separated list of keys. If there is collision between `label` and `env` keys, the value of the `env` takes precedence. Both options add additional fields to the extra attributes of a logging message.

The `env-regex` and `labels-regex` options are similar to and compatible with respectively `env` and `labels`. Their values are regular expressions to match logging-related environment variables and labels. It is used for advanced [log tag options](https://docs.docker.com/engine/logging/log_tags/).

### [fluentd-async](#fluentd-async) {#fluentd-async .scroll-mt-20 .flex .items-center .gap-2}

Docker connects to Fluentd in the background. Messages are buffered until the connection is established. Defaults to `false`.

### [fluentd-async-reconnect-interval](#fluentd-async-reconnect-interval) {#fluentd-async-reconnect-interval .scroll-mt-20 .flex .items-center .gap-2}

When `fluentd-async` is enabled, the `fluentd-async-reconnect-interval` option defines the interval, in milliseconds, at which the connection to `fluentd-address` is re-established. This option is useful if the address resolves to one or more IP addresses, for example a Consul service address.

### [fluentd-buffer-limit](#fluentd-buffer-limit) {#fluentd-buffer-limit .scroll-mt-20 .flex .items-center .gap-2}

Sets the number of events buffered on the memory. Records will be stored in memory up to this number. If the buffer is full, the call to record logs will fail. The default is 1048576. ([https://github.com/fluent/fluent-logger-golang/tree/master#bufferlimit](https://github.com/fluent/fluent-logger-golang/tree/master#bufferlimit))

### [fluentd-retry-wait](#fluentd-retry-wait) {#fluentd-retry-wait .scroll-mt-20 .flex .items-center .gap-2}

How long to wait between retries. Defaults to 1 second.

### [fluentd-max-retries](#fluentd-max-retries) {#fluentd-max-retries .scroll-mt-20 .flex .items-center .gap-2}

The maximum number of retries. Defaults to `4294967295` (2\*\*32 - 1).

### [fluentd-sub-second-precision](#fluentd-sub-second-precision) {#fluentd-sub-second-precision .scroll-mt-20 .flex .items-center .gap-2}

Generates event logs in nanosecond resolution. Defaults to `false`.

### [fluentd-write-timeout](#fluentd-write-timeout) {#fluentd-write-timeout .scroll-mt-20 .flex .items-center .gap-2}

Sets the timeout for the write call to the `fluentd` daemon. By default, writes have no timeout and will block indefinitely.

## [Fluentd daemon management with Docker](#fluentd-daemon-management-with-docker) {#fluentd-daemon-management-with-docker .scroll-mt-20 .flex .items-center .gap-2}

About `Fluentd` itself, see [the project webpage](https://www.fluentd.org) and [its documents](https://docs.fluentd.org).

To use this logging driver, start the `fluentd` daemon on a host. We recommend that you use [the Fluentd docker image](https://hub.docker.com/r/fluent/fluentd/). This image is especially useful if you want to aggregate multiple container logs on each host then, later, transfer the logs to another Fluentd node to create an aggregate store.

### [Test container loggers](#test-container-loggers) {#test-container-loggers .scroll-mt-20 .flex .items-center .gap-2}

1.  Write a configuration file (`test.conf`) to dump input logs:

    ``` {.chroma tabindex="0"}
    <source>
      @type forward
    </source>

    <match *>
      @type stdout
    </match>
    ```

2.  Launch Fluentd container with this configuration file:

    ``` {.chroma tabindex="0"}
    $ docker run -it -p 24224:24224 -v /path/to/conf/test.conf:/fluentd/etc/test.conf -e FLUENTD_CONF=test.conf fluent/fluentd:latest
    ```

3.  Start one or more containers with the `fluentd` logging driver:

    ``` {.chroma tabindex="0"}
    $ docker run --log-driver=fluentd your/application
    ```
