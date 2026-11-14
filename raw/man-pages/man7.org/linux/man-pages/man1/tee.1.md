---
{"title": "tee(1) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/tee.1.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# tee(1) --- Linux manual page

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [AUTHOR](#AUTHOR) \| [REPORTING BUGS](#REPORTING_BUGS) \| [COPYRIGHT](#COPYRIGHT) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                              |                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    TEE(1)                        User Commands                        TEE(1)

## [](#NAME)NAME

           tee - read from standard input and write to standard output and
           files

## [](#SYNOPSIS)SYNOPSIS

           tee [OPTION]... [FILE]...

## [](#DESCRIPTION)DESCRIPTION

           Copy standard input to each FILE, and also to standard output.

           -a, --append
                  append to the given FILEs, do not overwrite

           -i, --ignore-interrupts
                  ignore interrupt signals

           -p     operate in a more appropriate MODE with pipes

           --output-error[=MODE]
                  set behavior on write error.  See MODE below

           --help display this help and exit

           --version
                  output version information and exit

       MODE determines behavior with write errors on the outputs:
           warn   diagnose errors writing to any output

           warn-nopipe
                  diagnose errors writing to any output not a pipe

           exit   exit on error writing to any output

           exit-nopipe
                  exit on error writing to any output not a pipe

           The default MODE for the -p option is 'warn-nopipe'.  With
           "nopipe" MODEs, exit immediately if all outputs become broken
           pipes.  The default operation when --output-error is not
           specified, is to exit immediately on error writing to a pipe, and
           diagnose errors writing to non pipe outputs.

## [](#AUTHOR)AUTHOR

           Written by Mike Parker, Richard M. Stallman, and David MacKenzie.

## [](#REPORTING_BUGS)REPORTING BUGS

           Report bugs to: bug-coreutils@gnu.org
           GNU coreutils home page: <https://www.gnu.org/software/coreutils/>
           General help using GNU software: <https://www.gnu.org/gethelp/>
           Report any translation bugs to
           <https://translationproject.org/team/>

## [](#COPYRIGHT)COPYRIGHT

           Copyright © 2026 Free Software Foundation, Inc.  License GPLv3+:
           GNU GPL version 3 or later <https://gnu.org/licenses/gpl.html>.
           This is free software: you are free to change and redistribute it.
           There is NO WARRANTY, to the extent permitted by law.

## [](#SEE_ALSO)SEE ALSO

           Full documentation <https://www.gnu.org/software/coreutils/tee>
           or available locally via: info '(coreutils) tee invocation'

## [](#COLOPHON)COLOPHON

           This page is part of the coreutils (basic file, shell and text
           manipulation utilities) project.  Information about the project
           can be found at ⟨http://www.gnu.org/software/coreutils/⟩.  If you
           have a bug report for this manual page, see
           ⟨http://www.gnu.org/software/coreutils/⟩.  This page was obtained
           from the tarball coreutils-9.11.tar.xz fetched from
           ⟨http://ftp.gnu.org/gnu/coreutils/⟩ on 2026-08-03.  If you
           discover any rendering problems in this HTML version of the page,
           or you believe there is a better or more up-to-date source for the
           page, or you have corrections or improvements to the information
           in this COLOPHON (which is not part of the original manual page),
           send a mail to man-pages@man7.org

    GNU coreutils 9.11              April 2026                         TEE(1)

------------------------------------------------------------------------

Pages that refer to this page: [tee(2)](../man2/tee.2.html)

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
