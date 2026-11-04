---
{"title": "Oil Shell", "url": "https://wiki.archlinux.org/title/Oil_Shell", "retrieved": "2026-11-01", "license": "GFDL-1.3-or-later"}
---

# Oil Shell

**Oil Shell** (OSH) is a Bash-compatible UNIX [command-line shell](../en/Command-line_shell.html "Command-line shell"). OSH can be run on most UNIX-like operating systems, including GNU/Linux. It is written in Python (v2.7), but ships with a native executable. The dialect of Bash recognized by OSH is called the OSH language.

## Installation {#Installation}

[Install](../en/Help:Reading.html#Installation_of_packages "Install") the [oils-for-unix](https://archlinux.org/packages/?name=oils-for-unix) package.

### Smoke Test {#Smoke_Test}

Make sure that OSH has been installed correctly by running the following in a terminal:

    $ osh

This will start an OSH session and display a shell prompt:

    osh$

Identify an installed binary and attempt to invoke it in the OSH session to confirm that the output is correct.

For example:

    osh$ ls
    ...

### Making OSH your default shell {#Making_OSH_your_default_shell}

See [Command-line shell#Changing your default shell](../en/Command-line_shell.html#Changing_your_default_shell "Command-line shell").

## Removal {#Removal}

See [Command-line shell#Uninstalling shell](../en/Command-line_shell.html#Uninstalling_shell "Command-line shell").

## Troubleshooting {#Troubleshooting}

Reproducible bugs/errors may be reported on [Github](https://github.com/oils-for-unix/oils/issues). When filing a report, please include the output of OSH when it is running in verbose mode. To enable verbose mode, execute the following:

    $> export OVM_VERBOSE=1

## See also {#See_also}

-   [Oil Github](https://github.com/oils-for-unix/oils)
-   [Oil Project Home](https://www.oils.pub/)
-   [Oil Twitter Feed](https://x.com/oilsforunix)
-   [Oil Subreddit](https://old.reddit.com/r/oilsforunix/)
