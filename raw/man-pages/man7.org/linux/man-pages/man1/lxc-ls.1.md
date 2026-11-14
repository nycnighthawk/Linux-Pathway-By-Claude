---
{"title": "lxc-ls(1) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/lxc-ls.1.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# lxc-ls(1) --- Linux manual page

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [EXAMPLES](#EXAMPLES) \| [COMMON OPTIONS](#COMMON_OPTIONS) \| [SEE ALSO](#SEE_ALSO) \| [HISTORY](#HISTORY) \| [COLOPHON](#COLOPHON) |                                   |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                     |                                   |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    lxc-ls(1)                                                       lxc-ls(1)

## [](#NAME)NAME

           lxc-ls - list the containers existing on the system

## [](#SYNOPSIS)SYNOPSIS

           lxc-ls [-1] [--active] [--frozen] [--running] [--stopped]
                  [--defined] [-f] [-F format] [-g groups] [--nesting=NUM]
                  [--filter=regex]

## [](#DESCRIPTION)DESCRIPTION

           lxc-ls list the containers existing on the system.

## [](#OPTIONS)OPTIONS

           -1     Show one entry per line. (default when /dev/stdout isn't a
                  tty)

           --active
                  List only active containers (same as --frozen --running).

           --frozen
                  List only frozen containers.

           --running
                  List only running containers.

           --stopped
                  List only stopped containers.

           --defined
                  List only defined containers.

           -f,--fancy
                  Use a fancy, column-based output.

           -F,--fancy-format format
                  Comma separated list of columns to show in the fancy out‐
                  put.  The list of accepted and default fields is listed in
                  --help.

           -g,--groups groups
                  Comma separated list of groups the container must have to
                  be displayed.  The parameter may be passed multiple times.

           --nesting=NUM
                  Show nested containers. The number of nesting levels to be
                  shown can be specified by passing a number as argument.

           --filter=regex
                  The regular expression passed to lxc-ls will be applied to
                  the container name. The format is a POSIX extended regular
                  expression. It can also be given as additional argument
                  without explicitly using --filter.

## [](#EXAMPLES)EXAMPLES

           lxc-ls --fancy
                  list all the containers, listing one per line along with
                  its name, state, ipv4 and ipv6 addresses.

           lxc-ls --active -1
                  list active containers and display the list in one column.

## [](#COMMON_OPTIONS)COMMON OPTIONS

           These options are common to most of lxc commands.

           -?, -h, --help
                  Print a longer usage message than normal.

           --usage
                  Give the usage message

           -q, --quiet
                  mute on

           -P, --lxcpath=PATH
                  Use an alternate container path. The default is
                  /var/lib/lxc.

           -o, --logfile=FILE
                  Output to an alternate log FILE. The default is no log.

           -l, --logpriority=LEVEL
                  Set log priority to LEVEL. The default log priority is ER‐
                  ROR. Possible values are : FATAL, ALERT, CRIT, WARN, ERROR,
                  NOTICE, INFO, DEBUG, TRACE.

                  Note that this option is setting the priority of the events
                  log in the alternate log file. It do not have effect on the
                  ERROR events log on stderr.

           -n, --name=NAME
                  Use container identifier NAME.  The container identifier
                  format is an alphanumeric string.

           --rcfile=FILE
                  Specify the configuration file to configure the virtualiza‐
                  tion and isolation functionalities for the container.

                  This configuration file if present will be used even if
                  there is already a configuration file present in the previ‐
                  ously created container (via lxc-create).

           --version
                  Show the version number.

## [](#SEE_ALSO)SEE ALSO

           lxc(7), lxc-create(1), lxc-copy(1), lxc-destroy(1), lxc-start(1),
           lxc-stop(1), lxc-execute(1), lxc-console(1), lxc-monitor(1),
           lxc-wait(1), lxc-cgroup(1), lxc-ls(1), lxc-info(1), lxc-freeze(1),
           lxc-unfreeze(1), lxc-attach(1), lxc.conf(5)

## [](#HISTORY)HISTORY

           Written originally as a shell script by Daniel Lezcano and Serge
           Hallyn.  Later reimplemented and extended in Python by Stéphane
           Graber and then reimplemented and extended in C by Christian
           Brauner.

## [](#COLOPHON)COLOPHON

           This page is part of the lxc (Linux containers) project.  Informa‐
           tion about the project can be found at 
           ⟨http://linuxcontainers.org/⟩.  If you have a bug report for this
           manual page, send it to lxc-devel@lists.linuxcontainers.org.  This
           page was obtained from the project's upstream Git repository
           ⟨https://github.com/lxc/lxc.git⟩ on 2026-08-04.  (At that time,
           the date of the most recent commit that was found in the
           repository was 2026-07-23.)  If you discover any rendering
           problems in this HTML version of the page, or you believe there is
           a better or more up-to-date source for the page, or you have
           corrections or improvements to the information in this COLOPHON
           (which is not part of the original manual page), send a mail to
           man-pages@man7.org

                                    2026-04-29                      lxc-ls(1)

------------------------------------------------------------------------

Pages that refer to this page: [lxc-attach(1)](../man1/lxc-attach.1.html),  [lxc-autostart(1)](../man1/lxc-autostart.1.html),  [lxc-cgroup(1)](../man1/lxc-cgroup.1.html),  [lxc-checkconfig(1)](../man1/lxc-checkconfig.1.html),  [lxc-checkpoint(1)](../man1/lxc-checkpoint.1.html),  [lxc-config(1)](../man1/lxc-config.1.html),  [lxc-console(1)](../man1/lxc-console.1.html),  [lxc-copy(1)](../man1/lxc-copy.1.html),  [lxc-create(1)](../man1/lxc-create.1.html),  [lxc-destroy(1)](../man1/lxc-destroy.1.html),  [lxc-device(1)](../man1/lxc-device.1.html),  [lxc-execute(1)](../man1/lxc-execute.1.html),  [lxc-freeze(1)](../man1/lxc-freeze.1.html),  [lxc-info(1)](../man1/lxc-info.1.html),  [lxc-ls(1)](../man1/lxc-ls.1.html),  [lxc-monitor(1)](../man1/lxc-monitor.1.html),  [lxc-snapshot(1)](../man1/lxc-snapshot.1.html),  [lxc-start(1)](../man1/lxc-start.1.html),  [lxc-stop(1)](../man1/lxc-stop.1.html),  [lxc-top(1)](../man1/lxc-top.1.html),  [lxc-unfreeze(1)](../man1/lxc-unfreeze.1.html),  [lxc-unshare(1)](../man1/lxc-unshare.1.html),  [lxc-update-config(1)](../man1/lxc-update-config.1.html),  [lxc-usernsexec(1)](../man1/lxc-usernsexec.1.html),  [lxc-wait(1)](../man1/lxc-wait.1.html),  [lxc.container.conf(5)](../man5/lxc.container.conf.5.html),  [lxc.system.conf(5)](../man5/lxc.system.conf.5.html),  [lxc(7)](../man7/lxc.7.html)

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
