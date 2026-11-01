---
{"title": "Format command and log output", "url": "https://docs.docker.com/engine/cli/formatting/", "retrieved": "2026-11-01", "license": "Apache-2.0"}
---

# Format command and log output {#format-command-and-log-output pagefind-weight="10"}

------------------------------------------------------------------------

Table of contents

------------------------------------------------------------------------

Docker supports [Go templates](https://golang.org/pkg/text/template/) which you can use to manipulate the output format of certain commands and log drivers.

Docker provides a set of basic functions to manipulate template elements. All of these examples use the `docker inspect` command, but many other CLI commands have a `--format` flag, and many of the CLI command references include examples of customizing the output format.

> Note
>
> When using the `--format` flag, you need to observe your shell environment. In a POSIX shell, you can run the following with a single quote:
>
> ``` {.chroma tabindex="0"}
> $ docker inspect --format '{{join .Args " , "}}'
> ```
>
> Otherwise, in a Windows shell (for example, PowerShell), you need to use single quotes, but escape the double quotes inside the parameters as follows:
>
> ``` {.chroma tabindex="0"}
> $ docker inspect --format '{{join .Args \" , \"}}'
> ```

## [join](#join) {#join .scroll-mt-20 .flex .items-center .gap-2}

`join` concatenates a list of strings to create a single string. It puts a separator between each element in the list.

``` {.chroma tabindex="0"}
$ docker inspect --format '{{join .Args " , "}}' container
```

## [table](#table) {#table .scroll-mt-20 .flex .items-center .gap-2}

`table` specifies which fields you want to see its output.

``` {.chroma tabindex="0"}
$ docker image list --format "table {{.ID}}\t{{.Repository}}\t{{.Tag}}\t{{.Size}}"
```

## [json](#json) {#json .scroll-mt-20 .flex .items-center .gap-2}

`json` encodes an element as a json string.

``` {.chroma tabindex="0"}
$ docker inspect --format '{{json .Mounts}}' container
```

## [lower](#lower) {#lower .scroll-mt-20 .flex .items-center .gap-2}

`lower` transforms a string into its lowercase representation.

``` {.chroma tabindex="0"}
$ docker inspect --format "{{lower .Name}}" container
```

## [split](#split) {#split .scroll-mt-20 .flex .items-center .gap-2}

`split` slices a string into a list of strings separated by a separator.

``` {.chroma tabindex="0"}
$ docker inspect --format '{{split .Image ":"}}' container
```

## [title](#title) {#title .scroll-mt-20 .flex .items-center .gap-2}

`title` capitalizes the first character of a string.

``` {.chroma tabindex="0"}
$ docker inspect --format "{{title .Name}}" container
```

## [upper](#upper) {#upper .scroll-mt-20 .flex .items-center .gap-2}

`upper` transforms a string into its uppercase representation.

``` {.chroma tabindex="0"}
$ docker inspect --format "{{upper .Name}}" container
```

## [pad](#pad) {#pad .scroll-mt-20 .flex .items-center .gap-2}

`pad` adds whitespace padding to a string. You can specify the number of spaces to add before and after the string.

``` {.chroma tabindex="0"}
$ docker image list --format '{{pad .Repository 5 10}}'
```

This example adds 5 spaces before the image repository name and 10 spaces after.

## [truncate](#truncate) {#truncate .scroll-mt-20 .flex .items-center .gap-2}

`truncate` shortens a string to a specified length. If the string is shorter than the specified length, it remains unchanged.

``` {.chroma tabindex="0"}
$ docker image list --format '{{truncate .Repository 15}}'
```

This example displays the image repository name, truncating it to the first 15 characters if it\'s longer.

## [`println`](#println) {#println .scroll-mt-20 .flex .items-center .gap-2}

`println` prints each value on a new line.

``` {.chroma tabindex="0"}
$ docker inspect --format='{{range .NetworkSettings.Networks}}{{println .IPAddress}}{{end}}' container
```

## [Hint](#hint) {#hint .scroll-mt-20 .flex .items-center .gap-2}

To find out what data can be printed, show all content as json:

``` {.chroma tabindex="0"}
$ docker container ls --format='{{json .}}'
```
