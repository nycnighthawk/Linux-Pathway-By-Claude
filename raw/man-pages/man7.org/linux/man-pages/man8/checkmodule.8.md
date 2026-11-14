---
{"title": "checkmodule(8) — Linux manual page", "url": "https://man7.org/linux/man-pages/man8/checkmodule.8.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# checkmodule(8) --- Linux manual page

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [EXAMPLE](#EXAMPLE) \| [SEE ALSO](#SEE_ALSO) \| [AUTHOR](#AUTHOR) \| [COLOPHON](#COLOPHON) |                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                            |                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    CHECKMODULE(8)           System Manager's Manual           CHECKMODULE(8)

## [](#NAME)NAME

           checkmodule - SELinux policy module compiler

## [](#SYNOPSIS)SYNOPSIS

           checkmodule [-h] [-b] [-c policy_version] [-C] [-E] [-m] [-M] [-N]
           [-L] [-U handle_unknown] [-V] [-o output_file] [input_file]

## [](#DESCRIPTION)DESCRIPTION

           This manual page describes the checkmodule command.

           checkmodule is a program that checks and compiles a SELinux
           security policy module into a binary representation.  It can
           generate either a base policy module (default) or a non-base
           policy module (-m option); typically, you would build a non-base
           policy module to add to an existing module store that already has
           a base module provided by the base policy.  Use
           semodule_package(8) to combine this module with its optional file
           contexts to create a policy package, and then use semodule(8) to
           install the module package into the module store and load the
           resulting policy.

## [](#OPTIONS)OPTIONS

           -b,--binary
                  Read an existing binary policy module file rather than a
                  source policy module file.  This option is a
                  development/debugging aid.

           -C,--cil
                  Write CIL policy file rather than binary policy file.

           -E,--werror
                  Treat warnings as errors

           -h,--help
                  Print usage.

           -m     Generate a non-base policy module.

           -M,--mls
                  Enable the MLS/MCS support when checking and compiling the
                  policy module.

           -N,--disable-neverallow
                  Do not check neverallow rules.

           -L,--line-marker-for-allow
                  Output line markers for allow rules, in addition to
                  neverallow rules. This option increases the size of the
                  output CIL policy file, but the additional line markers
                  helps debugging, especially neverallow failure reports. Can
                  only be used when writing a CIL policy file.

           -V,--version
                  Show policy versions created by this program.

           -o,--output filename
                  Write a binary policy module file to the specified
                  filename.  Otherwise, checkmodule will only check the
                  syntax of the module source file and will not generate a
                  binary module at all.

           -U,--handle-unknown <action>
                  Specify how the kernel should handle unknown classes or
                  permissions (deny, allow or reject).

           -c policyvers
                  Specify the policy version, defaults to the latest.

## [](#EXAMPLE)EXAMPLE

           # Build a MLS/MCS-enabled non-base policy module.
           $ checkmodule -M -m httpd.te -o httpd.mod

## [](#SEE_ALSO)SEE ALSO

           semodule(8), semodule_package(8) SELinux Reference Policy
           documentation at https://github.com/SELinuxProject/refpolicy/wiki

## [](#AUTHOR)AUTHOR

           This manual page was copied from the checkpolicy man page written
           by Árpád Magosányi <mag@bunuel.tii.matav.hu>, and edited by Dan
           Walsh <dwalsh@redhat.com>.

## [](#COLOPHON)COLOPHON

           This page is part of the selinux (Security-Enhanced Linux user-
           space libraries and tools) project.  Information about the project
           can be found at ⟨https://github.com/SELinuxProject/selinux/wiki⟩.
           If you have a bug report for this manual page, see
           ⟨https://github.com/SELinuxProject/selinux/wiki/Contributing⟩.
           This page was obtained from the project's upstream Git repository
           ⟨https://github.com/SELinuxProject/selinux⟩ on 2026-08-04.  (At
           that time, the date of the most recent commit that was found in
           the repository was 2026-08-03.)  If you discover any rendering
           problems in this HTML version of the page, or you believe there is
           a better or more up-to-date source for the page, or you have
           corrections or improvements to the information in this COLOPHON
           (which is not part of the original manual page), send a mail to
           man-pages@man7.org

                                                               CHECKMODULE(8)

------------------------------------------------------------------------

Pages that refer to this page: [semodule(8)](../man8/semodule.8.html)

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
