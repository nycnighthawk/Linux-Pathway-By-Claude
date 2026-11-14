---
{"title": "systemd.syntax(7) — Linux manual page", "url": "https://man7.org/linux/man-pages/man7/systemd.syntax.7.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# systemd.syntax(7) --- Linux manual page

+--------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [INTRODUCTION](#INTRODUCTION) \| [QUOTING](#QUOTING) \| [SEE ALSO](#SEE_ALSO) \| [NOTES](#NOTES) \| [COLOPHON](#COLOPHON) |                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                            |                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    SYSTEMD.SYNTAX(7)             systemd.syntax            SYSTEMD.SYNTAX(7)

## [](#NAME)NAME

           systemd.syntax - General syntax of systemd configuration files

## [](#INTRODUCTION)INTRODUCTION

           This page describes the basic principles of configuration files
           used by systemd(1) and related programs for:

           •   systemd unit files, see systemd.unit(5), systemd.service(5),
               systemd.socket(5), systemd.device(5), systemd.mount(5),
               systemd.automount(5), systemd.swap(5), systemd.target(5),
               systemd.path(5), systemd.timer(5), systemd.slice(5),
               systemd.scope(5)

           •   link files, see systemd.link(5)

           •   netdev and network files, see systemd.netdev(5),
               systemd.network(5)

           •   daemon config files, see systemd-system.conf(5),
               systemd-user.conf(5), logind.conf(5), journald.conf(5),
               journal-remote.conf(5), journal-upload.conf(5),
               systemd-sleep.conf(5), timesyncd.conf(5)

           •   nspawn files, see systemd.nspawn(5)

           The syntax is inspired by XDG Desktop Entry Specification[1]
           .desktop files, which are in turn inspired by Microsoft Windows
           .ini files.

           Each file is a plain text file divided into sections, with
           configuration entries in the style key=value. Whitespace
           immediately before or after the "=" is ignored. Empty lines and
           lines starting with "#" or ";" are ignored, which may be used for
           commenting.

           Lines ending in a backslash are concatenated with the following
           line while reading and the backslash is replaced by a space
           character. This may be used to wrap long lines. The limit on line
           length is very large (currently 1 MB), but it is recommended to
           avoid such long lines and use multiple directives, variable
           substitution, or other mechanism as appropriate for the given file
           type. When a comment line or lines follow a line ending with a
           backslash, the comment block is ignored, so the continued line is
           concatenated with whatever follows the comment block.

               [Section A]
               KeyOne=value 1
               KeyTwo=value 2

               # a comment

               [Section B]
               Setting="something" "some thing" "..."
               KeyTwo=value 2 \
                      value 2 continued

               [Section C]
               KeyThree=value 3\
               # this line is ignored
               ; this line is ignored too
                      value 3 continued

           Boolean arguments used in configuration files can be written in
           various formats. For positive settings the strings 1, yes, true
           and on are equivalent. For negative settings, the strings 0, no,
           false and off are equivalent.

           Time span values encoded in configuration files can be written in
           various formats. A stand-alone number specifies a time in seconds.
           If suffixed with a time unit, the unit is honored. A concatenation
           of multiple values with units is supported, in which case the
           values are added up. Example: "50" refers to 50 seconds;
           "2min 200ms" refers to 2 minutes and 200 milliseconds, i.e.
           120200 ms. The following time units are understood: "s", "min",
           "h", "d", "w", "ms", "us". For details see systemd.time(7).

           Various settings are allowed to be specified more than once, in
           which case the interpretation depends on the setting. Often,
           multiple settings form a list, and setting to an empty value
           "resets", which means that previous assignments are ignored. When
           this is allowed, it is mentioned in the description of the
           setting. Note that using multiple assignments to the same value
           makes the file incompatible with parsers for the XDG .desktop file
           format.

## [](#QUOTING)QUOTING

           For settings where quoting is allowed, the following general rules
           apply: double quotes ("...") and single quotes ('...') may be used
           to wrap a whole item (the opening quote may appear only at the
           beginning or after whitespace that is not quoted, and the closing
           quote must be followed by whitespace or the end of line), in which
           case everything until the next matching quote becomes part of the
           same item. Quotes themselves are removed. C-style escapes are
           supported. The table below contains the list of known escape
           patterns. Only escape patterns which match the syntax in the table
           are allowed; other patterns may be added in the future and unknown
           patterns will result in a warning. In particular, any backslashes
           should be doubled. Finally, a trailing backslash ("\") may be used
           to merge lines, as described above. UTF-8 is accepted, and hence
           typical unicode characters do not need to be escaped.

           Table 1. Supported escapes
           ┌──────────────┬─────────────────────────┐
           │ Literal      │ Actual value            │
           ├──────────────┼─────────────────────────┤
           │ "\a"         │ bell                    │
           ├──────────────┼─────────────────────────┤
           │ "\b"         │ backspace               │
           ├──────────────┼─────────────────────────┤
           │ "\f"         │ form feed               │
           ├──────────────┼─────────────────────────┤
           │ "\n"         │ newline                 │
           ├──────────────┼─────────────────────────┤
           │ "\r"         │ carriage return         │
           ├──────────────┼─────────────────────────┤
           │ "\t"         │ tab                     │
           ├──────────────┼─────────────────────────┤
           │ "\v"         │ vertical tab            │
           ├──────────────┼─────────────────────────┤
           │ "\\"         │ backslash               │
           ├──────────────┼─────────────────────────┤
           │ "\""         │ double quotation mark   │
           ├──────────────┼─────────────────────────┤
           │ "\'"         │ single quotation mark   │
           ├──────────────┼─────────────────────────┤
           │ "\s"         │ space                   │
           ├──────────────┼─────────────────────────┤
           │ "\xxx"       │ character number xx in  │
           │              │ hexadecimal encoding    │
           ├──────────────┼─────────────────────────┤
           │ "\nnn"       │ character number nnn in │
           │              │ octal encoding          │
           ├──────────────┼─────────────────────────┤
           │ "\unnnn"     │ unicode code point nnnn │
           │              │ in hexadecimal encoding │
           ├──────────────┼─────────────────────────┤
           │ "\Unnnnnnnn" │ unicode code point      │
           │              │ nnnnnnnn in hexadecimal │
           │              │ encoding                │
           └──────────────┴─────────────────────────┘

## [](#SEE_ALSO)SEE ALSO

           systemd(1), systemd.time(7)

## [](#NOTES)NOTES

            1. XDG Desktop Entry Specification
               https://standards.freedesktop.org/desktop-entry-spec/latest/

## [](#COLOPHON)COLOPHON

           This page is part of the systemd (systemd system and service
           manager) project.  Information about the project can be found at
           ⟨http://www.freedesktop.org/wiki/Software/systemd⟩.  If you have a
           bug report for this manual page, see
           ⟨http://www.freedesktop.org/wiki/Software/systemd/#bugreports⟩.
           This page was obtained from the project's upstream Git repository
           ⟨https://github.com/systemd/systemd.git⟩ on 2026-08-04.  (At that
           time, the date of the most recent commit that was found in the
           repository was 2026-08-03.)  If you discover any rendering
           problems in this HTML version of the page, or you believe there is
           a better or more up-to-date source for the page, or you have
           corrections or improvements to the information in this COLOPHON
           (which is not part of the original manual page), send a mail to
           man-pages@man7.org

    systemd 262~devel                                       SYSTEMD.SYNTAX(7)

------------------------------------------------------------------------

Pages that refer to this page: [journald.conf(5)](../man5/journald.conf.5.html),  [journal-remote.conf(5)](../man5/journal-remote.conf.5.html),  [journal-upload.conf(5)](../man5/journal-upload.conf.5.html),  [logind.conf(5)](../man5/logind.conf.5.html),  [oomd.conf(5)](../man5/oomd.conf.5.html),  [sysext.conf(5)](../man5/sysext.conf.5.html),  [systemd.exec(5)](../man5/systemd.exec.5.html),  [systemd.link(5)](../man5/systemd.link.5.html),  [systemd.netdev(5)](../man5/systemd.netdev.5.html),  [systemd.network(5)](../man5/systemd.network.5.html),  [systemd.nspawn(5)](../man5/systemd.nspawn.5.html),  [systemd.service(5)](../man5/systemd.service.5.html),  [systemd-sleep.conf(5)](../man5/systemd-sleep.conf.5.html),  [systemd-system.conf(5)](../man5/systemd-system.conf.5.html),  [systemd.unit(5)](../man5/systemd.unit.5.html),  [timesyncd.conf(5)](../man5/timesyncd.conf.5.html),  [systemd.index(7)](../man7/systemd.index.7.html),  [nss-resolve(8)](../man8/nss-resolve.8.html)

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
