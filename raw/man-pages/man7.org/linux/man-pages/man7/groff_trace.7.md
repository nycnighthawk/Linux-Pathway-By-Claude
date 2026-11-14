---
{"title": "groff_trace(7) — Linux manual page", "url": "https://man7.org/linux/man-pages/man7/groff_trace.7.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# groff_trace(7) --- Linux manual page

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [Name](#Name) \| [Synopsis](#Synopsis) \| [Description](#Description) \| [Files](#Files) \| [Examples](#Examples) \| [Authors](#Authors) \| [See also](#See_also) \| [COLOPHON](#COLOPHON) |                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                            |                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    groff_trace(7)       Miscellaneous Information Manual      groff_trace(7)

## [](#Name)Name

           groff_trace - macros for debugging GNU roff documents

## [](#Synopsis)Synopsis

           groff -m trace [option ...] [file ...]

## [](#Description)Description

           trace is a macro package for the groff(7) document formatting
           system, designed as an aid for debugging documents written in its
           language.  It issues a message to the standard error stream upon
           entry to and exit from each macro call.  This can ease the process
           of isolating errors in macro definitions.

           Activate the package by specifying the command-line option
           “-m trace” to the formatter program (often groff(1)).  You can
           achieve finer control by including the macro file within the
           document; invoke the mso request, as in “.mso trace.tmac”.  Only
           macros that are defined after this invocation are traced.  If the
           trace-full register is set to a true value, as with the command-
           line option “-r trace-full=1”, register and string assignments,
           along with some other requests, are traced also.  If another macro
           package should be traced as well, specify it after “-m trace” on
           the command line.

           The macro file trace.tmac is unusual because it does not contain
           any macros to be called by a user.  Instead, groff's macro
           definition and alteration facilities are wrapped such that they
           display diagnostic messages.

       Limitations
           Because trace.tmac wraps the de request (and its cousins), macro
           arguments are expanded one level more.  This causes problems if an
           argument uses four or more backslashes to delay interpretation of
           an escape sequence.  For example, the macro call
                  .foo \\\\n[bar]
           normally passes “\\n[bar]” to macro “foo”, but with de redefined,
           it passes “\n[bar]” instead.

           The solution to this problem is to use groff's \E escape sequence,
           an escape character that is not interpreted in copy mode.
                  .foo \En[bar]

## [](#Files)Files

           /usr/local/share/groff/1.24.1/tmac/trace.tmac
                  implements the package.

## [](#Examples)Examples

           We will illustrate trace.tmac using the shell's “here document”
           feature to supply groff with a document on the standard input
           stream.  Since we are interested only in diagnostic messages
           appearing on the standard error stream, we discard the formatted
           output by redirecting the standard output stream to /dev/null.

       Observing nested macro calls
           Macro calls can be nested, even with themselves.  Tracing recurses
           along with them; this feature can help to detangle complex call
           stacks.

                  $ cat <<EOF | groff -m trace > /dev/null
                  .de countdown
                  . nop \\$1
                  . nr count (\\$1 - 1)
                  . if \\n[count] .countdown \\n[count]
                  ..
                  .countdown 3
                  blastoff
                  EOF
                   *** .de countdown
                   *** de trace enter: .countdown "3"
                    *** de trace enter: .countdown "2"
                     *** de trace enter: .countdown "1"
                     *** trace exit: .countdown "1"
                    *** trace exit: .countdown "2"
                   *** trace exit: .countdown "3"

       Tracing with the mso request
           Now let us activate tracing within the document, not with a
           command-line option.  We might do so when employing a macro
           package like ms or mom, to avoid distraction by traces of macros
           we didn't write.

                  $ cat <<EOF | groff -ms > /dev/null
                  .LP
                  This is my introductory paragraph.
                  .mso trace.tmac
                  .de Mymac
                  ..
                  .Mymac
                  .PP
                  Let us review the existing literature.
                  EOF
                   *** .de Mymac
                   *** de trace enter: .Mymac
                   *** trace exit: .Mymac

           As tracing was not yet active when the macros “LP” and “PP” were
           defined (by s.tmac), their calls were not traced; contrast with
           the macro “Mymac”.

## [](#Authors)Authors

           trace.tmac was written by James Clark.  This document was written
           by Bernd Warken ⟨groff-bernd.warken-72@web.de⟩ and G. Branden
           Robinson ⟨g.branden.robinson@gmail.com⟩.

## [](#See_also)See also

           Groff: The GNU Implementation of troff, by Trent A. Fisher and
           Werner Lemberg, is the primary groff manual.  You can browse it
           interactively with “info groff”.

           groff(1)
                  gives an overview of the groff document formatting system.

           troff(1)
                  supplies details of the -m command-line option.

           groff_tmac(5)
                  offers a survey of groff macro packages.

           groff(7)
                  is a reference manual for the groff language.

## [](#COLOPHON)COLOPHON

           This page is part of the groff (GNU troff) project.  Information
           about the project can be found at 
           ⟨http://www.gnu.org/software/groff/⟩.  If you have a bug report for
           this manual page, see ⟨http://www.gnu.org/software/groff/⟩.  This
           page was obtained from the tarball groff-1.24.1.tar.gz fetched
           from ⟨https://ftp.gnu.org/gnu/groff/⟩ on 2026-08-04.  If you
           discover any rendering problems in this HTML version of the page,
           or you believe there is a better or more up-to-date source for the
           page, or you have corrections or improvements to the information
           in this COLOPHON (which is not part of the original manual page),
           send a mail to man-pages@man7.org

    groff 1.24.1                    2026-03-14                 groff_trace(7)

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
