---
{"title": "localedef(1p) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/localedef.1p.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# localedef(1p) --- Linux manual page

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [PROLOG](#PROLOG) \| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [OPERANDS](#OPERANDS) \| [STDIN](#STDIN) \| [INPUT FILES](#INPUT_FILES) \| [ENVIRONMENT VARIABLES](#ENVIRONMENT_VARIABLES) \| [ASYNCHRONOUS EVENTS](#ASYNCHRONOUS_EVENTS) \| [STDOUT](#STDOUT) \| [STDERR](#STDERR) \| [OUTPUT FILES](#OUTPUT_FILES) \| [EXTENDED DESCRIPTION](#EXTENDED_DESCRIPTION) \| [EXIT STATUS](#EXIT_STATUS) \| [CONSEQUENCES OF ERRORS](#CONSEQUENCES_OF_ERRORS) \| [APPLICATION USAGE](#APPLICATION_USAGE) \| [EXAMPLES](#EXAMPLES) \| [RATIONALE](#RATIONALE) \| [FUTURE DIRECTIONS](#FUTURE_DIRECTIONS) \| [SEE ALSO](#SEE_ALSO) \| [COPYRIGHT](#COPYRIGHT) |                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    LOCALEDEF(1P)           POSIX Programmer's Manual           LOCALEDEF(1P)

## [](#PROLOG)PROLOG

           This manual page is part of the POSIX Programmer's Manual.  The
           Linux implementation of this interface may differ (consult the
           corresponding Linux manual page for details of Linux behavior), or
           the interface may not be implemented on Linux.

## [](#NAME)NAME

           localedef — define locale environment

## [](#SYNOPSIS)SYNOPSIS

           localedef [-c] [-f charmap] [-i sourcefile] [-u code_set_name] name

## [](#DESCRIPTION)DESCRIPTION

           The localedef utility shall convert source definitions for locale
           categories into a format usable by the functions and utilities
           whose operational behavior is determined by the setting of the
           locale environment variables defined in the Base Definitions
           volume of POSIX.1‐2017, Chapter 7, Locale.  It is implementation-
           defined whether users have the capability to create new locales,
           in addition to those supplied by the implementation. If the
           symbolic constant POSIX2_LOCALEDEF is defined, the system supports
           the creation of new locales.  On XSI-conformant systems, the
           symbolic constant POSIX2_LOCALEDEF shall be defined.

           The utility shall read source definitions for one or more locale
           categories belonging to the same locale from the file named in the
           -i option (if specified) or from standard input.

           The name operand identifies the target locale. The utility shall
           support the creation of public, or generally accessible locales,
           as well as private, or restricted-access locales. Implementations
           may restrict the capability to create or modify public locales to
           users with appropriate privileges.

           Each category source definition shall be identified by the
           corresponding environment variable name and terminated by an END
           category-name statement. The following categories shall be
           supported. In addition, the input may contain source for
           implementation-defined categories.

           LC_CTYPE  Defines character classification and case conversion.

           LC_COLLATE
                     Defines collation rules.

           LC_MONETARY
                     Defines the format and symbols used in formatting of
                     monetary information.

           LC_NUMERIC
                     Defines the decimal delimiter, grouping, and grouping
                     symbol for non-monetary numeric editing.

           LC_TIME   Defines the format and content of date and time
                     information.

           LC_MESSAGES
                     Defines the format and values of affirmative and
                     negative responses.

## [](#OPTIONS)OPTIONS

           The localedef utility shall conform to the Base Definitions volume
           of POSIX.1‐2017, Section 12.2, Utility Syntax Guidelines.

           The following options shall be supported:

           -c        Create permanent output even if warning messages have
                     been issued.

           -f charmap
                     Specify the pathname of a file containing a mapping of
                     character symbols and collating element symbols to
                     actual character encodings.  The format of the charmap
                     is described in the Base Definitions volume of
                     POSIX.1‐2017, Section 6.4, Character Set Description
                     File.  The application shall ensure that this option is
                     specified if symbolic names (other than collating
                     symbols defined in a collating-symbol keyword) are used.
                     If the -f option is not present, an implementation-
                     defined character mapping shall be used.

           -i inputfile
                     The pathname of a file containing the source
                     definitions. If this option is not present, source
                     definitions shall be read from standard input. The
                     format of the inputfile is described in the Base
                     Definitions volume of POSIX.1‐2017, Section 7.3, Locale
                     Definition.

           -u code_set_name
                     Specify the name of a codeset used as the target mapping
                     of character symbols and collating element symbols whose
                     encoding values are defined in terms of the
                     ISO/IEC 10646‐1:2000 standard position constant values.

## [](#OPERANDS)OPERANDS

           The following operand shall be supported:

           name      Identifies the locale; see the Base Definitions volume
                     of POSIX.1‐2017, Chapter 7, Locale for a description of
                     the use of this name. If the name contains one or more
                     <slash> characters, name shall be interpreted as a
                     pathname where the created locale definitions shall be
                     stored. If name does not contain any <slash> characters,
                     the interpretation of the name is implementation-defined
                     and the locale shall be public. The ability to create
                     public locales in this way may be restricted to users
                     with appropriate privileges. (As a consequence of
                     specifying one name, although several categories can be
                     processed in one execution, only categories belonging to
                     the same locale can be processed.)

## [](#STDIN)STDIN

           Unless the -i option is specified, the standard input shall be a
           text file containing one or more locale category source
           definitions, as described in the Base Definitions volume of
           POSIX.1‐2017, Section 7.3, Locale Definition.  When lines are
           continued using the escape character mechanism, there is no limit
           to the length of the accumulated continued line.

## [](#INPUT_FILES)INPUT FILES

           The character set mapping file specified as the charmap option-
           argument is described in the Base Definitions volume of
           POSIX.1‐2017, Section 6.4, Character Set Description File.  If a
           locale category source definition contains a copy statement, as
           defined in the Base Definitions volume of POSIX.1‐2017, Chapter 7,
           Locale, and the copy statement names a valid, existing locale,
           then localedef shall behave as if the source definition had
           contained a valid category source definition for the named locale.

## [](#ENVIRONMENT_VARIABLES)ENVIRONMENT VARIABLES

           The following environment variables shall affect the execution of
           localedef:

           LANG      Provide a default value for the internationalization
                     variables that are unset or null. (See the Base
                     Definitions volume of POSIX.1‐2017, Section 8.2,
                     Internationalization Variables for the precedence of
                     internationalization variables used to determine the
                     values of locale categories.)

           LC_ALL    If set to a non-empty string value, override the values
                     of all the other internationalization variables.

           LC_COLLATE
                     (This variable has no affect on localedef; the POSIX
                     locale is used for this category.)

           LC_CTYPE  Determine the locale for the interpretation of sequences
                     of bytes of text data as characters (for example,
                     single-byte as opposed to multi-byte characters in
                     arguments and input files). This variable has no affect
                     on the processing of localedef input data; the POSIX
                     locale is used for this purpose, regardless of the value
                     of this variable.

           LC_MESSAGES
                     Determine the locale that should be used to affect the
                     format and contents of diagnostic messages written to
                     standard error.

           NLSPATH   Determine the location of message catalogs for the
                     processing of LC_MESSAGES.

## [](#ASYNCHRONOUS_EVENTS)ASYNCHRONOUS EVENTS

           Default.

## [](#STDOUT)STDOUT

           The utility shall report all categories successfully processed, in
           an unspecified format.

## [](#STDERR)STDERR

           The standard error shall be used only for diagnostic messages.

## [](#OUTPUT_FILES)OUTPUT FILES

           The format of the created output is unspecified. If the name
           operand does not contain a <slash>, the existence of an output
           file for the locale is unspecified.

## [](#EXTENDED_DESCRIPTION)EXTENDED DESCRIPTION

           When the -u option is used, the code_set_name option-argument
           shall be interpreted as an implementation-defined name of a
           codeset to which the ISO/IEC 10646‐1:2000 standard position
           constant values shall be converted via an implementation-defined
           method. Both the ISO/IEC 10646‐1:2000 standard position constant
           values and other formats (decimal, hexadecimal, or octal) shall be
           valid as encoding values within the charmap file. The codeset
           represented by the implementation-defined name can be any codeset
           that is supported by the implementation.

           When conflicts occur between the charmap specification of
           <code_set_name>, <mb_cur_max>, or <mb_cur_min> and the
           implementation-defined interpretation of these respective items
           for the codeset represented by the -u option-argument
           code_set_name, the result is unspecified.

           When conflicts occur between the charmap encoding values specified
           for symbolic names of characters of the portable character set and
           the implementation-defined assignment of character encoding
           values, the result is unspecified.

           If a non-printable character in the charmap has a width specified
           that is not -1, the result will be undefined.

## [](#EXIT_STATUS)EXIT STATUS

           The following exit values shall be returned:

            0    No errors occurred and the locales were successfully
                 created.

            1    Warnings occurred and the locales were successfully created.

            2    The locale specification exceeded implementation limits or
                 the coded character set or sets used were not supported by
                 the implementation, and no locale was created.

            3    The capability to create new locales is not supported by the
                 implementation.

           >3    Warnings or errors occurred and no output was created.

## [](#CONSEQUENCES_OF_ERRORS)CONSEQUENCES OF ERRORS

           If an error is detected, no permanent output shall be created.

           If warnings occur, permanent output shall be created if the -c
           option was specified. The following conditions shall cause warning
           messages to be issued:

            *  If a symbolic name not found in the charmap file is used for
               the descriptions of the LC_CTYPE or LC_COLLATE categories (for
               other categories, this shall be an error condition).

            *  If the number of operands to the order keyword exceeds the
               {COLL_WEIGHTS_MAX} limit.

            *  If optional keywords not supported by the implementation are
               present in the source.

           Other implementation-defined conditions may also cause warnings.

           The following sections are informative.

## [](#APPLICATION_USAGE)APPLICATION USAGE

           The charmap definition is optional, and is contained outside the
           locale definition. This allows both completely self-defined source
           files, and generic sources (applicable to more than one codeset).
           To aid portability, all charmap definitions must use the same
           symbolic names for the portable character set. As explained in the
           Base Definitions volume of POSIX.1‐2017, Section 6.4, Character
           Set Description File, it is implementation-defined whether or not
           users or applications can provide additional character set
           description files. Therefore, the -f option might be operable only
           when an implementation-defined charmap is named.

## [](#EXAMPLES)EXAMPLES

           None.

## [](#RATIONALE)RATIONALE

           The output produced by the localedef utility is implementation-
           defined. The name operand is used to identify the specific locale.
           (As a consequence, although several categories can be processed in
           one execution, only categories belonging to the same locale can be
           processed.)

## [](#FUTURE_DIRECTIONS)FUTURE DIRECTIONS

           None.

## [](#SEE_ALSO)SEE ALSO

           locale(1p)

           The Base Definitions volume of POSIX.1‐2017, Section 6.4,
           Character Set Description File, Chapter 7, Locale, Chapter 8,
           Environment Variables, Section 12.2, Utility Syntax Guidelines

## [](#COPYRIGHT)COPYRIGHT

           Portions of this text are reprinted and reproduced in electronic
           form from IEEE Std 1003.1-2017, Standard for Information
           Technology -- Portable Operating System Interface (POSIX), The
           Open Group Base Specifications Issue 7, 2018 Edition, Copyright
           (C) 2018 by the Institute of Electrical and Electronics Engineers,
           Inc and The Open Group.  In the event of any discrepancy between
           this version and the original IEEE and The Open Group Standard,
           the original IEEE and The Open Group Standard is the referee
           document. The original Standard can be obtained online at
           http://www.opengroup.org/unix/online.html .

           Any typographical or formatting errors that appear in this page
           are most likely to have been introduced during the conversion of
           the source files to man page format. To report such errors, see
           https://www.kernel.org/doc/man-pages/reporting_bugs.html .

    IEEE/The Open Group                2017                     LOCALEDEF(1P)

------------------------------------------------------------------------

Pages that refer to this page: [locale(1p)](../man1/locale.1p.html),  [strings(1p)](../man1/strings.1p.html)

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
