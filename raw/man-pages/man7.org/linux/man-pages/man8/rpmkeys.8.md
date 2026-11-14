---
{"title": "rpmkeys(8) — Linux manual page", "url": "https://man7.org/linux/man-pages/man8/rpmkeys.8.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# rpmkeys(8) --- Linux manual page

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPERATIONS](#OPERATIONS) \| [ARGUMENTS](#ARGUMENTS) \| [OPTIONS](#OPTIONS) \| [REBUILD OPTIONS](#REBUILD_OPTIONS) \| [VERIFICATION POLICY](#VERIFICATION_POLICY) \| [OUTPUT](#OUTPUT) \| [TROUBLESHOOTING](#TROUBLESHOOTING) \| [CONFIGURATION](#CONFIGURATION) \| [EXIT STATUS](#EXIT_STATUS) \| [EXAMPLES](#EXAMPLES) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                                                                                                                                                                                                                                     |                                   |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    RPMKEYS(8)               System Manager's Manual               RPMKEYS(8)

## [](#NAME)NAME

           rpmkeys - RPM Keyring

## [](#SYNOPSIS)SYNOPSIS

           rpmkeys {-K|--checksig} [options] PACKAGE_FILE ...

           rpmkeys {-d|--delete|-e|--erase} [options] FINGERPRINT ...

           rpmkeys {-x|--export} [options] [FINGERPRINT ...]

           rpmkeys {-i|--import} [options] PUBKEY ...

           rpmkeys {-l|--list} [options] [FINGERPRINT ...]

           rpmkeys --rebuild [options] [rebuild-options]

## [](#DESCRIPTION)DESCRIPTION

           rpmkeys is used for manipulating the rpm keyring and verifying
           package digital signatures with the contained keys.

           For all available operations, see OPERATIONS.

## [](#OPERATIONS)OPERATIONS

           -K, --checksig
               Verify the digests and signatures contained in PACKAGE_FILE to
               ensure the integrity and origin of the package. See
               VERIFICATION POLICY for details of operation.

           -d, --delete, -e, --erase
               Erase the key(s) designated by FINGERPRINT. The --delete and
               -d options are deprecated.

           -x, --export
               Output the key(s) designated by FINGERPRINT using an ASCII-
               armor encoding.  If FINGERPRINT is not specified, output all
               keys.

           --import
               Import ASCII-armored public keys. Digital signatures cannot be
               verified without the corresponding public key (aka
               certificate).

           -l, --list
               List currently imported public key(s) (aka certificates) by
               their fingerprint and user ID. If no fingerprints are
               specified, list all keys.

           --rebuild
               Recreate the public key storage. Update to the latest format
               and drop unreadable keys.

## [](#ARGUMENTS)ARGUMENTS

           FINGERPRINT
               The handle used for all operations on the keys.
           PACKAGE_FILE
               An rpm package file or a manifest.
           PUBKEY
               An ASCII-armored OpenPGP public key (aka certificate).

## [](#OPTIONS)OPTIONS

           See rpm-common(8) for the options common to all rpm executables.

## [](#REBUILD_OPTIONS)REBUILD OPTIONS

           --from <fs|openpgp|rpmdb>
               Use the keys from the specified backend to rebuild the
               currently configured keystore backend. This can be used to
               convert from one key storage to another.

## [](#VERIFICATION_POLICY)VERIFICATION POLICY

           To deal with three generations of package formats and as many
           decades of cryptographic algorithms and differing system policies,
           the RPM package verification is a complicated system with many
           moving parts.

           RPM packages contain multiple individual verifiables that cover
           different parts of the package: header, payload or both. There are
           two classes of verifiables: digests and signatures. Each
           verifiable may use a different cryptographic algorithm. A class-
           level verification result (pass or fail) is computed based on the
           results from its individual verifiables. When a class or
           verifiable passes, it is also said to verify.

           For a class to verify, both the header and payload must be covered
           by a passing verifiable. Non-trusted signatures (such as expired,
           or ones using legacy algorithms) are ignored on the individual
           level, so they only cause a class-level failure if no passing
           signature is present.

           An outright failure of an individual verifiable typically fails
           the whole class as well, but some verifiables have alternatives
           where either of the verifiables passing is sufficient and
           nullifies the other one failing.

           The final verification result is computed based on the class
           results, and the package verification mode set with the
           %_pkgverify_level macro (see rpm-config(5) for details).

           Which of the individual verifiables are used depends on the system
           cryptography libraries and their policies, RPM configuration and
           the package format version.

## [](#OUTPUT)OUTPUT

           --checksig
               <_PACKAGE_FILE_>: [<digests|DIGESTS>] [<signatures|SIGNATURES>] <OK|NOT OK>

               The output is on the level of digest and signature class,
               which often includes results from multiple individual
               verifiables. Classes that verify are printed in lowercase,
               failing classes in UPPERCASE. The final package level
               conclusion per current VERIFICATION POLICY is printed out as
               OK or NOT OK.

           --list
               <fingerprint> <name> <userid> public key

## [](#TROUBLESHOOTING)TROUBLESHOOTING

           Use --checksig --verbose to troubleshoot verification on per-
           veriable level.

           See VERIFICATION POLICY for background on interpreting the output.
           The per-class results and the final conclusion are not printed at
           all in this mode. One should not attempt to calculate the final
           result from this output.

               <_PACKAGE_FILE_>:
                   <range> <description> [ALT] <class>: <result>
                   ...

               The output is on the level of individual verifiables.

               Range describes the area which the verifiable covers. Possible
               values are:
               •   Header: The main header of the package
               •   Payload: The payload of the package
               •   Legacy: The main header and the payload of the package

               Description includes general information about this
               verifiable. For digests, this is just the hash algorithm name,
               such as SHA256. Signatures are prefixed with OpenPGP. For
               discovered signatures, the rest of the description is one of
               the following, depending on whether the public key is
               available or not:

                   <version> <sign_algo>/<hash_algo>, key fingerprint <fprint>
                   <version> <sign_algo>/<hash_algo>, key ID <id>

               Note that the version is OpenPGP version, not to be confused
               with similar looking RPM signature versions. For non-present
               signatures such details are not available, but for RPM V3 and
               V4 signatures the "algorithm family" (RSA or DSA) is emitted.
               RPM V6 signatures may use arbitrary OpenPGP algorithms.

               ALT indicates the verifiable is an optional alternative to
               another verifiable.

               Class is one of digest or signature.

               Result is one of the following:
               •   OK: Verification passed.
               •   NOKEY: The public key is not available (signatures only).
               •   NOTTRUSTED: Verifiable is not trusted, eg. expired key or
                   a legacy algorithm (signatures only). Does not necessarily
                   indicate class failure if there are other usable
                   signatures present.
               •   NOTFOUND: Verifiable was not found. Only emitted on class-
                   level failure, and indicates which individual verifiables
                   RPM looked for.
               •   BAD: Verification failed.

## [](#CONFIGURATION)CONFIGURATION

           There are several configurables affecting the behavior of this
           verification, see rpm-config(5) for details:
           •   %_keyring
           •   %_keyringpath
           •   %_pkgverify_flags
           •   %_pkgverify_level

## [](#EXIT_STATUS)EXIT STATUS

           On success, 0 is returned. In particular, for verification it
           means all arguments were verified successfully as per current
           VERIFICATION POLICY.

           A non-zero code indicates the number of failures encountered, but
           this is capped to 254 to avoid overflowing the return. 255 is
           returned on output error, this special code is used by xargs(1) to
           stop processing immediately.

## [](#EXAMPLES)EXAMPLES

           rpmkeys --export 771b18d3d7baa28734333c424344591e1964c5fc | sq
           inspect
               Export key 771b18d3d7baa28734333c424344591e1964c5fc for
               inspecting with sequoia-sq.

           rpmkeys --erase 771b18d3d7baa28734333c424344591e1964c5fc
               Erase key 771b18d3d7baa28734333c424344591e1964c5fc from the
               keyring.

           rpmkeys -K hello-2.0-1.x86_64.rpm
               Verify hello-2.0-1.x86_64.rpm package file.

## [](#SEE_ALSO)SEE ALSO

           popt(3), rpm(8), rpm-common(8), rpm-config(5), rpmsign(1)

           rpmkeys --help - as rpm(8) supports customizing the options via
           popt aliases it's impossible to guarantee that what's described in
           the manual matches what's available.

           http://www.rpm.org/ 

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

    RPM 6.1.90                      2026-08-03                     RPMKEYS(8)

------------------------------------------------------------------------

Pages that refer to this page: [rpmbuild(1)](../man1/rpmbuild.1.html),  [rpmsign(1)](../man1/rpmsign.1.html),  [rpm(8)](../man8/rpm.8.html),  [rpm-common(8)](../man8/rpm-common.8.html)

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
