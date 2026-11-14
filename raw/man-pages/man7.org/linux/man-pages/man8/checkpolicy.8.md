---
{"title": "checkpolicy(8) — Linux manual page", "url": "https://man7.org/linux/man-pages/man8/checkpolicy.8.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# checkpolicy(8) --- Linux manual page

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [EXAMPLE](#EXAMPLE) \| [SEE ALSO](#SEE_ALSO) \| [AUTHOR](#AUTHOR) \| [COLOPHON](#COLOPHON) |                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                            |                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    CHECKPOLICY(8)           System Manager's Manual           CHECKPOLICY(8)

## [](#NAME)NAME

           checkpolicy - SELinux policy compiler

## [](#SYNOPSIS)SYNOPSIS

           checkpolicy [-b[F]] [-C] [-d] [-U handle_unknown
           (allow,deny,reject)] [-M] [-N] [-L] [-c policyvers] [-o
           output_file|-] [-S] [-t target_platform (selinux,xen)] [-O] [-E]
           [-V] [input_file]

## [](#DESCRIPTION)DESCRIPTION

           This manual page describes the checkpolicy command.

           checkpolicy is a program that checks and compiles a SELinux
           security policy configuration into a binary representation that
           can be loaded into the kernel.  If no input file name is
           specified, checkpolicy will attempt to read from policy.conf or
           policy, depending on whether the -b flag is specified.

## [](#OPTIONS)OPTIONS

           -b,--binary
                  Read an existing binary policy file rather than a source
                  policy.conf file.

           -F,--conf
                  Write policy.conf file rather than binary policy file. Can
                  only be used with binary policy file.

           -C,--cil
                  Write CIL policy file rather than binary policy file.

           -d,--debug
                  Enter debug mode after loading the policy.

           -U,--handle-unknown <action>
                  Specify how the kernel should handle unknown classes or
                  permissions (deny, allow or reject).

           -M,--mls
                  Enable the MLS policy when checking and compiling the
                  policy.

           -N,--disable-neverallow
                  Do not check neverallow rules.

           -L,--line-marker-for-allow
                  Output line markers for allow rules, in addition to
                  neverallow rules. This option increases the size of the
                  output CIL policy file, but the additional line markers
                  helps debugging, especially neverallow failure reports. Can
                  only be used when writing a CIL policy file.

           -c policyvers
                  Specify the policy version, defaults to the latest.

           -o,--output filename
                  Write a policy file (binary, policy.conf, or CIL policy) to
                  the specified filename. If - is given as filename, write it
                  to standard output.

           -S,--sort
                  Sort ocontexts before writing out the binary policy. This
                  option makes output of checkpolicy consistent with binary
                  policies created by semanage and secilc.

           -t,--target
                  Specify the target platform (selinux or xen).

           -O,--optimize
                  Optimize the final kernel policy (remove redundant rules).

           -E,--werror
                  Treat warnings as errors

           -V,--version
                  Show version information.

           -h,--help
                  Show usage information.

## [](#EXAMPLE)EXAMPLE

           Generate policy.conf based on the system policy
           # checkpolicy -b -M -F /etc/selinux/targeted/policy/policy.33 -o policy.conf
           Recompile system policy so that unknown permissions are denied (uses policy.conf from ^^).
           Note that binary policy extension represents its version, which is subject to change
           # checkpolicy -M -U deny -o /etc/selinux/targeted/policy/policy.33 policy.conf
           # load_policy
           Generate CIL representation of current system policy
           # checkpolicy -b -M -C /etc/selinux/targeted/policy/policy.33 -o policy.out

## [](#SEE_ALSO)SEE ALSO

           SELinux Reference Policy documentation at
           https://github.com/SELinuxProject/refpolicy/wiki

## [](#AUTHOR)AUTHOR

           This manual page was written by Árpád Magosányi
           <mag@bunuel.tii.matav.hu>, and edited by Stephen Smalley
           <stephen.smalley.work@gmail.com>.  The program was written by
           Stephen Smalley <stephen.smalley.work@gmail.com>.

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

                                                               CHECKPOLICY(8)

------------------------------------------------------------------------

Pages that refer to this page: [restorecon(8)](../man8/restorecon.8.html),  [setfiles(8)](../man8/setfiles.8.html)

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
