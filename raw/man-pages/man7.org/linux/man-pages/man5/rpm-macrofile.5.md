---
{"title": "rpm-macrofile(5) — Linux manual page", "url": "https://man7.org/linux/man-pages/man5/rpm-macrofile.5.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# rpm-macrofile(5) --- Linux manual page

+--------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [EXAMPLES](#EXAMPLES) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                  |                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    RPM-MACROFILE(5)           File Formats Manual           RPM-MACROFILE(5)

## [](#NAME)NAME

           rpm-macrofile - rpm macro file format

## [](#SYNOPSIS)SYNOPSIS

           %NAME[([OPTS]) BODY

## [](#DESCRIPTION)DESCRIPTION

           Rpm macro files are used to define rpm-macros(7) in the global
           macro context. The two primary uses of macros are assisting
           packaging work, and configuring rpm behavior. A pre-determined set
           of macro files is read upon rpm library initialization as
           described in rpm-config(5) but they can also be loaded via the
           %load macro separately.

           The format of a macro file is: the macro NAME prefixed with %,
           followed by whitespace and then the macro body, each new
           definition separated with a newline. The syntax is exactly the
           same as when using %define. See rpm-macros(7) for details on the
           macro syntax.

           A trailing \ indicates line continuation, but can be omitted
           inside macro bodies wrapped in a %{macro:...} block.

           Lines starting with # or consisting solely of whitespace are
           ignored.

           Reading a macro file is always fully declarative: no macros are
           ever expanded when reading a macro file.

## [](#EXAMPLES)EXAMPLES

       Example 1. Simple macro
               %mytool   /usr/bin/mytool-with-annoying-name

       Example 2. Multiline macro with a preceding comment
               # Trailing %{nil} is handy for ensuring a newline at the end
               %mycmd %{mytool} \
                   --one \
                   --with \
                   --too \
                   --many arguments \
               %{nil}

       Example 3. Multiline parametric Lua macro:
               %myhelper() %{lua:
                   function dostuff(arg)
                       return 'do stuff to '..arg
                   end
                   print(dostuff(arg[1]))
               }

## [](#SEE_ALSO)SEE ALSO

           rpm-config(5) rpmbuild-config(5) rpm-macros(7)

## [](#COLOPHON)COLOPHON

           This page is part of the rpm (RPM Package Manager) project.
           Information about the project can be found at 
           ⟨https://github.com/rpm-software-management/rpm⟩.  It is not known
           how to report bugs for this man page; if you know, please send a
           mail to man-pages@man7.org.  This page was obtained from the
           project's upstream Git repository
           ⟨https://github.com/rpm-software-management/rpm.git⟩ on
           2026-08-04.  (At that time, the date of the most recent commit
           that was found in the repository was 2026-07-27.)  If you discover
           any rendering problems in this HTML version of the page, or you
           believe there is a better or more up-to-date source for the page,
           or you have corrections or improvements to the information in this
           COLOPHON (which is not part of the original manual page), send a
           mail to man-pages@man7.org

    RPM 6.1.90                      2026-08-03               RPM-MACROFILE(5)

------------------------------------------------------------------------

Pages that refer to this page: [rpmbuild-config(5)](../man5/rpmbuild-config.5.html),  [rpm-config(5)](../man5/rpm-config.5.html),  [rpm-dependency-generators(7)](../man7/rpm-dependency-generators.7.html),  [rpm-macros(7)](../man7/rpm-macros.7.html),  [rpm-spec-macros(7)](../man7/rpm-spec-macros.7.html),  [rpm-common(8)](../man8/rpm-common.8.html)

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
