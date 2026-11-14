---
{"title": "stg-completion(1) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/stg-completion.1.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# stg-completion(1) --- Linux manual page

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [COMMANDS](#COMMANDS) \| [OPTIONS](#OPTIONS) \| [STGIT](#STGIT) \| [COLOPHON](#COLOPHON) |                                   |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                   |                                   |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    STG-COMPLETION(1)              StGit Manual             STG-COMPLETION(1)

## [](#NAME)NAME

           stg-completion - Support for shell completions

## [](#SYNOPSIS)SYNOPSIS

           stg completion bash [OPTIONS]
           stg completion fish [OPTIONS]
           stg completion zsh [OPTIONS]
           stg completion list aliases [OPTIONS]
           stg completion list commands [OPTIONS]
           stg completion list commands-and-aliases [OPTIONS]
           stg completion list help aliases
           stg completion list help commands
           stg completion list help commands-and-aliases
           stg completion list help help
           stg completion man [OPTIONS]
           stg completion help bash
           stg completion help fish
           stg completion help zsh
           stg completion help list aliases
           stg completion help list commands
           stg completion help list commands-and-aliases
           stg completion help man
           stg completion help help

## [](#DESCRIPTION)DESCRIPTION

           Support completions for bash, fish, and zsh. Also provides stg
           completion list command for dynamically introspecting StGit’s
           commands and aliases.

## [](#COMMANDS)COMMANDS

           bash
               Generate bash completion script

           fish
               Generate fish shell completion script

           zsh
               Generate zsh completion script

           list aliases
               List aliases

           list commands
               List StGit commands

           list commands-and-aliases
               List StGit commands and aliases

           man
               Generate man pages in asciidoc format. The generated asciidoc
               files may be further processed by asciidoc or asciidoctor to
               produce roff, html, or other output formats.

               One file is generated for each stg command. The output
               directory defaults to the current directory, but may be
               specified with --output. The output files are named
               stg-<command>.txt.

## [](#OPTIONS)OPTIONS

           -o <path>, --output=<path>
               Output to <path>

       BASH OPTIONS
           -o <path>, --output=<path>
               Output completion script to <path>

       FISH OPTIONS
           -o <path>, --output=<path>
               Output completion script to <path>

       ZSH OPTIONS
           -o <path>, --output=<path>
               Output completion script to <path>

       LIST ALIASES OPTIONS
           --show-expansion
               Show alias expansion

           --style=(name-only|asciidoc|fish|zsh)
               Choose output format style

           -o <path>, --output=<path>
               Output to <path>

       LIST COMMANDS OPTIONS
           --style=(name-only|asciidoc|fish|zsh)
               Choose output format style

           -o <path>, --output=<path>
               Output to <path>

       LIST COMMANDS-AND-ALIASES OPTIONS
           --style=(name-only|asciidoc|fish|zsh)
               Choose output format style

           -o <path>, --output=<path>
               Output to <path>

       MAN OPTIONS
           -o <dir>, --output=<dir>
               Output man pages to <dir>

## [](#STGIT)STGIT

           Part of the StGit suite - see stg(1)

## [](#COLOPHON)COLOPHON

           This page is part of the stgit (Stacked Git) project.  Information
           about the project can be found at ⟨http://www.procode.org/stgit/⟩.
           If you have a bug report for this manual page, see
           ⟨http://www.procode.org/stgit/⟩.  This page was obtained from the
           project's upstream Git repository
           ⟨https://github.com/stacked-git/stgit.git⟩ on 2026-08-04.  (At
           that time, the date of the most recent commit that was found in
           the repository was 2026-07-19.)  If you discover any rendering
           problems in this HTML version of the page, or you believe there is
           a better or more up-to-date source for the page, or you have
           corrections or improvements to the information in this COLOPHON
           (which is not part of the original manual page), send a mail to
           man-pages@man7.org

    StGit 2.6.1                     08/04/2026              STG-COMPLETION(1)

------------------------------------------------------------------------

Pages that refer to this page: [stg(1)](../man1/stg.1.html)

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
