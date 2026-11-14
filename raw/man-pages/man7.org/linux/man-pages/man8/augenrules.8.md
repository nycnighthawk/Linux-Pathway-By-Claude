---
{"title": "augenrules(8) — Linux manual page", "url": "https://man7.org/linux/man-pages/man8/augenrules.8.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# augenrules(8) --- Linux manual page

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [FILES](#FILES) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                   |                                   |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    AUGENRULES(8)        System Administration Utilities        AUGENRULES(8)

## [](#NAME)NAME

           augenrules - a script that merges component audit rule files

## [](#SYNOPSIS)SYNOPSIS

           augenrules [--check] [--load]

## [](#DESCRIPTION)DESCRIPTION

           augenrules is a script that merges all component audit rules
           files, found in the audit rules directory, /etc/audit/rules.d,
           placing the merged file in /etc/audit/audit.rules. Component audit
           rule files, must end in .rules in order to be processed. All other
           files in /etc/audit/rules.d are ignored.

           The files are concatenated in order, based on their natural sort
           (see -v option of ls(1)) and stripped of empty and comment (#)
           lines.

           The last processed -D directive without an option, if present, is
           always emitted as the first line in the resultant file. Those with
           an option are replicated in place.  The last processed -b
           directive, if present, is always emitted as the second line in the
           resultant file.  The last processed -f directive, if present, is
           always emitted as the third line in the resultant file.  The last
           processed -e directive, if present, is always emitted as the last
           line in the resultant file.

           The generated file is only copied to /etc/audit/audit.rules, if it
           differs.

## [](#OPTIONS)OPTIONS

           --check
                  test if rules have changed and need updating without
                  overwriting audit.rules.

           --load load old or newly built rules into the kernel.

## [](#FILES)FILES

           /etc/audit/rules.d/ /etc/audit/audit.rules

## [](#SEE_ALSO)SEE ALSO

           audit.rules(7), auditctl(8), auditd(8).

## [](#COLOPHON)COLOPHON

           This page is part of the audit (Linux Audit) project.  Information
           about the project can be found at 
           ⟨http://people.redhat.com/sgrubb/audit/⟩.  If you have a bug report
           for this manual page, send it to linux-audit@redhat.com.  This
           page was obtained from the project's upstream Git repository
           ⟨https://github.com/linux-audit/audit-userspace.git⟩ on
           2026-08-03.  (At that time, the date of the most recent commit
           that was found in the repository was 2026-07-29.)  If you discover
           any rendering problems in this HTML version of the page, or you
           believe there is a better or more up-to-date source for the page,
           or you have corrections or improvements to the information in this
           COLOPHON (which is not part of the original manual page), send a
           mail to man-pages@man7.org

    Red Hat                          Apr 2013                   AUGENRULES(8)

------------------------------------------------------------------------

Pages that refer to this page: [auditd(8)](../man8/auditd.8.html)

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
