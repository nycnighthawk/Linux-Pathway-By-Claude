---
{"title": "error::pass1(7stap) — Linux manual page", "url": "https://man7.org/linux/man-pages/man7/error::pass1.7stap.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# error::pass1(7stap) --- Linux manual page

+-------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [DESCRIPTION](#DESCRIPTION) \| [GATHERING MORE INFORMATION](#GATHERING_MORE_INFORMATION) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                             |                                   |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    ERROR::PASS1(7stap)                                   ERROR::PASS1(7stap)

## [](#NAME)NAME

           error::pass1 - systemtap pass-1 errors

## [](#DESCRIPTION)DESCRIPTION

           Errors that occur during pass 1 (parsing) usually mean a basic
           syntax error of some sort occurred in the systemtap script.  There
           are several classes of problems possible:

           plain syntax error
                  The systemtap script parser detects a large variety of
                  errors, such as missing operands, bad punctuation.  It
                  tries to list what kinds of tokens it was expecting to see,
                  and will show the region of the source code with the
                  problem.  Please review the stap(1) man page and/or the
                  tutorial, to correct the script's syntax.

           grammar ambiguities
                  There is at least one known ambiguity in the systemtap
                  grammar.  It relates to the optionality of ; (semicolon)
                  separators between statements, and the ++ and --
                  increment/decrement operators.  If the parser indicates an
                  error, consider adding some explicit ; separators between
                  nearby statements and try again.

           missing command line arguments
                  A systemtap script that uses the $N and @N constructs for
                  substituting in command-line options may fail if not enough
                  options were given on the stap command line.

           compatibility changes
                  Some versions of systemtap have changed the language
                  incompatibly, for example by adding the try/catch keywords
                  for exception handling.  In such cases, rerun systemtap
                  with the --compatibility=VERSION option, substituting the
                  last systemtap version where your script was known to work.
                  You may also check the release-history NEWS file for
                  compatibility changes.

## [](#GATHERING_MORE_INFORMATION)GATHERING MORE INFORMATION

           Increasing the verbosity of pass-1 with an option such as --vp 1
           can help pinpoint the problem.

## [](#SEE_ALSO)SEE ALSO

           stap(1),
           error::reporting(7stap)

## [](#COLOPHON)COLOPHON

           This page is part of the systemtap (a tracing and live-system
           analysis tool) project.  Information about the project can be
           found at ⟨https://sourceware.org/systemtap/⟩.  If you have a bug
           report for this manual page, send it to systemtap@sourceware.org.
           This page was obtained from the project's upstream Git repository
           ⟨git://sourceware.org/git/systemtap.git⟩ on 2026-08-04.  (At that
           time, the date of the most recent commit that was found in the
           repository was 2026-07-30.)  If you discover any rendering
           problems in this HTML version of the page, or you believe there is
           a better or more up-to-date source for the page, or you have
           corrections or improvements to the information in this COLOPHON
           (which is not part of the original manual page), send a mail to
           man-pages@man7.org

                                                          ERROR::PASS1(7stap)

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
