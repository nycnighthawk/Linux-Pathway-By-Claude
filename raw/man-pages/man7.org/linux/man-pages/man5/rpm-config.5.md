---
{"title": "rpm-config(5) — Linux manual page", "url": "https://man7.org/linux/man-pages/man5/rpm-config.5.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# rpm-config(5) --- Linux manual page

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [FILES](#FILES) \| [DESCRIPTION](#DESCRIPTION) \| [CONFIGURATION](#CONFIGURATION) \| [ENVIRONMENT](#ENVIRONMENT) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                              |                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    RPM-CONFIG(5)              File Formats Manual              RPM-CONFIG(5)

## [](#NAME)NAME

           rpm-config - rpm runtime macro configuration

## [](#SYNOPSIS)SYNOPSIS

           NAME VALUE

## [](#FILES)FILES

           /usr/lib/rpm/macros
           /usr/lib/rpm/macros.d/macros.*
           /usr/lib/rpm/platform/%{_target}/macros
           /usr/lib/rpm/fileattrs/*.attr
           /usr/lib/rpm/<vendor>/macros
           /etc/rpm/macros.*
           /etc/rpm/macros
           /etc/rpm/%{_target}/macros
           ~/.config/rpm/macros

## [](#DESCRIPTION)DESCRIPTION

           The primary configuration mechanism in rpm is rpm-macros(7). On
           startup, rpm reads a set of rpm-macrofile(5) files determined by
           the macro path.

           Each file or glob(7) pattern in the colon-separated macro path is
           read sequentially by rpm for macro definitions. %{_target} is
           expanded to the detected <arch>-<os> platform. Tildes are expanded
           to the value of the environment variable HOME.

           If a macro is defined multiple times, the last entry wins. The
           default macro path uses this to achieve the following hierarchy of
           settings:
           1.  Generic rpm factory defaults
           2.  Platform-specific rpm factory defaults
           3.  Vendor (distribution) specific settings
           4.  Host specific settings
           5.  User specific settings
           6.  Command-line override settings

           The default macro path can be inspected with rpm --showrc|grep
           ^Macro.

           In older versions of rpm, the path of per-user macros was
           ~/.rpmmacros. This is still processed if it exists and the new
           configuration directory does not exist.

## [](#CONFIGURATION)CONFIGURATION

           The following configurables are supported for the rpm runtime (as
           opposed to just package building) parts:

           %_color_output MODE
               Output coloring mode. Valid values are never and auto.

           %_db_backend BACKEND
               The database backend to use. Possible values for BACKEND are:
               •   dummy: Dummy backend (no actual functionality)
               •   bdb_ro: Berkeley DB (read-only)
               •   ndb: Native database (no external dependencies)
               •   sqlite: Sqlite database

           %_dbpath DIRECTORY
               The location of the rpm database file(s).

           %_excludedocs VALUE
               Boolean (i.e. 1 == "yes", 0 == "no") that controls whether
               files marked as %doc should be installed.

           %_flush_io VALUE
               Flush file IO during transactions (at a severe cost in
               performance for rotational disks). Possible values are 1 to
               enable, 0 to disable.

           %_group_path PATHS
               A colon separated list of group(5) file paths for group name
               and GID lookups in package operations. Files are consulted in
               the given order until a match is found.

               If unset or empty, rpm uses NSS (Name Service Switch) when
               operating on the system root, or /etc/group inside the target
               root when using --root (see rpm-common(8) for details).

           %_httpport PORT
               The port of HTTP proxy (used for FTP/HTTP).

           %_httpproxy HOSTNAME
               The hostname of HTTP proxy (used for FTP/HTTP).

           %_install_langs LOCALES
               A colon separated list of desired locales to be installed; all
               means install all locale specific files.

           %_install_script_path PATH
               The PATH used in rpm-scriptlet(7) execution environment.

           %_keyring BACKEND
               The keyring type to use. Possible values for BACKEND are:
               •   fs: Plain ASCII files in a directory
               •   openpgp: Shared OpenPGP certificate directory
               •   rpmdb: Pseudo-packages in the rpmdb

           %_keyringpath DIRECTORY
               The location of the keyring path for non-rpmdb variants.

           %_minimize_writes VALUE
               Minimize writes during transactions (at the cost of more
               reads) to conserve eg SSD disks (EXPERIMENTAL). Possible
               values are:
               •   0: disable
               •   1: enable
               •   -1: (or undefined) autodetect on platforms where
                   supported, otherwise default to disabled

           %_netsharedpath PATH
               A colon separated list of paths where files should not be
               installed. Usually, these are network filesystem mount points.

           %_passwd_path PATHS
               A colon separated list of passwd(5) file paths for username
               and UID lookups in package operations. Files are consulted in
               the given order until a match is found.

               If unset or empty, rpm uses NSS (Name Service Switch) when
               operating on the system root, or /etc/passwd inside the target
               root when using --root (see rpm-common(8) for details).

           %_pkgverify_digests HASHALGOS
               A colon separated list of hash algorithms to calculate digests
               on the entire package files during verification. The
               calculated digests are stored in the Packagedigests tag of
               packages in the rpmdb, and the corresponding algorithms in the
               Packagedigestalgos tag. No package digests are calculated or
               stored if --noverify is used during package installation.

           %_pkgverify_flags VSFLAGS
               Transaction package verification flags, used for fine-grained
               control of %_pkgverify_level operation. Set to 0x0 for full
               compatibility with v4 packages.

           %_pkgverify_level MODE
               Enforced package verification mode in transactions, where MODE
               is one of:
               •   all: require valid digest(s) and signature(s)
               •   signature: require valid signature(s)
               •   digest: require valid digest(s)
               •   none: legacy rpm behavior, nothing required

           %_prefer_color VALUE
               Package conflict resolution in bi-arch transactions. See also
               %_transaction_color. Possible values are:
               •   0: disabled
               •   1: prefer 32-bit packages
               •   2: prefer 64-bit packages

           %__plugindir DIRECTORY
               Transaction plugin directory.

           %_query_all_fmt FORMAT
               Default output format for rpm(8) query operations, as
               described by rpm-queryformat(7). Percent signs need to be
               escaped, for example %%{nevra}.

           %_rpmlock_path FILE
               The path of the file used for transaction fcntl lock.

           %_tmppath PATH
               The directory where temporary files are created.

           %__urlhelpercmd EXECUTABLE
               The executable to use for retrieving remote files.

           %__urlhelperopts OPTIONS
               Generic options to pass to the %__urlhelpercmd command.

           %__urlhelper_localopts OPTIONS
               User/host specific options to pass to the %__urlhelpercmd
               command.

           %__urlhelper_proxyopts OPTIONS
               Proxy options to pass to the %__urlhelpercmd command.

           %_urlhelper COMMAND
               Full command (with options) to use when retrieving remote
               files. Normally pieced together from the double-underscore
               %__urlhelper* macros.

           %_transaction_color VALUE
               Package and file conflict behavior in bi-arch transactions.
               See also %_prefer_color. Possible values are:
               •   0: do not consider "colors", only use arch compatibility
                   map
               •   1: only allow 32-bit packages
               •   2: only allow 64-bit packages
               •   3: allow 32- and 64-bit packages to share files

           %_vsflags_erase VSFLAGS
               Transaction verification flags used when erasing or updating
               packages.

           %_vsflags_install VSFLAGS
               Transaction verification flags used when installing packages.

           %_vsflags_query VSFLAGS
               Transaction verification flags used when querying packages.

           %_vsflags_rebuilddb VSFLAGS
               Transaction verification flags used when rebuilding the
               database.

           %_vsflags_verify VSFLAGS
               Transaction verification flags used when verifying packages.

       Verification flags
           Digest/signature verification flags for various rpm operations are
           controlled by a bitmask known as VSFLAGS. These flags control
           various aspects of digital checksum and signature verification
           when reading rpm package files and their headers.

           VSFLAGS is formed by bitwise or'ing the individual flags:
           •   0x00001 (RPMVSF_NOHDRCHK): don't verify headers from rpmdb
           •   0x00100 (RPMVSF_NOSHA1HEADER): don't verify header SHA1 digest
           •   0x00200 (RPMVSF_NOSHA256HEADER): don't verify header SHA256
               digest
           •   0x00400 (RPMVSF_NODSAHEADER): don't verify header DSA
               signature(s)
           •   0x00800 (RPMVSF_NORSAHEADER): don't verify header RSA
               signature(s)
           •   0x01000 (RPMVSF_NOOPENPGP): don't verify header OpenPGP
               signature(s)
           •   0x02000 (RPMVSF_NOSHA3_256HEADER): don't verify header
               SHA3_256 digest
           •   0x04000 (RPMVSF_NOSHA512PAYLOAD): don't verify package payload
               SHA512 digest
           •   0x08000 (RPMVSF_NOSHA3_256PAYLOAD): don't verify package
               payload SHA3_256 digest
           •   0x10000 (RPMVSF_NOSHA256PAYLOAD): don't verify package payload
               SHA256 digest
           •   0x20000 (RPMVSF_NOMD5): don't verify legacy header+payload MD5
               digest
           •   0x40000 (RPMVSF_NODSA): don't verify legacy header+payload DSA
               signature
           •   0x80000 (RPMVSF_NORSA): don't verify legacy header+payload RSA
               signature

           RPM's Python bindings can be helpful for working with these
           values, for example:
               >>> import rpm
               >>> hex(rpm.RPMVSF_NOSHA1HEADER)
               '0x100'
               >>> hex(rpm.RPMVSF_NOSHA1HEADER|rpm.RPMVSF_NOMD5)
               '0x20100'
               >>>

       Hash algorithms
           The following hash algorithms (denoted by HASHALGO) are known to
           rpm, but availability can vary depending how rpm and it's
           underlying libraries have been built:
           •   1: MD5 (obsolete)
           •   2: SHA1 (obsolete)
           •   8: SHA256
           •   9: SHA384
           •   10: SHA512
           •   12: SHA3-256
           •   14: SHA3-512

## [](#ENVIRONMENT)ENVIRONMENT

           If XDG_CONFIG_HOME environment variable is set, it replaces
           ~/.config in the macro path.

## [](#SEE_ALSO)SEE ALSO

           rpm(8), rpm-common(8), rpm-macrofile(5), rpm-rpmrc(5),
           rpm-macros(7)

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

    RPM 6.1.90                      2026-08-03                  RPM-CONFIG(5)

------------------------------------------------------------------------

Pages that refer to this page: [rpmbuild(1)](../man1/rpmbuild.1.html),  [rpm-setup-autosign(1)](../man1/rpm-setup-autosign.1.html),  [rpmsign(1)](../man1/rpmsign.1.html),  [rpmbuild-config(5)](../man5/rpmbuild-config.5.html),  [rpm-macrofile(5)](../man5/rpm-macrofile.5.html),  [rpm-rpmrc(5)](../man5/rpm-rpmrc.5.html),  [rpm-spec(5)](../man5/rpm-spec.5.html),  [rpm-macros(7)](../man7/rpm-macros.7.html),  [rpm-payloadflags(7)](../man7/rpm-payloadflags.7.html),  [rpm-queryformat(7)](../man7/rpm-queryformat.7.html),  [rpm(8)](../man8/rpm.8.html),  [rpm-common(8)](../man8/rpm-common.8.html),  [rpmdb(8)](../man8/rpmdb.8.html),  [rpmkeys(8)](../man8/rpmkeys.8.html)

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
