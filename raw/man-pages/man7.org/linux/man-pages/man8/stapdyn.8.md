---
{"title": "stapdyn(8) — Linux manual page", "url": "https://man7.org/linux/man-pages/man8/stapdyn.8.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# stapdyn(8) --- Linux manual page

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [ARGUMENTS](#ARGUMENTS) \| [EXAMPLES](#EXAMPLES) \| [SAFETY AND SECURITY](#SAFETY_AND_SECURITY) \| [SEE ALSO](#SEE_ALSO) \| [BUGS](#BUGS) \| [COLOPHON](#COLOPHON) |                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                                                    |                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    STAPDYN(8)               System Manager's Manual               STAPDYN(8)

## [](#NAME)NAME

           stapdyn - systemtap dyninst runtime

## [](#SYNOPSIS)SYNOPSIS

           stapdyn [ OPTIONS ] MODULE [ MODULE-OPTIONS ]

## [](#DESCRIPTION)DESCRIPTION

           The stapdyn program is the dyninst back-end of the Systemtap tool.
           It expects a shared library produced by the front-end stap tool,
           when run with --dyninst.

           Splitting the systemtap tool into a front-end and a back-end
           allows a user to compile a systemtap script on a development
           machine that has the debugging information (need to compile the
           script) and then transfer the resulting shared object to a
           production machine that doesn't have any development tools or
           debugging information installed.

           Please refer to stappaths (7) for the version number, or run rpm
           -q systemtap (fedora/red hat) apt-get -v systemtap (ubuntu)

## [](#OPTIONS)OPTIONS

           The stapdyn program supports the following options.  Any other
           option prints a list of supported options.

           -v     Verbose mode.

           -V     Print version number and exit.

           -w     Suppress warnings from the script.

           -c CMD Command CMD will be run and the stapdyn program will exit
                  when CMD does.  The '_stp_target' variable will contain the
                  pid for CMD.

           -x PID The '_stp_target' variable will be set to PID.

           -o FILE
                  Send output to FILE. If the module uses bulk mode, the
                  output will be in percpu files FILE_x(FILE_cpux in
                  background and bulk mode) where 'x' is the cpu number. This
                  supports strftime(3) formats for FILE.

           -C WHEN
                  Control coloring of error messages. WHEN must be either
                  "never", "always", or "auto" (i.e. enable only if at a ter‐
                  minal). If the option is missing, then "auto" is assumed.
                  Colors can be modified using the SYSTEMTAP_COLORS environ‐
                  ment variable. See the stap(1) manual page for more infor‐
                  mation on syntax and behaviour.

           var1=val
                  Sets the value of global variable var1 to val. Global vari‐
                  ables contained within a script are treated as options and
                  can be set from the stapdyn command line.

## [](#ARGUMENTS)ARGUMENTS

           MODULE is either a module path or a module name.  If it is a mod‐
           ule name, the module will be looked for in the following directory
           (where 'VERSION' is the output of "uname -r"):

                  /lib/modules/VERSION/systemtap

            $ stap --dyninst -p4 -m mod1 -e 'global var1="foo"; probe be‐
           gin{printf("%s\n", var1); exit()}'

           Running this with an additional module argument:

            $ stapdyn mod1.so var1="HelloWorld"
            HelloWorld

           Spaces and exclamation marks currently cannot be passed into glob‐
           al variables this way.

## [](#EXAMPLES)EXAMPLES

           See the stapex(3stap) manual page for a collection of sample
           scripts.

           Here is a very basic example of how to use stapdyn.  First, use
           stap to compile a script.  The stap program will report the path‐
           name to the resulting module.

            $ stap --dyninst -p4 -e 'probe begin { printf("Hello World!\n");
           exit() }'
            /home/user/.systemtap/cache/85/stap_8553d83f78c_265.so

           Run stapdyn with the pathname to the module as an argument.

            $ stapdyn /home/user/.systemtap/cache/85/stap_8553d83f78c_265.so
            Hello World!

## [](#SAFETY_AND_SECURITY)SAFETY AND SECURITY

           Systemtap, in DynInst mode, is a developer tool, and runs com‐
           pletely unprivileged.  The Linux kernel will only permit one's own
           processes to be accessed, which is enforced by the ptrace(2) sys‐
           tem call.  See the stap(1) manual page for additional information
           on safety and security.

## [](#SEE_ALSO)SEE ALSO

           stap(1), stapprobes(3stap), stap-server(8), staprun(8),
           stapex(3stap)

## [](#BUGS)BUGS

           Use the Bugzilla link of the project web page or our mailing list.
           http://sourceware.org/systemtap/ , <systemtap@sourceware.org>.

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

                                                                   STAPDYN(8)

------------------------------------------------------------------------

Pages that refer to this page: [stap(1)](../man1/stap.1.html),  [staprun(8)](../man8/staprun.8.html)

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
