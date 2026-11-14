---
{"title": "rpm-sysusers(7) — Linux manual page", "url": "https://man7.org/linux/man-pages/man7/rpm-sysusers.7.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# rpm-sysusers(7) --- Linux manual page

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [DEPENDENCIES](#DEPENDENCIES) \| [LIMITATIONS](#LIMITATIONS) \| [PORTABILITY](#PORTABILITY) \| [COMPATIBILITY](#COMPATIBILITY) \| [TECHNICAL DETAILS](#TECHNICAL_DETAILS) \| [TROUBLESHOOTING](#TROUBLESHOOTING) \| [EXAMPLES](#EXAMPLES) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                                                                                                                                                      |                                   |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    RPM-SYSUSERS(7)      Miscellaneous Information Manual     RPM-SYSUSERS(7)

## [](#NAME)NAME

           rpm-sysusers - RPM native allocation of users and groups through
           sysusers.d(5)

## [](#SYNOPSIS)SYNOPSIS

       Declaration
           %{_sysusersdir}/*.conf
           %{add_sysuser [-b] ENTRY}

       File format
           ENTRY
           # COMMENT

       Entry format
           u USERNAME UID GECOS HOMEDIR SHELL
           u USERNAME UID:GID GECOS HOMEDIR SHELL
           u USERNAME FILE GECOS HOMEDIR SHELL
           g GROUPNAME GID
           g GROUPNAME FILE
           m USERNAME GROUPNAME

       Notes
           •   Suffix u with an exclamation mark (!) to create a fully locked
               account (recommended)
           •   Use a dash (-) as UID/GID for automatic number allocation
               (recommended)
           •   FILE is an absolute path to a file whose UID/GID should be
               used

## [](#DESCRIPTION)DESCRIPTION

           RPM has native support for declarative user and group creation by
           integrating with the sysusers.d(5) format (introduced by systemd).
           Packagers only need to drop one or more files to
           /usr/lib/sysusers.d/ and RPM will handle the rest, such as
           dependency generation and the invocation of systemd-sysusers(8)
           during the build and installation, respectively.

           Vendors on non-systemd platforms can enable the feature by
           shipping any missing tools and configuring RPM accordingly (see
           PORTABILITY for details).

           Note that for certain types of systemd services (such as transient
           or socket activated), it may be possible to avoid package level
           user/group allocation altogether by using Dynamic Users (see
           DynamicUser= in systemd.exec(5) and the URL in SEE ALSO for
           details).

           Added: 4.19.0

## [](#DEPENDENCIES)DEPENDENCIES

           Packaged sysusers.d(5) files generate virtual provides for the
           users and/or groups they define. Similarly, any non-root ownership
           defined with %attr() or %defattr() in an rpm-spec(5) file
           generates virtual requires for the named users and/or groups. Both
           dependencies complement each other to ensure correct installation
           when a package relies on a user/group from another package.

           Explicit group membership (the m sysusers.d directive) will also
           generate virtual requires for both the user and the group name in
           the originating package.

           For more details on the mechanism itself, see
           rpm-dependency-generators(7).

## [](#LIMITATIONS)LIMITATIONS

           Currently, RPM only supports the following sysusers.d directives:
           •   u and g (Added: 4.19.0)
           •   m (Added: 4.20.0)
           •   u! (Added: 4.20.1)

           Other directives, if used, will be ignored. If such are needed,
           the package has to call systemd-sysusers(8) with the correct
           arguments manually.

## [](#PORTABILITY)PORTABILITY

           RPM provides a number of macros to enable vendors and packagers to
           implement the declarative user and group integration on platforms
           that do not ship with the default systemd tooling. Note, however,
           that some of these tunables may need tweaking even on platforms
           with systemd.

       Vendors
           %__systemd_sysusers PATH
               Path to the systemd-sysusers(8) executable or a compatible
               program.

               On systemd native platforms, set PATH to the
               systemd-sysusers(8) program, typically at /usr/bin/systemd-
               sysusers. Note that the program may also be shipped by a
               standalone package with no systemd dependencies (such as
               systemd-standalone-sysusers on Fedora Linux) which makes it
               useful in containers or similar environments.

               RPM ships with a replacement shell script that calls the
               standard UNIX tools such as useradd(8) or groupadd(8) for
               account creation. The script is installed at
               %{_rpmconfigdir}/sysusers.sh and can be used on platforms
               where the original program is not available.

               On platforms without the standard UNIX account tools, a custom
               script or program can be written, which must:
               •   Process sysusers.d(5) entries on standard input
               •   Create or modify users and groups accordingly
               •   Never delete any users or groups
               •   Handle the --root and --replace options like the original
                   program
               •   Avoid changing the host if --root is used

           %_sysusersdir PATH
               Path to the drop-in directory where packages are supposed to
               install the sysusers.d(5) files. Defaults to
               /usr/lib/sysusers.d.

       Packagers
           %add_sysusers [-b] ENTRY
               Interpret ENTRY as if written in a sysusers.d(5) file and
               expand to a (bare) dependency string as described in Encoding.
               ENTRY denotes the individual fields passed as macro arguments.

               When used with -b, expand to a bare dependency string. This
               form can be used to implement rpm-dependency-generators(7) for
               sysusers.d(5) files. RPM ships with such a generator
               (sysusers.attr) installed by default.

               When used without -b, expand to a dependency string and prefix
               it with the appropriate dependency tag for use in rpm-spec(5)
               files. This form can be used in the (sub)package context of a
               spec file, to declare users and/or groups directly, without
               having to package sysusers.d(5) files. It is mainly intended
               for development purposes, and is discouraged otherwise since
               it conflicts with the original sysusers.d(5) scheme (see also
               TECHNICAL DETAILS).

## [](#COMPATIBILITY)COMPATIBILITY

       Vendors
           By default, the generated virtual requires are hard dependencies.
           This can be problematic when upgrading an existing distribution to
           RPM 4.19, however, so it is possible to weaken these requires into
           recommends, by setting %_use_weak_usergroup_deps to 1 in the
           rpmbuild-config(5).

## [](#TECHNICAL_DETAILS)TECHNICAL DETAILS

       Encoding
           RPM will generate any combination of the following virtual
           provides based on, and attached to, the packaged sysusers.d(5)
           file(s):

           user(username) = base64
           group(groupname) [= base64]
           groupmember(username/groupname) = base64

           base64 is a base64 encoded representation of the given sysusers.d
           entry, with the input \0-padded as needed, in order to avoid the
           base64 native = padding in the output, which is illegal in an EVR
           string.

           For example, the following sysusers.d entry:

               u dnsmasq - "Dnsmasq DHCP and DNS server" /var/lib/dnsmasq

           would emit the following provides attached to the originating
           file:

               user(dnsmasq) = dSBkbnNtYXNxIC0gIkRuc21hc3EgREhDUCBhbmQgRE5TIHNlcnZlciIgL3Zhci9saWIvZG5zbWFzcQAA
               group(dnsmasq)

           As systemd-sysusers(8) implicitly creates a matching group for any
           created users, the group provides does not have an EVR here. Only
           explicitly created groups will have the encoded sysusers.d entry
           as an EVR.

           Entries adding users to groups, such as:

               m klangd klong

           will create a provides:

               groupmember(klangd/klong) = bSBrbGFuZ2Qga2xvbmcA

           They will also create two requires (or recommends if
           %_use_weak_usergroup_deps is set to 1):

               group(klong)
               user(klangd)

           to make sure the packages creating the user and group are
           installed first.

       Decoding
           When RPM installs a package with virtual provides as described in
           ENCODING, it decodes their EVR strings back from base64 to the
           original sysusers.d entries, and groups them by their source file.
           Then, it runs the systemd-sysusers(8) program once for each source
           file, with --replace pointing to the path of the source file when
           installed, and passes the decoded entries pertaining to that file
           on standard input. The program then creates new, or modifies
           existing, users and groups on the system, according to those
           entries.

           Since the above process happens before the payload is unpacked to
           disk, packages can ship files owned by their own users and groups.

           Virtual provides generated with the %add_sysuser macro in
           rpm-spec(5) files are package-level, with no source files to group
           them by. Thus, RPM does not use --replace when calling
           systemd-sysusers(8) for such entries. That may cause unintended
           behavior since the program then gives the entries on standard
           input higher priority than any sysusers.d(5) overrides that the
           administrator may have configured on the system.

           Note that the packaged sysusers.d(5) files, if any, are installed
           as normal, but do not participate in the user/group creation
           itself. They simply serve as static definition files for
           reconstructing /etc/passwd and /etc/group later, as per
           sysusers.d(5).

## [](#TROUBLESHOOTING)TROUBLESHOOTING

           rpm -q {--provides|--requires} PACKAGE_NAME | grep
           '^\(user(\|group(\|groupmember(\)'
               Display the virtual user/group/groupmember provides/requires
               of PACKAGE_NAME.

           rpm -q --queryformat '[%{SYSUSERS}\n]' PACKAGE_NAME
               Display the original sysusers.d entries decoded from the
               virtual provides of PACKAGE_NAME by using rpm-queryformat(7).

## [](#EXAMPLES)EXAMPLES

       Example 1. Packaging a sysusers.d(5) file
           Consider a dnsmasq.spec file with the following contents
           (irrelevant parts ellipsized or omitted):

               %install
               mkdir -p ${RPM_BUILD_ROOT}/%{_var}/lib/dnsmasq
               mkdir -p ${RPM_BUILD_ROOT}/%{_sysusersdir}
               cat << EOF > ${RPM_BUILD_ROOT}/%{_sysusersdir}/dnsmasq.conf
               u dnsmasq - "Dnsmasq DHCP and DNS server" /var/lib/dnsmasq
               EOF
               [...]

               %files
               %dir %attr(0755,root,dnsmasq) %{_var}/lib/dnsmasq
               %{_sysusersdir}/dnsmasq.conf
               [...]

           When the package is built, it will contain the following requires
           and provides:

               $ rpm -qp --requires /path/to/dnsmasq.rpm
               group(dnsmasq)
               [...]
               $ rpm -qp --provides /path/to/dnsmasq.rpm
               group(dnsmasq)
               user(dnsmasq) = dSBkbnNtYXNxIC0gIkRuc21hc3EgREhDUCBhbmQgRE5TIHNlcnZlciIgL3Zhci9saWIvZG5zbWFzcQAA
               [...]

           Finally, when the package is installed, RPM will create the
           dnsmasq user and group automatically, and the /var/lib/dnsmasq
           directory installed by the package itself will be owned by that
           group as per the spec file:

               $ getent passwd dnsmasq
               dnsmasq:x:999:999:Dnsmasq DHCP and DNS server:/var/lib/dnsmasq:/usr/sbin/nologin
               $ getent group dnsmasq
               dnsmasq:x:999:
               $ stat -c '%G:%g' /var/lib/dnsmasq
               dnsmasq:999

           The original sysusers.d(5) file will be installed as normal:

               $ rpm -ql dnsmasq | grep sysusers
               /usr/lib/sysusers.d/dnsmasq.conf
               $ cat /usr/lib/sysusers.d/dnsmasq.conf
               u dnsmasq - "Dnsmasq DHCP and DNS server" /var/lib/dnsmasq

       Example 2. Declaring a sysusers.d entry manually
           Consider a dnsmasq.spec file with the following contents starting
           just below the preamble block (irrelevant parts ellipsized or
           omitted):

               %{add_sysuser u dnsmasq - "Dnsmasq DHCP and DNS server" /var/lib/dnsmasq}
               [...]

               %files
               %dir %attr(0755,root,dnsmasq) %{_var}/lib/dnsmasq
               [...]

           Building and installing this package will have the same effect as
           described in Example 1. The only difference is that, in this
           example, no sysusers.d(5) file is packaged or installed.

## [](#SEE_ALSO)SEE ALSO

           rpm(8), rpmbuild-config(5), rpm-spec(5), rpm-scriptlets(7),
           rpm-dependency-generators(7), sysusers.d(5), systemd-sysusers(8),
           systemd.exec(5), useradd(8), groupadd(8)

           https://0pointer.net/blog/dynamic-users-with-systemd.html 

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

    RPM 6.1.90                      2026-08-03                RPM-SYSUSERS(7)

------------------------------------------------------------------------

Pages that refer to this page: [rpmbuild-config(5)](../man5/rpmbuild-config.5.html),  [rpm-spec(5)](../man5/rpm-spec.5.html),  [rpm-scriptlets(7)](../man7/rpm-scriptlets.7.html),  [rpm(8)](../man8/rpm.8.html)

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
