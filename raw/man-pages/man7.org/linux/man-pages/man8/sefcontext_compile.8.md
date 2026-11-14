---
{"title": "sefcontext_compile(8) — Linux manual page", "url": "https://man7.org/linux/man-pages/man8/sefcontext_compile.8.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# sefcontext_compile(8) --- Linux manual page

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [RETURN VALUE](#RETURN_VALUE) \| [EXAMPLES](#EXAMPLES) \| [AUTHOR](#AUTHOR) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                               |                                   |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    sefcon...ompile(8)  SELinux Command Line documentation sefcon...ompile(8)

## [](#NAME)NAME

           sefcontext_compile - compile file context regular expression files

## [](#SYNOPSIS)SYNOPSIS

           sefcontext_compile [-o outputfile] [-p policyfile] inputfile

## [](#DESCRIPTION)DESCRIPTION

           sefcontext_compile is used to compile file context regular
           expressions into pcre(3) format.

           The compiled file is used by libselinux file labeling functions.

           By default sefcontext_compile writes the compiled pcre file with
           the .bin suffix appended (e.g. inputfile.bin).

## [](#OPTIONS)OPTIONS

           -o     Specify an outputfile that must be a fully qualified file
                  name as the .bin suffix is not automatically added.

           -p     Specify a binary policyfile that will be used to validate
                  the context entries in the inputfile
                  If an invalid context is found the pcre formatted file will
                  not be written and an error will be returned.

## [](#RETURN_VALUE)RETURN VALUE

           On error -1 is returned.  On success 0 is returned.

## [](#EXAMPLES)EXAMPLES

           Example 1:
           sefcontext_compile
           /etc/selinux/targeted/contexts/files/file_contexts

           Results in the following file being generated:
                  /etc/selinux/targeted/contexts/files/file_contexts.bin

           Example 2:
           sefcontext_compile -o new_fc.bin
           /etc/selinux/targeted/contexts/files/file_contexts

           Results in the following file being generated in the cwd:
                  new_fc.bin

## [](#AUTHOR)AUTHOR

           Dan Walsh, <dwalsh@redhat.com>

## [](#SEE_ALSO)SEE ALSO

           selinux(8), semanage(8),

## [](#COLOPHON)COLOPHON

           This page is part of the selinux (Security-Enhanced Linux user-
           space libraries and tools) project.  Information about the project
           can be found at ⟨https://github.com/SELinuxProject/selinux/wiki⟩.
           If you have a bug report for this manual page, see
           ⟨https://github.com/SELinuxProject/selinux/wiki/Contributing⟩.
           This page was obtained from the project's upstream Git repository
           ⟨https://github.com/SELinuxProject/selinux⟩ on 2026-08-04.  (At
           that time, the date of the most recent commit that was found in
           the repository was 2026-08-03.)  If you discover any rendering
           problems in this HTML version of the page, or you believe there is
           a better or more up-to-date source for the page, or you have
           corrections or improvements to the information in this COLOPHON
           (which is not part of the original manual page), send a mail to
           man-pages@man7.org

    dwalsh@redhat.com              12 Aug 2015             sefcon...ompile(8)

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
