---
{"title": "rpm-queryformat(7) — Linux manual page", "url": "https://man7.org/linux/man-pages/man7/rpm-queryformat.7.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# rpm-queryformat(7) --- Linux manual page

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [SYNTAX](#SYNTAX) \| [EXAMPLES](#EXAMPLES) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                       |                                   |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    RPM-QUERYFORMAT(7)   Miscellaneous Information Manual  RPM-QUERYFORMAT(7)

## [](#NAME)NAME

           rpm-queryformat - RPM query mini-language

## [](#SYNOPSIS)SYNOPSIS

       Query format
           [PLACEHOLDER|ITERATOR|EXPRESSION|TEXT ...]

       Placeholder
           %[WIDTH]{TAG[:FORMAT]}

       Iterator
           [QUERYFORMAT ...]

           Note: Square brackets are literal and QUERYFORMAT must contain an
           array placeholder.

       Expression
           %|TAG?{PRESENT}:{ABSENT}|

           Note: Vertical bars are literal, PRESENT and ABSENT are query
           formats.

## [](#DESCRIPTION)DESCRIPTION

           RPM supports a simple query language for extracting header data to
           plain text. Its syntax resembles that of printf(3) where header
           tags enclosed in %{ and }, for example %{NAME}, are used as
           placeholders. A string written in this syntax is called a query
           format.

           Query formats are currently accepted in the following places:

           1.  Query operations with rpm(8), as a way to control the output
               (see --queryformat)
           2.  rpm-scriptlets(7), to access arbitrary header data at runtime
               (see -q)
           3.  Configuration macros in rpm-config(5) and rpmbuild-config(5),
               such as %_query_all_fmt or %_rpmfilename

           See the EXAMPLES section for more details.

## [](#SYNTAX)SYNTAX

           A valid query format is composed of optional literal text and zero
           or more placeholders. A placeholder has the following syntax:

               %[WIDTH]{TAG[:FORMAT]}

           When RPM produces output according to a query format, it
           substitutes each placeholder with the TAG data from the queried
           package and formats the data according to the specified WIDTH and
           FORMAT (if given). The rest of the query format is copied to the
           output unchanged.

           Special characters such as \n or \t, with the exception of \0, are
           also supported. Curly braces, the percent sign and the backslash
           may be escaped with a backslash.

           The individual components of a placeholder, as well as some
           additional language features, are described in the subsections
           below.

       Tags
           Every RPM package contains a key-value store (the header) that
           represents the package's properties, such as its name, version or
           file list. The keys in this store are called tags, and can be used
           in a query format as placeholders for the values (data) they point
           to. The data is either a single scalar (string, integer or binary
           blob), or an array (argv) of multiple scalars of the same type.

           To obtain a list of all tags supported by the installed version of
           RPM, run the following command:

               rpm -v --querytags

           This will print a list of available tags, along with their
           internal numbers and types, for example:

               BASENAMES              1117 argv
               BUILDHOST              1007 string
               BUILDTIME              1006 int32
               DESCRIPTION            1005 i18nstring
               EPOCH                  1003 int32
               INSTALLTIME            1008 int32
               NAME                   1000 string
               RELEASE                1002 string
               SIZE                   1009 int32
               SUMMARY                1004 i18nstring
               VERSION                1001 string

           Tags are case-insensitive. Each tag also has an implicit variant
           with the RPMTAG_ prefix, such as RPMTAG_NAME. Both variants can be
           used in a query format interchangeably.

           See the tags documentation in SEE ALSO for more details.

       Formats
           Each tag is printed in a specific output FORMAT. When no format is
           specified, the default :string is used which displays a bare-bones
           representation of the data. You can specify a different format by
           appending its name after a colon, for example:

               %{INSTALLTIME:date}

           This is useful for tags that are not stored in human-readable
           form, such as sizes, dates or signatures. Some formats allow for
           performing more complex transformations of the data, such as
           encoding it in base64 or wrapping it in JSON syntax.

           The following formats are currently available:

           Name           Description
           :armor         Wrap a public key in ASCII armor
           :arraysize     Display number of elements in array tags
           :base64        Encode binary data using base64
           :date          Use strftime(3) "%c" format
           :day           Use strftime(3) "%a %b %d %Y" format
           :depflags      Format dependency comparison operator
           :deptype       Format dependency type
           :expand        Perform macro expansion
           :fflags        Format file flags
           :fstate        Format file state
           :fstatus       Format file verify status
           :hashalgo      Display hash algorithm name
           :hex           Format in hexadecimal
           :octal         Format in octal
           :humaniec      Human readable number (in IEC 80000) where K =
                          1024, M = 1048576, ...
           :humansi       Human readable number (in SI) where K = 1000, M =
                          1000000, ...
           :json          Wrap data in JSON
           :perms         Format file permissions
           :pgpsig        Display signature fingerprint and time
           :shescape      Escape single quotes for use in a script
           :string        Display string format (default)
           :tagname       Display tag name
           :tagnum        Display tag number
           :triggertype   Display trigger suffix
           :vflags        Format file verification flags
           :xml           Wrap data in simple XML markup

           Note that some formats are type specific, which means they can
           only be used with a specific tag type. If you attempt to use them
           with an incompatible type, RPM will replace them with a
           placeholder text. For example, the following query format will
           result in the output "(not a number)":

               %{NAME:date}

           Similarly, if a tag is not present in the queried package, it will
           be replaced with the text "(none)".

       Width
           You can specify the minimum WIDTH of the data when printed, by
           placing a number in between the % and { characters, similarly to
           field width used in printf(3). Optionally, prefix the number with
           the minus sign to left-justify the text.

       Iterators
           Tags pointing to arrays may be expanded to the individual elements
           by using iterators. An iterator is a query (sub-)format enclosed
           in square brackets that contains a placeholder for an array, for
           example:

               [%{FILENAMES}\n]

           RPM will loop through the enclosed array, outputting the
           (sub-)format each turn and substituting the placeholder with the
           current element. This example includes a newline character, which
           will result in one filename per line.

           Multiple arrays may be placed into a single iterator. RPM will
           then iterate over all of them in lockstep, meaning that the first
           iteration will substitute each placeholder with its array's first
           element, the second iteration will use each array's second
           element, and so on. For example:

               [%10{FILESIZES} %{FILENAMES}\n]

           This is useful with parallel arrays that RPM keeps internally.
           These are sets of arrays where all elements at the same index
           correspond to each other. One can think of parallel arrays as
           table columns that can be arbitrarily rearranged. The above
           example will output a table of files and their sizes.

           Sometimes, it is useful to combine an array with one or more
           scalars in the same iterator. This is possible since RPM
           internally treats all scalars as arrays of size one. However,
           iterators may only contain arrays of the same size, otherwise RPM
           will complain. To avoid that, you can "lock" an array so that only
           its first element is used in each iteration, by prefixing the tag
           with the equal sign, for example:

               [%{=NAME} %{FILENAMES}\n]

           This will produce an "annotated" file list where each filename is
           preceded by the name of the package that contains it.

       Expressions
           Simple conditionals may be evaluated through query expressions in
           the form of

               %|EXPR|

           where EXPR is an expression.

           The only type of expression currently supported is a C-like
           ternary operator for simple if/then/else conditions, which has the
           syntax

               %|TAG?{PRESENT}:{ABSENT}|

           where PRESENT and ABSENT are query formats that should be expanded
           if the queried package does and doesn't have the TAG,
           respectively. Thus, expressions can be nested.

## [](#EXAMPLES)EXAMPLES

       Example 1. Query commands
           rpm -qa --queryformat "%-30{NAME} %{SIZE:humaniec}\n"
               Print a table of all installed package names and their human-
               readable sizes.

           rpm -q --queryformat "%{NAME} %{INSTALLTIME:date}\n" fileutils
               Print the fileutils package name followed by its installation
               date.

           rpm -q --queryformat "[%{FILEMODES:perms} %{FILENAMES}\n]" rpm
               Print all filenames owned by the rpm package, one per line,
               with each name preceded by a file permissions string similar
               to the long listing format of ls(1).

           rpm -q --queryformat "[%{REQUIRENAME} %{REQUIREFLAGS:depflags}
           %{REQUIREVERSION}\n]" vlock
               Print all capabilities on which the vlock package depends in
               the form of version comparisons, one per line, with the
               capability name and the required version as the left and right
               operand, respectively.

           rpm -qa --queryformat "%-30{NAME} %|PREINPROG?{ %{PREINPROG}}:{
           no}|\n"
               Print a table of all installed package names in the left
               column and the program names used for their prein scriptlets
               (such as the default /bin/sh) in the right column, with the
               latter being no if the given package has no prein scriptlet.

       Example 2. Command aliases
           /usr/lib/rpm/rpmpopt-VERSION
               A popt(3) alias file used by rpm(8) itself to implement
               various shorthand options (such as --scripts) with the help of
               query formats. Replace VERSION with the version of RPM
               installed on your system.

       Example 3. Transaction scriptlets
           Print the exact file list of a package after its installation:

               %post -q
               for f in [%%{instfilenames} ]; do
                   echo $f
               done

           Note that the trailing space inside the square brackets is
           required in order for the query format to be expanded to separate
           words that the for statement can loop over.

           See rpm-scriptlets(7) for more information on scriptlets in
           general.

## [](#SEE_ALSO)SEE ALSO

           rpm(8), rpm-common(8), rpm-config(5), rpm-scriptlets(7),
           rpm-spec(5), popt(3)

           https://rpm.org/docs/latest/manual/tags 

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

    RPM 6.1.90                      2026-08-03             RPM-QUERYFORMAT(7)

------------------------------------------------------------------------

Pages that refer to this page: [rpmspec(1)](../man1/rpmspec.1.html),  [rpmbuild-config(5)](../man5/rpmbuild-config.5.html),  [rpm-config(5)](../man5/rpm-config.5.html),  [rpm-scriptlets(7)](../man7/rpm-scriptlets.7.html),  [rpm-sysusers(7)](../man7/rpm-sysusers.7.html),  [rpm(8)](../man8/rpm.8.html)

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
