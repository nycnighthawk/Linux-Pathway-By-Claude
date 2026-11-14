---
{"title": "glob(7) — Linux manual page", "url": "https://man7.org/linux/man-pages/man7/glob.7.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# glob(7) --- Linux manual page

+-------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [DESCRIPTION](#DESCRIPTION) \| [NOTES](#NOTES) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+-------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                   |                                   |
+-------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    glob(7)              Miscellaneous Information Manual             glob(7)

## [](#NAME)NAME

           glob - globbing pathnames

## [](#DESCRIPTION)DESCRIPTION

           Long ago, in UNIX V6, there was a program /etc/glob that would
           expand wildcard patterns.  Soon afterward this became a shell
           built-in.

           These days there is also a library routine glob(3) that will
           perform this function for a user program.

           The rules are as follows (POSIX.2, 3.13).

       Wildcard matching
           A string is a wildcard pattern if it contains one of the
           characters '?', '*', or '['.  Globbing is the operation that
           expands a wildcard pattern into the list of pathnames matching the
           pattern.  Matching is defined by:

           A '?' (not between brackets) matches any single character.

           A '*' (not between brackets) matches any string, including the
           empty string.

           Character classes

           An expression "[...]" where the first character after the leading
           '[' is not an '!' matches a single character, namely any of the
           characters enclosed by the brackets.  The string enclosed by the
           brackets cannot be empty; therefore ']' can be allowed between the
           brackets, provided that it is the first character.  (Thus, "[][!]"
           matches the three characters '[', ']', and '!'.)

           Ranges

           There is one special convention: two characters separated by '-'
           denote a range.  (Thus, "[A-Fa-f0-9]" is equivalent to
           "[ABCDEFabcdef0123456789]".)  One may include '-' in its literal
           meaning by making it the first or last character between the
           brackets.  (Thus, "[]-]" matches just the two characters ']' and
           '-', and "[--0]" matches the three characters '-', '.', and '0',
           since '/' cannot be matched.)

           Complementation

           An expression "[!...]" matches a single character, namely any
           character that is not matched by the expression obtained by
           removing the first '!' from it.  (Thus, "[!]a-]" matches any
           single character except ']', 'a', and '-'.)

           One can remove the special meaning of '?', '*', and '[' by
           preceding them by a backslash, or, in case this is part of a shell
           command line, enclosing them in quotes.  Between brackets these
           characters stand for themselves.  Thus, "[[?*\]" matches the four
           characters '[', '?', '*', and '\'.

       Pathnames
           Globbing is applied on each of the components of a pathname
           separately.  A '/' in a pathname cannot be matched by a '?' or '*'
           wildcard, or by a range like "[.-0]".  A range containing an
           explicit '/' character is syntactically incorrect.  (POSIX
           requires that syntactically incorrect patterns are left
           unchanged.)

           If a filename starts with a '.', this character must be matched
           explicitly.  (Thus, rm * will not remove .profile, and tar c *
           will not archive all your files; tar c .  is better.)

       Empty lists
           The nice and simple rule given above: "expand a wildcard pattern
           into the list of matching pathnames" was the original UNIX
           definition.  It allowed one to have patterns that expand into an
           empty list, as in

               xv -wait 0 *.gif *.jpg

           where perhaps no *.gif files are present (and this is not an
           error).  However, POSIX requires that a wildcard pattern is left
           unchanged when it is syntactically incorrect, or the list of
           matching pathnames is empty.  With bash one can force the
           classical behavior using this command:

               shopt -s nullglob

           (Similar problems occur elsewhere.  For example, where old scripts
           have

               rm `find . -name "*~"`

           new scripts require

               rm -f nosuchfile `find . -name "*~"`

           to avoid error messages from rm called with an empty argument
           list.)

## [](#NOTES)NOTES

       Regular expressions
           Note that wildcard patterns are not regular expressions, although
           they are a bit similar.  First of all, they match filenames,
           rather than text, and secondly, the conventions are not the same:
           for example, in a regular expression '*' means zero or more copies
           of the preceding thing.

           Now that regular expressions have bracket expressions where the
           negation is indicated by a '^', POSIX has declared the effect of a
           wildcard pattern "[^...]" to be undefined.

       Character classes and internationalization
           Of course ranges were originally meant to be ASCII ranges, so that
           "[ -%]" stands for "[ !"#$%]" and "[a-z]" stands for "any
           lowercase letter".  Some UNIX implementations generalized this so
           that a range X-Y stands for the set of characters with code
           between the codes for X and for Y.  However, this requires the
           user to know the character coding in use on the local system, and
           moreover, is not convenient if the collating sequence for the
           local alphabet differs from the ordering of the character codes.
           Therefore, POSIX extended the bracket notation greatly, both for
           wildcard patterns and for regular expressions.  In the above we
           saw three types of items that can occur in a bracket expression:
           namely (i) the negation, (ii) explicit single characters, and
           (iii) ranges.  POSIX specifies ranges in an internationally more
           useful way and adds three more types:

           (iii) Ranges X-Y comprise all characters that fall between X and Y
           (inclusive) in the current collating sequence as defined by the
           LC_COLLATE category in the current locale.

           (iv) Named character classes, like

           [:alnum:]  [:alpha:]  [:blank:]  [:cntrl:]
           [:digit:]  [:graph:]  [:lower:]  [:print:]
           [:punct:]  [:space:]  [:upper:]  [:xdigit:]

           so that one can say "[[:lower:]]" instead of "[a-z]", and have
           things work in Denmark, too, where there are three letters past
           'z' in the alphabet.  These character classes are defined by the
           LC_CTYPE category in the current locale.

           (v) Collating symbols, like "[.ch.]" or "[.a-acute.]", where the
           string between "[." and ".]" is a collating element defined for
           the current locale.  Note that this may be a multicharacter
           element.

           (vi) Equivalence class expressions, like "[=a=]", where the string
           between "[=" and "=]" is any collating element from its
           equivalence class, as defined for the current locale.  For
           example, "[[=a=]]" might be equivalent to "[aáàäâ]", that is, to
           "[a[.a-acute.][.a-grave.][.a-umlaut.][.a-circumflex.]]".

## [](#SEE_ALSO)SEE ALSO

           sh(1), fnmatch(3), glob(3), locale(7), regex(7)

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

    Linux man-pages 6.19            2026-02-08                        glob(7)

------------------------------------------------------------------------

Pages that refer to this page: [dpkg(1)](../man1/dpkg.1.html),  [git-describe(1)](../man1/git-describe.1.html),  [git-for-each-ref(1)](../man1/git-for-each-ref.1.html),  [git-grep(1)](../man1/git-grep.1.html),  [grep(1)](../man1/grep.1.html),  [pmseries(1)](../man1/pmseries.1.html),  [semind(1)](../man1/semind.1.html),  [systemctl(1)](../man1/systemctl.1.html),  [systemd-analyze(1)](../man1/systemd-analyze.1.html),  [whereis(1)](../man1/whereis.1.html),  [fnmatch(3)](../man3/fnmatch.3.html),  [glob(3)](../man3/glob.3.html),  [dracut.conf(5)](../man5/dracut.conf.5.html),  [ld.so.conf(5)](../man5/ld.so.conf.5.html),  [loader.conf(5)](../man5/loader.conf.5.html),  [mdadm.conf(5)](../man5/mdadm.conf.5.html),  [rpm-config(5)](../man5/rpm-config.5.html),  [rpm-manifest(5)](../man5/rpm-manifest.5.html),  [rpm-spec(5)](../man5/rpm-spec.5.html),  [sysctl.d(5)](../man5/sysctl.d.5.html),  [systemd.exec(5)](../man5/systemd.exec.5.html),  [tunables.conf(5)](../man5/tunables.conf.5.html),  [systemd.image-filter(7)](../man7/systemd.image-filter.7.html),  [uri(7)](../man7/uri.7.html),  [dracut(8)](../man8/dracut.8.html),  [pam_succeed_if(8)](../man8/pam_succeed_if.8.html)

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
