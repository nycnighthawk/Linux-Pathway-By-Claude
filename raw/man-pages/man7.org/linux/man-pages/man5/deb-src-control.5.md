---
{"title": "deb-src-control(5) — Linux manual page", "url": "https://man7.org/linux/man-pages/man5/deb-src-control.5.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# deb-src-control(5) --- Linux manual page

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [SOURCE FIELDS](#SOURCE_FIELDS) \| [BINARY FIELDS](#BINARY_FIELDS) \| [USER-DEFINED FIELDS](#USER-DEFINED_FIELDS) \| [EXAMPLE](#EXAMPLE) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                                                     |                                   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    deb-src-control(5)              dpkg suite             deb-src-control(5)

## [](#NAME)NAME

           deb-src-control - Debian source package template control file
           format

## [](#SYNOPSIS)SYNOPSIS

           debian/control

## [](#DESCRIPTION)DESCRIPTION

           Each Debian source package contains the «debian/control» template
           source control file, and its deb822(5) format is a superset of the
           control file shipped in Debian binary packages, see
           deb-control(5).

           This file contains at least 2 stanzas, separated by a blank line.
           The first stanza is called the source package stanza and lists all
           information about the source package in general, while each
           following stanzas are called the binary package stanzas and
           describe exactly one binary package per stanza.  Each stanza
           consists of at least one field.  A field starts with a field name,
           such as Package or Section (case insensitive), followed by a
           colon, the body of the field (case sensitive unless stated
           otherwise) and a newline.  Multi-line fields are also allowed, but
           each supplementary line, without a field name, must start with at
           least one space.  The content of the multi-line fields is
           generally joined to a single line by the tools (except in the case
           of the Description field, see below).  To insert empty lines into
           a multi-line field, insert a dot after the space.  Lines starting
           with a ‘#’ are treated as comments.

## [](#SOURCE_FIELDS)SOURCE FIELDS

           Source: source-package-name (required)
               The value of this field is the name of the source package, and
               must match the name of the source package in the
               debian/changelog file.  A package name must consist only of
               lowercase letters (a-z), digits (0-9), plus (+) and minus (-)
               signs, and periods (.).  Package names must be at least two
               characters long and must start with a lowercase alphanumeric
               character (a-z0-9).

           Maintainer: fullname-email (recommended)
               Should be in the format «Joe Bloggs <jbloggs@foo.com>», and
               references the person who currently maintains the package, as
               opposed to the author of the software or the original
               packager.

               The format is described in deb-email(7).

           Uploaders: fullname-email
               Lists all the names and email addresses of co-maintainers of
               the package, in the same format as the Maintainer field.
               Multiple co-maintainers should be separated by a comma.

               The format is described in deb-email(7).

           Standards-Version: version-string
               This documents the most recent version of the distribution
               policy standards this package complies with.

           Description short-description
            long-description
               The format for the source package description is a short brief
               summary on the first line (after the Description field).  The
               following lines should be used as a longer, more detailed
               description.  Each line of the long description must be
               preceded by a space, and blank lines in the long description
               must contain a single ‘.’ following the preceding space.

           Homepage: url
               The upstream project home page URL.

           Bugs: url
               The url of the bug tracking system for this package.  The
               current used format is bts-type://bts-address, like
               debbugs://bugs.debian.org.  This field is usually not needed.

           Build-Driver: driver-name
               This experimental field specifies the name of the build driver
               to use to build this package.  When omitted the driver-name
               defaults to debian-rules.

               Supported since dpkg 1.22.7.

           Rules-Requires-Root: no|binary-targets|impl-keywords
               This field is used to indicate whether the debian/rules file
               requires (fake)root privileges to run some of its targets, and
               if so when.

               Supported since dpkg 1.19.0.

               no  The binary targets will not require (fake)root at all.
                   This is the default in dpkg-build-api level >= 1, or since
                   dpkg 1.22.13.

               binary-targets
                   The binary targets must always be run under (fake)root.
                   This value is the default in dpkg-build-api level 0 until
                   dpkg 1.22.13, when the field is omitted; adding the field
                   with an explicit binary-targets, while not strictly
                   needed, marks it as having been analyzed for this
                   requirement.

               impl-keywords
                   This is a space-separated list of keywords which define
                   when (fake)root is required.

                   Keywords consist of namespace/cases.  The namespace part
                   cannot contain "/" or whitespace.  The cases part cannot
                   contain whitespace.  Furthermore, both parts must consist
                   entirely of printable ASCII characters.

                   Each tool/package will define a namespace named after
                   itself and provide a number of cases where (fake)root is
                   required.  (See "Implementation provided keywords" in
                   rootless-builds.txt).

                   When the field is set to one of the impl-keywords, the
                   builder will expose an interface that is used to run a
                   command under (fake)root.  (See "Gain Root API" in
                   rootless-builds.txt.)

           Testsuite: name-list
           Testsuite-Triggers: package-list
               These fields are described in the dsc(5) manual page, as they
               are generated from information inferred from
               debian/tests/control or copied literally to the source control
               file.

           Vcs-Arch: url
           Vcs-Bzr: url
           Vcs-Cvs: url
           Vcs-Darcs: url
           Vcs-Git: url
           Vcs-Hg: url
           Vcs-Mtn: url
           Vcs-Svn: url
               The url of the Version Control System repository used to
               maintain this package.  Currently supported are Arch, Bzr
               (Bazaar), Cvs, Darcs, Git, Hg (Mercurial), Mtn (Monotone) and
               Svn (Subversion).  Usually this field points to the latest
               version of the package, such as the main branch or the trunk.

           Vcs-Browser: url
               The url of a web interface to browse the Version Control
               System repository.

           Origin: name
               The name of the distribution this package is originating from.
               This field is usually not needed.

           Section: section
               This is a general field that gives the package a category
               based on the software that it installs.  Some common sections
               are utils, net, mail, text, x11, etc.

               When omitted, the section defaults to unknown (since dpkg
               1.22.13).

               The accepted values are based on the specific distribution
               policy.

           Priority: priority
               Sets the importance of this package in relation to the system
               as a whole.  The known priorities are required, important,
               standard, optional, extra, and unknown, but other values can
               be used as well.

               When omitted, the priority defaults to optional (since dpkg
               1.22.13).

               How to apply these values depends on the specific distribution
               policy.

           Build-Depends: package-list
               A list of packages that need to be installed and configured to
               be able to build from source package.  These dependencies need
               to be satisfied when building binary architecture dependent or
               independent packages and source packages.  Including a
               dependency in this field does not have the exact same effect
               as including it in both Build-Depends-Arch and
               Build-Depends-Indep, because the dependency also needs to be
               satisfied when building the source package.

           Build-Depends-Arch: package-list
               Same as Build-Depends, but they are only needed when building
               the architecture dependent packages.  The Build-Depends are
               also installed in this case.

               Supported since dpkg 1.16.4; in order to build with older dpkg
               versions, Build-Depends should be used instead.

           Build-Depends-Indep: package-list
               Same as Build-Depends, but they are only needed when building
               the architecture independent packages.  The Build-Depends are
               also installed in this case.

           Build-Conflicts: package-list
               A list of packages that should not be installed when the
               package is built, for example because they interfere with the
               build system used.  Including a dependency in this list has
               the same effect as including it in both Build-Conflicts-Arch
               and Build-Conflicts-Indep, with the additional effect of being
               used for source-only builds.

           Build-Conflicts-Arch: package-list
               Same as Build-Conflicts, but only when building the
               architecture dependent packages.

               Supported since dpkg 1.16.4; in order to build with older dpkg
               versions, Build-Conflicts should be used instead.

           Build-Conflicts-Indep: package-list
               Same as Build-Conflicts, but only when building the
               architecture independent packages.

           The syntax of the Build-Depends, Build-Depends-Arch and
           Build-Depends-Indep fields is a list of groups of alternative
           packages.  Each group is a list of packages separated by vertical
           bar (or “pipe”) symbols, ‘|’.  The groups are separated by commas
           ‘,’, and can end with a trailing comma that will be eliminated
           when generating the fields for deb-control(5) (since dpkg
           1.10.14).  Commas are to be read as “AND”, and pipes as “OR”, with
           pipes binding more tightly.  Each package name is optionally
           followed by an architecture qualifier appended after a colon ‘:’,
           optionally followed by a version number specification in
           parentheses ‘(’ and ‘)’, an architecture specification in square
           brackets ‘[’ and ‘]’, and a restriction formula consisting of one
           or more lists of profile names in angle brackets ‘<’ and ‘>’.

           The syntax of the Build-Conflicts, Build-Conflicts-Arch and
           Build-Conflicts-Indep fields is a list of comma-separated package
           names, where the comma is read as an “AND”, and where the list can
           end with a trailing comma that will be eliminated when generating
           the fields for deb-control(5) (since dpkg 1.10.14).  Specifying
           alternative packages using a “pipe” is not supported.  Each
           package name is optionally followed by a version number
           specification in parentheses, an architecture specification in
           square brackets, and a restriction formula consisting of one or
           more lists of profile names in angle brackets.

           An architecture qualifier name can be a real Debian architecture
           name (since dpkg 1.16.5), any (since dpkg 1.16.2) or native (since
           dpkg 1.16.5).  If omitted, the default for Build-Depends fields is
           the current host architecture, the default for Build-Conflicts
           fields is any.  A real Debian architecture name will match exactly
           that architecture for that package name, any will match any
           architecture for that package name if the package is marked with
           Multi-Arch: allowed, and native will match the current build
           architecture if the package is not marked with Multi-Arch:
           foreign.

           A version number may start with a ‘>>’, in which case any later
           version will match, and may specify or omit the Debian packaging
           revision (separated by a hyphen).  Accepted version relationships
           are ‘>>’ for greater than, ‘<<’ for less than, ‘>=’ for greater
           than or equal to, ‘<=’ for less than or equal to, and ‘=’ for
           equal to.

           An architecture specification consists of one or more architecture
           names, separated by whitespace.  Exclamation marks (!) may be
           prepended to each of the names, meaning “NOT”.

           A restriction formula consists of one or more restriction lists,
           separated by whitespace.  Each restriction list is enclosed in
           angle brackets (< and >).  Items in the restriction list are build
           profile names, separated by whitespace and can be prefixed with an
           exclamation mark (!), meaning “NOT”.  A restriction formula
           represents a disjunctive normal form expression, that is
           whitespace inside enclosed angle brackets is read as “AND”, and
           whitespace between enclosing angle brackets is read as “OR“, such
           as “<foo AND bar> OR <quux AND baz>”.

           Note that dependencies on packages in the build-essential set can
           be omitted and that declaring build conflicts against them is
           impossible.  A list of these packages is in the build-essential
           package.

## [](#BINARY_FIELDS)BINARY FIELDS

           Package: binary-package-name (required)
               This field is used to name the binary package name.  The same
               restrictions as to a source package name apply.

           Package-Type: deb|udeb|type
               This field defines the type of the package.  udeb is for
               size-constrained packages used by the debian installer.  deb
               is the default value, it is assumed if the field is absent.
               More types might be added in the future.

           Architecture: arch-list (required)
               The architecture list specifies on which type of machine this
               package runs.  The value should be a list of architecture
               names and/or wildcards separated by spaces.

               The special all value, by itself, is meant for packages that
               are architecture independent (such as shell and Perl scripts
               or documentation), the special any wildcard value, by itself,
               is meant for packages that are architecture dependent but run
               on all architectures (which matches on all specific
               architecture names, excluding all).  Most packages will use
               either all or any.  To restrict the packages to a certain set
               of architectures, specify one or more architecture names
               and/or architecture wildcards, separated by spaces.

               An architecture name or wildcard must start with an
               alphanumeric character (“0-9a-zA-Z”), and then gets followed
               by alphanumeric and dash (”-”) characters.

               For more information about architecture names and wildcards,
               see dpkg-architecture(1).

           Build-Profiles: restriction-formula
               This field specifies the conditions for which this binary
               package does or does not build.  To express that condition,
               the same restriction formula syntax from the Build-Depends
               field is used (including the angle brackets).

               If a binary package stanza does not contain this field, then
               it implicitly means that it builds with all build profiles
               (including none at all).

               In other words, if a binary package stanza is annotated with a
               non-empty Build-Profiles field, then this binary package is
               generated if and only if the condition expressed by the
               conjunctive normal form expression evaluates to true.

           Protected: yes|no
           Essential: yes|no
           Build-Essential: yes|no
           Multi-Arch: same|foreign|allowed|no
           Tag: tag-list
           Description: short-description (recommended)
               These fields are described in the deb-control(5) manual page,
               as they are copied literally to the control file of the binary
               package.

           Section: section
               Overrides the value from the same field in the source package
               stanza.

               If there is no field in the binary or source stanza, then the
               it defaults to unknown (since dpkg 1.22.13).

           Priority: priority
               Overrides the value from the same field in the source package
               stanza.

               If there is no field in the binary or source stanza, then the
               it defaults to optional (since dpkg 1.22.13).

           Homepage: url
               Overrides the value from the same field in the source package
               stanza.

           Depends: package-list
           Pre-Depends: package-list
           Recommends: package-list
           Suggests: package-list
           Breaks: package-list
           Enhances: package-list
           Replaces: package-list
           Conflicts: package-list
           Provides: package-list
           Built-Using: package-list
           Static-Built-Using: package-list
               These fields declare relationships between packages.  They are
               discussed in the deb-control(5) manual page.  When these
               fields are found in debian/control they can also end with a
               trailing comma (since dpkg 1.10.14), have architecture
               specifications and restriction formulas which will all get
               reduced when generating the fields for deb-control(5).

           Subarchitecture: value
           Kernel-Version: value
           Installer-Menu-Item: value
               These fields are used by the debian-installer in udebs and are
               usually not needed.  For more details about them, see
               <https://salsa.debian.org/installer-team/debian-installer/-/raw/master/doc/devel/modules.txt>.

## [](#USER-DEFINED_FIELDS)USER-DEFINED FIELDS

           It is allowed to add additional user-defined fields to the control
           file.  The tools will ignore these fields.  If you want the fields
           to be copied over to the output files, such as the binary
           packages, you need to use a custom naming scheme: the fields
           should start with an X, followed by zero or more of the letters
           SBC and a hyphen.

           S   The field will appear in the source package control file, see
               dsc(5).

               Only expected in the source package stanza.

           B   The field will appear in the control file in the binary
               package, see deb-control(5).

               Allowed in the source package stanza or any binary package
               stanza.

           C   The field will appear in the upload control (.changes) file,
               see deb-changes(5).

               Only expected in the source package stanza.

           Note that the X[SBC]- prefixes are stripped when the fields are
           copied over to the output files.  A field XC-Approved-By will
           appear as Approved-By in the changes file and will not appear in
           the binary or source package control files.

           Take into account that these user-defined fields will be using the
           global namespace, which might at some point in the future collide
           with officially recognized fields.  To avoid such potential
           situation you can prefix those fields with Private-, such as
           XB-Private-New-Field.

## [](#EXAMPLE)EXAMPLE

            # Comment.
            Source: dpkg
            Section: admin
            Priority: required
            Maintainer: Dpkg Developers <debian-dpkg@lists.debian.org>
            # This field is copied to the binary and source packages.
            XBS-Upstream-Release-Status: stable
            Homepage: https://wiki.debian.org/Teams/Dpkg
            Vcs-Browser: https://git.dpkg.org/cgit/dpkg/dpkg.git
            Vcs-Git: https://git.dpkg.org/git/dpkg/dpkg.git
            Standards-Version: 4.7.4
            Build-Depends:
             dpkg-build-api (= 1),
             debhelper-compat (= 13),
             debhelper (>= 13.10~),
             pkgconf,
             libselinux1-dev (>= 1.28-4) [!linux-any],

            Package: dpkg-dev
            Section: utils
            Priority: optional
            Architecture: all
            # This is a custom field in the binary package.
            XB-Mentoring-Contact: Raphael Hertzog <hertzog@debian.org>
            Depends:
             libdpkg-perl (= ${source:Version}),
             dpkg (>= 1.14.6),
             binutils,
             bzip2,
             xz-utils,
            # This is a comment in the middle of a field value.
             make,
             patch (>= 2.2-1),
             perl-modules,
             perl5,
            Recommends:
             build-essential,
             gcc | c-compiler,
            Suggests:
             debian-keyring,
            Conflicts:
             devscripts (<< 2.10.26),
            Replaces:
             manpages-pl (<= 20051117-1),
            Provides:
             dpkg-build-api (= 0),
             dpkg-build-api (= 1),
            Description: Debian package development tools
             This package provides the development tools (including dpkg-source)
             required to unpack, build and upload Debian source packages.
             .
             Most Debian source packages will require additional tools to build;
             for example, most packages need make and the C compiler gcc.

## [](#SEE_ALSO)SEE ALSO

           /usr/local/share/doc/dpkg/spec/rootless-builds.txt, deb822(5),
           deb-control(5), deb-email(7), deb-version(7), dpkg-source(1)

## [](#COLOPHON)COLOPHON

           This page is part of the dpkg (Debian Package Manager) project.
           Information about the project can be found at 
           ⟨https://wiki.debian.org/Teams/Dpkg/⟩.  If you have a bug report
           for this manual page, see
           ⟨http://bugs.debian.org/cgi-bin/pkgreport.cgi?src=dpkg⟩.  This
           page was obtained from the project's upstream Git repository ⟨git
           clone https://git.dpkg.org/git/dpkg/dpkg.git⟩ on 2026-08-03.  (At
           that time, the date of the most recent commit that was found in
           the repository was 2026-08-01.)  If you discover any rendering
           problems in this HTML version of the page, or you believe there is
           a better or more up-to-date source for the page, or you have
           corrections or improvements to the information in this COLOPHON
           (which is not part of the original manual page), send a mail to
           man-pages@man7.org

    1.23.7-216-gff7e9               2026-03-07             deb-src-control(5)

------------------------------------------------------------------------

Pages that refer to this page: [dpkg-genchanges(1)](../man1/dpkg-genchanges.1.html),  [dpkg-gencontrol(1)](../man1/dpkg-gencontrol.1.html),  [dpkg-source(1)](../man1/dpkg-source.1.html),  [deb-changes(5)](../man5/deb-changes.5.html),  [deb-control(5)](../man5/deb-control.5.html),  [dsc(5)](../man5/dsc.5.html),  [dpkg-build-api(7)](../man7/dpkg-build-api.7.html)

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
