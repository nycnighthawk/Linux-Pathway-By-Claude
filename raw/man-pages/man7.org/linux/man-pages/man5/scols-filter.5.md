---
{"title": "scols-filter(5) — Linux manual page", "url": "https://man7.org/linux/man-pages/man5/scols-filter.5.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# scols-filter(5) --- Linux manual page

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNTAX](#SYNTAX) \| [DESCRIPTION](#DESCRIPTION) \| [SYNTAX NOTES](#SYNTAX_NOTES) \| [LIMITATIONS](#LIMITATIONS) \| [AUTHORS](#AUTHORS) \| [REPORTING BUGS](#REPORTING_BUGS) \| [AVAILABILITY](#AVAILABILITY) |                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                |                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    SCOLS-FILTER(5)        File formats and conventions       SCOLS-FILTER(5)

## [](#NAME)NAME

           scols-filter - syntax for libsmartcols filter expressions

## [](#SYNTAX)SYNTAX

               expr: param
                     | ( expr )
                     | expr && expr | expr AND expr
                     | expr || expr | expr OR expr
                     | !expr        | NOT expr
                     | expr == expr | expr EQ expr
                     | expr != expr | expr NE expr
                     | expr >= expr | expr GE expr
                     | expr <= expr | expr LE expr
                     | expr >  expr | expr GT expr
                     | expr <  expr | expr LT expr
                     | expr =~ string
                     | expr !~ string

               param: integer
                     | float
                     | string
                     | boolean
                     | holder

               integer: [0-9]*
                     | [0-9]*[KMGTPEZY]
                     | [0-9]*[KMGTPEZY]iB

               float: integer.integer

               boolean: "true" | "false" | "TRUE" | "FALSE"

               string: "[^\n\"]*" | '[^\n\']*'

               holder: [a-zA-Z][a-zA-Z_.%:/\-0-9]*

## [](#DESCRIPTION)DESCRIPTION

           The filter expression can be used by application linked with
           libsmartcols to filter output data. The application can use the
           filter before it gathers all data for the output to reduce
           resources and improve performance. This makes scols filter more
           effective than grep(1) on the complete output. For example

                lsblk --output NAME,LABEL,FSTYPE --filter 'NAME=="sda1"'

           helps lsblk(1) to not read LABELs for all block device from udevd
           or libblkid, but read it only for device sda1.

           The filter can be also used for columns which are not used in the
           output.

## [](#SYNTAX_NOTES)SYNTAX NOTES

           An expression consists of holders, params, and operators.

           The currently supported holder type is column name only. The name
           has to be used without quotes. Before evaluation, application maps
           column names in the given expression to the output table columns
           and assign column data type to the holder. The default type is
           "string".

           The param is for representing a value directly. The currently
           supported data types are integer, float, string and boolean.

           An operator works with one or two operand(s). An operator has an
           expectation about the data type(s) of its operands. Giving an
           unexpected data type to an operator causes a syntax error. The
           library can cast between data types, the preferred is always the
           type as specified by param and in case of expression with number
           and float the preferred is the float.

           Operators taking two operands are and, or, eq, ne, le, lt, ge, gt,
           =~, !~. Alphabetically named operators have C-language flavored
           aliases: &&, ||, ==, !=, <, ⇐, >=, and >.

           ! is the only operator that takes one operand. If no operator is
           specified then expression is true if param or holder are not
           empty. For example --filter NAME will return lines where column
           NAME is not empty.

           =~ and !~ is for regular expression matching; if a string at the
           right side matches (or not matches for !~ a regular expression at
           the left side), the result is true. The right side operand must be
           a string literal.

           The precedences within operators is or, and, and eq, ne, le, gt,
           ge, =~, !~, not.

## [](#LIMITATIONS)LIMITATIONS

           About float and integer typed values, the filter engine supports
           only non-negative numbers. The integer is unsigned 64-bit number,
           and float is long double. The integer may be followed by the
           multiplicative suffixes KiB, GiB, TiB, PiB, EiB, ZiB, and YiB (the
           "iB" is optional, e.g., "K" has the same meaning as "KiB").

           The filter expression string is limited to 1024 bytes. The number
           of nodes (parameters and operators) in a single expression is
           limited to 256.

           Regular expression patterns used with the =~ and !~ operators are
           limited to 256 bytes. Patterns with consecutive quantifiers (e.g.,
           a+`, `a**`), nested group repetitions (e.g., `(a)+), or interval
           repetitions with bounds larger than 1024 (e.g., {,9999}) are
           rejected because they can cause excessive memory consumption in
           the POSIX regex compiler.

## [](#AUTHORS)AUTHORS

           Karel Zak <kzak@redhat.com>

           Based on original implementation from Masatake YAMATO
           <yamato@redhat.com>.

## [](#REPORTING_BUGS)REPORTING BUGS

           For bug reports, use the issue tracker
           <https://github.com/util-linux/util-linux/issues>.

## [](#AVAILABILITY)AVAILABILITY

           The libsmartcols library is part of the util-linux package since
           version 2.25. It can be downloaded from Linux Kernel Archive
           <https://www.kernel.org/pub/linux/utils/util-linux/>. This page is
           part of the util-linux (a random collection of Linux utilities)
           project. Information about the project can be found at 
           ⟨https://www.kernel.org/pub/linux/utils/util-linux/⟩. If you have a
           bug report for this manual page, send it to
           util-linux@vger.kernel.org. This page was obtained from the
           project's upstream Git repository
           ⟨git://git.kernel.org/pub/scm/utils/util-linux/util-linux.git⟩ on
           2026-08-04. (At that time, the date of the most recent commit that
           was found in the repository was 2026-08-03.) If you discover any
           rendering problems in this HTML version of the page, or you
           believe there is a better or more up-to-date source for the page,
           or you have corrections or improvements to the information in this
           COLOPHON (which is not part of the original manual page), send a
           mail to man-pages@man7.org

    util-linux 2.43.devel-1062-f... 2026-08-03                SCOLS-FILTER(5)

------------------------------------------------------------------------

Pages that refer to this page: [lsfd(1)](../man1/lsfd.1.html),  [findmnt(8)](../man8/findmnt.8.html),  [lsblk(8)](../man8/lsblk.8.html),  [lslocks(8)](../man8/lslocks.8.html),  [lsns(8)](../man8/lsns.8.html)

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
