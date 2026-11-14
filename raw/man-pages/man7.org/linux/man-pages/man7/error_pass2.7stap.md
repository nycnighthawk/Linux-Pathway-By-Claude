---
{"title": "error::pass2(7stap) — Linux manual page", "url": "https://man7.org/linux/man-pages/man7/error::pass2.7stap.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# error::pass2(7stap) --- Linux manual page

+-------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [DESCRIPTION](#DESCRIPTION) \| [GATHERING MORE INFORMATION](#GATHERING_MORE_INFORMATION) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                             |                                   |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    ERROR::PASS2(7stap)                                   ERROR::PASS2(7stap)

## [](#NAME)NAME

           error::pass2 - systemtap pass-2 errors

## [](#DESCRIPTION)DESCRIPTION

           Errors that occur during pass 2 (elaboration) can have a variety
           of causes.  Common types include:

           missing debuginfo
                  The script requires debuginfo to resolve a probe point, but
                  could not find any.  See error::dwarf(7stap) and
                  warning::debuginfo(7stap) for more details.

           unavailable probe point classes
                  Some types of probe points are only available on certain
                  system versions, architectures, and configurations.  For
                  example, user-space process.*  probes may require utrace or
                  uprobes capability in the kernel for this architecture.

           unavailable probe points
                  Some probe points may be individually unavailable even when
                  their class is fine.  For example,
                  kprobe.function("foobar") may fail if function foobar does
                  not exist in the kernel any more.  Debugging or symbol data
                  may be absent for some types of .function or .statement
                  probes; check for availability of debuginfo.  Try the
                  stap-prep program to download possibly-required debuginfo.
                  Use a wildcard parameter such as stap -l
                  'kprobe.function("*foo*")' to locate still-existing
                  variants.  Use ! or ?  probe point suffixes to denote
                  optional / preferred-alternatives, to let the working parts
                  of a script continue.

           typos  There might be a spelling error in the probe point name
                  ("sycsall" vs.  "syscall").  Wildcard probes may not find a
                  match at all in the tapsets.  Recheck the names using stap
                  -l PROBEPOINT.  Another common mistake is to use the .
                  operator instead of the correct -> when dereferencing
                  context variable subfields or pointers: $foo->bar->baz even
                  if in C one would say foo->bar.baz.

           unavailable context variables
                  Systemtap scripts often wish to refer to variables from the
                  context of the probed programs using $variable notation.
                  These variables may not always be available, depending on
                  versions of the compiler, debugging/optimization flags
                  used, architecture, etc.  Use stap -L PROBEPOINT to list
                  available context variables for given probes.  Use the
                  @defined() expression to test for the resolvability of a
                  context variable expression.  Consider using the stap
                  --skip-badvars option to silently replace misbehaving
                  context variable expressions with zero.  Experiment with
                  the stap --prologue-searching option.

           module cache inconsistencies
                  Occasionally, the systemtap module cache
                  ($HOME/.systemtap/cache) might contain obsolete information
                  from a prior system configuration/version, and produce
                  false results as systemtap attempts to reuse it.  Retrying
                  with stap --poison-cache ...  forces new information to be
                  generated.  Note: this should not happen and likely
                  represents a systemtap bug.  Please report it.

## [](#GATHERING_MORE_INFORMATION)GATHERING MORE INFORMATION

           Increasing the verbosity of pass-2 with an option such as --vp 02
           can help pinpoint the problem.

## [](#SEE_ALSO)SEE ALSO

           stap(1),
           stap-prep(1),
           stapprobes(3stap),
           probe::*(3stap),
           error::dwarf(7stap),
           error::inode-uprobes(7stap),
           warning::debuginfo(7stap),
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

                                                          ERROR::PASS2(7stap)

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
