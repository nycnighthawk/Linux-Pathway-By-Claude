---
{"title": "rpm-dependency-generators(7) — Linux manual page", "url": "https://man7.org/linux/man-pages/man7/rpm-dependency-generators.7.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# rpm-dependency-generators(7) --- Linux manual page

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [FILE ATTRIBUTES](#FILE_ATTRIBUTES) \| [GENERATORS](#GENERATORS) \| [PER-PACKAGE TUNABLES](#PER-PACKAGE_TUNABLES) \| [TROUBLESHOOTING](#TROUBLESHOOTING) \| [EXAMPLES](#EXAMPLES) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                                                                                              |                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    RPM-DE...ERATORS(7)  Miscellaneous Information Manual RPM-DE...ERATORS(7)

## [](#NAME)NAME

           rpm-dependency-generators - RPM file attribute and dependency
           generator interface

## [](#SYNOPSIS)SYNOPSIS

       File attributes
           %__NAME_path PATH_RE
           %__NAME_magic MAGIC_RE
           %__NAME_mime MIME_RE

           %__NAME_exclude_path PATH_RE
           %__NAME_exclude_magic MAGIC_RE
           %__NAME_exclude_mime MIME_RE

           %__NAME_flags FLAG[,FLAG ...]
           %__NAME_exclude_flags FLAG[,FLAG ...]

       Generators
           %__NAME_​TYPE COMMAND
           %__NAME_​TYPE() BODY

           %__NAME_protocol {singlefile|multifile}

       Per-package tunables
           %_local_file_attrs NAME[:NAME ...]
           %__TYPE_exclude DEPSTRING_RE
           %__TYPE_exclude_from PATH_RE
           %__NAME_​TYPE_opts OPTS

       Notes
           TYPE can be one of conflicts, enhances, obsoletes,
           orderwithrequires, provides, recommends, requires, suggests and
           supplements. FLAG can be one of exeonly and magic_and_path.

## [](#DESCRIPTION)DESCRIPTION

           RPM uses a pluggable interface coupled with a file classifier to
           add dependency information to packages at build time. This system
           relies on specialized executables, called generators, that do the
           heavy-lifting of extracting dependencies from files in their
           domain, called a file attribute. It complements the manual tags,
           such as Requires or Provides, in rpm-spec(5) files.

## [](#FILE_ATTRIBUTES)FILE ATTRIBUTES

           A file attribute is a logical label that RPM gives to one or more
           files in the buildroot, based on a set of matching rules and their
           tunables, defined as macros. It can represent a single file type,
           such as ELF, or a broader domain, such as all files installed into
           a specific location or written in a specific programming language.

           These attributes are distinct from the file attributes in the
           filesystem and are only kept in memory during package builds. A
           single file may have an arbitrary number of attributes, and a
           single attribute may be assigned to an arbitrary number of files.

           To introduce a file attribute called NAME for use during package
           builds, drop an rpm-macrofile(5) named NAME.attr into the
           %{_fileattrsdir} directory. The file should define at least one of
           the matching rules described below.

       Matching rules
           %__NAME_path PATH_RE
               Match regex(7) string PATH_RE, macro-expanded on use, against
               filenames without the %{buildroot} prefix (for example,
               /bin/bash).

           %__NAME_magic MAGIC_RE
               Match regex(7) string MAGIC_RE, macro-expanded on use, against
               file magic(5).

               To determine a compatible MAGIC_RE, use the command:
                   file -z -e tokens /some/file

           %__NAME_mime MIME_RE
               Match regex(7) string MIME_RE, macro-expanded on use, against
               MIME file types.

               To determine a compatible MIME_RE, use the command:
                   file --mime /some/file

           %__NAME_exclude_path PATH_RE
           %__NAME_exclude_magic MAGIC_RE
           %__NAME_exclude_mime MIME_RE
               Filter out files matching the given regex(7). These rules are
               the exclusion counterparts of the above inclusion rules.

           Matching is inclusive unless changed by flags (see below): If the
           path, magic or both match, the file is said to have the attribute
           in question, unless there is a matching exclusion rule (also
           inclusive by default) or a flag that prevents the match. If both
           the magic and mime rules are defined, the magic rule is ignored
           and a warning is printed.

       Tunables
           %__NAME_flags FLAGS
           %__NAME_exclude_flags FLAGS
               Tweak the inclusion and exclusion rules, respectively.

               FLAGS is a comma-separated list of the following possible
               values:
               •   exeonly: require executable bit set
               •   magic_and_path: require both magic and path to match

## [](#GENERATORS)GENERATORS

           A generator is an executable that reads filenames from standard
           input and writes dependencies of a single type to standard output,
           according to a protocol. It is written for a specific file
           attribute and defined as a macro in the respective NAME.attr file.
           Zero or more generators, one for each supported type, can be
           defined for a single file attribute.

       Generator macros
           %__NAME_conflicts COMMAND
           %__NAME_enhances COMMAND
           %__NAME_obsoletes COMMAND
           %__NAME_orderwithrequires COMMAND (Added: 4.17.0)
           %__NAME_provides COMMAND
           %__NAME_recommends COMMAND
           %__NAME_requires COMMAND
           %__NAME_suggests COMMAND
           %__NAME_supplements COMMAND
               Generate dependencies of the respective type. Executes COMMAND
               (a program name and any arguments), passing it one or more
               filenames that have the file attribute NAME on standard input,
               and reads dependency strings on its standard output. See
               Protocols for details on the input and output format.

       Protocols
           %__NAME_protocol PROTOCOL
               Use PROTOCOL when running dependency generators for the file
               attribute NAME. Determines the standard input and standard
               output format for the generators to implement.

               PROTOCOL can be one of the following:

               singlefile
                   •   stdin: one matching filename at a time
                   •   stdout: dependency strings, one per line

               multifile
                   •   stdin: all matching filenames at once, one per line
                   •   stdout: dependency strings, one per line, with the
                       original filename, prepended with ; (semicolon),
                       printed on its own line before the dependencies for
                       that file (Added: 4.20.0)

               If this macro is not defined, the singlefile protocol will be
               used. For newly written generators, the multifile protocol is
               recommended since it's more performant.

           Unlike the PATH_RE in file attributes, generators receive
           filenames with the %{buildroot} prefix so that they can access the
           actual file contents on disk.

           Generators must always consume all of standard input. For
           backwards compatibility, generators should not make any
           assumptions about the number of files passed, regardless of the
           protocol used.

       Exported macros
           In addition to globally defined macros, the following macros are
           automatically exported to generators, on a subpackage basis:

           •   %{name}
           •   %{epoch}
           •   %{version}
           •   %{release}

           Added: 4.15.0

       Parametric generators
           If a generator is declared as a parametric macro, the macro itself
           is called for dependency generation, with the filename as its
           first argument (%1). The macro expansion itself is considered as
           the generated dependencies, one per line.

           The following trivial example creates provides from path
           basenames, which is enormously faster than the equivalent
           traditional generator shelling out to execute a script that calls
           basename(1):

               %__foo_provides()   %{basename:%{1}}

           While RPM's own macro primitives are limited, using %{lua} enables
           the writing of complicated, macro-only generators.

           See PARAMETRIC MACROS and Lua expansion in rpm-macros(7) for
           details.

           Added: 4.16.0

       External generators
           %__find_​TYPE COMMAND
               Generate dependencies of the respective TYPE. Executes COMMAND
               (a program name and any arguments), passing it the entire file
               list of the package at once, and reads dependency strings on
               its standard output. See Generator macros for the possible
               TYPE values.

           This is a legacy, deprecated interface that's only available for
           v4 packages for backwards compatibility, and should not be used.
           Packages built this way contain less data about their files, such
           as no "color" information (which is vital for RPM's functionality
           on multiarch systems), file type information or per-file
           dependency tracking.

           To enable this interface regardless, define the macro:
               %_use_internal_dependency_generator 0

## [](#PER-PACKAGE_TUNABLES)PER-PACKAGE TUNABLES

           The following macros can be used on a per-package basis, either by
           defining them directly in the rpm-spec(5) file or by passing them
           to rpmbuild(1) via the --define option:

           %_local_file_attrs NAMES
               Register file attribute NAMES (separated by colons) for the
               duration of the build. The respective file attribute and
               generator macros must be defined separately.

               This is useful for running generators shipped by the package
               itself.

               Added: 4.20.0

           %__TYPE_exclude DEPSTRING_RE
               Filter out unwanted dependencies of TYPE by matching regex(7)
               string DEPSTRING_RE, macro-expanded on use, against dependency
               strings. See Generator macros for the possible TYPE values.

               Example:
                   %define __requires_exclude ^lib.*$

           %__TYPE_exclude_from PATH_RE
               Filter out unwanted dependencies of TYPE by matching regex(7)
               string PATH_RE, macro-expanded on use, against filenames
               without the %{buildroot} prefix (for example, /bin/bash). See
               Generator macros for the possible TYPE values.

               Example:
                   %define __provides_exclude_from ^%{_libdir}/mypkg/.*.so$

           %__NAME_​TYPE_opts OPTS
               Pass additional command line switches to the TYPE generator.
               See Generator macros for the possible TYPE values.

               Note that this macro should NOT be used when writing a file
               attribute file. Instead, just pass the required arguments
               directly on the generator's command line when defining it.

## [](#TROUBLESHOOTING)TROUBLESHOOTING

       Displaying debug information
           The rpmbuild(1) and rpmdeps(1) tools have a hidden --rpmfcdebug
           switch that enables additional output for the dependency
           generation stage. The output format is currently roughly as
           follows:

               <file number> <on-disk path> <color info> <file attribute matches>
                   <list of dependencies associated with this file>

           File attribute matches are the names of the rules that matched for
           the file, and that is where rule troubleshooting typically starts:
           a file with no attributes will not have any dependencies attached.

       Global excludes
           Global variants of the per-package exclusion macros may also be
           defined on the system:

           %__global_​TYPE_exclude DEPSTRING_RE
           %__global_​TYPE_exclude_from PATH_RE

           These apply to all package builds and thus may affect the output
           of a particular generator in unexpected ways. Make sure to inspect
           the contents of these macros if that's the case.

## [](#EXAMPLES)EXAMPLES

       Example 1. A trivial multifile generator
           Suppose there's a %{_fileattrsdir}/frob.attr file with the
           following contents:

               %__frob_provides %{_rpmconfigdir}/frobnize --provides
               %__frob_requires %{_rpmconfigdir}/frobnize --requires
               %__frob_protocol multifile
               %__frob_path \.frob$
               %__frob_magic ^.* a frob file .*$

           This file defines a file attribute called frob that has two
           generators, both of which use a frobnize script that implements
           the multifile protocol. The file attribute matches all files with
           the .frob suffix as well as those that contain the "a frob file"
           magic string.

           The %{_rpmconfigdir}/frobnize script has the following contents:

               #!/bin/bash
               # Frob dependency extractor

               # Type of dependency strings to print
               mode=$1

               # Process every file on standard input
               while read -r file; do
                   # Print currently processed file as per multifile protocol
                   echo ";$file"

                   # Get basename and first line
                   name=$(basename $file | cut -f1 -d.)
                   line=$(head -n1 $file)

                   # Print dependency strings
                   case $mode in
                      --provides)
                          echo "frob($name)"
                          echo "frob($line)"
                          ;;
                      --requires)
                          echo "bard($name)"
                          echo "bard($line)"
                          ;;
                   esac
               done

           Now, suppose there's a frob.spec file that installs the file
           hello.frob with the contents "world" to some location on the
           filesystem. When the spec is built, the resulting package will
           have the following provides and requires:

               $ rpmbuild -bb /path/to/frob.spec
               ...
               $ rpm -qp --provides --requires /path/to/frob.rpm
               ...
               frob(hello)
               frob(world)
               bard(hello)
               bard(world)
               ...

           If multiple files with the .frob suffix or "a frob file" magic
           were present in the package, the frobnize script would only be
           executed once, with all the matching filenames passed at once.

           Note that if the generator decided to break from the while loop,
           it would have to discard any remaining input prior to exiting, as
           per protocol, which could be done with the following command
           placed after the loop:

               cat > /dev/null

       Example 2. Spec-local generators
           This spec file snippet introduces two spec-local file attributes,
           frob and bard, that match any and all files, and their generators
           that use a frobnize and bardize.sh script shipped by the package
           itself and only included with the sources, respectively:

               ...
               Source1: bardize.sh
               ...
               %define _local_file_attrs frob:bard
               %define __frob_provides %{buildroot}/%{_rpmconfigdir}/frobnize
               %define __frob_path .*
               %define __bard_provides %{SOURCE1}
               %define __bard_path .*
               ...

       Example 3. Bundled file attributes and generators
           %{_fileattrsdir}/*.attr
           %{_rpmconfigdir}/*.req
           %{_rpmconfigdir}/*.prov
               A small, curated set of file attributes and their generators
               bundled with RPM itself. These cover the core domains on a
               UNIX/Linux system, such as ELF binaries, executable scripts or
               sysusers.d(5) files.

## [](#SEE_ALSO)SEE ALSO

           rpm(8) rpm-common(8) rpmbuild(1) rpmbuild-config(5) rpmdeps(1)
           rpm-spec(5) file(1) magic(5)

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

    RPM 6.1.90                      2026-08-03            RPM-DE...ERATORS(7)

------------------------------------------------------------------------

Pages that refer to this page: [elfdeps(1)](../man1/elfdeps.1.html),  [rpmbuild(1)](../man1/rpmbuild.1.html),  [rpm-spec(5)](../man5/rpm-spec.5.html),  [rpm-sysusers(7)](../man7/rpm-sysusers.7.html)

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
