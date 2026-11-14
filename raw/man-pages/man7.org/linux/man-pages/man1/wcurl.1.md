---
{"title": "wcurl(1) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/wcurl.1.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# wcurl(1) --- Linux manual page

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [CURL_OPTIONS](#CURL_OPTIONS) \| [URL](#URL) \| [EXAMPLES](#EXAMPLES) \| [AUTHORS](#AUTHORS) \| [REPORTING BUGS](#REPORTING_BUGS) \| [COPYRIGHT](#COPYRIGHT) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                                                                                                |                                   |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    wcurl(1)                 General Commands Manual                 wcurl(1)

## [](#NAME)NAME

           wcurl - a simple wrapper around curl to easily download files.

## [](#SYNOPSIS)SYNOPSIS

           wcurl <URL>...

           wcurl [--curl-options <CURL_OPTIONS>]... [--dry-run]
           [--no-decode-filename] [-o|-O|--output <PATH>] [--] <URL>...

           wcurl [--curl-options=<CURL_OPTIONS>]... [--dry-run]
           [--no-decode-filename] [--output=<PATH>] [--] <URL>...

           wcurl -V|--version

           wcurl -h|--help

## [](#DESCRIPTION)DESCRIPTION

           wcurl is a simple curl wrapper which lets you use curl to download
           files without having to remember any parameters.

           Call wcurl with a list of URLs you want to download and wcurl
           picks sane defaults.

           If you need anything more complex, you can provide any of curl's
           supported parameters via the --curl-options option. Beware that
           you likely should be using curl directly if your use case is not
           covered.

           By default, wcurl does:

           * Percent-encode whitespace in URLs;

           * Download multiple URLs in parallel
                  if the installed curl's version is >= 7.66.0 (--parallel);

           * Use a total number of 5 parallel connections to the same
           protocol + hostname + port number target
                  if the installed curl's version is >= 8.16.0 (--parallel-max-host);

           * Follow redirects;

           * Automatically choose a filename as output;

           * Avoid overwriting files
                  if the installed curl's version is >= 7.83.0 (--no-clobber);

           * Perform retries;

           * Set the downloaded file timestamp
                  to the value provided by the server, if available;

           * Default to https
                  if the URL does not contain any scheme;

           * Disable curl's URL globbing parser
                  so {} and [] characters in URLs are not treated specially;

           * Percent-decode the resulting filename;

           * Use 'index.html' as the default filename
                  if there is none in the URL.

## [](#OPTIONS)OPTIONS

           --curl-options, --curl-options=<CURL_OPTIONS>...
                  Specify extra options to be passed when invoking curl. May
                  be specified more than once.

           -o, -O, --output, --output=<PATH>
                  Use the provided output path instead of getting it from the
                  URL. If multiple URLs are provided, resulting files share
                  the same name with a number appended to the end (curl >=
                  7.83.0). If this option is provided multiple times, only
                  the last value is considered.

           --no-decode-filename
                  Do not percent-decode the output filename, even if the
                  percent-encoding in the URL was done by wcurl, e.g.: The
                  URL contained whitespace.

           --dry-run
                  Do not actually execute curl, print what would be invoked.

           -V, --version
                  Print version information.

           -h, --help
                  Print help message.

## [](#CURL_OPTIONS)CURL_OPTIONS

           Any option supported by curl can be set here. This is not used by
           wcurl; it is instead forwarded to the curl invocation.

## [](#URL)URL

           URL to be downloaded. Anything that is not a parameter is
           considered an URL. Whitespace is percent-encoded and the URL is
           passed to curl, which then performs the parsing. May be specified
           more than once.

## [](#EXAMPLES)EXAMPLES

           Download a single file:

           wcurl example.com/filename.txt

           Download two files in parallel:

           wcurl example.com/filename1.txt example.com/filename2.txt

           Download a file passing the --progress-bar and --http2 flags to
           curl:

           wcurl --curl-options="--progress-bar --http2"
           example.com/filename.txt

           Resume from an interrupted download. The options necessary to
           resume the download (--clobber --continue-at -) must be the last
           options specified in --curl-options.  Note that the only way to
           resume interrupted downloads is to allow wcurl to overwrite the
           destination file:

           wcurl --curl-options="--clobber --continue-at -"
           example.com/filename.txt

           Download multiple files without a limit of concurrent connections
           per host (the default limit is 5):

           wcurl --curl-options="--parallel-max-host 0"
           example.com/filename1.txt example.com/filename2.txt

## [](#AUTHORS)AUTHORS

           Samuel Henrique <samueloph@debian.org>
           Sergio Durigan Junior <sergiodj@debian.org>
           and many contributors, see the AUTHORS file.

## [](#REPORTING_BUGS)REPORTING BUGS

           If you experience any problems with wcurl that you do not
           experience with curl, submit an issue on GitHub:
           https://github.com/curl/wcurl

## [](#COPYRIGHT)COPYRIGHT

           wcurl is licensed under the curl license

## [](#SEE_ALSO)SEE ALSO

           curl(1), trurl(1)

## [](#COLOPHON)COLOPHON

           This page is part of the curl (Command line tool and library for
           transferring data with URLs) project.  Information about the
           project can be found at ⟨https://curl.haxx.se/⟩.  If you have a
           bug report for this manual page, see
           ⟨https://curl.haxx.se/docs/bugs.html⟩.  This page was obtained
           from the project's upstream Git repository
           ⟨https://github.com/curl/curl.git⟩ on 2026-08-03.  (At that time,
           the date of the most recent commit that was found in the
           repository was 2026-08-03.)  If you discover any rendering
           problems in this HTML version of the page, or you believe there is
           a better or more up-to-date source for the page, or you have
           corrections or improvements to the information in this COLOPHON
           (which is not part of the original manual page), send a mail to
           man-pages@man7.org

    wcurl                           2026-05-24                       wcurl(1)

------------------------------------------------------------------------

------------------------------------------------------------------------

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------+----------------------------+
| HTML rendering created 2026-09-09 by [Michael Kerrisk](https://man7.org/mtk/index.html), author of [*The Linux Programming Interface*](https://man7.org/tlpi/). |                       | [](https://man7.org/tlpi/) |
|                                                                                                                                                                 |                       |                            |
| For details of in-depth **Linux/UNIX system programming training courses** that I teach, look [here](https://man7.org/training/).                               |                       |                            |
|                                                                                                                                                                 |                       |                            |
| Hosting by [jambit GmbH](https://www.jambit.com/index_en.html).                                                                                                 |                       |                            |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------+----------------------------+

------------------------------------------------------------------------
