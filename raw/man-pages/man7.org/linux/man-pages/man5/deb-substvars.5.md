---
{"title": "deb-substvars(5) — Linux manual page", "url": "https://man7.org/linux/man-pages/man5/deb-substvars.5.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# deb-substvars(5) --- Linux manual page

+--------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [FILES](#FILES) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                            |                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    deb-substvars(5)                dpkg suite               deb-substvars(5)

## [](#NAME)NAME

           deb-substvars - Debian source substitution variables

## [](#SYNOPSIS)SYNOPSIS

           debian/substvars, debian/binary-package.substvars, variables

## [](#DESCRIPTION)DESCRIPTION

           Before dpkg-source, dpkg-gencontrol and dpkg-genchanges write
           their control information (to the source control file .dsc for
           dpkg-source and to standard output for dpkg-gencontrol and
           dpkg-genchanges) they perform some variable substitutions on the
           output file.

       Variable Syntax
           A variable substitution has the form ${variable-name}.  Variable
           names consist of alphanumerics (a-zA-Z0-9), hyphens (-) and colons
           (:) and start with an alphanumeric, and are case-sensitive, even
           though they might refer to other entities which are
           case-preserving.  Variable substitutions are performed repeatedly
           until none are left; the full text of the field after the
           substitution is rescanned to look for more substitutions.

       File Syntax
           Substitution variables can be specified in a file.  These files
           consist of lines with variable assignments, that start with the
           variable name, immediately followed by an assignment operator, and
           then the value.  Each operator gives the variable specific
           attributes.  Trailing whitespace on each line, blank lines, and
           lines starting with a # symbol (comments) are ignored.

           The following operators are supported:

           =   Assigns a normal substitution variable.

           ?=  Assigns an optional substitution variable which will emit no
               warnings even if unused.

               Supported since dpkg 1.21.8.

           !=  Assigns a required substitution variable which will error out
               if unused.

               Supported since dpkg 1.22.7.

           $=  Assigns an implicit substitution variable which will get
               automatically instantiated as a field, if that field is not
               defined for .dsc and .deb control files.

               The variable name needs to be formed as a namespace followed
               by a colon (‘:’) and then the field name, such as
               tool:Depends.  All implicit variables for any namespace
               matching the same field will get concatenated using a known
               field separator, or a space if the field separator is unknown.

               Supported since dpkg 1.23.0.

           For example "some-package:Depends?=other-package (= 1.0),
           the-package".

       Substitution
           Variables can be set using the -V common option.  They can be also
           specified in the file debian/substvars (or whatever other file is
           specified using the -T common option).

           After all the substitutions have been done each occurrence of the
           string ${} (which is not an actual substitution variable) is
           replaced with a $ sign.  This can be used as an escape sequence
           such as ${}{VARIABLE} which will end up as ${VARIABLE} on the
           output.

           If a variable is referred to but not defined it generates a
           warning and an empty value is assumed.

           While variable substitution is done on all control fields, some of
           those fields are used and needed during the build when the
           substitution did not yet occur.  That's why you can't use
           variables in the Package, Source and Architecture fields.

           Variable substitution happens on the content of the fields after
           they have been parsed, thus if you want a variable to expand over
           multiple lines you do not have to include a space after the
           newline.  This is done implicitly when the field is output.  For
           example, if the variable ${Description} is set to "foo is
           bar.${Newline}foo is great." and if you have the following field:

            Description: foo application
             ${Description}
             .
             More text.

           It will result in:

            Description: foo application
             foo is bar.
             foo is great.
             .
             More text.

       Built-in Variable
           Additionally, the following standard variables are always
           available:

           Arch
               The current host architecture (i.e. the architecture the
               package is being built for, the equivalent of DEB_HOST_ARCH).

           vendor:Name
               The current vendor name.  This value comes from the Vendor
               field for the current vendor's origin file, as dpkg-vendor(1)
               would retrieve it.

               Supported since dpkg 1.20.0.

           vendor:Id
               The current vendor ID.  This is just the lowercase variant of
               vendor:Name.

               Supported since dpkg 1.20.0.

           source:Version
               The source package version.

               Supported since dpkg 1.13.19.

           source:Upstream-Version
               The upstream source package version, including the Debian
               version epoch if any.

               Supported since dpkg 1.13.19.

           binary:Version
               The binary package version (which may differ from
               source:Version in a binNMU for example).

               Supported since dpkg 1.13.19.

           Source-Version
               The source package version (from the changelog file).  This
               variable is now obsolete and emits an error when used as its
               meaning is different from its function, use the source:Version
               or binary:Version as appropriate.

           source:Synopsis
               The source package synopsis, extracted from the source stanza
               Description field, if it exists.

               Supported since dpkg 1.19.0.

           source:Extended-Description
               The source package extended description, extracted from the
               source stanza Description field, if it exists.

               Supported since dpkg 1.19.0.

           Installed-Size
               The approximate total size of the package's installed files.
               This value is copied into the corresponding control file
               field; setting it will modify the value of that field.  If
               this variable is not set dpkg-gencontrol will compute the
               default value by accumulating the size of each regular file
               and symlink rounded to 1 KiB used units, and a baseline of 1
               KiB for any other filesystem object type.  With hardlinks only
               being counted once as a regular file.

               Note: Take into account that this can only ever be an
               approximation, as the actual size used on the installed system
               will depend greatly on the filesystem used and its parameters,
               which might end up using either more or less space than the
               specified in this field.

           Extra-Size
               Additional disk space used when the package is installed.  If
               this variable is set its value is added to that of the
               Installed-Size variable (whether set explicitly or using the
               default value) before it is copied into the Installed-Size
               control file field.

           S:field-name
               The value of the source stanza field field-name (which must be
               given in the canonical capitalization).  Setting these
               variables has no effect other than on places where they are
               expanded explicitly.  These variables are only available when
               generating binary control files.

               Supported since dpkg 1.18.11.

           F:field-name
               The value of the output field field-name (which must be given
               in the canonical capitalization).  Setting these variables has
               no effect other than on places where they are expanded
               explicitly.

           Format
               The .changes file format version generated by this version of
               the source packaging scripts.  If you set this variable the
               contents of the Format field in the .changes file will change
               too.

           Newline, Space, Tab
               These variables each hold the corresponding character.

           shlibs:dependencyfield
               Variable settings with names of this form are generated by
               dpkg-shlibdeps.

           dpkg:Upstream-Version
               The upstream version of dpkg.

               Supported since dpkg 1.13.19.

           dpkg:Version
               The full version of dpkg.

               Supported since dpkg 1.13.19.

## [](#FILES)FILES

           debian/substvars
               List of substitution variables and values.

## [](#SEE_ALSO)SEE ALSO

           dpkg(1), dpkg-vendor(1), dpkg-genchanges(1), dpkg-gencontrol(1),
           dpkg-shlibdeps(1), dpkg-source(1).

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

    1.23.7-216-gff7e9               2026-03-07               deb-substvars(5)

------------------------------------------------------------------------

Pages that refer to this page: [dpkg-genchanges(1)](../man1/dpkg-genchanges.1.html),  [dpkg-gencontrol(1)](../man1/dpkg-gencontrol.1.html),  [dpkg-shlibdeps(1)](../man1/dpkg-shlibdeps.1.html),  [dpkg-source(1)](../man1/dpkg-source.1.html),  [deb-control(5)](../man5/deb-control.5.html)

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
