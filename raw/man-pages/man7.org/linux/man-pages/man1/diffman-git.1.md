---
{"title": "diffman-git(1) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/diffman-git.1.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# diffman-git(1) --- Linux manual page

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [ENVIRONMENT](#ENVIRONMENT) \| [EXAMPLES](#EXAMPLES) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                        |                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    diffman-git(1)           General Commands Manual           diffman-git(1)

## [](#NAME)NAME

           diffman-git - compare changes to manual pages line by line

## [](#SYNOPSIS)SYNOPSIS

           diffman-git [diff-options ...] [[base-commit] commit]

## [](#DESCRIPTION)DESCRIPTION

           The diffman-git command formats a manual page at two git(1)
           commits, and then runs diff(1) on the formatted outputs.

           If the commit is not specified, it diffs the working directory
           against HEAD.

           If the base-commit is not specified, the comparison is done
           against the previous commit.

## [](#OPTIONS)OPTIONS

           -s     Report when two files are the same.

           -Un    output n (default 3) lines of unified context.

           -w     Ignore all white space.

## [](#ENVIRONMENT)ENVIRONMENT

           See man(1).

## [](#EXAMPLES)EXAMPLES

           $ MAN_KEEP_FORMATTING= diffman-git 437e4afec6ca | less -R;
           --- 437e4afec6ca^:man/man3/sem_open.3
           +++ 437e4afec6ca:man/man3/sem_open.3
           @@ -14,3 +14,2 @@
           -     sem_t *sem_open(const char *name, int oflag);
           -     sem_t *sem_open(const char *name, int oflag,
           -                     mode_t mode, unsigned int value);
           +     sem_t *sem_open(const char *name, int oflag, ...
           +                     /* mode_t mode, unsigned int value */ );

## [](#SEE_ALSO)SEE ALSO

           diff(1), man(1), git(1), less(1)

## [](#COLOPHON)COLOPHON

           This page is part of the man-pages (Linux kernel and C library
           user-space interface documentation) project.  Information about
           the project can be found at 
           ⟨https://www.kernel.org/doc/man-pages/⟩.  If you have a bug report
           for this manual page, see
           ⟨https://git.kernel.org/pub/scm/docs/man-pages/man-pages.git/tree/CONTRIBUTING⟩.
           This page was obtained from the tarball man-pages-6.19.tar.gz
           fetched from
           ⟨https://mirrors.edge.kernel.org/pub/linux/docs/man-pages/⟩ on
           2026-09-09.  If you discover any rendering problems in this HTML
           version of the page, or you believe there is a better or more up-
           to-date source for the page, or you have corrections or
           improvements to the information in this COLOPHON (which is not
           part of the original manual page), send a mail to
           man-pages@man7.org

    Linux man-pages 6.19            2025-05-17                 diffman-git(1)

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
