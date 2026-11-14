---
{"title": "rpmlua(1) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/rpmlua.1.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# rpmlua(1) --- Linux manual page

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [ARGUMENTS](#ARGUMENTS) \| [OPTIONS](#OPTIONS) \| [EXIT STATUS](#EXIT_STATUS) \| [EXAMPLES](#EXAMPLES) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                   |                                   |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    RPMLUA(1)                General Commands Manual                RPMLUA(1)

## [](#NAME)NAME

           rpmlua - RPM Lua interpreter

## [](#SYNOPSIS)SYNOPSIS

           rpmlua [options] [LUA_SCRIPT] [-- ARG ...]

## [](#DESCRIPTION)DESCRIPTION

           Run RPM internal Lua interpreter.

           Note: indexes start at 1 in Lua, so the program name is at arg[1]
           instead of the more customary index zero.

## [](#ARGUMENTS)ARGUMENTS

           LUA SCRIPT
               A Lua script.

           ARG
               Options and arguments to be passed to SCRIPT_FILE. rpmlua
               stops processing at --.

## [](#OPTIONS)OPTIONS

           -i, --interactive
               Run an interactive session after executing optional script or
               statement.

           --opts=OPTSTRING
               Perform getopt(3) option processing on the passed arguments
               according to OPTSTRING.

           -e "STATEMENT", --execute "STATEMENT"
               Execute a Lua statement before executing optional script.

## [](#EXIT_STATUS)EXIT STATUS

           On success, 0 is returned, a nonzero failure code otherwise.

## [](#EXAMPLES)EXAMPLES

           rpmlua test.lua
               Execute test.lua script file.

           rpmlua --opts=ab:c args.lua -- 1 2 3 -c -b5
               Execute args.lua script file with option processing.

           rpmlua -e "print(rpm.ver('1.0') < rpm.ver('2.0'))"
               Execute single statement to compare rpm versions.

           rpmlua -i
               Run an interactive session.

## [](#SEE_ALSO)SEE ALSO

           lua(1), popt(3), getopt(3), rpm(8) rpm-lua(7)

           http://www.rpm.org/ 

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

    RPM 6.1.90                      2026-08-03                      RPMLUA(1)

------------------------------------------------------------------------

Pages that refer to this page: [rpm-lua(7)](../man7/rpm-lua.7.html),  [rpm-macros(7)](../man7/rpm-macros.7.html)

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
