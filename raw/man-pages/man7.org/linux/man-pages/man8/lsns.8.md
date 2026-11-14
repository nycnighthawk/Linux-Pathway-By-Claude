---
{"title": "lsns(8) — Linux manual page", "url": "https://man7.org/linux/man-pages/man8/lsns.8.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# lsns(8) --- Linux manual page

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [EXIT STATUS](#EXIT_STATUS) \| [ENVIRONMENT](#ENVIRONMENT) \| [AUTHORS](#AUTHORS) \| [SEE ALSO](#SEE_ALSO) \| [REPORTING BUGS](#REPORTING_BUGS) \| [AVAILABILITY](#AVAILABILITY) |                                   |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                                                                  |                                   |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    LSNS(8)                   System Administration                   LSNS(8)

## [](#NAME)NAME

           lsns - list namespaces

## [](#SYNOPSIS)SYNOPSIS

           lsns [options] [namespace ID]

## [](#DESCRIPTION)DESCRIPTION

           lsns lists information about all the currently accessible
           namespaces or about the given namespace. The namespace identifier
           is an inode number.

           The default output is subject to change. So whenever possible, you
           should avoid using default outputs in your scripts. Always
           explicitly define expected output mode (--tree or --list) and
           columns by using the --output option together with a columns list
           in environments where a stable output is required.

           The NSFS column, printed when net is specified for the --type
           option, is special; it uses multi-line cells. Use the option
           --nowrap to switch to ","-separated single-line representation.

           Note that lsns reads information directly from the /proc
           filesystem and for unprivileged users it may return incomplete
           information. The current /proc filesystem may be unshared and
           affected by a PID namespace (see unshare --mount-proc for more
           details). lsns is not able to see persistent namespaces without
           processes where the namespace instance is held by a bind mount to
           /proc/pid/ns/type.

## [](#OPTIONS)OPTIONS

           -H, --list-columns
               List the columns that can be specified with the --output
               option. Can be used with --json or --raw to get the list in a
               machine-readable format.

           -J, --json
               Use JSON output format.

           -l, --list
               Use list output format.

           -n, --noheadings
               Do not print a header line.

           -o, --output list
               Specify which output columns to print. Use --help to get a
               list of all supported columns.

               The default list of columns may be extended if list is
               specified in the format +list (e.g., lsns -o +PATH).

           --output-all
               Output all available columns.

           -P, --persistent
               Display only the namespaces without processes (aka persistent
               namespaces), created by bind mounting /proc/pid/ns/type files
               to a filesystem path.

           -p, --task PID
               Display only the namespaces held by the process with this PID.

           -Q, --filter expr
               Print only the namespaces that meet the conditions specified
               by the expr.

               This feature is EXPERIMENTAL. See also scols-filter(5). For
               example exclude root as username, but print every namespaces
               more than one process belongs to:

                  lsns --filter 'USER != "root" and NPROCS > 1'

           -r, --raw
               Use the raw output format.

           -t, --type type
               Display the specified type of namespaces only. The supported
               types are mnt, net, ipc, user, pid, uts, cgroup and time. This
               option may be given more than once.

           -u, --notruncate
               Do not truncate text in columns.

           -W, --nowrap
               Do not use multi-line text in columns.

           -T, --tree[=rel]
               Use tree-like output format. If process is given as rel, print
               process tree(s) in each name space. This is default when
               --tree is not specified. If parent is given, print tree(s)
               constructed by the parent/child relationship. If owner is
               given, print tree(s) constructed by the owner/owned
               relationship. owner is used as default when rel is omitted.

           -h, --help
               Display help text and exit.

           -V, --version
               Display version and exit.

## [](#EXIT_STATUS)EXIT STATUS

           The lsns utility exits with one of the following values:

           0
               Success.

           1
               General error.

           2
               An ioctl was unknown to the kernel.

## [](#ENVIRONMENT)ENVIRONMENT

           LIBSMARTCOLS_DEBUG=all
               Enable libsmartcols debug output.

           LIBSMARTCOLS_DEBUG_PADDING=on
               Use visible padding characters.

           LIBSMARTCOLS_JSON=compact|lines
               Control JSON output format when using --json. Supported values
               are compact for JSON output with minimal whitespace, and lines
               for JSON Lines format (one JSON object per line). If unset or
               set to any other value, pretty-printed JSON is used.

           LSNS_DEBUG=all
               Enable lsns debug output.

## [](#AUTHORS)AUTHORS

           Karel Zak <kzak@redhat.com>

## [](#SEE_ALSO)SEE ALSO

           nsenter(1), unshare(1), clone(2), namespaces(7), ioctl_ns(2),
           ip-netns(8), scols-filter(5)

## [](#REPORTING_BUGS)REPORTING BUGS

           For bug reports, use the issue tracker
           <https://github.com/util-linux/util-linux/issues>.

## [](#AVAILABILITY)AVAILABILITY

           The lsns command is part of the util-linux package which can be
           downloaded from Linux Kernel Archive
           <https://www.kernel.org/pub/linux/utils/util-linux/>. This page is
           part of the util-linux (a random collection of Linux utilities)
           project. Information about the project can be found at 
           ⟨https://www.kernel.org/pub/linux/utils/util-linux/⟩. If you have a
           bug report for this manual page, send it to
           util-linux@vger.kernel.org. This page was obtained from the
           project's upstream Git repository
           ⟨git://git.kernel.org/pub/scm/utils/util-linux/util-linux.git⟩ on
           2026-08-04. (At that time, the date of the most recent commit that
           was found in the repository was 2026-08-03.) If you discover any
           rendering problems in this HTML version of the page, or you
           believe there is a better or more up-to-date source for the page,
           or you have corrections or improvements to the information in this
           COLOPHON (which is not part of the original manual page), send a
           mail to man-pages@man7.org

    util-linux 2.43.devel-739-eee2e 2026-05-24                        LSNS(8)

------------------------------------------------------------------------

Pages that refer to this page: [nsenter(1)](../man1/nsenter.1.html),  [unshare(1)](../man1/unshare.1.html),  [namespaces(7)](../man7/namespaces.7.html)

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
