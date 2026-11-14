---
{"title": "libabigail(7) — Linux manual page", "url": "https://man7.org/linux/man-pages/man7/libabigail.7.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# libabigail(7) --- Linux manual page

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [OVERVIEW OF THE ABIGAIL FRAMEWORK](#OVERVIEW_OF_THE_ABIGAIL_FRAMEWORK) \| [CONCEPTS](#CONCEPTS) \| [TOOLS](#TOOLS) \| [Author](#Author) \| [Copyright](#Copyright) \| [COLOPHON](#COLOPHON) |                                   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                               |                                   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    LIBABIGAIL(7)                   Libabigail                  LIBABIGAIL(7)

## [](#NAME)NAME

           libabigail - Library to analyze and compare ELF ABIs

## [](#OVERVIEW_OF_THE_ABIGAIL_FRAMEWORK)OVERVIEW OF THE ABIGAIL FRAMEWORK

           ABIGAIL stands for the Application Binary Interface Generic
           Analysis and Instrumentation Library.

           It's a framework which aims at helping developers and software
           distributors to spot some ABI-related issues like interface
           incompatibility in ELF
           <http://en.wikipedia.org/wiki/Executable_and_Linkable_Format>
           shared libraries by performing a static analysis of the ELF
           <http://en.wikipedia.org/wiki/Executable_and_Linkable_Format>
           binaries at hand.

           The type of interface incompatibilities that Abigail focuses on is
           related to changes on the exported ELF functions and variables
           symbols, as well as layout and size changes of data types of the
           functions and variables exported by shared libraries.

           In other words, if the return type of a function exported by a
           shared library changes in an incompatible way from one version of
           a given shared library to another, we want Abigail to help people
           catch that.

           In more concrete terms, the Abigail framwork provides a shared
           library named libabigail which exposes an API to parse a shared
           library in ELF
           <http://en.wikipedia.org/wiki/Executable_and_Linkable_Format>
           format (accompanied with its associated debug information in DWARF
           <http://www.dwarfstd.org> format) build an internal representation
           of all the functions and variables it exports, along with their
           types.  Libabigail also builds an internal representation of the
           ELF symbols
           <https://blogs.oracle.com/ali/entry/inside_elf_symbol_tables> of
           these functions and variables.  That information about these
           exported functions and variables is roughly what we consider as
           being the ABI of the shared library, at least, in the scope of
           Libabigail.

           Aside of this internal representation, libabigail provides
           facilities to perform deep comparisons of two ABIs.  That is, it
           can compare the types of two sets of functions or variables and
           represents the result in a way that allows it to emit textual
           reports about the differences.

           This allows us to write tools like abidiff <> that can compare the
           ABI of two shared libraries and represent the result in a
           meaningful enough way to help us spot ABI incompatibilities.
           There are several other tools <> that are built using the Abigail
           framwork.

## [](#CONCEPTS)CONCEPTS

       ABI artifacts
           An ABI artifact is a relevant part of the ABI of a shared library
           or program.  Examples of ABI artifacts are exported types,
           variables, functions, or ELF
           <http://en.wikipedia.org/wiki/Executable_and_Linkable_Format>
           symbols exported by a shared library.

           The set of ABI artifacts for a binary is called an ABI Corpus.

           Scalar types have a name, a size and other scalar properties.

           An aggregate type is generally constituted of sub-types.

           For instance, class or union types are a kind of aggregate type.
           They have a name, a size and members.  Each member can be either

              • a data member with a type representing a sub-type of the
                aggregate type, an offset and a name

              • or a function with a type representing another sub-type of
                the aggregate type and a name.  Some (virtual) member
                functions might have an offset as well.

           Another example of aggregate type is a function type, which is the
           union of the return type and parameter types of the function.

           Functions and variables are declarations that have a name and a
           type.  They are both associated with an ELF
           <http://en.wikipedia.org/wiki/Executable_and_Linkable_Format>
           symbol.

       ABI changes
           Libabigail represents and analyzes changes of types, functions,
           variables and ELF symbols.

           Those different kinds of ABI artifact changes are categorized
           depending on the impact they have on ABI compatibility.

           ABI artifact changes are reported by tools like abidiff <#
           abidiff-label> and abipkgdiff <#abipkgdiff-label> in textual diff
           reports organized around the different kinds of changes listed
           below.

           Please note that users can instruct the tools to avoid emitting
           reports about certain changes.  This is done via suppression
           specifications <#suppr-spec-label>.

       Harmless changes
           A change in the diff report is considered harmless if it does not
           cause any ABI compatibility issue.  That is, it does not prevent
           an application dynamically linked against a given version of a
           library to keep working with the changed subsequent versions of
           the same library.

           By default, abidiff <#abidiff-label> and abipkgdiff <#
           abipkgdiff-label> filters harmless changes from the diff report.

       Harmful changes
           An ABI change is considered harmful if it might cause ABI
           compatibility issues.  That is, it might prevent an application
           dynamically linked against a given version of a library to keep
           working with the changed subsequent versions of the same library.

           Said otherwise, a harmful change is a change that is not harmless.

           A harmful change absolutely needs to be reviewed by a human being
           to know if it actually causes an ABI compatibility issue.

           By default, abidiff <#abidiff-label> shows harmful changes for
           functions and global variables.

           If the tool emits at least one harmful change then the bit
           ABIDIFF_ABI_CHANGE <#abidiff-return-value-label> of the bit-field
           returned in the exit code is set to 1.

       Incompatible changes
           An incompatible change is a harmful change that causes ABI
           incompatibilities issues.  In the colloquial language of
           programmers, such a change is said to break ABI.

           If the abidiff <#abidiff-label> or abipkgdiff <#abipkgdiff-label>
           tool emits at least one incompatible change then the bits
           ABIDIFF_ABI_INCOMPATIBLE_CHANGE <#abidiff-return-value-label> and
           ABIDIFF_ABI_CHANGE <#abidiff-return-value-label> of the bit-field
           returned in the exit code are set to 1.

           Changes recognized as ABI incompatible are the following:

           • SONAME change of shared library

           • change of the architecture of a binary

           • remove of exported function or global variable ELF symbols (not
             necessarily described by debug information)

           • removal of exported functions or global variables that are
             described by debug information.

           • any incompatible change to the layout of the type which is used
             as a type of a global variable or a return or parameter type of
             a function.  That incompatible layout type change might be:

                • a modification to the size of the type

                • or the removal of a data member

                • or a modification of a data member offset

                • or an incompatible change to a sub-type of the type

             Please note that if a type is used neither as a type of a global
             variable nor as a return or parameter type of a function, then
             abidiff <#abidiff-label> (or abipkgdiff <#abipkgdiff-label>)
             will not consider an incompatible change of this type as an
             incompatible ABI change.  That change will just be considered as
             harmful.  The ABIDIFF_ABI_CHANGE <#abidiff-return-value-label>
             bit of the bit-field returned in the exit code is set to 1,
             meaning that the change requires a human review.  This is a
             current limitation of the libabigail analysis framework that
             might be addressed in future refinements.

       Suppression specifications
       Definition
           A suppression specification file is a way for a user to instruct
           abidiff <#abidiff-label>, abipkgdiff <#abipkgdiff-label> or any
           other relevant libabigail tool to avoid emitting reports for
           changes involving certain ABI artifacts <#abi-artifacts-label>.

           It contains directives (or specifications) that describe the set
           of ABI artifacts to avoid emitting change reports about.

       Introductory examples
           Its syntax is based on a simplified and customized form of Ini
           File Syntax <http://en.wikipedia.org/wiki/INI_file>.  For
           instance, to specify that change reports on a type named
           FooPrivateType should be suppressed, one could write this
           suppression specification:

              [suppress_type]
                name = FooPrivateType

           If we want to ensure that only change reports about structures
           named FooPrivateType should be suppressed, we could write:

              [suppress_type]
                type_kind = struct
                name = FooPrivateType

           But we could also want to suppress change reports avoid typedefs
           named FooPrivateType.  In that case we would write:

              [suppress_type]
                type_kind = typedef
                name = FooPrivateType

           Or, we could want to suppress change reports about all struct
           which names end with the string "PrivateType":

              [suppress_type]
                type_kind = struct
                name_regexp = ^.*PrivateType

           Let's now look at the generic syntax of suppression specification
           files.

       Syntax
       Properties
           More generally, the format of suppression lists is organized
           around the concept of property.  Every property has a name and a
           value, delimited by the = sign.  E.g:

              name = value

           Leading and trailing white spaces are ignored around property
           names and values.

       Regular expressions
           The value of some properties might be a regular expression.  In
           that case, they must comply with the syntax of extended POSIX
           regular expressions
           <http://www.gnu.org/software/findutils/manual/html_node/find_html/posix_002dextended-regular-expression-syntax.html#posix_002dextended-regular-expression-syntax>.
           Note that Libabigail uses the regular expression engine of the GNU
           C Library <http://www.gnu.org/software/libc>.

       Escaping a character in a regular expression
           When trying to match a string that contains a * character, like in
           the pointer type int*, one must be careful to notice that the
           character * is a special character in the extended POSIX regular
           expression syntax.  And that character must be escaped for the
           regular expression engine.  Thus the regular expression that would
           match the string int* in a suppression file should be

              int\\*

           Wait; but then why the two \ characters?  Well, because the \
           character is a special character in the Ini File Syntax
           <http://en.wikipedia.org/wiki/INI_file> used for specifying
           suppressions.  So it must be escaped as well, so that the Ini File
           parser leaves a \ character intact in the data stream that is
           handed to the regular expression engine.  Hence the \\ targeted at
           the Ini File parser.

           So, in short, to escape a character in a regular expression,
           always prefix the character with the \\ sequence.

       Modus operandi
           Suppression specifications can be applied at two different points
           of the processing pipeline of libabigail.

           In the default operating mode called "late suppression mode",
           suppression specifications are applied to the result of comparing
           the in-memory internal representations of two ABIs.  In this mode,
           if an ABI artifact matches a suppression specification, its
           changes are not mentioned in the ABI change report.  The internal
           representation of the "suppressed" changed ABI artifact is still
           present in memory; it is just not mentioned in the ABI change
           report.  The change report can still mention statistics about the
           number of changed ABI artifacts that were suppressed.

           This is the default mode of interpretation of suppression
           specifications for most tools including abidiff <#abidiff-label>
           and abidw <#abidw-label>.

           There is another operating mode called the "early suppression
           mode" where suppression specifications are applied during the
           construction of the in-memory internal representation of a given
           ABI.  In that mode, if an ABI artifact matches a suppression
           specification, no in-memory internal representation is built for
           it.  As a result, no change about the matched ABI artifact is
           going to be mentioned in the ABI change report and no statistic
           about the number of suppressed ABI changes is available.  Also,
           please note that because suppressed ABI artifacts are removed from
           the in-memory internal representation in this mode, the amount of
           memory used by the internal representation is potentially smaller
           than the memory consumption in the late suppression mode.

           Please note that this mode suppresses data from the internal
           representation constructed by libabigail and thus can lead to
           unintended and surprising consequences.  Consequently this mode
           has to be set explicitly by users either by using the drop
           property in a suppression specification or by using a special tool
           command line option like abidw --force-early-suppression <#
           abidw-force-early-suppression-option-label>.

       Sections
           Properties are then grouped into arbitrarily named sections that
           shall not be nested.  The name of the section is on a line by
           itself and is surrounded by square brackets, i.e:

              [section_name]
              property1_name = property1_value
              property2_name = property2_value

           A section might or might not have properties.  Sections that
           expect to have properties and which are found nonetheless empty
           are just ignored.  Properties that are not recognized by the
           reader are ignored as well.

       Section names
           Each different section can be thought of as being a directive to
           suppress ABI change reports for a particular kind of ABI artifact.

       [suppress_file]
           This directive prevents a given tool from loading a file (binary
           or abixml file) if its file name or other properties match certain
           properties.  Thus, if the tool is meant to compare the ABIs of two
           files, and if the directive prevents it from loading either one of
           the files, then no comparison is performed.

           Note that for the [suppress_file] directive to work, at least one
           of the following properties must be provided:
              file_name_regexp, file_name_not_regexp, soname_regexp,
              soname_not_regexp.

           If none of the above properties are provided, then the
           [suppress_file] directive is simply ignored.

           The potential properties of this sections are listed below:

           • file_name_not_regexp

             Usage:
                file_name_not_regexp = <regular-expression>

             Prevents the system from loading the file which name does not
             match the regular expression specified as value of this
             property.

           • file_name_regexp

             Usage:
                file_name_regexp = <regular-expression>

             Prevents the system from loading the file which name matches the
             regular expression specified as value of this property.

           • label
              Usage:
                  label = <some-value>

              Define a label for the section.  A label is just an informative
              string that might be used by the tool to refer to a type
              suppression in error messages.  There can also be some special
              label names that make the suppression system behave a certain
              way.

           • soname_regexp

             Usage:
                soname_regexp = <regular-expression>

             Prevents the system from loading the file which contains a
             SONAME property that matches the regular expression of this
             property.  Note that this property also works on an abixml file
             if it contains a SONAME property.

           • soname_not_regexp

             Usage:
                soname_not_regexp = <regular-expression>

             Prevents the system from loading the file which contains a
             SONAME property that does NOT match the regular expression of
             this property.  Note that this property also works on an abixml
             file if it contains a SONAME property.

       [suppress_type]
           This directive suppresses report messages about a type change.

           Note that for the [suppress_type] directive to work, at least one
           of the following properties must be provided:
              file_name_regexp, file_name_not_regexp, soname_regexp,
              soname_not_regexp, name, name_regexp, name_not_regexp,
              source_location_not_in, source_location_not_regexp, type_kind.

           If none of the above properties are provided, then the
           [suppress_type] directive is simply ignored.

           The potential properties of this sections are listed below:

           • accessed_through
              Usage:
                  accessed_through = <some-predefined-values>

              Suppress change reports involving a type which is referred to
              either directly or through a pointer or a reference.  The
              potential values of this property are the predefined keywords
              below:

                  • direct

                    So if the [suppress_type] contains the property
                    description:

                       accessed_through = direct

                    then changes about a type that is referred-to directly
                    (i.e, not through a pointer or a reference) are going to
                    be suppressed.

                  • pointer

                    If the accessed_through property is set to the value
                    pointer then changes about a type that is referred-to
                    through a pointer are going to be suppressed.

                  • reference

                    If the accessed_through property is set to the value
                    reference then changes about a type that is referred-to
                    through a reference are going to be suppressed.

                  • reference-or-pointer

                    If the accessed_through property is set to the value
                    reference-or-pointer then changes about a type that is
                    referred-to through either a reference or a pointer are
                    going to be suppressed.

              For an extensive example of how to use this property, please
              check out the example below about suppressing change reports
              about types accessed either directly or through pointers.

           • changed_enumerators

             Usage:
                changed_enumerators = <list-of-enumerators>

             Suppresses change reports involving changes in the value of
             enumerators of a given enum type.  This property is applied if
             the type_kind property is set to the value enum, at least.  The
             value of the changed_enumerators is a comma-separated list of
             the enumerators that the user expects to change.  For instance:

                changed_enumerators = LAST_ENUMERATORS0, LAST_ENUMERATOR1

           • changed_enumerators_regexp

             Usage:
                changed_enumerators_regexp =
                <list-of-enumerator-regular-expressions>

             Suppresses change reports involving changes in the value of
             enumerators of a given enum type.  This property is applied if
             the type_kind property is set to the value enum, at least.  The
             value of the changed_enumerators_regexp property is a
             comma-separated list of regular expressions that should match
             the names of the enumerators that the user expects to change.
             For instance:

                changed_enumerators_regexp = .*_MAX$, .*_LAST$, .*_NUM$, .*_NBITS$

             In the example above, change reports to any enumerator which
             name ends with _MAX, _LAST, _NUM or _NBITS will be suppressed.

             Note that for this property to be applied to changes to an enum
             type, the size of the enum type must NOT have changed.

           • drop
              Usage:
                  drop = yes | no

              If a type is matched by a suppression specification which
              contains the "drop" property set to "yes" (or to "true") then
              the type is not even going to be represented in the internal
              representation of the ABI being analyzed.  This property makes
              its enclosing suppression specification to be applied in the
              early suppression specification mode.  The net effect is that
              it potentially reduces the amount of memory used to represent
              the ABI being analyzed.

              Please note that for struct, class or enum types matching a
              suppression specification with this property having a value set
              to "yes" (or to "true"), if the specification also has a label
              property with a value set to libabigail::OPAQUE_TYPE_LABEL,
              then the type is transformed into an opaque type, rather than
              being just dropped on the floor.  That also reduces the amount
              of memory used to represent the ABI being analyzed, but with
              potentially less disruption in the resulting ABI
              representation.

              Please note that for this property to be effective, the
              enclosing suppression specification must have at least one of
              the following properties specified: name_regexp, name,
              name_regexp, source_location_not_in or
              source_location_not_regexp.

           • file_name_not_regexp

             Usage:
                file_name_not_regexp = <regular-expression>

             Suppresses change reports about ABI artifacts that are defined
             in a binary file which name does not match the regular
             expression specified as value of this property.

           • file_name_regexp

             Usage:
                file_name_regexp = <regular-expression>

             Suppresses change reports about ABI artifacts that are defined
             in a binary file which name matches the regular expression
             specified as value of this property.

           • has_data_member

             Usage:
                has_data_member = <list-of-data-member-names>

           Suppresses change reports involving a type which contains data
           members whose names are provided in the list value of this
           property.

           A usage examples of this property would be:

              has_data_member = {private_data_member0, private_data_member1}

           The property above would match any type which contains at least
           two data members whose names are private_data_member0 and
           private_data_member1.

           Another usage examples of this property would be:

              has_data_member = another_private_data_member

           The property above would match any type which contains a data
           member which name is another_private_data_member0.

           • has_data_member_regexp

             Usage:
                has_data_member_regexp = <a-regular-expression>

           Suppresses change reports involving a type which contains data
           members whose names match the regular expression provided as the
           value of this property.

           A usage examples of this property would be:

              has_data_member_regexp = ^private_data_member

           The property above would match any type which contains data
           members whose names match the regular expression
           ^private_data_member.  In other words, it would match any type
           which contains data members whose names start with the string
           "private_data_member".

           • has_data_member_inserted_at
              Usage:
                  has_data_member_inserted_at = <offset-in-bit>

              Suppresses change reports involving a type which has at least
              one data member inserted at an offset specified by the property
              value offset-in-bit.  Please note that if the size of the type
              changed, then the type change will NOT be suppressed by the
              evaluation of this property, unless the has_size_change
              property is present and set to yes.

              The value offset-in-bit is either:

                  • an integer value, expressed in bits, which denotes the
                    offset of the insertion point of the data member,
                    starting from the beginning of the relevant structure or
                    class.

                  • data member offset selector expressions, such as:

                       • the keyword end which is a named constant which
                         value equals the offset of the end of the structure
                         or class.

                       • the keyword offset_of_flexible_array_data_member
                         which is a named constant that evaluates to the
                         offset of the flexible array data member contained
                         in the relevant structure.

                       • the function call expression
                         offset_of(data-member-name) where data-member-name
                         is the name of a given data member of the relevant
                         structure or class.  The value of this function call
                         expression is an integer that represents the offset
                         of the data member denoted by data-member-name.

                       • the function call expression
                         offset_after(data-member-name) where
                         data-member-name is the name of a given data member
                         of the relevant structure or class.  The value of
                         this function call expression is an integer that
                         represents the offset of the point that comes right
                         after the region occupied by the data member denoted
                         by data-member-name.

                       • the function call expression
                         offset_of_first_data_member_regexp(data-member-name-regexp)
                         where data-member-name-regexp is a regular
                         expression matching a data member.  The value of
                         this function call expression is an integer that
                         represents the offset of the first data member which
                         name matches the regular expression argument.  If no
                         data member of a given class type matches the
                         regular expression, then the class type won't match
                         the current directive.

                       • the function call expression
                         offset_of_last_data_member_regexp(data-member-name-regexp)
                         where data-member-name-regexp is a regular
                         expression matching a data member.  The value of
                         this function call expression is an integer that
                         represents the offset of the last data member which
                         name matches the regular expression argument.  If no
                         data member of a given class type matches the
                         regular expression, then the class type won't match
                         the current directive.

           • has_data_member_inserted_between
              Usage:
                  has_data_member_inserted_between = {<range-begin>,
                  <range-end>}

              Suppresses change reports involving a type which has at least
              one data member inserted at an offset that is comprised in the
              range between range-begin and range-end.  Please note that each
              of the values range-begin and range-end can be of the same form
              as the has_data_member_inserted_at property above.  Please also
              note that if the size of the type changed, then the type change
              will NOT be suppressed by the evaluation of this property,
              unless the has_size_change property is present and set to yes.
              Note that data member deletions happening in the range between
              range-begin and range-end won't prevent the type change from
              being suppressed by the evaluation of this property if the size
              of the type doesn't change or if the has_size_change property
              is present and set to yes.

              Usage examples of this properties are:

                  has_data_member_inserted_between = {8, 64}

              or:

                  has_data_member_inserted_between = {16, end}

              or:

                  has_data_member_inserted_between = {offset_after(member1), end}

           • has_data_members_inserted_between
              Usage:
                  has_data_members_inserted_between = {<sequence-of-ranges>}

              Suppresses change reports involving a type which has multiple
              data member inserted in various offset ranges.  A usage example
              of this property is, for instance:

                  has_data_members_inserted_between = {{8, 31}, {72, 95}}

              This usage example suppresses change reports involving a type
              which has data members inserted in bit offset ranges [8 31] and
              [72 95].  The length of the sequence of ranges or this
              has_data_members_inserted_between is not bounded; it can be as
              long as the system can cope with.  The values of the boundaries
              of the ranges are of the same kind as for the
              has_data_member_inserted_at property above.  Please also note
              that if the size of the type changed, then the type will NOT be
              suppressed by the evaluation of this property, unless the
              has_size_change property is present and set to yes.  Note that
              data member deletions happening in the defined ranges won't
              prevent the type change from being suppressed by the evaluation
              of this property if the size of the type doesn't change or if
              the has_size_change property is present and set to yes.

              Another usage example of this property is thus:

                  has_data_members_inserted_between =
                    {
                         {offset_after(member0), offset_of(member1)},
                         {72, end}
                    }

           • has_strict_flexible_array_data_member_conversion
              Usage:
                  has_strict_flexible_array_data_member_conversion = yes | no

              Suppresses change reports involving a type which has a "fake"
              flexible array member at the end of the struct which is
              converted to a real flexible array member. This would be a
              member like data[1] being converted to data[].

              Please note that if the size of the type changed, then the type
              change will NOT be suppressed by the evaluation of this
              property, unless the has_size_change property is present and
              set to yes.

           • has_size_change
              Usage:
                  has_size_change = yes | no

           This property is to be used in conjunction with the properties
           has_data_member_inserted_between,
           has_data_members_inserted_between, and
           has_strict_flexible_array_data_member_conversion Those properties
           will not match a type change if the size of the type changes,
           unless the has_size_changes property is set to yes.

           • label
              Usage:
                  label = <some-value>

              Define a label for the section.  In general, a label is just an
              informative string that might be used by a tool to refer to a
              type suppression in error messages.

              Note however that there are some special label values that can
              trigger a special kind of behavior.  Below are those special
              label values:

                  • libabigail::OPAQUE_TYPE_LABEL: A struct, class or enum
                    type that matches a [suppress_type] section with this
                    label property value is going to be replaced by an opaque
                    type of the same kind.  Note that an opaque type is
                    essentially a declaration-only type, thus with no member.
                    Also note that for a [suppress_type] section with this
                    label to trigger the transformation of a type into an
                    opaque type, the section must have the drop property
                    value set to yes|true.

           • name
              Usage:
                  name = <a-value>

              Suppresses change reports involving types whose name equals the
              value of this property.

           • name_not_regexp
              Usage:
                  name_not_regexp = <regular-expression>

              Suppresses change reports involving types whose name does NOT
              match the regular expression specified as value of this
              property.  Said otherwise, this property specifies which types
              to keep, rather than types to suppress from reports.

           • name_regexp
              Usage:
                  name_regexp = <regular-expression>

              Suppresses change reports involving types whose name matches
              the regular expression specified as value of this property.

           • soname_not_regexp

             Usage:
                soname_not_regexp = <regular-expression>

             Suppresses change reports about ABI artifacts that are defined
             in a shared library which SONAME property does not match the
             regular expression specified as value of this property.

           • soname_regexp

             Usage:
                soname_regexp = <regular-expression>

             Suppresses change reports about ABI artifacts that are defined
             in a shared library which SONAME property matches the regular
             expression specified as value of this property.

           • source_location_not_in
              Usage:
                  source_location_not_in = <list-of-file-paths>

              Suppresses change reports involving a type which is defined in
              a file which path is NOT listed in the value
              list-of-file-paths.  Note that the value is a comma-separated
              list of file paths e.g, this property

                  source_location_not_in = libabigail/abg-ir.h, libabigail/abg-dwarf-reader.h

              suppresses change reports about all the types that are NOT
              defined in header files whose path end up with the strings
              libabigail/abg-ir.h or libabigail/abg-dwarf-reader.h.

           • source_location_not_regexp
              Usage:
                  source_location_not_regexp = <regular-expression>

              Suppresses change reports involving a type which is defined in
              a file which path does NOT match the regular expression
              provided as value of the property. E.g, this property

                  source_location_not_regexp = libabigail/abg-.*\\.h

              suppresses change reports involving all the types that are NOT
              defined in header files whose path match the regular expression
              provided a value of the property.

           • type_kind
              Usage:

                  type_kind = class | struct | union | enum |
                         array | typedef | builtin

              Suppresses change reports involving a certain kind of type.
              The kind of type to suppress change reports for is specified by
              the possible values listed above:

                  •

                    class: suppress change reports for class types. Note that
                           even if class types don't exist for C, this value
                           still triggers the suppression of change reports
                           for struct types, in C.  In C++ however, it should
                           do what it suggests.

                  •

                    struct: suppress change reports for struct types in C or
                    C++.
                           Note that the value class above is a super-set of
                           this one.

                  • union: suppress change reports for union types.

                  • enum: suppress change reports for enum types.

                  • array: suppress change reports for array types.

                  • typedef: suppress change reports for typedef types.

                  • builtin: suppress change reports for built-in (or native)
                    types.  Example of built-in types are char, int, unsigned
                    int, etc.

       [suppress_function]
           This directive suppresses report messages about changes on a set
           of functions.

           Note that for the [suppress_function] directive to work, at least
           one of the following properties must be provided:
              label, file_name_regexp, file_name_not_regexp, soname_regexp,
              soname_not_regexp, name, name_regexp, name_not_regexp,
              parameter, return_type_name, return_type_regexp, symbol_name,
              symbol_name_regexp, symbol_name_not_regexp, symbol_version,
              symbol_version_regexp.

           If none of the above properties are provided, then the
           [suppress_function] directive is simply ignored.

           The potential properties of this sections are:

           • change_kind
              Usage:
                  change_kind = <predefined-possible-values>

              Specifies the kind of changes this suppression specification
              should apply to.  The possible values of this property as well
              as their meaning are listed below:

                  • function-subtype-change

                    This suppression specification applies to functions that
                    which have at least one sub-type that has changed.

                  • added-function

                    This suppression specification applies to functions that
                    have been added to the binary.

                  • deleted-function

                    This suppression specification applies to functions that
                    have been removed from the binary.

                  • all

                    This suppression specification applies to functions that
                    have all of the changes above.  Note that not providing
                    the change_kind property at all is equivalent to setting
                    it to the value all.

           • drop
              Usage:
                  drop = yes | no

              If a function is matched by a suppression specification which
              contains the "drop" property set to "yes" (or to "true") then
              the function is not even going to be represented in the
              internal representation of the ABI being analyzed.  This
              property makes its enclosing suppression specification to be
              applied in the early suppression specification mode.  The net
              effect is that it potentially reduces the memory used to
              represent the ABI being analyzed.

              Please note that for this property to be effective, the
              enclosing suppression specification must have at least one of
              the following properties specified: name_regexp, name,
              name_regexp, source_location_not_in or
              source_location_not_regexp.

           • file_name_not_regexp

             Usage:
                file_name_not_regexp = <regular-expression>

             Suppresses change reports about ABI artifacts that are defined
             in a binary file which name does not match the regular
             expression specified as value of this property.

           • file_name_regexp

             Usage:

             file_name_regexp = <regular-expression>

             Suppresses change reports about ABI artifacts that are defined
             in a binary file which name matches the regular expression
             specified as value of this property.

           • label
              Usage:
                  label = <some-value>

              This property is the same as the label property defined above.

           • name
              Usage:
                  name = <some-value>

              Suppresses change reports involving functions whose name equals
              the value of this property.

           • name_not_regexp
              Usage:
                  name_not_regexp = <regular-expression>

              Suppresses change reports involving functions whose names don't
              match the regular expression specified as value of this
              property.

              The rules for functions that have several symbol names are the
              same rules as for the name_regexp property above.

           • name_regexp
              Usage:
                  name_regexp = <regular-expression>

              Suppresses change reports involving functions whose name
              matches the regular expression specified as value of this
              property.

              Let's consider the case of functions that have several symbol
              names.  This happens when the underlying symbol for the
              function has aliases.  Each symbol name is actually one alias
              name.

              In this case, if the regular expression matches the name of at
              least one of the aliases names, then it must match the names of
              all of the aliases of the function for the directive to
              actually suppress the diff reports for said function.

           • parameter
              Usage:
                  parameter = <function-parameter-specification>

              Suppresses change reports involving functions whose parameters
              match the parameter specification indicated as value of this
              property.

              The format of the function parameter specification is:

              ' <parameter-index> <space> <type-name-or-regular-expression>

              That is, an apostrophe followed by a number that is the index
              of the parameter, followed by one of several spaces, followed
              by either the name of the type of the parameter, or a regular
              expression describing a family of parameter type names.

              If the parameter type name is designated by a regular
              expression, then said regular expression must be enclosed
              between two slashes; like /some-regular-expression/.

              The index of the first parameter of the function is zero.  Note
              that for member functions (methods of classes), the this is the
              first parameter that comes after the implicit "this" pointer
              parameter.

              Examples of function parameter specifications are:

                  '0 int

              Which means, the parameter at index 0, whose type name is int.

                  '4 unsigned char*

              Which means, the parameter at index 4, whose type name is
              unsigned char*.

                  '2 /^foo.*&/

              Which means, the parameter at index 2, whose type name starts
              with the string "foo" and ends with an '&'.  In other words,
              this is the third parameter and it's a reference on a type that
              starts with the string "foo".

           • return_type_name
              Usage:
                  return_type_name = <some-value>

              Suppresses change reports involving functions whose return type
              name equals the value of this property.

           • return_type_regexp
              Usage:
                  return_type_regexp = <regular-expression>

              Suppresses change reports involving functions whose return type
              name matches the regular expression specified as value of this
              property.

           • soname_regexp

             Usage:
                soname_regexp = <regular-expression>

             Suppresses change reports about ABI artifacts that are defined
             in a shared library which SONAME property matches the regular
             expression specified as value of this property.

           • soname_not_regexp

             Usage:
                soname_not_regexp = <regular-expression>

             Suppresses change reports about ABI artifacts that are defined
             in a shared library which SONAME property does not match the
             regular expression specified as value of this property.

           • symbol_name
              Usage:
                  symbol_name = <some-value>

              Suppresses change reports involving functions whose symbol name
              equals the value of this property.

           • symbol_name_regexp
              Usage:
                  symbol_name_regexp = <regular-expression>

              Suppresses change reports involving functions whose symbol name
              matches the regular expression specified as value of this
              property.

              Let's consider the case of functions that have several symbol
              names.  This happens when the underlying symbol for the
              function has aliases.  Each symbol name is actually one alias
              name.

              In this case, the regular expression must match the names of
              all of the aliases of the function for the directive to
              actually suppress the diff reports for said function.

           • symbol_name_not_regexp
              Usage:
                  symbol_name_not_regexp = <regular-expression>

              Suppresses change reports involving functions whose symbol name
              does not match the regular expression specified as value of
              this property.

           • symbol_version
              Usage:
                  symbol_version = <some-value>

              Suppresses change reports involving functions whose symbol
              version equals the value of this property.

           • symbol_version_regexp
              Usage:
                  symbol_version_regexp = <regular-expression>

              Suppresses change reports involving functions whose symbol
              version matches the regular expression specified as value of
              this property.

       [suppress_variable]
           This directive suppresses report messages about changes on a set
           of variables.

           Note that for the [suppress_variable] directive to work, at least
           one of the following properties must be provided:
              label, file_name_regexp, file_name_not_regexp, soname_regexp,
              soname_not_regexp, name, name_regexp, name_not_regexp,
              symbol_name, symbol_name_regexp, symbol_name_not_regexp,
              symbol_version, symbol_version_regexp, type_name,
              type_name_regexp.

           If none of the above properties are provided, then the
           [suppress_variable] directive is simply ignored.

           The potential properties of this sections are:

           • label
              Usage:
                  label = <some-value>

              This property is the same as the label property defined above.

           • file_name_regexp

             Usage:

             file_name_regexp = <regular-expression>

             Suppresses change reports about ABI artifacts that are defined
             in a binary file which name matches the regular expression
             specified as value of this property.

           • file_name_not_regexp

             Usage:
                file_name_not_regexp = <regular-expression>

             Suppresses change reports about ABI artifacts that are defined
             in a binary file which name does not match the regular
             expression specified as value of this property.

           • soname_regexp

             Usage:
                soname_regexp = <regular-expression>

             Suppresses change reports about ABI artifacts that are defined
             in a shared library which SONAME property matches the regular
             expression specified as value of this property.

           • soname_not_regexp

             Usage:
                soname_not_regexp = <regular-expression>

             Suppresses change reports about ABI artifacts that are defined
             in a shared library which SONAME property does not match the
             regular expression specified as value of this property.

           • name
              Usage:
                  name = <some-value>

              Suppresses change reports involving variables whose name equals
              the value of this property.

           • name_regexp
              Usage:
                  name_regexp = <regular-expression>

              Suppresses change reports involving variables whose name
              matches the regular expression specified as value of this
              property.

           • change_kind
              Usage:
                  change_kind = <predefined-possible-values>

              Specifies the kind of changes this suppression specification
              should apply to.  The possible values of this property as well
              as their meaning are the same as when it's used in the
              [suppress_function] section.

           • symbol_name
              Usage:
                  symbol_name = <some-value>

              Suppresses change reports involving variables whose symbol name
              equals the value of this property.

           • symbol_name_regexp
              Usage:
                  symbol_name_regexp = <regular-expression>

              Suppresses change reports involving variables whose symbol name
              matches the regular expression specified as value of this
              property.

           • symbol_name_not_regexp
              Usage:
                  symbol_name_not_regexp = <regular-expression>

              Suppresses change reports involving variables whose symbol name
              does not match the regular expression specified as value of
              this property.

           • symbol_version
              Usage:
                  symbol_version = <some-value>

              Suppresses change reports involving variables whose symbol
              version equals the value of this property.

           • symbol_version_regexp
              Usage:
                  symbol_version_regexp = <regular-expression>

              Suppresses change reports involving variables whose symbol
              version matches the regular expression specified as value of
              this property.

           • type_name
              Usage:
                  type_name = <some-value>

              Suppresses change reports involving variables whose type name
              equals the value of this property.

           • type_name_regexp
              Usage:
                  type_name_regexp = <regular-expression>

              Suppresses change reports involving variables whose type name
              matches the regular expression specified as value of this
              property.

       Comments
           ; or # ASCII character at the beginning of a line indicates a
           comment.  Comment lines are ignored.

       Code examples
           1. Suppressing change reports about types.

              Suppose we have a library named libtest1-v0.so which contains
              this very useful code:

                 $ cat -n test1-v0.cc
                      1  // A forward declaration for a type considered to be opaque to
                      2  // function foo() below.
                      3  struct opaque_type;
                      4
                      5  // This function cannot touch any member of opaque_type.  Hence,
                      6  // changes to members of opaque_type should not impact foo, as far as
                      7  // ABI is concerned.
                      8  void
                      9  foo(opaque_type*)
                     10  {
                     11  }
                     12
                     13  struct opaque_type
                     14  {
                     15    int member0;
                     16    char member1;
                     17  };
                 $

           Let's change the layout of struct opaque_type by inserting a data
           member around line 15, leading to a new version of the library,
           that we shall name libtest1-v1.so:

              $ cat -n test1-v1.cc
                   1  // A forward declaration for a type considered to be opaque to
                   2  // function foo() below.
                   3  struct opaque_type;
                   4
                   5  // This function cannot touch any member of opaque_type;  Hence,
                   6  // changes to members of opaque_type should not impact foo, as far as
                   7  // ABI is concerned.
                   8  void
                   9  foo(opaque_type*)
                  10  {
                  11  }
                  12
                  13  struct opaque_type
                  14  {
                  15    char added_member; // <-- a new member got added here now.
                  16    int member0;
                  17    char member1;
                  18  };
              $

           Let's compile both examples.  We shall not forget to compile them
           with debug information generation turned on:

              $ g++ -shared -g -Wall -o libtest1-v0.so test1-v0.cc
              $ g++ -shared -g -Wall -o libtest1-v1.so test1-v1.cc

           Let's ask abidiff <#abidiff-label> which ABI differences it sees
           between libtest1-v0.so and libtest1-v1.so:

              $ abidiff libtest1-v0.so libtest1-v1.so
              Functions changes summary: 0 Removed, 1 Changed, 0 Added function
              Variables changes summary: 0 Removed, 0 Changed, 0 Added variable

              1 function with some indirect sub-type change:

                [C]'function void foo(opaque_type*)' has some indirect sub-type changes:
                  parameter 0 of type 'opaque_type*' has sub-type changes:
                    in pointed to type 'struct opaque_type':
                      size changed from 64 to 96 bits
                      1 data member insertion:
                        'char opaque_type::added_member', at offset 0 (in bits)
                      2 data member changes:
                       'int opaque_type::member0' offset changed from 0 to 32
                       'char opaque_type::member1' offset changed from 32 to 64

           So abidiff reports that the opaque_type's layout has changed in a
           significant way, as far as ABI implications are concerned, in
           theory.  After all, a sub-type (struct opaque_type) of an exported
           function (foo()) has seen its layout change.  This might have non
           negligible ABI implications.  But in practice here, the programmer
           of the litest1-v1.so library knows that the "soft" contract
           between the function foo() and the type struct opaque_type is to
           stay away from the data members of the type.  So layout changes of
           struct opaque_type should not impact foo().

           Now to teach abidiff about this soft contract and have it avoid
           emitting what amounts to false positives in this case, we write
           the suppression specification file below:

              $ cat test1.suppr
              [suppress_type]
                type_kind = struct
                name = opaque_type

           Translated in plain English, this suppression specification would
           read: "Do not emit change reports about a struct which name is
           opaque_type".

           Let's now invoke abidiff on the two versions of the library again,
           but this time with the suppression specification:

              $ abidiff --suppressions test1.suppr libtest1-v0.so libtest1-v1.so
              Functions changes summary: 0 Removed, 0 Changed (1 filtered out), 0 Added function
              Variables changes summary: 0 Removed, 0 Changed, 0 Added variable

           As you can see, abidiff does not report the change anymore; it
           tells us that it was filtered out instead.

           Suppressing change reports about types with data member insertions

           Suppose the first version of a library named libtest3-v0.so has
           this source code:

              /* Compile this with:
                   gcc -g -Wall -shared -o libtest3-v0.so test3-v0.c
               */

              struct S
              {
                char member0;
                int member1; /*
                                between member1 and member2, there is some padding,
                                at least on some popular platforms.  On
                                these platforms, adding a small enough data
                                member into that padding shouldn't change
                                the offset of member1.  Right?
                              */
              };

              int
              foo(struct S* s)
              {
                return s->member0 + s->member1;
              }

           Now, suppose the second version of the library named
           libtest3-v1.so has this source code in which a data member has
           been added in the padding space of struct S and another data
           member has been added at its end:

              /* Compile this with:
                   gcc -g -Wall -shared -o libtest3-v1.so test3-v1.c
               */

              struct S
              {
                char member0;
                char inserted1; /* <---- A data member has been added here...  */
                int member1;
                char inserted2; /* <---- ... and another one has been added here.  */
              };

              int
              foo(struct S* s)
              {
                return s->member0 + s->member1;
              }

           In libtest3-v1.so, adding char data members S::inserted1 and
           S::inserted2 can be considered harmless (from an ABI compatibility
           perspective), at least on the x86 platform, because that doesn't
           change the offsets of the data members S::member0 and S::member1.
           But then running abidiff on these two versions of library yields:

              $ abidiff libtest3-v0.so libtest3-v1.so
              Functions changes summary: 0 Removed, 1 Changed, 0 Added function
              Variables changes summary: 0 Removed, 0 Changed, 0 Added variable

              1 function with some indirect sub-type change:

                [C]'function int foo(S*)' has some indirect sub-type changes:
                  parameter 0 of type 'S*' has sub-type changes:
                    in pointed to type 'struct S':
                      type size changed from 64 to 96 bits
                      2 data member insertions:
                        'char S::inserted1', at offset 8 (in bits)
                        'char S::inserted2', at offset 64 (in bits)
              $

           That is, abidiff shows us the two changes, even though we (the
           developers of that very involved library) know that these changes
           are harmless in this particular context.

           Luckily, we can devise a suppression specification that
           essentially tells abidiff to filter out change reports about
           adding a data member between S::member0 and S::member1, and adding
           a data member at the end of struct S.  We have written such a
           suppression specification in a file called test3-1.suppr and it
           unsurprisingly looks like:

              [suppress_type]
                name = S
                has_data_member_inserted_between = {offset_after(member0), offset_of(member1)}
                has_data_member_inserted_at = end

           Now running abidiff with this suppression specification yields:

              $ ../build/tools/abidiff --suppressions test3-1.suppr libtest3-v0.so libtest3-v1.so
              Functions changes summary: 0 Removed, 0 Changed (1 filtered out), 0 Added function
              Variables changes summary: 0 Removed, 0 Changed, 0 Added variable

              $

           Hooora! \o/ (I guess)

           Suppressing change reports about types accessed either directly or
           through pointers

           Suppose we have a first version of an object file which source
           code is the file widget-v0.cc below:

              // Compile with: g++ -g -c widget-v0.cc

              struct widget
              {
                int x;
                int y;

                widget()
                  :x(), y()
                {}
              };

              void
              fun0(widget*)
              {
                // .. do stuff here.
              }

              void
              fun1(widget&)
              {
                // .. do stuff here ..
              }

              void
              fun2(widget w)
              {
                // ... do other stuff here ...
              }

           Now suppose in the second version of that file, named
           widget-v1.cc, we have added some data members at the end of the
           type struct widget; here is what the content of that file would
           look like:

              // Compile with: g++ -g -c widget-v1.cc

              struct widget
              {
                int x;
                int y;
                int w; // We have added these two new data members here ..
                int h; // ... and here.

                widget()
                  : x(), y(), w(), h()
                {}
              };

              void
              fun0(widget*)
              {
                // .. do stuff here.
              }

              void
              fun1(widget&)
              {
                // .. do stuff here ..
              }

              void
              fun2(widget w)
              {
                // ... do other stuff here ...
              }

           When we invoke abidiff on the object files resulting from the
           compilation of the two file above, here is what we get:

               $ abidiff widget-v0.o widget-v1.o
               Functions changes summary: 0 Removed, 2 Changed (1 filtered out), 0 Added functions
               Variables changes summary: 0 Removed, 0 Changed, 0 Added variable

               2 functions with some indirect sub-type change:

                 [C]'function void fun0(widget*)' has some indirect sub-type changes:
                   parameter 1 of type 'widget*' has sub-type changes:
                     in pointed to type 'struct widget':
                       type size changed from 64 to 128 bits
                       2 data member insertions:
                         'int widget::w', at offset 64 (in bits)
                         'int widget::h', at offset 96 (in bits)

                 [C]'function void fun2(widget)' has some indirect sub-type changes:
                   parameter 1 of type 'struct widget' has sub-type changes:
                     details were reported earlier
              $

           I guess a little bit of explaining is due here.  abidiff detects
           that two data member got added at the end of struct widget.  it
           also tells us that the type change impacts the exported function
           fun0() which uses the type struct widget through a pointer, in its
           signature.

           Careful readers will notice that the change to struct widget also
           impacts the exported function fun1(), that uses type struct widget
           through a reference.  But then abidiff doesn't tell us about the
           impact on that function fun1() because it has evaluated that
           change as being redundant with the change it reported on fun0().
           It has thus filtered it out, to avoid cluttering the output with
           noise.

           Redundancy detection and filtering is fine and helpful to avoid
           burying the important information in a sea of noise.  However, it
           must be treated with care, by fear of mistakenly filtering out
           relevant and important information.

           That is why abidiff tells us about the impact that the change to
           struct widget has on function fun2().  In this case, that function
           uses the type struct widget directly (in its signature).  It does
           not use it via a pointer or a reference.  In this case, the direct
           use of this type causes fun2() to be exposed to a potentially
           harmful ABI change.  Hence, the report about fun2() is not
           filtered out, even though it's about that same change on struct
           widget.

           To go further in suppressing reports about changes that are
           harmless and keeping only those that we know are harmful, we would
           like to go tell abidiff to suppress reports about this particular
           struct widget change when it impacts uses of struct widget through
           a pointer or reference.  In other words, suppress the change
           reports about fun0() and fun1().  We would then write this
           suppression specification, in file widget.suppr:

              [suppress_type]
                name = widget
                type_kind = struct
                has_data_member_inserted_at = end
                accessed_through = reference-or-pointer

                # So this suppression specification says to suppress reports about
                # the type 'struct widget', if this type was added some data member
                # at its end, and if the change impacts uses of the type through a
                # reference or a pointer.

           Invoking abidiff on widget-v0.o and widget-v1.o with this
           suppression specification yields:

              $ abidiff --suppressions widget.suppr widget-v0.o widget-v1.o
              Functions changes summary: 0 Removed, 1 Changed (2 filtered out), 0 Added function
              Variables changes summary: 0 Removed, 0 Changed, 0 Added variable

              1 function with some indirect sub-type change:

                [C]'function void fun2(widget)' has some indirect sub-type changes:
                  parameter 1 of type 'struct widget' has sub-type changes:
                    type size changed from 64 to 128 bits
                    2 data member insertions:
                      'int widget::w', at offset 64 (in bits)
                      'int widget::h', at offset 96 (in bits)
              $

           As expected, I guess.

           Suppressing change reports about functions.

           Suppose we have a first version a library named libtest2-v0.so
           whose source code is:

               $ cat -n test2-v0.cc

                1     struct S1
                2     {
                3       int m0;
                4
                5       S1()
                6         : m0()
                7       {}
                8     };
                9
               10     struct S2
               11     {
               12       int m0;
               13
               14       S2()
               15         : m0()
               16       {}
               17     };
               18
               19     struct S3
               20     {
               21       int m0;
               22
               23       S3()
               24         : m0()
               25       {}
               26     };
               27
               28     int
               29     func(S1&)
               30     {
               31       // suppose the code does something with the argument.
               32       return 0;
               33
               34     }
               35
               36     char
               37     func(S2*)
               38     {
               39       // suppose the code does something with the argument.
               40       return 0;
               41     }
               42
               43     unsigned
               44     func(S3)
               45     {
               46       // suppose the code does something with the argument.
               47       return 0;
               48     }
              $

           And then we come up with a second version libtest2-v1.so of that
           library; the source code is modified by making the structures S1,
           S2, S3 inherit another struct:

              $ cat -n test2-v1.cc
                    1 struct base_type
                    2 {
                    3   int m_inserted;
                    4 };
                    5
                    6 struct S1 : public base_type // <--- S1 now has base_type as its base
                    7                              // type.
                    8 {
                    9   int m0;
                   10
                   11   S1()
                   12     : m0()
                   13   {}
                   14 };
                   15
                   16 struct S2 : public base_type // <--- S2 now has base_type as its base
                   17                              // type.
                   18 {
                   19   int m0;
                   20
                   21   S2()
                   22     : m0()
                   23   {}
                   24 };
                   25
                   26 struct S3 : public base_type // <--- S3 now has base_type as its base
                   27                              // type.
                   28 {
                   29   int m0;
                   30
                   31   S3()
                   32     : m0()
                   33   {}
                   34 };
                   35
                   36 int
                   37 func(S1&)
                   38 {
                   39   // suppose the code does something with the argument.
                   40   return 0;
                   41
                   42 }
                   43
                   44 char
                   45 func(S2*)
                   46 {
                   47   // suppose the code does something with the argument.
                   48   return 0;
                   49 }
                   50
                   51 unsigned
                   52 func(S3)
                   53 {
                   54   // suppose the code does something with the argument.
                   55   return 0;
                   56 }
               $

           Now let's build the two libraries:

              g++ -Wall -g -shared -o libtest2-v0.so test2-v0.cc
              g++ -Wall -g -shared -o libtest2-v0.so test2-v0.cc

           Let's look at the output of abidiff:

              $ abidiff libtest2-v0.so libtest2-v1.so
              Functions changes summary: 0 Removed, 3 Changed, 0 Added functions
              Variables changes summary: 0 Removed, 0 Changed, 0 Added variable

              3 functions with some indirect sub-type change:

                [C]'function unsigned int func(S3)' has some indirect sub-type changes:
                  parameter 0 of type 'struct S3' has sub-type changes:
                    size changed from 32 to 64 bits
                    1 base class insertion:
                      struct base_type
                    1 data member change:
                     'int S3::m0' offset changed from 0 to 32

                [C]'function char func(S2*)' has some indirect sub-type changes:
                  parameter 0 of type 'S2*' has sub-type changes:
                    in pointed to type 'struct S2':
                      size changed from 32 to 64 bits
                      1 base class insertion:
                        struct base_type
                      1 data member change:
                       'int S2::m0' offset changed from 0 to 32

                [C]'function int func(S1&)' has some indirect sub-type changes:
                  parameter 0 of type 'S1&' has sub-type changes:
                    in referenced type 'struct S1':
                      size changed from 32 to 64 bits
                      1 base class insertion:
                        struct base_type
                      1 data member change:
                       'int S1::m0' offset changed from 0 to 32
              $

           Let's tell abidiff to avoid showing us the differences on the
           overloads of func that takes either a pointer or a reference.  For
           that, we author this simple suppression specification:

              $ cat -n libtest2.suppr
                   1 [suppress_function]
                   2   name = func
                   3   parameter = '0 S1&
                   4
                   5 [suppress_function]
                   6   name = func
                   7   parameter = '0 S2*
              $

           And then let's invoke abidiff with the suppression specification:

              $ ../build/tools/abidiff --suppressions libtest2.suppr libtest2-v0.so libtest2-v1.so
              Functions changes summary: 0 Removed, 1 Changed (2 filtered out), 0 Added function
              Variables changes summary: 0 Removed, 0 Changed, 0 Added variable

              1 function with some indirect sub-type change:

                     [C]'function unsigned int func(S3)' has some indirect sub-type changes:
                       parameter 0 of type 'struct S3' has sub-type changes:
                         size changed from 32 to 64 bits
                         1 base class insertion:
                           struct base_type
                         1 data member change:
                          'int S3::m0' offset changed from 0 to 32

           The suppression specification could be reduced using regular
           expressions:

              $ cat -n libtest2-1.suppr
                        1   [suppress_function]
                        2     name = func
                        3     parameter = '0 /^S.(&|\\*)/
              $

              $ ../build/tools/abidiff --suppressions libtest2-1.suppr libtest2-v0.so libtest2-v1.so
              Functions changes summary: 0 Removed, 1 Changed (2 filtered out), 0 Added function
              Variables changes summary: 0 Removed, 0 Changed, 0 Added variable

              1 function with some indirect sub-type change:

                     [C]'function unsigned int func(S3)' has some indirect sub-type changes:
                       parameter 0 of type 'struct S3' has sub-type changes:
                         size changed from 32 to 64 bits
                         1 base class insertion:
                           struct base_type
                         1 data member change:
                          'int S3::m0' offset changed from 0 to 32

              $

## [](#TOOLS)TOOLS

       Overview
           The upstream code repository of Libabigail contains several tools
           written using the library.  They are maintained and released as
           part of the project.  All tools come with a bash-completion
           script.

       Tools manuals
       abidiff
           abidiff compares the Application Binary Interfaces (ABI) of two
           shared libraries in ELF
           <http://en.wikipedia.org/wiki/Executable_and_Linkable_Format>
           format.  It emits a meaningful report describing the differences
           between the two ABIs.

           This tool can also compare the textual representations of the ABI
           of two ELF binaries (as emitted by abidw) or an ELF binary against
           a textual representation of another ELF binary.

           For a comprehensive ABI change report between two input shared
           libraries that includes changes about function and variable
           sub-types, abidiff uses by default, debug information in DWARF
           <http://www.dwarfstd.org> format, if present, otherwise it
           compares interfaces using debug information in CTF
           <https://raw.githubusercontent.com/wiki/oracle/binutils-gdb/files/ctf-spec.pdf>
           or BTF <https://docs.kernel.org/bpf/btf.html> formats, if present.
           Finally, if no debug info in these formats is found, it only
           considers ELF
           <http://en.wikipedia.org/wiki/Executable_and_Linkable_Format>
           symbols and report about their addition or removal.

           This tool uses the libabigail library to analyze the binary as
           well as its associated debug information.  Here is its general
           mode of operation.

           When instructed to do so, a binary and its associated debug
           information is read and analyzed.  To that effect, libabigail
           analyzes by default the descriptions of the types reachable by the
           interfaces (functions and variables) that are visible outside of
           their translation unit.  Once that analysis is done, an
           Application Binary Interface Corpus is constructed by only
           considering the subset of types reachable from interfaces
           associated to ELF
           <http://en.wikipedia.org/wiki/Executable_and_Linkable_Format>
           symbols that are defined and exported by the binary.  It's that
           final ABI corpus which libabigail considers as representing the
           ABI of the analyzed binary.

           Libabigail then has capabilities to generate textual
           representations of ABI Corpora, compare them, analyze their
           changes and report about them.

       Invocation
              abidiff [options] <first-shared-library> <second-shared-library>

       Environment
           abidiff loads two default suppression specifications files <#
           suppr-spec-label>, merges their content and use it to filter out
           ABI change reports that might be considered as false positives to
           users.

           • Default system-wide suppression specification file

             It's located by the optional environment variable
             LIBABIGAIL_DEFAULT_SYSTEM_SUPPRESSION_FILE.  If that environment
             variable is not set, then abidiff tries to load the suppression
             file $libdir/libabigail/libabigail-default.abignore.  If that
             file is not present, then no default system-wide suppression
             specification file is loaded.

           • Default user suppression specification file.

             It's located by the optional environment
             LIBABIGAIL_DEFAULT_USER_SUPPRESSION_FILE.  If that environment
             variable is not set, then abidiff tries to load the suppression
             file $HOME/.abignore.  If that file is not present, then no
             default user suppression specification is loaded.

       Options
              • --add-binaries1 <bin1,bin2,bin3,..>

                For each of the comma-separated binaries given in argument to
                this option, if the binary is found in the directory
                specified by the --added-binaries-dir1 option, then abidiff
                loads the ABI corpus of the binary and adds it to a set of
                corpora (called an ABI Corpus Group) that includes the first
                argument of abidiff.

                That ABI corpus group is then compared against the second
                corpus group given in argument to abidiff.

              • --add-binaries2 <bin1,bin2,bin3,..>

                For each of the comma-separated binaries given in argument to
                this option, if the binary is found in the directory
                specified by the --added-binaries-dir2 option, then abidiff
                loads the ABI corpus of the binary and adds it to a set of
                corpora(called an ABI Corpus Group) that includes the second
                argument of abidiff.

                That ABI corpus group is then compared against the first
                corpus group given in argument to abidiff.

              • --added-binaries-dir1 | --abd1 <added-binaries-directory-1>

                This option is to be used in conjunction with the
                --add-binaries1, --follow-dependencies and
                --list-dependencies options.  Binaries referred to by these
                options, if found in the directory
                added-binaries-directory-1, are loaded as ABI corpus and are
                added to the first ABI corpus group that is to be used in the
                comparison.

              • --added-binaries-dir2 | --abd2 <added-binaries-directory-2>

                This option is to be used in conjunction with the
                --add-binaries2, --follow-dependencies and
                --list-dependencies options.  Binaries referred to by these
                options, if found in the directory
                added-binaries-directory-2, are loaded as ABI corpus and are
                added to the second ABI corpus group to be used in the
                comparison.

              • --added-fns

                In the resulting report about the differences between
                first-shared-library and second-shared-library, only display
                the globally defined functions that were added to
                second-shared-library.

              • --added-vars

                In the resulting report about the differences between
                first-shared-library and second-shared-library, only display
                the global variables that were added (defined) to
                second-shared-library.

              • --allow-non-exported-interfaces

                When looking at the debug information accompanying a binary,
                this tool analyzes the descriptions of the types reachable by
                the interfaces (functions and variables) that are visible
                outside of their translation unit.  Once that analysis is
                done, an ABI corpus is constructed by only considering the
                subset of types reachable from interfaces associated to ELF
                <http://en.wikipedia.org/wiki/Executable_and_Linkable_Format>
                symbols that are defined and exported by the binary.  It's
                those final ABI Corpora that are compared by this tool.

                The problem with that approach however is that analyzing all
                the interfaces that are visible from outside their
                translation unit can amount to a lot of data, especially when
                those binaries are applications, as opposed to shared
                libraries.  One example of such applications is the Linux
                Kernel <https://kernel.org/>.  Analyzing massive ABI Corpora
                like these can be extremely slow.

                In the presence of an "average sized" binary however one can
                afford having libabigail analyze all interfaces that are
                visible outside of their translation unit, using this option.

                Note that this option is turned on by default, unless we are
                in the presence of the Linux Kernel <https://kernel.org/>.

              • --btf

                When comparing binaries, extract ABI information from BTF
                <https://docs.kernel.org/bpf/btf.html> debug information, if
                present.

              • --changed-fns

                In the resulting report about the differences between
                first-shared-library and second-shared-library, only display
                the changes in sub-types of the global functions defined in
                first-shared-library.

              • --changed-vars

                In the resulting report about the differences between
                first-shared-library and second-shared-library, only display
                the changes in the sub-types of the global variables defined
                in first-shared-library

              • --ctf

                When comparing binaries, extract ABI information from CTF
                <https://raw.githubusercontent.com/wiki/oracle/binutils-gdb/files/ctf-spec.pdf>
                debug information, if present.

              • --debug-info-dir1 | --d1 <di-path1>

                For cases where the debug information for
                first-shared-library is split out into a separate file, tells
                abidiff where to find that separate debug information file.

                Note that di-path must point to the root directory under
                which the debug information is arranged in a tree-like
                manner.  Under Red Hat based systems, that directory is
                usually <root>/usr/lib/debug.

                This option can be provided several times with different root
                directories.  In that case, abidiff will potentially look
                into all those root directories to find the split debug info
                for first-shared-library.

                Note also that this option is not mandatory for split debug
                information installed by your system's package manager
                because then abidiff knows where to find it.

              • --debug-info-dir2 | --d2 <di-path2>

                Like --debug-info-dir1, this options tells abidiff where to
                find the split debug information for the
                second-shared-library file.

                This option can be provided several times with different root
                directories.  In that case, abidiff will potentially look
                into all those root directories to find the split debug info
                for second-shared-library.

              • --debug-self-comparison

                In this mode, error messages are emitted for types which fail
                type canonicalization, in some circumstances, when comparing
                a binary against itself.

                When comparing a binary against itself, canonical types of
                the second binary should be equal (as much as possible) to
                canonical types of the first binary.  When some discrepancies
                are detected in this mode, an abort signal is emitted and
                execution is halted.  This option should be used while
                executing the tool in a debugger, for troubleshooting
                purposes.

                This is an optional debugging and sanity check option.  To
                enable it the libabigail package needs to be configured with
                the --enable-debug-self-comparison configure option.

              • --debug-tc

                In this mode, the process of type canonicalization is put
                under heavy scrutiny.  Basically, during type
                canonicalization, each type comparison is performed twice:
                once in a structural mode (comparing every sub-type
                member-wise), and once using canonical comparison.  The two
                comparisons should yield the same result.  Otherwise, an
                abort signal is emitted and the process can be debugged to
                understand why the two kinds of comparison yield different
                results.

                This is an optional debugging and sanity check option.  To
                enable it the libabigail package needs to be configured with
                the --enable-debug-type-canonicalization configure option.

              • --deleted-fns

                In the resulting report about the differences between
                first-shared-library and second-shared-library, only display
                the globally defined functions that got deleted from
                first-shared-library.

              • --deleted-vars

                In the resulting report about the differences between
                first-shared-library and second-shared-library, only display
                the globally defined variables that were deleted from
                first-shared-library.

              • --drop <regex>

                When reading the first-shared-library and
                second-shared-library ELF input files, drop the globally
                defined functions and variables which name match the regular
                expression regex.  As a result, no change involving these
                functions or variables will be emitted in the diff report.

              • --drop-fn <regex>

                When reading the first-shared-library and
                second-shared-library ELF input files, drop the globally
                defined functions which name match the regular expression
                regex.  As a result, no change involving these functions will
                be emitted in the diff report.

              • --drop-var <regex>

                When reading the first-shared-library and
                second-shared-library ELF input files, drop the globally
                defined variables matching a the regular expression regex.

              • --drop-private-types

                This option is to be used with the --headers-dir1,
                header-file1, header-file2 and --headers-dir2 options.  With
                this option, types that are NOT defined in the headers are
                entirely dropped from the internal representation build by
                Libabigail to represent the ABI.  They thus don't have to be
                filtered out from the final ABI change report because they
                are not even present in Libabigail's representation.

                Without this option however, those private types are kept in
                the internal representation and later filtered out from the
                report.

                This options thus potentially makes Libabigail consume less
                memory.  It's meant to be mainly used to optimize the memory
                consumption of the tool on binaries with a lot of publicly
                defined and exported types.

              • --dump-diff-tree
                  After the diff report, emit a textual representation of the
                  diff nodes tree used by the comparison engine to represent
                  the changed functions and variables.  That representation
                  is emitted to the error output for debugging purposes.
                  Note that this diff tree is relevant only to functions and
                  variables that have some sub-type changes.  Added or
                  removed functions and variables do not have any diff nodes
                  tree associated to them.

              • --exported-interfaces-only

                By default, when looking at the debug information
                accompanying a binary, this tool analyzes the descriptions of
                the types reachable by the interfaces (functions and
                variables) that are visible outside of their translation
                unit.  Once that analysis is done, an ABI corpus is
                constructed by only considering the subset of types reachable
                from interfaces associated to ELF
                <http://en.wikipedia.org/wiki/Executable_and_Linkable_Format>
                symbols that are defined and exported by the binary.  It's
                those final ABI Corpora that are compared by this tool.

                The problem with that approach however is that analyzing all
                the interfaces that are visible from outside their
                translation unit can amount to a lot of data, especially when
                those binaries are applications, as opposed to shared
                libraries.  One example of such applications is the Linux
                Kernel <https://kernel.org/>.  Analyzing massive ABI corpora
                like these can be extremely slow.

                To mitigate that performance issue, this option allows
                libabigail to only analyze types that are reachable from
                interfaces associated with defined and exported ELF
                <http://en.wikipedia.org/wiki/Executable_and_Linkable_Format>
                symbols.

                Note that this option is turned on by default when analyzing
                the Linux Kernel <https://kernel.org/>.  Otherwise, it's
                turned off by default.

              • --fail-no-debug-info

                If no debug info was found, then this option makes the
                program to fail.  Otherwise, without this option, the program
                will attempt to compare properties of the binaries that are
                not related to debug info, like pure ELF properties.

              • --follow-dependencies | --fdeps

                For each dependency of the first argument of abidiff, if it's
                found in the directory specified by the --added-binaries-dir1
                option, then construct an ABI corpus out of the dependency,
                add it to a set of corpora (called an ABI Corpus Group) that
                includes the first argument of abidiff.

                Similarly, for each dependency of the second argument of
                abidiff, if it's found in the directory specified by the
                --added-binaries-dir2 option, then construct an ABI corpus
                out of the dependency, add it to an ABI corpus group that
                includes the second argument of abidiff.

                These two ABI corpus groups are then compared against each
                other.

                Said otherwise, this makes abidiff compare the set of its
                first input and its dependencies against the set of its
                second input and its dependencies.

              • --harmless

                In the diff report, display only the harmless <#
                harmlesschangeconcept-label> changes.  By default, the
                harmless changes are filtered out of the diff report keep the
                clutter to a minimum and have a greater chance to spot real
                ABI issues.

              • --headers-dir1 | --hd1 <headers-directory-path-1>

                Specifies where to find the public headers of the first
                shared library (or binary in general) that the tool has to
                consider.  The tool will thus filter out ABI changes on types
                that are not defined in public headers.

                Note that several public header directories can be specified
                for the first shared library.  In that case the
                --headers-dir1 option should be present several times on the
                command line, like in the following example:

                    $ abidiff --headers-dir1 /some/path       \
                              --headers-dir1 /some/other/path \
                              binary-version-1 binary-version-2

              • --headers-dir2 | --hd2 <headers-directory-path-2>

                Specifies where to find the public headers of the second
                shared library that the tool has to consider.  The tool will
                thus filter out ABI changes on types that are not defined in
                public headers.

                Note that several public header directories can be specified
                for the second shared library.  In that case the
                --headers-dir2 option should be present several times like in
                the following example:

                    $ abidiff --headers-dir2 /some/path       \
                              --headers-dir2 /some/other/path \
                              binary-version-1 binary-version-2

              • --header-file1 | --hf1 <header-file-path-1>

                Specifies where to find one public header of the first shared
                library that the tool has to consider.  The tool will thus
                filter out ABI changes on types that are not defined in
                public headers.

              • --header-file2 | --hf2 <header-file-path-2>

                Specifies where to find one public header of the second
                shared library that the tool has to consider.  The tool will
                thus filter out ABI changes on types that are not defined in
                public headers.

              • --help | -h

                Display a short help about the command and exit.

              • --ignore-soname

                Ignore differences in the SONAME when doing a comparison

              • --impacted-interfaces

                When showing leaf changes, this option instructs abidiff to
                show the list of impacted interfaces.  This option is thus to
                be used in addition the --leaf-changes-only option,
                otherwise, it's ignored.

              • --keep <regex>

                When reading the first-shared-library and
                second-shared-library ELF input files, keep the globally
                defined functions and variables which names match the regular
                expression regex.  All other functions and variables are
                dropped on the floor and will thus not appear in the
                resulting diff report.

              • --keep-fn <regex>

                When reading the first-shared-library and
                second-shared-library ELF input files, keep the globally
                defined functions which name match the regular expression
                regex.  All other functions are dropped on the floor and will
                thus not appear in the resulting diff report.

              • --keep-var <regex>

                When reading the first-shared-library and
                second-shared-library ELF input files, keep the globally
                defined which names match the regular expression regex.  All
                other variables are dropped on the floor and will thus not
                appear in the resulting diff report.

              • --kmi-whitelist | -w <path-to-whitelist>

                When analyzing a Linux kernel binary, this option points to
                the white list of names of ELF symbols of functions and
                variables which ABI must be considered.  That white list is
                called a "Kernel Module Interface white list".  This is
                because for the Kernel, we don't talk about ABI; we rather
                talk about the interface between the Kernel and its module.
                Hence the term KMI rather than ABI.

                Any other function or variable which ELF symbol are not
                present in that white list will not be considered by this
                tool.

                If this option is not provided -- thus if no white list is
                provided -- then the entire KMI, that is, the set of all
                publicly defined and exported functions and global variables
                by the Linux Kernel binaries, is considered.

              • --leaf-changes-only|-l only show leaf changes, so don't show
                impact analysis report.  This option implies --redundant.

                The typical output of abidiff when comparing two binaries
                looks like this

                    $ abidiff libtest-v0.so libtest-v1.so
                    Functions changes summary: 0 Removed, 1 Changed, 0 Added function
                    Variables changes summary: 0 Removed, 0 Changed, 0 Added variable

                    1 function with some indirect sub-type change:

                      [C]'function void fn(C&)' at test-v1.cc:13:1 has some indirect sub-type changes:
                        parameter 1 of type 'C&' has sub-type changes:
                          in referenced type 'struct C' at test-v1.cc:7:1:
                            type size hasn't changed
                            1 data member change:
                             type of 'leaf* C::m0' changed:
                               in pointed to type 'struct leaf' at test-v1.cc:1:1:
                                 type size changed from 32 to 64 bits
                                 1 data member insertion:
                                   'char leaf::m1', at offset 32 (in bits) at test-v1.cc:4:1

                    $

                So in that example the report emits information about how the
                data member insertion change of "struct leaf" is reachable
                from function "void fn(C&)".  In other words, the report not
                only shows the data member change on "struct leaf", but it
                also shows the impact of that change on the function "void
                fn(C&)".

                In abidiff parlance, the change on "struct leaf" is called a
                leaf change.  So the --leaf-changes-only
                --impacted-interfaces options show, well, only the leaf
                change.  And it goes like this:

                    $ abidiff -l libtest-v0.so libtest-v1.so
                    'struct leaf' changed:
                      type size changed from 32 to 64 bits
                      1 data member insertion:
                        'char leaf::m1', at offset 32 (in bits) at test-v1.cc:4:1

                      one impacted interface:
                        function void fn(C&)
                    $

                Note how the report ends by showing the list of interfaces
                impacted by the leaf change.

                Now if you don't want to see that list of impacted
                interfaces, then you can just avoid using the
                --impacted-interface option.  You can learn about that option
                below, in any case.

              • --list-dependencies | --ldeps

                This option lists all the dependencies of the input arguments
                of abidiff that are found in the directories specified by the
                options --added-binaries-dir1 and --added-binaries-dir2

              • --no-added-syms

                In the resulting report about the differences between
                first-shared-library and second-shared-library, do not
                display added functions or variables.  Do not display added
                functions or variables ELF symbols either.  All other kinds
                of changes are displayed unless they are explicitely
                forbidden by other options on the command line.

              • --no-assume-odr-for-cplusplus

                When analyzing a binary originating from C++ code using DWARF
                <http://www.dwarfstd.org> debug information, libabigail
                assumes the One Definition Rule
                <https://en.wikipedia.org/wiki/One_Definition_Rule> to
                speed-up the analysis.  In that case, when several types have
                the same name in the binary, they are assumed to all be
                equal.

                This option disables that assumption and instructs libabigail
                to actually actually compare the types to determine if they
                are equal.

              • --no-architecture

                Do not take architecture in account when comparing ABIs.

              • --no-change-categorization | -x

                This option disables the categorization of changes into
                harmless and harmful changes.  Note that this categorization
                is a pre-requisite for the filtering of changes so this
                option disables that filtering.  The goal of this option is
                to speed-up the execution of the program for cases where the
                graph of changes is huge and where the user is just
                interested in looking at, for instance, leaf node changes
                without caring about their possible impact on interfaces.  In
                that case, this option would be used along with the
                --leaf-changes-only one.

              • --no-corpus-path

                Do not emit the path attribute for the ABI corpus.

              • --no-default-suppression

                Do not load the default suppression specification files.

              • --no-harmful

                In the diff report, do not display the harmful <#
                harmfulchangeconcept-label> changes.  By default, only the
                harmful changes are displayed in diff report.

              • --no-leverage-dwarf-factorization

                When analyzing a binary which DWARF <http://www.dwarfstd.org>
                debug information was processed with the DWZ
                <https://sourceware.org/dwz> tool, the type information is
                supposed to be already factorized.  That context is used by
                libabigail to perform some speed optimizations.

                This option disables those optimizations.

              • --no-linkage-name

                In the resulting report, do not display the linkage names of
                the added, removed, or changed functions or variables.

              • --no-linux-kernel-mode

                Without this option, if abidiff detects that the binaries it
                is looking at are Linux Kernel binaries (either vmlinux or
                modules) then it only considers functions and variables which
                ELF symbols are listed in the __ksymtab and __ksymtab_gpl
                sections.

                With this option, abidiff considers the binary as a
                non-special ELF binary.  It thus considers functions and
                variables which are defined and exported in the ELF sense.

              • --no-redundant

                In the diff report, do NOT display redundant changes.  A
                redundant change is a change that has been displayed
                elsewhere in the report.  This option is switched on by
                default.

              • --no-show-locs
                  Do not show information about where in the second shared
                  library the respective type was changed.

              • --no-show-relative-offset-changes

                Without this option, when the offset of a data member
                changes, the change report not only mentions the older and
                newer offset, but it also mentions by how many bits the data
                member changes.  With this option, the latter is not shown.

              • --no-unreferenced-symbols

                In the resulting report, do not display change information
                about function and variable symbols that are not referenced
                by any debug information.  Note that for these symbols not
                referenced by any debug information, the change information
                displayed is either added or removed symbols.

              • --non-reachable-types|-t

                Analyze and emit change reports for all the types of the
                binary, including those that are not reachable from global
                functions and variables.

                This option might incur some serious performance degradation
                as the number of types analyzed can be huge.  However, if
                paired with the --headers-dir{1,2} and/or header-file{1,2}
                options, the additional non-reachable types analyzed are
                restricted to those defined in public headers files, thus
                hopefully making the performance hit acceptable.

                Also, using this option alongside suppression specifications
                (by also using the --suppressions option) might help keep the
                number of analyzed types (and the potential performance
                degradation) in control.

                Note that without this option, only types that are reachable
                from global functions and variables are analyzed, so the tool
                detects and reports changes on these reachable types only.

              • --redundant

                In the diff report, do display redundant changes.  A
                redundant change is a change that has been displayed
                elsewhere in the report.

              • --show-bits

                Show sizes and offsets in bits, not bytes.  This option is
                activated by default.

              • --show-bytes

                Show sizes and offsets in bytes, not bits.  By default, sizes
                and offsets are shown in bits.

              • --show-dec

                Show sizes and offsets in decimal base.  This option is
                activated by default.

              • --show-hex

                Show sizes and offsets in hexadecimal base.

              • --stat

                Rather than displaying the detailed ABI differences between
                first-shared-library and second-shared-library, just display
                some summary statistics about these differences.

              • --stats

                Emit statistics about various internal things.

              • --suppressions | --suppr <path-to-suppressions>

                Use a suppression specification <#suppr-spec-label> file
                located at path-to-suppressions.  Note that this option can
                appear multiple times on the command line.  In that case, all
                of the provided suppression specification files are taken
                into account.

                Please note that, by default, if this option is not provided,
                then the default suppression specification files are loaded .

              • --symtabs

                Only display the symbol tables of the first-shared-library
                and second-shared-library.

              • --verbose

                Emit verbose logs about the progress of miscellaneous
                internal things.

              • --version | -v

                Display the version of the program and exit.

       Return values
           The exit code of the abidiff command is either 0 if the ABI of the
           binaries being compared are equal, or non-zero if they differ or
           if the tool encountered an error.

           In the later case, the exit code is a 8-bits-wide bit field in
           which each bit has a specific meaning.

           The first bit, of value 1, named ABIDIFF_ERROR means there was an
           error.

           The second bit, of value 2, named ABIDIFF_USAGE_ERROR means there
           was an error in the way the user invoked the tool.  It might be
           set, for instance, if the user invoked the tool with an unknown
           command line switch, with a wrong number or argument, etc.  If
           this bit is set, then the ABIDIFF_ERROR bit must be set as well.

           The third bit, of value 4, named ABIDIFF_ABI_CHANGE means the ABI
           of the binaries being compared are different.

           The fourth bit, of value 8, named ABIDIFF_ABI_INCOMPATIBLE_CHANGE
           means the ABI of the binaries compared are different in an
           incompatible way.  If this bit is set, then the ABIDIFF_ABI_CHANGE
           bit must be set as well.  If the ABIDIFF_ABI_CHANGE is set and the
           ABIDIFF_INCOMPATIBLE_CHANGE is NOT set, then it means that the
           ABIs being compared might or might not be compatible.  In that
           case, a human being needs to review the ABI changes to decide if
           they are compatible or not.

           Note that, at the moment, there are only a few kinds of ABI
           changes that would result in setting the flag
           ABIDIFF_ABI_INCOMPATIBLE_CHANGE.  Those ABI changes are either:

              • the removal of the symbol of a function or variable that has
                been defined and exported.

              • the modification of the index of a member of a virtual
                function table (for C++ programs and libraries).

           With time, when more ABI change patterns are found to always
           constitute incompatible ABI changes, we will adapt the code to
           recognize those cases and set the ABIDIFF_ABI_INCOMPATIBLE_CHANGE
           accordingly.  So, if you find such patterns, please let us know.

           The remaining bits are not used for the moment.

       Usage examples
              1. Detecting an ABI change in a sub-type of a function:

                     $ cat -n test-v0.cc
                              1      // Compile this with:
                              2      //   g++ -g -Wall -shared -o libtest-v0.so test-v0.cc
                              3
                              4      struct S0
                              5      {
                              6        int m0;
                              7      };
                              8
                              9      void
                             10      foo(S0* /*parameter_name*/)
                             11      {
                             12        // do something with parameter_name.
                             13      }
                     $
                     $ cat -n test-v1.cc
                              1      // Compile this with:
                              2      //   g++ -g -Wall -shared -o libtest-v1.so test-v1.cc
                              3
                              4      struct type_base
                              5      {
                              6        int inserted;
                              7      };
                              8
                              9      struct S0 : public type_base
                             10      {
                             11        int m0;
                             12      };
                             13
                             14      void
                             15      foo(S0* /*parameter_name*/)
                             16      {
                             17        // do something with parameter_name.
                             18      }
                     $
                     $ g++ -g -Wall -shared -o libtest-v0.so test-v0.cc
                     $ g++ -g -Wall -shared -o libtest-v1.so test-v1.cc
                     $
                     $ abidiff libtest-v0.so libtest-v1.so; echo "exit code: $?"
                     Functions changes summary: 0 Removed, 1 Changed, 0 Added function
                     Variables changes summary: 0 Removed, 0 Changed, 0 Added variable

                     1 function with some indirect sub-type change:

                       [C]'function void foo(S0*)' has some indirect sub-type changes:
                             parameter 0 of type 'S0*' has sub-type changes:
                               in pointed to type 'struct S0':
                                 size changed from 32 to 64 bits
                                 1 base class insertion:
                                   struct type_base
                                 1 data member change:
                                  'int S0::m0' offset changed from 0 to 32
                     exit code: 4
                     $

           Note how the exit code is 4, meaning the third bit
           ABIDIFF_ABI_CHANGE of value 4 is set to 1.  This means the tool
           categorizes the ABI change as harmful <#
           harmfulchangeconcept-label> and thus requires a user review.

              2. Detecting an incompatible ABI change in the type of a
                 function:

                     $ cat -n test-v0.cc
                          1  // Compile this with:
                          2  //   g++ -g -Wall -shared -o libtest-v0.so test-v0.cc
                          3
                          4  struct S0
                          5  {
                          6    int m0;
                          7  };
                          8
                          9  S0
                         10  foo()
                         11  {
                         12    S0 s = {};
                         13    return s;
                         14  }
                     $
                     $ cat -n test-v1.cc
                          1  // Compile this with:
                          2  //   g++ -g -Wall -shared -o libtest-v1.so test-v1.cc
                          3
                          4  struct type_base
                          5  {
                          6    int inserted;
                          7  };
                          8
                          9  struct S0 : public type_base
                         10  {
                         11    int m0;
                         12  };
                         13
                         14  S0
                         15  foo()
                         16  {
                         17    S0 s = {};
                         18    return s;
                         19  }
                     $
                     $ g++ -g -Wall -shared -o libtest-v0.so test-v0.cc
                     $ g++ -g -Wall -shared -o libtest-v1.so test-v1.cc
                     $
                     $ abidiff libtest-v0.so libtest-v1.so; echo "exit code: $?"
                     Functions changes summary: 0 Removed, 1 Changed, 0 Added function
                     Variables changes summary: 0 Removed, 0 Changed, 0 Added variable

                     1 function with incompatible sub-type changes:

                       [C] 'function S0 foo(void)' at test-v0.cc:10:1 has some sub-type changes:
                         return type changed:
                           type size changed from 32 to 64 (in bits)
                           1 base class insertion:
                             struct type_base at test-v1.cc:4:1
                           1 data member change:
                             'int m0' offset changed from 0 to 32 (in bits) (by +32 bits)

                     exit code: 12
                     $

           Note how the exit code is 12, meaning both the third bit
           ABIDIFF_ABI_CHANGE of value 4 and the fourth bit
           ABIDIFF_ABI_INCOMPATIBLE_CHANGE of value 8 are set to 1.  This
           means the tool categorizes the ABI change as incompatible <#
           incompatiblechangeconcept-label>.  It's an ABI break.

              3. Detecting another change in a sub-type of a function:

                     $ cat -n test-v0.cc
                              1      // Compile this with:
                              2      //   g++ -g -Wall -shared -o libtest-v0.so test-v0.cc
                              3
                              4      struct S0
                              5      {
                              6        int m0;
                              7      };
                              8
                              9      void
                             10      foo(S0& /*parameter_name*/)
                             11      {
                             12        // do something with parameter_name.
                             13      }
                     $
                     $ cat -n test-v1.cc
                              1      // Compile this with:
                              2      //   g++ -g -Wall -shared -o libtest-v1.so test-v1.cc
                              3
                              4      struct S0
                              5      {
                              6        char inserted_member;
                              7        int m0;
                              8      };
                              9
                             10      void
                             11      foo(S0& /*parameter_name*/)
                             12      {
                             13        // do something with parameter_name.
                             14      }
                     $
                     $ g++ -g -Wall -shared -o libtest-v0.so test-v0.cc
                     $ g++ -g -Wall -shared -o libtest-v1.so test-v1.cc
                     $
                     $ abidiff libtest-v0.so libtest-v1.so; echo "exit code: $?"
                     Functions changes summary: 0 Removed, 1 Changed, 0 Added function
                     Variables changes summary: 0 Removed, 0 Changed, 0 Added variable

                     1 function with some indirect sub-type change:

                       [C]'function void foo(S0&)' has some indirect sub-type changes:
                             parameter 0 of type 'S0&' has sub-type changes:
                               in referenced type 'struct S0':
                                 size changed from 32 to 64 bits
                                 1 data member insertion:
                                   'char S0::inserted_member', at offset 0 (in bits)
                                 1 data member change:
                                  'int S0::m0' offset changed from 0 to 32

                     exit code: 4
                     $

              4. Detecting that functions got removed or added to a library:

                     $ cat -n test-v0.cc
                              1      // Compile this with:
                              2      //   g++ -g -Wall -shared -o libtest-v0.so test-v0.cc
                              3
                              4      struct S0
                              5      {
                              6        int m0;
                              7      };
                              8
                              9      void
                             10      foo(S0& /*parameter_name*/)
                             11      {
                             12        // do something with parameter_name.
                             13      }
                     $
                     $ cat -n test-v1.cc
                              1      // Compile this with:
                              2      //   g++ -g -Wall -shared -o libtest-v1.so test-v1.cc
                              3
                              4      struct S0
                              5      {
                              6        char inserted_member;
                              7        int m0;
                              8      };
                              9
                             10      void
                             11      bar(S0& /*parameter_name*/)
                             12      {
                             13        // do something with parameter_name.
                             14      }
                     $
                     $ g++ -g -Wall -shared -o libtest-v0.so test-v0.cc
                     $ g++ -g -Wall -shared -o libtest-v1.so test-v1.cc
                     $
                     $ abidiff libtest-v0.so libtest-v1.so; echo "exit code: $?"
                     Functions changes summary: 1 Removed, 0 Changed, 1 Added functions
                     Variables changes summary: 0 Removed, 0 Changed, 0 Added variable

                     1 Removed function:
                       'function void foo(S0&)'    {_Z3fooR2S0}

                     1 Added function:
                       'function void bar(S0&)'    {_Z3barR2S0}

                     exit code: 12
                     $

              5. Comparing two sets of binaries that are passed on the
                 command line:

                     $ abidiff --add-binaries1=file2-v1              \
                               --add-binaries2=file2-v2,file2-v1     \
                               --added-binaries-dir1 dir1            \
                               --added-binaries-dir2 dir2            \
                               file1-v1 file1-v2

                 Note that the files file2-v1, and file2-v2 are to be found
                 in dir1 and dir2 or in the current directory.

              6. Compare two libraries and their dependencies:

                     $ abidiff --follow-dependencies                      \
                               --added-binaries-dir1 /some/where          \
                               --added-binaries-dir2 /some/where/else     \
                               foo bar

                 This compares the set of binaries comprised by foo and its
                 dependencies against the set of binaries comprised by bar
                 and its dependencies.

       abipkgdiff
           abipkgdiff compares the Application Binary Interfaces (ABI) of the
           ELF <http://en.wikipedia.org/wiki/Executable_and_Linkable_Format>
           binaries contained in two sets of software packages.  The software
           package formats currently supported are Deb
           <https://en.wikipedia.org/wiki/Deb_%28file_format%29>, RPM
           <https://en.wikipedia.org/wiki/RPM_Package_Manager>, tar
           <https://en.wikipedia.org/wiki/Tar_%28computing%29> archives
           (either compressed or not) and plain directories that contain
           binaries.

           The ABI of the binaries contained in the second set of packages is
           compared against the ABI of the binaries contained in the first
           set of packages.

           For a comprehensive ABI change report that includes changes about
           function and variable sub-types, the two input package sets must
           be accompanied with their debug information packages that contain
           debug information either in DWARF <http://www.dwarfstd.org>, CTF
           <https://raw.githubusercontent.com/wiki/oracle/binutils-gdb/files/ctf-spec.pdf>
           or in BTF <https://docs.kernel.org/bpf/btf.html> formats.  Please
           note however that some packages contain binaries that embed the
           debug information directly in a section of said binaries.  In
           those cases, obviously, no separate debug information package is
           needed as the tool will find the debug information inside the
           binaries.

           By default, abipkgdiff uses debug information in DWARF
           <http://www.dwarfstd.org> format, if present, otherwise it
           compares binaries interfaces using debug information in CTF
           <https://raw.githubusercontent.com/wiki/oracle/binutils-gdb/files/ctf-spec.pdf>
           or in BTF <https://docs.kernel.org/bpf/btf.html> formats, if
           present. Finally, if no debug info in these formats is found, it
           only considers ELF
           <http://en.wikipedia.org/wiki/Executable_and_Linkable_Format>
           symbols and report about their addition or removal.

           This tool uses the libabigail library to analyze the binary as
           well as its associated debug information.  Here is its general
           mode of operation.

           When instructed to do so, a binary and its associated debug
           information is read and analyzed.  To that effect, libabigail
           analyzes by default the descriptions of the types reachable by the
           interfaces (functions and variables) that are visible outside of
           their translation unit.  Once that analysis is done, an
           Application Binary Interface Corpus is constructed by only
           considering the subset of types reachable from interfaces
           associated to ELF
           <http://en.wikipedia.org/wiki/Executable_and_Linkable_Format>
           symbols that are defined and exported by the binary.  It's that
           final ABI corpus which libabigail considers as representing the
           ABI of the analyzed binary.

           Libabigail then has capabilities to generate textual
           representations of ABI Corpora, compare them, analyze their
           changes and report about them.

       Invocation
              abipkgdiff [options] <package1> <package2>

           package1 and package2 are the packages that contain the binaries
           to be compared.

           An alternate invocation style would be:

              abipkgdiff [options] --set1 <pkg1-v1> <pkg2-v1> <pkg3-v1> \
                                   --set2 <pkg1-v2> <pkg2-v2> <pkg3-v2>

           or

              abipkgdiff [options] --set1 <pkg1-v1>,<pkg2-v1>,<pkg3-v1>
                     --set2 <pkg1-v2>,<pkg2-v2>,<pkg3-v2>

           where the ABI of binaries contained in the second set of packages
           are compared against binaries contained in the first set of
           packages.

           Packages in a set are delimited either by a white spaces or by a
           comma.

       Environment
           abipkgdiff loads two default suppression specifications files <#
           suppr-spec-label>, merges their content and use it to filter out
           ABI change reports that might be considered as false positives to
           users.

           • Default system-wide suppression specification file

             It's located by the optional environment variable
             LIBABIGAIL_DEFAULT_SYSTEM_SUPPRESSION_FILE.  If that environment
             variable is not set, then abipkgdiff tries to load the
             suppression file $libdir/libabigail/libabigail-default.abignore.
             If that file is not present, then no default system-wide
             suppression specification file is loaded.

           • Default user suppression specification file.

             It's located by the optional environment
             LIBABIGAIL_DEFAULT_USER_SUPPRESSION_FILE.  If that environment
             variable is not set, then abipkgdiff tries to load the
             suppression file $HOME/.abignore.  If that file is not present,
             then no default user suppression specification is loaded.

           In addition to those default suppression specification files,
           abipkgdiff will also look inside the packages being compared and
           if it sees a file that ends with the extension .abignore, then it
           will consider it as a suppression specification and it will
           combine it to the default suppression specification that might be
           already loaded.

           The user might as well use the --suppressions option (that is
           documented further below) to provide a suppression specification.

       Options
              • --allow-non-exported-interfaces

                When looking at the debug information accompanying a binary,
                this tool analyzes the descriptions of the types reachable by
                the interfaces (functions and variables) that are visible
                outside of their translation unit.  Once that analysis is
                done, an ABI corpus is constructed by only considering the
                subset of types reachable from interfaces associated to ELF
                <http://en.wikipedia.org/wiki/Executable_and_Linkable_Format>
                symbols that are defined and exported by the binary.  It's
                those final ABI Corpora that are compared by this tool.

                The problem with that approach however is that analyzing all
                the interfaces that are visible from outside their
                translation unit can amount to a lot of data, especially when
                those binaries are applications, as opposed to shared
                libraries.  One example of such applications is the Linux
                Kernel <https://kernel.org/>.  Analyzing massive ABI Corpora
                like these can be extremely slow.

                In the presence of an "average sized" binary however one can
                afford having libabigail analyze all interfaces that are
                visible outside of their translation unit, using this option.

                Note that this option is turned on by default, unless we are
                in the presence of the Linux Kernel <https://kernel.org/>.

              • --btf
                    This is used to compare packages with BTF
                    <https://docs.kernel.org/bpf/btf.html> debug information,
                    if present.

              • --ctf
                    This is used to compare packages with CTF
                    <https://raw.githubusercontent.com/wiki/oracle/binutils-gdb/files/ctf-spec.pdf>
                    debug information, if present.

              • --debug-info-pkg1 | --d1 <path>

                For cases where the debug information for package1 is split
                out into a separate file, tells abipkgdiff where to find that
                separate debug information package.

                Note that the debug info for package1 can have been split
                into several different debug info packages.  In that case,
                several instances of this options can be provided, along with
                those several different debug info packages.

              • --debug-info-pkg2 | --d2 <path>

                For cases where the debug information for package2 is split
                out into a separate file, tells abipkgdiff where to find that
                separate debug information package.

                Note that the debug info for package2 can have been split
                into several different debug info packages.  In that case,
                several instances of this options can be provided, along with
                those several different debug info packages.

              • --devel-pkg1 | --devel1 <path>

                Specifies where to find the Development Package
                <https://fedoraproject.org/wiki/Packaging:Guidelines?rd=Packaging/Guidelines#Devel_Packages>
                associated with the first package to be compared.  That
                Development Package
                <https://fedoraproject.org/wiki/Packaging:Guidelines?rd=Packaging/Guidelines#Devel_Packages>
                at path should at least contain header files in which public
                types exposed by the libraries (of the first package to be
                compared) are defined.  When this option is provided, the
                tool filters out reports about ABI changes to types that are
                NOT defined in these header files.

              • --devel-pkg2 | --devel2 <path>

                Specifies where to find the Development Package
                <https://fedoraproject.org/wiki/Packaging:Guidelines?rd=Packaging/Guidelines#Devel_Packages>
                associated with the second package to be compared.  That
                Development Package
                <https://fedoraproject.org/wiki/Packaging:Guidelines?rd=Packaging/Guidelines#Devel_Packages>
                at path should at least contains header files in which public
                types exposed by the libraries (of the second package to be
                compared) are defined.  When this option is provided, the
                tool filters out reports about ABI changes to types that are
                NOT defined in these header files.

              • --drop-private-types

                This option is to be used with the --devel-pkg1 and
                --devel-pkg2 options.  With this option, types that are NOT
                defined in the headers are entirely dropped from the internal
                representation build by Libabigail to represent the ABI.
                They thus don't have to be filtered out from the final ABI
                change report because they are not even present in
                Libabigail's representation.

                Without this option however, those private types are kept in
                the internal representation and later filtered out from the
                report.

                This options thus potentially makes Libabigail consume less
                memory.  It's meant to be mainly used to optimize the memory
                consumption of the tool on binaries with a lot of publicly
                defined and exported types.

              • --dso-only

                Compare ELF files that are shared libraries, only.  Do not
                compare executable files, for instance.

              • --exported-interfaces-only

                By default, when looking at the debug information
                accompanying a binary, this tool analyzes the descriptions of
                the types reachable by the interfaces (functions and
                variables) that are visible outside of their translation
                unit.  Once that analysis is done, an ABI corpus is
                constructed by only considering the subset of types reachable
                from interfaces associated to ELF
                <http://en.wikipedia.org/wiki/Executable_and_Linkable_Format>
                symbols that are defined and exported by the binary.  It's
                those final ABI Corpora that are compared by this tool.

                The problem with that approach however is that analyzing all
                the interfaces that are visible from outside their
                translation unit can amount to a lot of data, especially when
                those binaries are applications, as opposed to shared
                libraries.  One example of such applications is the Linux
                Kernel <https://kernel.org/>.  Analyzing massive ABI corpora
                like these can be extremely slow.

                To mitigate that performance issue, this option allows
                libabigail to only analyze types that are reachable from
                interfaces associated with defined and exported ELF
                <http://en.wikipedia.org/wiki/Executable_and_Linkable_Format>
                symbols.

                Note that this option is turned on by default when analyzing
                the Linux Kernel <https://kernel.org/>.  Otherwise, it's
                turned off by default.

              • --fail-no-dbg

                Make the program fail and return a non-zero exit code if
                couldn't read any of the debug information that comes from
                the debug info packages that were given on the command line.
                If no debug info package were provided on the command line
                then this option is not active.

                Note that the non-zero exit code returned by the program as a
                result of this option is the constant ABIDIFF_ERROR.  To know
                the numerical value of that constant, please refer to the
                exit code documentation <#abidiff-return-value-label>.

              • --full-impact|-f

                When comparing two Linux Kernel packages, this function
                instructs abipkgdiff to emit the so-called full impact
                report, which is the default report kind emitted by the
                abidiff tool:

                    $ abidiff libtest-v0.so libtest-v1.so
                    Functions changes summary: 0 Removed, 1 Changed, 0 Added function
                    Variables changes summary: 0 Removed, 0 Changed, 0 Added variable

                    1 function with some indirect sub-type change:

                      [C]'function void fn(C&)' at test-v1.cc:13:1 has some indirect sub-type changes:
                        parameter 1 of type 'C&' has sub-type changes:
                          in referenced type 'struct C' at test-v1.cc:7:1:
                            type size hasn't changed
                            1 data member change:
                             type of 'leaf* C::m0' changed:
                               in pointed to type 'struct leaf' at test-v1.cc:1:1:
                                 type size changed from 32 to 64 bits
                                 1 data member insertion:
                                   'char leaf::m1', at offset 32 (in bits) at test-v1.cc:4:1

                    $

              • --harmless

                In the diff report, display only the harmless <#
                harmlesschangeconcept-label> changes.  By default, the
                harmless changes are filtered out of the diff report keep the
                clutter to a minimum and have a greater chance to spot real
                ABI issues.

              • --help | -h

                Display a short help about the command and exit.

              • --ignore-soname

                If two binaries with different SONAMEs have the same name in
                the old and new packages to be compared, this option forces
                abipkgdiff to compare them regardless of their obvious SONAME
                change. This allows the analysis of the ABI changes that
                might have led developers to change the SONAME.

              • --impacted-interfaces
                  When showing leaf changes, this option instructs abipkgdiff
                  to show the list of impacted interfaces.  This option is
                  thus to be used in addition to the --leaf-changes-only
                  option, or, when comparing two Linux Kernel packages.
                  Otherwise, it's simply ignored.

              • --keep-tmp-files

                Do not erase the temporary directory files that are created
                during the execution of the tool.

              • --leaf-changes-only|-l only show leaf changes, so don't show
                impact analysis report.  This option implies --redundant

                The typical output of abipkgdiff and abidiff when comparing
                two binaries, that we shall call full impact report, looks
                like this

                    $ abidiff libtest-v0.so libtest-v1.so
                    Functions changes summary: 0 Removed, 1 Changed, 0 Added function
                    Variables changes summary: 0 Removed, 0 Changed, 0 Added variable

                    1 function with some indirect sub-type change:

                      [C]'function void fn(C&)' at test-v1.cc:13:1 has some indirect sub-type changes:
                        parameter 1 of type 'C&' has sub-type changes:
                          in referenced type 'struct C' at test-v1.cc:7:1:
                            type size hasn't changed
                            1 data member change:
                             type of 'leaf* C::m0' changed:
                               in pointed to type 'struct leaf' at test-v1.cc:1:1:
                                 type size changed from 32 to 64 bits
                                 1 data member insertion:
                                   'char leaf::m1', at offset 32 (in bits) at test-v1.cc:4:1

                    $

                So in that example the report emits information about how the
                data member insertion change of "struct leaf" is reachable
                from function "void fn(C&)".  In other words, the report not
                only shows the data member change on "struct leaf", but it
                also shows the impact of that change on the function "void
                fn(C&)".

                In abidiff (and abipkgdiff) parlance, the change on "struct
                leaf" is called a leaf change.  So the --leaf-changes-only
                --impacted-interfaces options show, well, only the leaf
                change.  And it goes like this:

                    $ abidiff -l libtest-v0.so libtest-v1.so
                    'struct leaf' changed:
                      type size changed from 32 to 64 bits
                      1 data member insertion:
                        'char leaf::m1', at offset 32 (in bits) at test-v1.cc:4:1

                      one impacted interface:
                        function void fn(C&)
                    $

                Note how the report ends up by showing the list of interfaces
                impacted by the leaf change.  That's the effect of the
                additional --impacted-interfaces option.

                Now if you don't want to see that list of impacted
                interfaces, then you can just avoid using the
                --impacted-interface option.  You can learn about that option
                below, in any case.

                Please note that when comparing two Linux Kernel packages,
                it's this leaf changes report that is emitted, by default.
                The normal so-called full impact report can be emitted with
                the option --full-impact which is documented later below.

              • --linux-kernel-abi-whitelist | -w <path-to-whitelist>

                When comparing two Linux kernel RPM packages, this option
                points to the white list of names of ELF symbols of functions
                and variables that must be compared for ABI changes.  That
                white list is called a "Linux kernel ABI white list".

                Any other function or variable which ELF symbol are not
                present in that white list will not be considered by the ABI
                comparison process.

                If this option is not provided -- thus if no white list is
                provided -- then the ABI of all publicly defined and exported
                functions and global variables by the Linux Kernel binaries
                are compared.

                Please note that if a white list package is given in
                parameter, this option handles it just fine, like if the --wp
                option was used.

              • --no-abignore

                Do not search the package for the presence of suppression
                files.

              • --no-added-binaries

                Do not show the list of binaries that got added to the second
                package.

                Please note that the presence of such added binaries is not
                considered like an ABI change by this tool; as such, it
                doesn't have any impact on the exit code of the tool.  It
                does only have an informational value.  Removed binaries are,
                however, considered as an ABI change.

              • --no-added-syms

                Do not show the list of functions, variables, or any symbol
                that was added.

              • --no-assume-odr-for-cplusplus

                When analysing a binary originating from C++ code using DWARF
                <http://www.dwarfstd.org> debug information, libabigail
                assumes the One Definition Rule
                <https://en.wikipedia.org/wiki/One_Definition_Rule> to
                speed-up the analysis.  In that case, when several types have
                the same name in the binary, they are assumed to all be
                equal.

                This option disables that assumption and instructs libabigail
                to actually actually compare the types to determine if they
                are equal.

              • --no-default-suppression

                Do not load the default suppression specification files.

              • --no-leverage-dwarf-factorization

                When analysing a binary which DWARF <http://www.dwarfstd.org>
                debug information was processed with the DWZ
                <https://sourceware.org/dwz> tool, the type information is
                supposed to be already factorized.  That context is used by
                libabigail to perform some speed optimizations.

                This option disables those optimizations.

              • --no-linkage-name

                In the resulting report, do not display the linkage names of
                the added, removed, or changed functions or variables.

              • --no-parallel

                By default, abipkgdiff will use all the processors it has
                available to execute concurrently.  This option tells it not
                to extract packages or run comparisons in parallel.

              • --non-reachable-types|-t

                Analyze and emit change reports for all the types of the
                binary, including those that are not reachable from global
                functions and variables.

                This option might incur some serious performance degradation
                as the number of types analyzed can be huge.  However, if
                paired with the --devel-pkg{1,2} options, the additional
                non-reachable types analyzed are restricted to those defined
                in the public headers files carried by the referenced
                development packages, thus hopefully making the performance
                hit acceptable.

                Also, using this option alongside suppression specifications
                (by also using the --suppressions option) might help keep the
                number of analyzed types (and the potential performance
                degradation) in control.

                Note that without this option, only types that are reachable
                from global functions and variables are analyzed, so the tool
                detects and reports changes on these reachable types only.

              • --no-show-locs
                  Do not show information about where in the second shared
                  library the respective type was changed.

              • --no-show-relative-offset-changes
                    Without this option, when the offset of a data member
                    changes, the change report not only mentions the older
                    and newer offset, but it also mentions by how many bits
                    the data member changes.  With this option, the latter is
                    not shown.

              • --no-unreferenced-symbols

                In the resulting report, do not display change information
                about function and variable symbols that are not referenced
                by any debug information.  Note that for these symbols not
                referenced by any debug information, the change information
                displayed is either added or removed symbols.

              • --show-bits

                Show sizes and offsets in bits, not bytes.  This option is
                activated by default.

              • --show-bytes

                Show sizes and offsets in bytes, not bits.  By default, sizes
                and offsets are shown in bits.

              • --show-dec

                Show sizes and offsets in decimal base.  This option is
                activated by default.

              • --show-hex

                Show sizes and offsets in hexadecimal base.

              • --show-identical-binaries
                  Show the names of the all binaries compared, including the
                  binaries whose ABI compare equal.  By default, when this
                  option is not provided, only binaries with ABI changes are
                  mentionned in the output.

              • --private-dso

                By default, abipkgdiff does not compare DSOs that are private
                to the RPM package.  A private DSO is a DSO which SONAME is
                NOT advertised in the "provides" property of the RPM.

                This option instructs abipkgdiff to also compare DSOs that
                are NOT advertised in the "provides" property of the RPM.

                Please note that the fact that (by default) abipkgdiff skips
                private DSO is a feature that is available only for RPMs, at
                the moment.  We would happily accept patches adding that
                feature for other package formats.

              • --redundant
                  In the diff reports, do display redundant changes.  A
                  redundant change is a change that has been displayed
                  elsewhere in a given report.

              • --self-check

                This is used to test the underlying Libabigail library.  When
                in used, the command expects only on input package, along
                with its associated debug info packages.  The command then
                compares each binary inside the package against its own
                ABIXML representation. The result of the comparison should
                yield the empty set if Libabigail behaves correctly.
                Otherwise, it means there is an issue that ought to be fixed.
                This option is used by people interested in Libabigail
                development for regression testing purposes.  Here is an
                example of the use of this option:

                    $ abipkgdiff --self-check --d1 mesa-libGLU-debuginfo-9.0.1-3.fc33.x86_64.rpm  mesa-libGLU-9.0.1-3.fc33.x86_64.rpm
                     ==== SELF CHECK SUCCEEDED for 'libGLU.so.1.3.1' ====
                    $

              • --set1 <package1-path> <package2-path> <package2-path> ...

                Specifies the first set of packages whose binaries are to be
                compared against the second one.  Note that the second set of
                packages is to be specified using the option --set2.

              • --set2 <package1-path> <package2-path> <package2-path> ...

                Specifies the second set of packages whose binaries are to be
                compared against the second one.  Note that the first set of
                packages is to be specified using the option --set1.

              • --suppressions | --suppr <path-to-suppressions>

                Use a suppression specification <#suppr-spec-label> file
                located at path-to-suppressions.  Note that this option can
                appear multiple times on the command line.  In that case, all
                of the suppression specification files are taken into
                account.

                Please note that, by default, if this option is not provided,
                then the default suppression specification files are loaded .

              • --version | -v

                Display the version of the program and exit.

              • --wp <path-to-whitelist-package>

                When comparing two Linux kernel RPM packages, this option
                points an RPM package containining several white lists of
                names of ELF symbols of functions and variables that must be
                compared for ABI changes.  Those white lists are called
                "Linux kernel ABI white lists".

                From the content of that white list package, this program
                then chooses the appropriate Linux kernel ABI white list to
                consider when comparing the ABI of Linux kernel binaries
                contained in the Linux kernel packages provided on the
                command line.

                That choosen Linux kernel ABI white list contains the list of
                names of ELF symbols of functions and variables that must be
                compared for ABI changes.

                Any other function or variable which ELF symbol are not
                present in that white list will not be considered by the ABI
                comparison process.

                Note that this option can be provided twice (not mor than
                twice), specifying one white list package for each Linux
                Kernel package that is provided on the command line.

                If this option is not provided -- thus if no white list is
                provided -- then the ABI of all publicly defined and exported
                functions and global variables by the Linux Kernel binaries
                are compared.

              • --verbose

                Emit verbose progress messages.

              • --verbose-diff

                Emit timed verbose progress messages about the diffing
                process.  This option implies the --verbose one.

       Return value
           The exit code of the abipkgdiff command is either 0 if the ABI of
           the binaries compared are equal, or non-zero if they differ or if
           the tool encountered an error.

           In the later case, the value of the exit code is the same as for
           the abidiff tool <#abidiff-return-value-label>.

       kmidiff
           kmidiff compares the binary Kernel Module Interfaces of two Linux
           Kernel trees.  The binary KMI is the interface that the Linux
           Kernel exposes to its modules.  The trees we are interested in
           here are the result of the build of the Linux Kernel source tree.

       General approach
           And example of how to build your kernel if you want to compare it
           to another one using kmidiff is:

              git clone -b v4.5 git://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git linux/v4.5
              cd linux/v4.5
              make allyesconfig all

           Then install the modules into a directory, for instance, the
           build/modules sub-directory of the your kernel source tree:

              mkdir build/modules
              make modules_install INSTALL_MOD_DIR=build/modules

           Then construct a list of interfaces exported by the kernel, that
           you want to compare:

              cat > kmi-whitelist << EOF
              [kernel_4.5_kmi_whitelist]
               init_task
               schedule
               dev_queue_xmit
               __kmalloc
               printk
              EOF

           Suppose you've done something similar for the v4.6 branch of the
           Linux kernel, you now have these two directories: linux/v4.5 and
           linux/v4.6.  Their modules are present under the directories
           linux/v4.5/build/modules and linux/v4.6/build/modules.

           To Comparing their KMI kmidiff needs to know where to find the
           vmlinux binaries and their associated modules.  Here would be what
           the command line looks like:

              kmidiff                                     \
                --kmi-whitelist  linux/v4.6/kmi-whitelist \
                --vmlinux1       linux/v4.5/vmlinux       \
                --vmlinux2       linux/v4.6/vmlinux       \
                                 linux/v4.5/build/modules \
                                 linux/v4.6/build/modules

           This tool uses the libabigail library to analyze the binary as
           well as its associated debug information.  Here is its general
           mode of operation.

           When instructed to do so, a binary and its associated debug
           information is read and analyzed.  To that effect, libabigail
           analyzes by default the descriptions of the types reachable by the
           interfaces (functions and variables) that are visible outside of
           their translation unit.  Once that analysis is done, an
           Application Binary Interface Corpus is constructed by only
           considering the subset of types reachable from interfaces
           associated to ELF
           <http://en.wikipedia.org/wiki/Executable_and_Linkable_Format>
           symbols that are defined and exported by the binary.  It's that
           final ABI corpus which libabigail considers as representing the
           ABI of the analyzed binary.

           Libabigail then has capabilities to generate textual
           representations of ABI Corpora, compare them, analyze their
           changes and report about them.

       Invocation
           More generally, kmidiff is invoked under the form:

              kmidiff [options] <first-modules-dir> <second-modules-dir>

       Environment
           By default, kmidiff compares all the interfaces (exported
           functions and variables) between the Kernel and its modules.  In
           practice, though, some users might want to compare a subset of the
           those interfaces.

           By default, kmidiff uses debug information in the DWARF
           <http://www.dwarfstd.org> debug info format, if present, otherwise
           it compares interfaces using CTF
           <https://raw.githubusercontent.com/wiki/oracle/binutils-gdb/files/ctf-spec.pdf>
           or BTF <https://docs.kernel.org/bpf/btf.html> debug info formats,
           if present.  Finally, if no debug info in these formats is found,
           it only considers ELF
           <http://en.wikipedia.org/wiki/Executable_and_Linkable_Format>
           symbols and report about their addition or removal.

           Users can then define a "white list" of the interfaces to compare.
           Such a white list is a just a file in the "INI" format that looks
           like:

              [kernel_version_x86_64_whitelist]
                function1_name
                function2_name
                global_variable1_name
                ....

           Note that the name of the section (the name that is between the
           two brackets) of that INI file just has to end with the string
           "whitelist".  So you can define the name you want, for instance
           [kernel_46_x86_64_whitelist].

           Then each line of that whitelist file is the name of an exported
           function or variable.  Only those interfaces along with the types
           reachable from their signatures are going to be compared by
           kmidiff recursively.

           Note that by default kmidiff analyzes the types reachable from the
           interfaces associated with ELF
           <http://en.wikipedia.org/wiki/Executable_and_Linkable_Format>
           symbols that are defined and exported by the Linux Kernel
           <https://kernel.org> as being the union of the vmlinux binary and
           all its compiled modules.  It then compares those interfaces
           (along with their types).

       Options
              • --help | -h

                Display a short help about the command and exit.

              • --version | -v

                Display the version of the program and exit.

              • --verbose

                Display some verbose messages while executing.

              • --debug-info-dir1 | --d1 <di-path1>

                For cases where the debug information for the binaries of the
                first Linux kernel is split out into separate files, tells
                kmidiff where to find those separate debug information files.

                Note that di-path must point to the root directory under
                which the debug information is arranged in a tree-like
                manner.  Under Red Hat based systems, that directory is
                usually <root>/usr/lib/debug.

              • --debug-info-dir2 | --d2 <di-path2>

                Like --debug-info-dir1, this options tells kmidiff where to
                find the split debug information for the binaries of the
                second Linux kernel.

              • --vmlinux1 | --l1 <path-to-first-vmlinux>

                Sets the path to the first vmlinux binary to consider.  This
                has to be the uncompressed vmlinux binary compiled with debug
                info.

              • --vmlinux2 | --l2 <path-to-first-vmlinux>

                Sets the path to the second vmlinux binary to consider.  This
                has to be the uncompressed vmlinux binary compiled with debug
                info.

              • --kmi-whitelist | -w <path-to-interface-whitelist>

                Set the path to the white list of interfaces to compare while
                comparing the Kernel Module Interface of the first kernel
                against the one of the second kernel.

                If this option is not provided, all the exported interfaces
                of the two kernels are compared.  That takes a lot of times
                and is not necessarily meaningful because many interface are
                probably meant to see their reachable types change.

                So please, make sure you always use this option unless you
                really know what you  are doing.

              • --suppressions | --suppr <path-to-suppressions>

                Use a suppression specification <#suppr-spec-label> file
                located at path-to-suppressions.  Note that this option can
                appear multiple times on the command line.  In that case, all
                of the provided suppression specification files are taken
                into account.

                Please note that, by default, if this option is not provided,
                then the default suppression specification files <#
                abidiff-default-supprs-label> are loaded .

              • --no-change-categorization | -x

                This option disables the categorization of changes into
                harmless and harmful changes.  Note that this categorization
                is a pre-requisite for the filtering of changes so this
                option disables that filtering.  The goal of this option is
                to speed-up the execution of the program for cases where the
                graph of changes is huge and where the user is just
                interested in looking at, for instance, leaf node changes
                without caring about their possible impact on interfaces.

              • --ctf

                Extract ABI information from CTF
                <https://raw.githubusercontent.com/wiki/oracle/binutils-gdb/files/ctf-spec.pdf>
                debug information, if present, in the Kernel and Modules.

              • --btf

                Extract ABI information from BTF
                <https://docs.kernel.org/bpf/btf.html> debug information, if
                present, in the Kernel and Modules.

              • --impacted-interfaces | -i

                Tell what interfaces got impacted by each individual ABI
                change.

              • --full-impact | -f

                Emit a change report that shows the full impact of each
                change on exported interfaces.  This is the default kind of
                report emitted by tools like abidiff or abipkgdiff.

              • --exported-interfaces-only

                When using this option, this tool analyzes the descriptions
                of the types reachable by the interfaces (functions and
                variables) associated with ELF
                <http://en.wikipedia.org/wiki/Executable_and_Linkable_Format>
                symbols that are defined and exported by the Linux Kernel
                <https://kernel.org>.

                Otherwise, the tool also has the ability to analyze the
                descriptions of the types reachable by the interfaces
                associated with ELF
                <http://en.wikipedia.org/wiki/Executable_and_Linkable_Format>
                symbols that are visible outside their translation unit.
                This later possibility is however much more resource
                intensive and results in much slower operations.

                That is why this option is enabled by default.

              • --allow-non-exported-interfaces

                When using this option, this tool analyzes the descriptions
                of the types reachable by the interfaces (functions and
                variables) that are visible outside of their translation
                unit.  Once that analysis is done, an ABI Corpus is
                constructed by only considering the subset of types reachable
                from interfaces associated to ELF
                <http://en.wikipedia.org/wiki/Executable_and_Linkable_Format>
                symbols that are defined and exported by the binary.  It's
                that final ABI corpus which is compared against another one.

                The problem with that approach however is that analyzing all
                the interfaces that are visible from outside their
                translation unit can amount to a lot of data, leading to very
                slow operations.

                Note that this option is turned off by default.

              • --show-bytes

                Show sizes and offsets in bytes, not bits.  This option is
                activated by default.

              • --show-bits

                Show sizes and offsets in bits, not bytes.  By default, sizes
                and offsets are shown in bytes.

              • --show-hex

                Show sizes and offsets in hexadecimal base.  This option is
                activated by default.

              • --show-dec

                Show sizes and offsets in decimal base.

       abidw
           abidw reads a shared library in ELF
           <http://en.wikipedia.org/wiki/Executable_and_Linkable_Format>
           format and emits an XML representation of its ABI to standard
           output.  The emitted representation format, named ABIXML, includes
           all the globally defined functions and variables, along with a
           complete representation of their types.  It also includes a
           representation of the globally defined ELF symbols of the file.

           When given the --linux-tree option, this program can also handle a
           Linux kernel <https://kernel.org/> tree.  That is, a directory
           tree that contains both the vmlinux binary and Linux Kernel
           <https://kernel.org/> modules.  It analyses those Linux Kernel
           <https://kernel.org/> binaries and emits an XML representation of
           the interface between the kernel and its module, to standard
           output.  In this case, we don't call it an ABI, but a KMI (Kernel
           Module Interface).  The emitted KMI includes all the globally
           defined functions and variables, along with a complete
           representation of their types.

           To generate either ABI or KMI representation, by default abidw
           uses debug information in the DWARF <http://www.dwarfstd.org>
           format, if present, otherwise it looks for debug information in
           CTF
           <https://raw.githubusercontent.com/wiki/oracle/binutils-gdb/files/ctf-spec.pdf>
           or BTF <https://docs.kernel.org/bpf/btf.html> formats, if present.
           Finally, if no debug info in these formats is found, it only
           considers ELF
           <http://en.wikipedia.org/wiki/Executable_and_Linkable_Format>
           symbols and report about their addition or removal.

           This tool uses the libabigail library to analyze the binary as
           well as its associated debug information.  Here is its general
           mode of operation.

           When instructed to do so, a binary and its associated debug
           information is read and analyzed.  To that effect, libabigail
           analyzes by default the descriptions of the types reachable by the
           interfaces (functions and variables) that are visible outside of
           their translation unit.  Once that analysis is done, an
           Application Binary Interface Corpus is constructed by only
           considering the subset of types reachable from interfaces
           associated to ELF
           <http://en.wikipedia.org/wiki/Executable_and_Linkable_Format>
           symbols that are defined and exported by the binary.  It's that
           final ABI corpus which libabigail considers as representing the
           ABI of the analyzed binary.

           Libabigail then has capabilities to generate textual
           representations of ABI Corpora, compare them, analyze their
           changes and report about them.

       Invocation
              abidw [options] [<path-to-elf-file>]

       Options
              • --abidiff
                  Load the ABI of the ELF binary given in argument, save it
                  in libabigail's XML format in a temporary file; read the
                  ABI from the temporary XML file and compare the ABI that
                  has been read back against the ABI of the ELF binary given
                  in argument.  The ABIs should compare equal.  If they
                  don't, the program emits a diagnostic and exits with a
                  non-zero code.

                  This is a debugging and sanity check option.

              • --abixml-version

                Display the version of the ABIXML format emitted by this
                program and exit.

              • --add-binaries <bin1,bin2,...>

                For each of the comma-separated binaries given in argument to
                this option, if the binary is found in the directory
                specified by the --added-binaries-dir option, then load the
                ABI corpus of the binary and add it to a set of ABI corpora
                (called a ABI Corpus Group) made of the binary denoted by the
                Argument of abidw.  That corpus group is then serialized out.

              • --added-binaries-dir | --abd <dir-path>

                This option is to be used in conjunction with the
                --add-binaries, the --follow-dependencies or the
                --list-dependencies option.  Binaries listed as arguments of
                the --add-binaries option or being dependencies of the input
                binary in the case of the --follow-dependencies option and
                found in the directory <dir-path> are going to be loaded as
                ABI corpus and added to the set of ABI corpora (called an ABI
                corpus group) built and serialized.

              • --allow-non-exported-interfaces

                When looking at the debug information accompanying a binary,
                this tool analyzes the descriptions of the types reachable by
                the interfaces (functions and variables) that are visible
                outside of their translation unit.  Once that analysis is
                done, an ABI corpus is constructed by only considering the
                subset of types reachable from interfaces associated to ELF
                <http://en.wikipedia.org/wiki/Executable_and_Linkable_Format>
                symbols that are defined and exported by the binary.  It's
                that final ABI corpus which textual representation is saved
                as ABIXML.

                The problem with that approach however is that analyzing all
                the interfaces that are visible from outside their
                translation unit can amount to a lot of data, especially when
                those binaries are applications, as opposed to shared
                libraries.  One example of such applications is the Linux
                Kernel <https://kernel.org/>.  Analyzing massive ABI corpora
                like these can be extremely slow.

                In the presence of an "average sized" binary however one can
                afford having libabigail analyze all interfaces that are
                visible outside of their translation unit, using this option.

                Note that this option is turned on by default, unless we are
                in the presence of the Linux Kernel <https://kernel.org/>.

              • --annotate
                  Annotate the ABIXML output with comments above most
                  elements.  The comments are made of the pretty-printed form
                  types, declaration or even ELF symbols.  The purpose is to
                  make the ABIXML output more human-readable for debugging or
                  documenting purposes.

              • --btf

                Extract ABI information from BTF
                <https://docs.kernel.org/bpf/btf.html> debug information, if
                present in the given object.

              • --check-alternate-debug-info <elf-path>

                If the debug info for the file elf-path contains a reference
                to an alternate debug info <alt-di-label> file, abidw checks
                that it can find that alternate debug info file.  In that
                case, it emits a meaningful success message mentioning the
                full path to the alternate debug info file found.  Otherwise,
                it emits an error code.

              • --check-alternate-debug-info-base-name <elf-path>

                Like --check-alternate-debug-info, but in the success
                message, only mention the base name of the debug info file;
                not its full path.

              • --debug-abidiff
                  Same as --abidiff but in debug mode.  In this mode, error
                  messages are emitted for types which fail type
                  canonicalization.

                  This is an optional debugging and sanity check option.  To
                  enable it the libabigail package needs to be configured
                  with the --enable-debug-self-comparison option.

              • --ctf

                Extract ABI information from CTF
                <https://raw.githubusercontent.com/wiki/oracle/binutils-gdb/files/ctf-spec.pdf>
                debug information, if present in the given object.

              • --debug-info-dir | -d <dir-path>

                In cases where the debug info for path-to-elf-file is in a
                separate file that is located in a non-standard place, this
                tells abidw where to look for that debug info file.

                Note that dir-path must point to the root directory under
                which the debug information is arranged in a tree-like
                manner.  Under Red Hat based systems, that directory is
                usually <root>/usr/lib/debug.

                This option can be provided several times with different root
                directories.  In that case, abidw will potentially look into
                all those root directories to find the split debug info for
                the elf file.

                Note that this option is not mandatory for split debug
                information installed by your system's package manager
                because then abidw knows where to find it.

              • --debug-type-canonicalization | --debug-tc
                  Debug the type canonicalization process.  This is done by
                  using structural and canonical equality when canonicalizing
                  every single type.  Structural and canonical equality
                  should yield the same result.  If they don't yield the same
                  result for a given type, then it means that the
                  canonicalization of that type went wrong.  In that case, an
                  error message is emitted and the execution of the program
                  is aborted.

                  This option is available only if the package was configured
                  with the --enable-debug-type-canonicalization option.

              • --drop-private-types

                This option is implicitly set by option --headers-dir and
                --header-file options.

                With this option, types that are NOT defined in the headers
                are entirely dropped from the internal representation build
                by Libabigail to represent the ABI and will not end up in the
                abi XML file.

                This option is provided or compatibility reasons only and
                should not be explicitly used anymore.

              • --drop-undefined-syms

                With this option functions or variables for which the
                (exported) ELF symbol is undefined are dropped from the
                internal representation build by Libabigail to represent the
                ABI and will not end up in the abi XML file.

              • --exported-interfaces-only

                By default, when looking at the debug information
                accompanying a binary, this tool analyzes the descriptions of
                the types reachable by the interfaces (functions and
                variables) that are visible outside of their translation
                unit.  Once that analysis is done, an ABI corpus is
                constructed by only considering the subset of types reachable
                from interfaces associated to ELF
                <http://en.wikipedia.org/wiki/Executable_and_Linkable_Format>
                symbols that are defined and exported by the binary.  It's
                that final ABI corpus which textual representation is saved
                as ABIXML.

                The problem with that approach however is that analyzing all
                the interfaces that are visible from outside their
                translation unit can amount to a lot of data, especially when
                those binaries are applications, as opposed to shared
                libraries.  One example of such applications is the Linux
                Kernel <https://kernel.org/>.  Analyzing massive ABI corpora
                like these can be extremely slow.

                To mitigate that performance issue, this option allows
                libabigail to only analyze types that are reachable from
                interfaces associated with defined and exported ELF
                <http://en.wikipedia.org/wiki/Executable_and_Linkable_Format>
                symbols.

                Note that this option is turned on by default when analyzing
                the Linux Kernel <https://kernel.org/>.  Otherwise, it's
                turned off by default.

              • --fail-no-debug-info

                If the program could not find the debug info for the input
                binary, then it exits with a non-zero error code.  Without
                this option, the program emits the ABI information about ELF
                symbols, in the absence of the debug info.  In that case,
                type information is omitted.

              • --follow-dependencies

                For each dependency of the input binary of abidw, if it is
                found in the directory specified by the --added-binaries-dir
                option, then construct an ABI corpus out of the dependency
                and add it to a set of ABI corpora (called an ABI Corpus
                Group) along with the ABI corpus of the input binary of the
                program.  The ABI Corpus Group is then serialized out.

              • --force-early-suppression

                This option must be used alongside option --suppression.

                It forces suppression specifications <#suppr-spec-label> to
                be applied in early suppression mode <#
                early-suppression-mode-label>.  Artifacts of the internal
                representation that are matched by suppression specifications
                are thus suppressed from memory.

                If this option is not used then only suppression
                specifications with the drop property set to 'yes' <#
                drop-property-label> are effective.  All other suppression
                specification directives will appear to be ignored.

              • --headers-dir | --hd <headers-directory-path-1>

                Specifies where to find the public headers of the binary that
                the tool has to consider.  The tool will thus filter out
                types that are not defined in public headers.  This option
                implicitly sets option --drop-private-types.

                Note that several public header directories can be specified
                for the binary to consider.  In that case the --header-dir
                option should be present several times on the command line,
                like in the following example:

                    $ abidw --header-dir /some/path       \
                            --header-dir /some/other/path \
                            binary > binary.abi

              • --header-file | --hf <header-file-path>

                Specifies where to find one of the public headers of the abi
                file that the tool has to consider.  The tool will thus
                filter out types that are not defined in public headers.

                This option implicitly sets option --drop-private-types.

              • --help | -h

                Display a short help about the command and exit.

              • --kmi-whitelist | --kmi-stablelist |-w <path-to-stablelist>

                When analyzing a Linux Kernel <https://kernel.org/> binary,
                this option points to the list of names of ELF symbols of
                functions and variables which ABI must be written out.  Any
                function or variable with a name that is not included in that
                list will not ignored.  That list is called a " Kernel Module
                Interface stable list".  This is because for the Kernel, we
                don't talk about the ABI; we rather talk about the interface
                between the Kernel and its module. Hence the term KMI rather
                than KABI.

                Any other function or variable which ELF symbol are not
                present in that stable list will not be considered by the KMI
                writing process.

                If this option is not provided -- thus if no stable list is
                provided -- then the entire KMI, that is, all publicly
                defined and exported functions and global variables by the
                Linux Kernel <https://kernel.org/> binaries is emitted.

              • --list-dependencies

                For each dependency of the input binary of``abidw``, if it's
                found in the directory specified by the --added-binaries-dir
                option, then the name of the dependency is printed out.

              • --load-all-types

                By default, libabigail (and thus abidw) only loads types that
                are reachable from functions and variables declarations that
                are publicly defined and exported by the binary.  So only
                those types are present in the output of abidw.  This option
                however makes abidw load all the types defined in the
                binaries, even those that are not reachable from public
                declarations.

              • --linux-tree | --lt

                Make abidw to consider the input path as a path to a
                directory containing the vmlinux binary as several kernel
                modules binaries.  In that case, this program emits the
                representation of the Kernel Module Interface (KMI) on the
                standard output.

                Below is an example of usage of abidw on a Linux Kernel
                <https://kernel.org/> tree.

                First, checkout a Linux Kernel <https://kernel.org/> source
                tree and build it.  Then install the kernel modules in a
                directory somewhere.  Copy the vmlinux binary into that
                directory too.  And then serialize the KMI of that kernel to
                disk, using abidw:

                    $ git clone git://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git
                    $ cd linux && git checkout v4.5
                    $ make allyesconfig all
                    $ mkdir build-output
                    $ make INSTALL_MOD_PATH=./build-output modules_install
                    $ cp vmlinux build-output/modules/4.5.0
                    $ abidw --linux-tree build-output/modules/4.5.0 > build-output/linux-4.5.0.kmi

              • --no-assume-odr-for-cplusplus

                When analysing a binary originating from C++ code using DWARF
                <http://www.dwarfstd.org> debug information, libabigail
                assumes the One Definition Rule
                <https://en.wikipedia.org/wiki/One_Definition_Rule> to
                speed-up the analysis.  In that case, when several types have
                the same name in the binary, they are assumed to all be
                equal.

                This option disables that assumption and instructs libabigail
                to actually actually compare the types to determine if they
                are equal.

              • --no-corpus-path

                Do not emit the path attribute for the ABI corpus.

              • --no-elf-needed

                Do not include the list of DT_NEEDED dependency names in the
                corpus.

              • --no-leverage-dwarf-factorization

                When analysing a binary which DWARF <http://www.dwarfstd.org>
                debug information was processed with the DWZ
                <https://sourceware.org/dwz> tool, the type information is
                supposed to be already factorized.  That context is used by
                libabigail to perform some speed optimizations.

                This option disables those optimizations.

              • --no-load-undefined-interfaces

                By default, libabigail (and thus abidw) loads information
                about undefined function and variable symbols as well as
                functions and variables that are associated with those
                undefined symbols.  Those are called undefined interfaces.
                This option however makes makes abidw avoid loading
                information about undefined interfaces.  The resulting XML
                file thus doesn't contain information about those undefined
                interfaces.

              • --no-linux-kernel-mode

                Without this option, if abipkgiff detects that the binaries
                it is looking at are Linux Kernel binaries (either vmlinux or
                modules) then it only considers functions and variables which
                ELF symbols are listed in the __ksymtab and __ksymtab_gpl
                sections.

                With this option, abipkgdiff considers the binary as a
                non-special ELF binary.  It thus considers functions and
                variables which are defined and exported in the ELF sense.

              • --noout

                This option instructs abidw to not emit the XML
                representation of the ABI.  So it only reads the ELF and
                debug information, builds the internal representation of the
                ABI and exits.  This option is usually useful for debugging
                purposes.

              • --no-parameter-names

                In the emitted ABI representation, do not show names of
                function parameters, just the types.

              • --no-show-locs
                  In the emitted ABI representation, do not show file, line
                  or column where ABI artifacts are defined.

              • --no-write-default-sizes

                In the XML ABI representation, do not write the size-in-bits
                for pointer type definitions, reference type definitions,
                function declarations and function types when they are equal
                to the default address size of the translation unit.  Note
                that libabigail before 1.8 will not set the default size and
                will interpret types without a size-in-bits attribute as zero
                sized.

              • --out-file | -o <file-path>

                This option instructs abidw to emit the XML representation of
                path-to-elf-file into the file file-path, rather than
                emitting it to its standard output.

              • --stats

                Emit statistics about various internal things.

              • --suppressions | suppr
                <path-to-suppression-specifications-file>

                Use a suppression specification <#suppr-spec-label> file
                located at path-to-suppression-specifications-file.  Note
                that this option can appear multiple times on the command
                line.  In that case, all of the provided suppression
                specification files are taken into account.  ABI artifacts
                matched by the suppression specifications are suppressed from
                the output of this tool.

                Only suppression specifications that have the drop property
                set to 'yes' <#drop-property-label> are going to be
                effective.  All other suppression specification directives
                will appear as being ignored, unless the command line option
                --force-early-suppression is provided.

              • --type-id-style <sequence``|``hash>

                This option controls how types are idenfied in the generated
                XML files.  The default sequence style just numbers (with
                type-id- as prefix) the types in the order they are
                encountered.  The hash style uses a (stable, portable) hash
                of libabigail's internal type names and is intended to make
                the XML files easier to diff.

              • --verbose

                Emit verbose logs about the progress of miscellaneous
                internal things.

              • --version | -v

                Display the version of the program and exit.

       Usage examples
              1. Emitting an ABIXML representation of a binary:

                     $ abidw binary > binary.abi

              2. Emitting an ABIXML representation of a set of binaries
                 specified on the command line:

                     $ abidw --added-binaries=bin1,bin2,bin3  \
                             --added-binaries-dir /some/where \
                             binary > binaries.abi

                 Note that the binaries bin1, bin2 and bin3 are to be found
                 in the directory /some/where.  A representation of the ABI
                 of the set of binaries binary, bin1, bin2 and bin3 called an
                 ABI corpus group is serialized in the file binaries.abi.

              3. Emitting an ABIXML representation of a binary and its
                 dependencies:

                     $ abidw --follow-dependencies              \
                             --added-binaries-dir /some/where   \
                             binary > binary.abi

                 Note that only the dependencies that are found in the
                 directory /some/where are analysed.  Their ABIs, along with
                 the ABI the binary named binary are represented as an ABI
                 corpus group and serialized in the file binary.abi, in the
                 ABIXML format.

       Notes
       Alternate debug info files
           As of the version 4 of the DWARF specification, Alternate debug
           information <http://www.dwarfstd.org/ShowIssue.php?issue=120604.1>
           is a GNU <http://www.gnu.org> extension to the DWARF
           specification.  It has however been proposed for inclusion into
           the upcoming version 5 of the DWARF standard.  You can read more
           about the GNU extensions to the DWARF standard here
           <https://fedorahosted.org/elfutils/wiki/DwarfExtensions>.

       abidb
           abidb manages a git repository of abixml files describing shared
           libraries, and checks binaries against them.  elfutils and
           libabigail programs are used to query and process the binaries.
           abidb works well with debuginfod to fetch needed DWARF content
           automatically.

       Invocation
              abidb [OPTIONS] [--submit PATH1 PATH2 ...] [--check PATH1 PATH2 ...]

       Common Options
              • --abicompat PATH

                Specify the path to the abicompat program to use.  By
                default, in the absence of this option, the abicompat program
                found in directories listed in the $PATH environment is used.

              • --abidw PATH

                Specify the path to the abidw program to use.  By default, in
                the absence of this option, the abidw program found in
                directories listed in the $PATH environment is used.

              • --distrobranch BRANCH

                Specify the git branch for the abixml files in the git repo.
                The default is a string like DISTRO/VERSION/ARCHITECTURE,
                computed from the running environment.

              • --git REPO

                Specify the preexisting git working tree for abidb to submit
                to or check against.  The default is the current working
                directory.  It may be used concurrently by multiple "check"
                operations, but only one "submit" operation.

              • --help | -h

                Display a short help about the command and exit.

              • --loglevel LOGLEVEL

                Specify the diagnostic level for messages to stderr.  One of
                debug, info, warning, error, or critical; case-insensitive.
                The default is info.

              • --timeout SECONDS

                Specify a maximum limit to the execution time (in seconds)
                allowed for the abidw and abicompat programs that are
                executed.  By default, no limit is set for the execution time
                of these programs.

       Submit Options
              • --allow-no-debug-info

                By default, the program fails to submit a binary if its
                associated debug info could not be found.  With this option
                however if no debug info was found, then the ABI information
                submitted for the binary only comes from ELF symbols; the
                type information is omitted.

              • --archive | -Z .EXT[=CMD]

                Designate PATH names with a .EXT suffix to be treated as
                archives.  If CMD is present, pipe the PATH through the given
                shell command, otherwise pass as if through cat.  The
                resulting stream is then opened by libarchive, to enumerate
                the contents of a wide variety of possible archive file
                format.  Process each file in the archive individually into
                abixml.

                For example, -Z .zip will process each file in a zip file,
                and -Z .deb='dpkg-deb --fsys-tarfile' will process each
                payload file in a Debian archive.

              • --filter REGEX

                Limit files selected for abixml extraction to those that
                match the given regular expression.  The default is
                /lib.*\.so, as a heuristic to identify shared libraries.

              • --submit PATH1 PATH2 ...

                Using abidw, extract abixml for each of the listed files,
                generally shared libraries, subject to the filename filter
                and the archive decoding options.  Save the output of each
                abidw run into the selected distrobranch of the selected git
                repo.  If --submit and --check are both given, do submit
                operations first.

              • --sysroot PREFIX Specify the a prefix path that is to be
                removed from submitted file names.

       Check Options
              • --check PATH1 PATH2 ...

                Using abidiff, compare each of the listed file, generally
                executables, against abixml documents for selected versions
                for all shared libraries needed by the executable.  These are
                listed by enumerating the dynamic segment tags DT_NEEDED of
                the executable.

              • --ld-library-path DIR1:DIR2:DIR3...

                Select the search paths for abixml documents used to locate
                any particular SONAME .  The first given directory wins.
                However, all versions of the same SONAME in that directory
                are selected for comparison.  The default is unspecified,
                which means to search for all matching SONAME entries in the
                distrobranch, regardless of specific directory.

       Exit Code
           In case of successful submission and/or checking of all paths, the
           exit code is 0.

           In case of error, the exit code of abidb is nonzero, and a brief
           listing of the binaries unable to be submitted and/or checked is
           printed.

       Git Repository Schema
           abidb stores abixml documents in a git repo with the following
           naming schema within the distrobranch:

           1. The directory path leading to the shared library file

           2. The SONAME of the shared library file, as a subdirectory name

           3. A file named BUILDID.xml, where BUILDID is the hexadecimal ELF
              build-id note of the shared library.

           For example:
    ┌───────────────────────────┬───────────────────────────────────────────────────────────────────┐
    │ shared library file name  │ abixml path in git                                                │
    ├───────────────────────────┼───────────────────────────────────────────────────────────────────┤
    │ /usr/lib64/libc.so.6.2.32 │ /usr/lib64/libc.so.6/788cdd41a15985bf8e0a48d213a46e07d58822df.xml │
    │ /usr/lib64/libc.so.6.2.33 │ /usr/lib64/libc.so.6/e2ca832f1c2112aea9d7b9bc639e97e873a6b516.xml │
    │ /lib/ld-linux.so.2        │ /lib/ld-linux.so.2/b65f3c15b129f33f44f504da1719926aec03c07d.xml   │
    └───────────────────────────┴───────────────────────────────────────────────────────────────────┘

           The intent of including the buildid in the name is so that as a
           distro is updated with multiple versions of a given shared
           library, they can be represented nearby but non-conflicting.  The
           SONAME is used in the second-last name component, inspired the
           behavior of ld.so and ldconfig, which rely on symbolic links to
           map references from the SONAME to an actual file.

       See Also
              • ELF:
                <http://en.wikipedia.org/wiki/Executable_and_Linkable_Format>

              • DWARF: <https://www.dwarfstd.org>

              • Debuginfod: <https://sourceware.org/elfutils/Debuginfod.html>

              • Git: <https://git-scm.com/>

              • Libarchive: <https://www.libarchive.org/>

       abicompat
           abicompat checks that an application that links against a given
           shared library is still ABI compatible with a subsequent version
           of that library.  If the new version of the library introduces an
           ABI incompatibility, then abicompat hints the user at what exactly
           that incompatibility is.

       Invocation
              abicompat [options] [<application> <shared-library-first-version> <shared-library-second-version>]

       Options
              • --help

                Display a short help about the command and exit.

              • --version | -v

                Display the version of the program and exit.

              • --list-undefined-symbols | -u

                Display the list of undefined symbols of the application and
                exit.

              • --show-base-names | -b

                In the resulting report emitted by the tool, this option
                makes the application and libraries be referred to by their
                base names only; not by a full absolute name.  This can be
                useful for use in scripts that wants to compare names of the
                application and libraries independently of what their
                directory names are.

              • --app-debug-info-dir | --appd
                <path-to-app-debug-info-directory>

                Set the path to the directory under which the debug
                information of the application is supposed to be laid out.
                This is useful for application binaries for which the debug
                info is in a separate set of files.

              • --lib-debug-info-dir1 | --libd1 <path-to-lib1-debug-info>

                Set the path to the directory under which the debug
                information of the first version of the shared library is
                supposed to be laid out.  This is useful for shared library
                binaries for which the debug info is in a separate set of
                files.

              • --lib-debug-info-dir2 | --libd2 <path-to-lib1-debug-info>

                Set the path to the directory under which the debug
                information of the second version of the shared library is
                supposed to be laid out.  This is useful for shared library
                binaries for which the debug info is in a separate set of
                files.

              • --suppressions | --suppr <path-to-suppressions>

                Use a suppression specification <#suppr-spec-label> file
                located at path-to-suppressions.  Note that this option can
                appear multiple times on the command line; all the
                suppression specification files are then taken into account.

              • --no-show-locs
                  Do not show information about where in the second shared
                  library the respective type was changed.

              • --btf

                When comparing binaries, extract ABI information from BTF
                debug information, if present.

              • --ctf

                When comparing binaries, extract ABI information from CTF
                debug information, if present.

              • --fail-no-debug-info

                If no debug info was found, then this option makes the
                program to fail.  Otherwise, without this option, the program
                will attempt to compare properties of the binaries that are
                not related to debug info, like pure ELF properties.

              • --ignore-soname

                Ignore differences in the SONAME when doing a comparison

              • --weak-mode

                This triggers the weak mode of abicompat.  In this mode, only
                one version of the library is required.  That is, abicompat
                is invoked like this:

                    abicompat --weak-mode <the-application> <the-library>

                Note that the --weak-mode option can even be omitted if only
                one version of the library is given, along with the
                application; in that case, abicompat automatically switches
                to operate in weak mode:

                    abicompat <the-application> <the-library>

                In this weak mode, the types of functions and variables
                exported by the library and consumed by the application (as
                in, the symbols of the these functions and variables are
                undefined in the application and are defined and exported by
                the library) are compared to the version of these types as
                expected by the application.  And if these two versions of
                types are different, abicompat tells the user what the
                differences are.

                In other words, in this mode, abicompat checks that the types
                of the functions and variables exported by the library mean
                the same thing as what the application expects, as far as the
                ABI is concerned.

                Note that in this mode, abicompat doesn't detect exported
                functions or variables (symbols) that are expected by the
                application but that are removed from the library.  That is
                why it is called weak mode.

       Return values
           The exit code of the abicompat command is either 0 if the ABI of
           the binaries being compared are equal, or non-zero if they differ
           or if the tool encountered an error.

           In the later case, the exit code is a 8-bits-wide bit field in
           which each bit has a specific meaning.

           The first bit, of value 1, named ABIDIFF_ERROR means there was an
           error.

           The second bit, of value 2, named ABIDIFF_USAGE_ERROR means there
           was an error in the way the user invoked the tool.  It might be
           set, for instance, if the user invoked the tool with an unknown
           command line switch, with a wrong number or argument, etc.  If
           this bit is set, then the ABIDIFF_ERROR bit must be set as well.

           The third bit, of value 4, named ABIDIFF_ABI_CHANGE means the ABI
           of the binaries being compared are different.

           The fourth bit, of value 8, named ABIDIFF_ABI_INCOMPATIBLE_CHANGE
           means the ABI of the binaries compared are different in an
           incompatible way.  If this bit is set, then the ABIDIFF_ABI_CHANGE
           bit must be set as well.  If the ABIDIFF_ABI_CHANGE is set and the
           ABIDIFF_INCOMPATIBLE_CHANGE is NOT set, then it means that the
           ABIs being compared might or might not be compatible.  In that
           case, a human being needs to review the ABI changes to decide if
           they are compatible or not.

           The remaining bits are not used for the moment.

       Usage examples
              • Detecting a possible ABI incompatibility in a new shared
                library version:

                    $ cat -n test0.h
                         1  struct foo
                         2  {
                         3    int m0;
                         4
                         5    foo()
                         6      : m0()
                         7    {}
                         8  };
                         9
                        10  foo*
                        11  first_func();
                        12
                        13  void
                        14  second_func(foo&);
                        15
                        16  void
                        17  third_func();
                    $

                    $ cat -n test-app.cc
                         1  // Compile with:
                         2  //  g++ -g -Wall -o test-app -L. -ltest-0 test-app.cc
                         3
                         4  #include "test0.h"
                         5
                         6  int
                         7  main()
                         8  {
                         9    foo* f = first_func();
                        10    second_func(*f);
                        11    return 0;
                        12  }
                    $

                    $ cat -n test0.cc
                         1  // Compile this with:
                         2  //  g++ -g -Wall -shared -o libtest-0.so test0.cc
                         3
                         4  #include "test0.h"
                         5
                         6  foo*
                         7  first_func()
                         8  {
                         9    foo* f = new foo();
                        10    return f;
                        11  }
                        12
                        13  void
                        14  second_func(foo&)
                        15  {
                        16  }
                        17
                        18  void
                        19  third_func()
                        20  {
                        21  }
                    $

                    $ cat -n test1.h
                         1  struct foo
                         2  {
                         3    int  m0;
                         4    char m1; /* <-- a new member got added here! */
                         5
                         6    foo()
                         7    : m0(),
                         8      m1()
                         9    {}
                        10  };
                        11
                        12  foo*
                        13  first_func();
                        14
                        15  void
                        16  second_func(foo&);
                        17
                        18  void
                        19  third_func();
                    $

                    $ cat -n test1.cc
                         1  // Compile this with:
                         2  //  g++ -g -Wall -shared -o libtest-1.so test1.cc
                         3
                         4  #include "test1.h"
                         5
                         6  foo*
                         7  first_func()
                         8  {
                         9    foo* f = new foo();
                        10    return f;
                        11  }
                        12
                        13  void
                        14  second_func(foo&)
                        15  {
                        16  }
                        17
                        18  /* Let's comment out the definition of third_func()
                        19     void
                        20     third_func()
                        21     {
                        22     }
                        23  */
                    $

                • Compile the first and second versions of the libraries:
                  libtest-0.so and libtest-1.so:

                      $ g++ -g -Wall -shared -o libtest-0.so test0.cc
                      $ g++ -g -Wall -shared -o libtest-1.so test1.cc

                • Compile the application and link it against the first
                  version of the library, creating the test-app binary:

                      $ g++ -g -Wall -o test-app -L. -ltest-0.so test-app.cc

                • Now, use abicompat to see if libtest-1.so is ABI compatible
                  with app, with respect to the ABI of libtest-0.so:

                      $ abicompat test-app libtest-0.so libtest-1.so
                      ELF file 'test-app' might not be ABI compatible with 'libtest-1.so' due to differences with 'libtest-0.so' below:
                      Functions changes summary: 0 Removed, 2 Changed, 0 Added functions
                      Variables changes summary: 0 Removed, 0 Changed, 0 Added variable

                      2 functions with some indirect sub-type change:

                        [C]'function foo* first_func()' has some indirect sub-type changes:
                          return type changed:
                            in pointed to type 'struct foo':
                              size changed from 32 to 64 bits
                              1 data member insertion:
                                'char foo::m1', at offset 32 (in bits)
                        [C]'function void second_func(foo&)' has some indirect sub-type changes:
                          parameter 0 of type 'foo&' has sub-type changes:
                            referenced type 'struct foo' changed, as reported earlier

                      $

                • Now use the weak mode of abicompat, that is, providing just
                  the application and the new version of the library:

                      $ abicompat --weak-mode test-app libtest-1.so
                      functions defined in library
                          'libtest-1.so'
                      have sub-types that are different from what application
                          'test-app'
                      expects:

                        function foo* first_func():
                          return type changed:
                            in pointed to type 'struct foo':
                              size changed from 32 to 64 bits
                              1 data member insertion:
                                'char foo::m1', at offset 32 (in bits)

                      $

       abilint
           abilint parses the native XML representation of an ABI as emitted
           by abidw <>.  Once it has parsed the XML representation of the
           ABI, abilint builds and in-memory model from it.  It then tries to
           save it back to an XML form, to standard output.  If that
           read-write operation succeeds chances are the input XML ABI
           representation is meaningful.

           Note that the main intent of this tool to help debugging issues in
           the underlying Libabigail library.

           Note also that abilint can also read an ELF
           <http://en.wikipedia.org/wiki/Executable_and_Linkable_Format>
           input file, build the in-memory model for its ABI, and serialize
           that model back into XML to standard output.  In that case, the
           ELF <http://en.wikipedia.org/wiki/Executable_and_Linkable_Format>
           input file must be accompanied with its debug information in the
           DWARF <http://www.dwarfstd.org> format.

       Invocation
              abilint [options] [<abi-file1>]

       Options
              • --annotate

                Annotate the ABIXML output with comments above most elements.
                The comments are made of the pretty-printed form of types,
                declaration or even ELF symbols.  The purpose is to make the
                ABIXML output more human-readable for debugging or
                documenting purposes.

              • --ctf

                Extract ABI information from CTF debug information, if
                present in the given object.

              • --debug-info-dir <path>

                When reading an ELF
                <http://en.wikipedia.org/wiki/Executable_and_Linkable_Format>
                input file which debug information is split out into a
                separate file, this options tells abilint where to find that
                separate debug information file.

                Note that path must point to the root directory under which
                the debug information is arranged in a tree-like manner.
                Under Red Hat based systems, that directory is usually
                <root>/usr/lib/debug.

                Note also that this option is not mandatory for split debug
                information installed by your system's package manager
                because then abidiff knows where to find it.

              • --diff

                For XML inputs, perform a text diff between the input and the
                memory model saved back to disk.  This can help to spot
                issues in the handling of the XML format by the underlying
                Libabigail library.

              • --header-file | --hf <header-file-path>

                Specifies where to find one of the public headers of the abi
                file that the tool has to consider.  The tool will thus
                filter out types that are not defined in public headers.

              • --headers-dir | --hd <headers-directory-path-1>

                Specifies where to find the public headers of the first
                shared library that the tool has to consider.  The tool will
                thus filter out types that are not defined in public headers.

              • --help

                Display a short help message and exits.

              • --noout

                Do not display anything on standard output.  The return code
                of the command is the only way to know if the command
                succeeded.

              • --suppressions | suppr
                <path-to-suppression-specifications-file>

                Use a suppression specification <#suppr-spec-label> file
                located at path-to-suppression-specifications-file.  Note
                that this option can appear multiple times on the command
                line.  In that case, all of the provided suppression
                specification files are taken into account.  ABI artifacts
                matched by the suppression specifications are suppressed from
                the output of this tool.

              • --stdin | --

                Read the input content from standard input.

              • --tu

                Expect the input XML to represent a single translation unit.

              • --verbose

                Shows verbose messages about internal stuff.  This is used to
                debug the tool and its underlying library.

              • --version | -v

                Display the version of the program and exit.

       fedabipkgdiff
           fedabipkgdiff compares the ABI of shared libraries in Fedora
           <https://getfedora.org> packages.  It's a convenient way to do so
           without having to manually download packages from the Fedora Build
           System <http://koji.fedoraproject.org/koji>.

           fedabipkgdiff knows how to talk with the Fedora Build System
           <http://koji.fedoraproject.org/koji> to find the right packages
           versions, their associated debug information and development
           packages, download them, compare their ABI locally, and report
           about the possible ABI changes.

           Note that by default, this tool reports ABI changes about types
           that are defined in public header files found in the development
           packages associated with the packages being compared.  It also
           reports ABI changes about functions and global variables whose
           symbols are defined and exported in the ELF binaries found in the
           packages being compared.

       Invocation
              fedabipkgdiff [option] <NVR> ...

       Environment
           fedabipkgdiff loads two default suppression specifications files
           <#suppr-spec-label>, merges their content and use it to filter out
           ABI change reports that might be considered as false positives to
           users.

           • Default system-wide suppression specification file

             It's located by the optional environment variable
             LIBABIGAIL_DEFAULT_SYSTEM_SUPPRESSION_FILE.  If that environment
             variable is not set, then fedabipkgdiff tries to load the
             suppression file $libdir/libabigail/libabigail-default.abignore.
             If that file is not present, then no default system-wide
             suppression specification file is loaded.

           • Default user suppression specification file.

             It's located by the optional environment
             LIBABIGAIL_DEFAULT_USER_SUPPRESSION_FILE.  If that environment
             variable is not set, then fedabipkgdiff tries to load the
             suppression file $HOME/.abignore.  If that file is not present,
             then no default user suppression specification is loaded.

       Options
              • --abipkgdiff <path/to/abipkgdiff>

                Specify an alternative abipkgdiff instead of the one
                installed in system.

              • --all-subpackages

                Instructs the tool to also compare the ABI of the binaries in
                the sub-packages of the packages specified.

              • --clean-cache

                If you want to clean cache both before and after ABI
                comparison, --clean-cache is the convenient way for you to
                save typing of two options at same time.

              • --clean-cache-after

                Clean cache after ABI comparison.

              • --clean-cache-before

                Clean cache before ABI comparison.

              • --debug

                Emit debugging messages about the execution of the program.
                Details about each method invocation, including input
                parameters and returned values, are emitted.

              • --dry-run

                Don't actually perform the ABI comparison.  Details about
                what is going to be done are emitted on standard output.

              • --dso-only

                Compares the ABI of shared libraries only.  If this option is
                not provided, the tool compares the ABI of all ELF binaries
                found in the packages.

              • --from <distro>

                Specifies the name of the baseline Fedora
                <https://getfedora.org> distribution in which to find the
                first build that is used for comparison. The distro value can
                be any valid value of the RPM macro %{?dist} for Fedora
                <https://getfedora.org>, for example, fc4, fc23, fc25.

              • --help | -h

                Display a short help about the command and exit.

              • --no-default-suppression

                Do not load the default suppression specification files.

              • --no-devel-pkg

                Do not take associated development packages into account when
                performing the ABI comparison.  This makes the tool report
                ABI changes about all types that are reachable from functions
                and global variables which symbols are defined and publicly
                exported in the binaries being compared, even if those types
                are not defined in public header files available from the
                packages being compared.

              • --private-dso

                Compare the ABI of shared libraries that are private to the
                packages.  If this option is not provided, shared libraries
                that are private to the packages being considered are not
                compared.

              • --server <URL>

                Specifies the URL of the Koji
                <https://fedoraproject.org/wiki/Koji> XMLRPC service the tool
                talks to.  The default value of this option is
                <http://koji.fedoraproject.org/kojihub>.

              • --show-identical-binaries
                  Show the names of the all binaries compared, including the
                  binaries whose ABI compare equal.  By default, when this
                  option is not provided, only binaries with ABI changes are
                  mentionned in the output.

              • --suppressions <path-to-suppresions>

                Use a suppression specification <#suppr-spec-label> file
                located at path-to-suppressions.

              • --to <distro>

                Specifies the name of the Fedora <https://getfedora.org>
                distribution in which to find the build that is compared
                against the baseline specified by option --from.  The distro
                value could be any valid value of the RPM macro %{?dist} for
                Fedora <https://getfedora.org>, for example, fc4, fc23.

              • --topurl <URL>

                Specifies the URL of the package store the tool downloads
                RPMs from.  The default value of this option is
                <https://kojipkgs.fedoraproject.org>.

              • --traceback

                Show traceback when an exception raised. This is useful for
                developers of the tool itself to know more exceptional
                errors.

           Note that a build is a specific version and release of an RPM
           package.  It's specified by its the package name, version and
           release. These are specified by the Fedora Naming Guidelines
           <https://fedoraproject.org/wiki/Packaging:NamingGuidelines>

       Return value
           The exit code of the abipkgdiff command is either 0 if the ABI of
           the binaries compared are equivalent, or non-zero if they differ
           or if the tool encountered an error.

           In the later case, the value of the exit code is the same as for
           the abidiff tool <#abidiff-return-value-label>.

       Use cases
           Below are some usage examples currently supported by
           fedabipkgdiff.

              1. Compare the ABI of binaries in a local package against the
                 ABI of the latest stable package in Fedora
                 <https://getfedora.org> 23.

                 Suppose you have built just built the httpd package and you
                 want to compare the ABI of the binaries in this locally
                 built package against the ABI of the binaries in the latest
                 http build from Fedora <https://getfedora.org> 23.  The
                 command line invocation would be:

                     $ fedabipkgdiff --from fc23 ./httpd-2.4.18-2.fc24.x86_64.rpm

              2. Compare the ABI of binaries in two local packages.

                 Suppose you have built two versions of package httpd, and
                 you want to see what ABI differences between these two
                 versions of RPM files. The command line invocation would be:

                     $ fedabipkgdiff path/to/httpd-2.4.23-3.fc23.x86_64.rpm another/path/to/httpd-2.4.23-4.fc24.x86_64.rpm

                 All what fedabipkgdiff does happens on local machine without
                 the need of querying or downloading RPMs from Koji.

              3. Compare the ABI of binaries in the latest build of the httpd
                 package in Fedora 23 against the ABI of the binaries in the
                 latest build of the same package in 24.

                 In this case, note that neither of the two packages are
                 available locally.  The tool is going to talk with the
                 Fedora Build System <http://koji.fedoraproject.org/koji>,
                 determine what the versions and releases of the latest
                 packages are, download them and perform the comparison
                 locally.  The command line invocation would be:

                     $ fedabipkgdiff --from fc23 --to fc24 httpd

              4. Compare the ABI of binaries of two builds of the httpd
                 package, designated their versions and releases.

                 If we want to do perform the ABI comparison for all the
                 processor architectures supported by Fedora
                 <https://getfedora.org> the command line invocation would
                 be:

                     $ fedabipkgdiff httpd-2.8.14.fc23 httpd-2.8.14.fc24

                 But if we want to perform the ABI comparison for a specific
                 architecture, say, x86_64, then the command line invocation
                 would be:

                     $ fedabipkgdiff httpd-2.8.14.fc23.x86_64 httpd-2.8.14.fc24.x86_64

              5. If the use wants to also compare the sub-packages of a given
                 package, she can use the --all-subpackages option.  The
                 first command of the previous example would thus look like:

                     $ fedabipkgdiff --all-subpackages httpd-2.8.14.fc23 httpd-2.8.14.fc24

## [](#Author)Author

           Dodji Seketeli

## [](#Copyright)Copyright

           2014-2025, Red Hat, Inc.

## [](#COLOPHON)COLOPHON

           This page is part of the libabigail (ABI Generic Analysis and
           Instrumentation Library) project.  Information about the project
           can be found at ⟨https://sourceware.org/libabigail/⟩.  If you have
           a bug report for this manual page, see
           ⟨http://sourceware.org/bugzilla/enter_bug.cgi?product=libabigail⟩.
           This page was obtained from the project's upstream Git repository
           ⟨git://sourceware.org/git/libabigail.git⟩ on 2026-08-04.  (At that
           time, the date of the most recent commit that was found in the
           repository was 2026-07-31.)  If you discover any rendering
           problems in this HTML version of the page, or you believe there is
           a better or more up-to-date source for the page, or you have
           corrections or improvements to the information in this COLOPHON
           (which is not part of the original manual page), send a mail to
           man-pages@man7.org

                                   Aug 03, 2026                 LIBABIGAIL(7)

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
