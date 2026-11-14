---
{"title": "pcp-python(1) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/pcp-python.1.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# pcp-python(1) --- Linux manual page

+----------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [PCP ENVIRONMENT](#PCP_ENVIRONMENT) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                |                                   |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    PCP-PYTHON(1)            General Commands Manual            PCP-PYTHON(1)

## [](#NAME)NAME

           pcp-python - run a python script using a preferred python variant

## [](#SYNOPSIS)SYNOPSIS

           pcp python [SCRIPT [ARG] ...]

## [](#DESCRIPTION)DESCRIPTION

           pcp-python has been replaced by pmpython(1) which is preferred,
           however pcp-python is still installed to provided backwards
           compatibility.

           pcp-python provides a way to run python scripts using a
           customisable python binary, rather than embedding any particular
           version of python into each script.

           This can be useful as it allows version-independent python code to
           be run anywhere.  All python modules shipped with PCP support
           versions 2.6 and later (in the python2 series), and 3.3 and later
           (in the python3 release series).

           Due to python monitoring and collecting scripts being relatively
           simple in PCP (not requiring new modules, language features, etc),
           it has been possible to ensure they work for all of the above
           python versions.  Thus, it is common for PCP python scripts to use
           a "shebang" line that invokes pcp-python as follows:

              #!/usr/bin/pcp python

           This allows the custom setting to be injected instead of a hard-
           coded python version, while still allowing the user to override
           the python version as follows:

              $ PCP_PYTHON_PROG=python3 /usr/bin/pcp python --version
              Python 3.3.2
              $ PCP_PYTHON_PROG=python2 /usr/bin/pcp python --version
              Python 2.7.5

           This is convenient for shipping identical scripts on multiple
           platforms, and for testing different python versions with the one
           script (e.g. in the case where multiple versions of python are
           installed, PCP_PYTHON_PROG can be set in the local environment to
           override the global setting).

           By default, the value of PCP_PYTHON_PROG from /etc/pcp.conf will
           be used.  The default value of this configuration parameter is set
           depending on some heuristics about the target build platform.
           These heuristics favour the use of python3 in all recent releases
           of PCP, for those platforms that support it.

## [](#PCP_ENVIRONMENT)PCP ENVIRONMENT

           Environment variables with the prefix PCP_ are used to
           parameterize the file and directory names used by PCP.  On each
           installation, the file /etc/pcp.conf contains the local values for
           these variables.  The $PCP_CONF variable may be used to specify an
           alternative configuration file, as described in pcp.conf(5).

## [](#SEE_ALSO)SEE ALSO

           PCPIntro(1) and pcp(1).

## [](#COLOPHON)COLOPHON

           This page is part of the PCP (Performance Co-Pilot) project.
           Information about the project can be found at 
           ⟨http://www.pcp.io/⟩.  If you have a bug report for this manual
           page, send it to pcp@groups.io.  This page was obtained from the
           project's upstream Git repository
           ⟨https://github.com/performancecopilot/pcp.git⟩ on 2026-08-04.
           (At that time, the date of the most recent commit that was found
           in the repository was 2026-08-04.)  If you discover any rendering
           problems in this HTML version of the page, or you believe there is
           a better or more up-to-date source for the page, or you have
           corrections or improvements to the information in this COLOPHON
           (which is not part of the original manual page), send a mail to
           man-pages@man7.org

    Performance Co-Pilot               PCP                      PCP-PYTHON(1)

------------------------------------------------------------------------

Pages that refer to this page: [pcp(1)](../man1/pcp.1.html),  [pmpython(1)](../man1/pmpython.1.html)

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
