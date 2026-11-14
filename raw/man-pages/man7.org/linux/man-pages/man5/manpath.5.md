---
{"title": "manpath(5) — Linux manual page", "url": "https://man7.org/linux/man-pages/man5/manpath.5.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# manpath(5) --- Linux manual page

+--------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [DESCRIPTION](#DESCRIPTION) \| [SEARCH PATH](#SEARCH_PATH) \| [FORMAT](#FORMAT) \| [BUGS](#BUGS) \| [COLOPHON](#COLOPHON) |                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                            |                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    MANPATH(5)              /usr/local/etc/man_db.conf             MANPATH(5)

## [](#NAME)NAME

           manpath - format of the /usr/local/etc/man_db.conf file

## [](#DESCRIPTION)DESCRIPTION

           The manpath configuration file is used by the manual page
           utilities to assess users' manpaths at run time, to indicate which
           manual page hierarchies (manpaths) are to be treated as system
           hierarchies and to assign them directories to be used for storing
           cat files.

           If the environment variable $MANPATH is already set, the
           information contained within /usr/local/etc/man_db.conf will not
           override it.

## [](#SEARCH_PATH)SEARCH PATH

           By default, man-db examines the user's $PATH.  For each
           path_element found there, it adds manpath_element to the search
           path.

           If there is no MANPATH_MAP line in the configuration file for a
           given path_element, then it adds all of path_element/../man,
           path_element/man, path_element/../share/man, and
           path_element/share/man that exist as directories to the search
           path.

           It then adds any MANDATORY_MANPATH entries from the configuration
           file to the search path.

           Finally, if the --systems option is used or the $SYSTEM
           environment variable is set, then that should consist of a
           sequence of operating system names separated by commas or colons.
           This acts as a template, expanding the search path once more to
           allow access to other operating systems' manual pages: for each
           system name, man-db looks for that name as a subdirectory of each
           entry in the search path, and adds it to the final search path if
           it exists.  A system name of man inserts the normal search path
           without subdirectories.  For example, if the search path would
           otherwise have been /usr/share/man:/usr/local/man, and $SYSTEM is
           set to newOS:man, then the final search path will be
           /usr/share/man/newOS:/usr/share/man:/usr/local/man/newOS:
           /usr/local/man.

           The $MANPATH environment variable overrides man-db's default
           manual page search paths.  Most users should not need to set it.
           Its syntax is similar to the $PATH environment variable: it
           consists of a sequence of directory names separated by colons.  It
           overrides the default search path described above.

           If the value of $MANPATH starts with a colon, then the default
           search path is added at its start.  If the value of $MANPATH ends
           with a colon, then the default search path is added at its end.
           If the value of $MANPATH contains a double colon (::), then the
           default search path is inserted in the middle of the value,
           between the two colons.

## [](#FORMAT)FORMAT

           The following field types are currently recognised:

           # comment
                  Blank lines or those beginning with a # will be treated as
                  comments and ignored.

           MANDATORY_MANPATH manpath_element
                  Lines of this form indicate manpaths that every
                  automatically generated $MANPATH should contain.  This will
                  typically include /usr/man.

           MANPATH_MAP path_element manpath_element
                  Lines of this form set up $PATH to $MANPATH mappings.  For
                  each path_element found in the user's $PATH,
                  manpath_element will be added to the $MANPATH.

           MANDB_MAP manpath_element [ catpath_element ]
                  Lines of this form indicate which manpaths are to be
                  treated as system manpaths, and optionally where their cat
                  files should be stored.  This field type is particularly
                  important if man is a setuid program, as (when in the
                  system configuration file /usr/local/etc/man_db.conf rather
                  than the per-user configuration file .manpath) it indicates
                  which manual page hierarchies to access as the setuid user
                  and which as the invoking user.

                  The system manual page hierarchies are usually those stored
                  under /usr such as /usr/man, /usr/local/man and
                  /usr/X11R6/man.

                  If cat pages from a particular manpath_element are not to
                  be stored or are to be stored in the traditional location,
                  catpath_element may be omitted.

                  Traditional cat placement would be impossible for read only
                  mounted manual page hierarchies and because of this it is
                  possible to specify any valid directory hierarchy for their
                  storage.  To observe the Linux FSSTND the keyword FSSTND
                  can be used in place of an actual directory.

                  Unfortunately, it is necessary to specify all system man
                  tree paths, including alternate operating system paths such
                  as /usr/man/sun and any NLS locale paths such as
                  /usr/man/de_DE.88591.

                  As the information is parsed line by line in the order
                  written, it is necessary for any manpath that is a sub-
                  hierarchy of another hierarchy to be listed first,
                  otherwise an incorrect match will be made.  An example is
                  that /usr/man/de_DE.88591 must come before /usr/man.

           DEFINE key value
                  Lines of this form define miscellaneous configuration
                  variables; see the default configuration file for those
                  variables used by the manual pager utilities.  They include
                  default paths to various programs (such as grep and tbl),
                  and default sets of arguments to those programs.

           SECTION section ...
                  Lines of this form define the order in which manual
                  sections should be searched.  If there are no SECTION
                  directives in the configuration file, the default is:

                         SECTION 1 n l 8 3 0 2 3type 5 4 9 6 7

                  If multiple SECTION directives are given, their section
                  lists will be concatenated.

                  If a particular extension is not in this list (say, 1mh) it
                  will be displayed with the rest of the section it belongs
                  to.  The effect of this is that you only need to explicitly
                  list extensions if you want to force a particular order.
                  Sections with extensions should usually be adjacent to
                  their main section (e.g. "1 1mh 8 ...").

                  SECTIONS is accepted as an alternative name for this
                  directive.

           MINCATWIDTH width
                  If the terminal width is less than width, cat pages will
                  not be created (if missing) or displayed.  The default is
                  80.

           MAXCATWIDTH width
                  If the terminal width is greater than width, cat pages will
                  not be created (if missing) or displayed.  The default is
                  80.

           CATWIDTH width
                  If width is non-zero, cat pages will always be formatted
                  for a terminal of the given width, regardless of the width
                  of the terminal actually being used.  This overrides
                  MINCATWIDTH and MAXCATWIDTH.

           NOCACHE
                  This flag prevents man(1) from creating cat pages
                  automatically.

## [](#BUGS)BUGS

           Unless the rules above are followed and observed precisely, the
           manual pager utilities will not function as desired.  The rules
           are overly complicated.

           https://gitlab.com/man-db/man-db/-/issues
           https://savannah.nongnu.org/bugs/?group=man-db

## [](#COLOPHON)COLOPHON

           This page is part of the man-db (manual pager suite) project.
           Information about the project can be found at 
           ⟨http://www.nongnu.org/man-db/⟩.  If you have a bug report for this
           manual page, send it to man-db-devel@nongnu.org.  This page was
           obtained from the project's upstream Git repository
           ⟨https://gitlab.com/cjwatson/man-db⟩ on 2026-08-04.  (At that
           time, the date of the most recent commit that was found in the
           repository was 2026-07-13.)  If you discover any rendering
           problems in this HTML version of the page, or you believe there is
           a better or more up-to-date source for the page, or you have
           corrections or improvements to the information in this COLOPHON
           (which is not part of the original manual page), send a mail to
           man-pages@man7.org

    2.13.1                          2025-05-02                     MANPATH(5)

------------------------------------------------------------------------

Pages that refer to this page: [apropos(1)](../man1/apropos.1.html),  [man(1)](../man1/man.1.html),  [manpath(1)](../man1/manpath.1.html),  [whatis(1)](../man1/whatis.1.html),  [catman(8)](../man8/catman.8.html),  [mandb(8)](../man8/mandb.8.html)

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
