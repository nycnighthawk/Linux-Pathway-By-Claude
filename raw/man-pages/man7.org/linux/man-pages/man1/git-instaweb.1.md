---
{"title": "git-instaweb(1) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/git-instaweb.1.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# git-instaweb(1) --- Linux manual page

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [CONFIGURATION](#CONFIGURATION) \| [SEE ALSO](#SEE_ALSO) \| [GIT](#GIT) \| [COLOPHON](#COLOPHON) |                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                  |                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    GIT-INSTAWEB(1)                 Git Manual                GIT-INSTAWEB(1)

## [](#NAME)NAME

           git-instaweb - Instantly browse your working repository in gitweb

## [](#SYNOPSIS)SYNOPSIS

           git instaweb [--local] [--httpd=<httpd>] [--port=<port>]
                          [--browser=<browser>]
           git instaweb [--start] [--stop] [--restart]

## [](#DESCRIPTION)DESCRIPTION

           A simple script to set up gitweb and a web server for browsing the
           local repository.

## [](#OPTIONS)OPTIONS

           -l, --local
               Only bind the web server to the local IP (127.0.0.1).

           -d, --httpd
               The HTTP daemon command-line that will be executed.
               Command-line options may be specified here, and the
               configuration file will be added at the end of the
               command-line. Currently apache2, lighttpd, mongoose, plackup,
               python and webrick are supported. (Default: lighttpd)

           -m, --module-path
               The module path (only needed if httpd is Apache). (Default:
               /usr/lib/apache2/modules)

           -p, --port
               The port number to bind the httpd to. (Default: 1234)

           -b, --browser
               The web browser that should be used to view the gitweb page.
               This will be passed to the git web--browse helper script along
               with the URL of the gitweb instance. See git-web--browse(1)
               for more information about this. If the script fails, the URL
               will be printed to stdout.

           start, --start
               Start the httpd instance and exit. Regenerate configuration
               files as necessary for spawning a new instance.

           stop, --stop
               Stop the httpd instance and exit. This does not generate any
               of the configuration files for spawning a new instance, nor
               does it close the browser.

           restart, --restart
               Restart the httpd instance and exit. Regenerate configuration
               files as necessary for spawning a new instance.

## [](#CONFIGURATION)CONFIGURATION

           You may specify configuration in your .git/config

               [instaweb]
                       local = true
                       httpd = apache2 -f
                       port = 4321
                       browser = konqueror
                       modulePath = /usr/lib/apache2/modules

           If the configuration variable instaweb.browser is not set,
           web.browser will be used instead if it is defined. See
           git-web--browse(1) for more information about this.

## [](#SEE_ALSO)SEE ALSO

           gitweb(1)

## [](#GIT)GIT

           Part of the git(1) suite

## [](#COLOPHON)COLOPHON

           This page is part of the git (Git distributed version control
           system) project.  Information about the project can be found at 
           ⟨http://git-scm.com/⟩.  If you have a bug report for this manual
           page, see ⟨http://git-scm.com/community⟩.  This page was obtained
           from the project's upstream Git repository
           ⟨https://github.com/git/git.git⟩ on 2026-08-04.  (At that time,
           the date of the most recent commit that was found in the
           repository was 2026-08-03.)  If you discover any rendering
           problems in this HTML version of the page, or you believe there is
           a better or more up-to-date source for the page, or you have
           corrections or improvements to the information in this COLOPHON
           (which is not part of the original manual page), send a mail to
           man-pages@man7.org

    Git 2.55.0.493.g5b2471          2026-08-03                GIT-INSTAWEB(1)

------------------------------------------------------------------------

Pages that refer to this page: [git(1)](../man1/git.1.html),  [git-config(1)](../man1/git-config.1.html),  [gitweb(1)](../man1/gitweb.1.html),  [gitweb.conf(5)](../man5/gitweb.conf.5.html),  [giteveryday(7)](../man7/giteveryday.7.html)

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
