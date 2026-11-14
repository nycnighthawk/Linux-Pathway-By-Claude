---
{"title": "semanage.conf(5) — Linux manual page", "url": "https://man7.org/linux/man-pages/man5/semanage.conf.5.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# semanage.conf(5) --- Linux manual page

+---------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [DESCRIPTION](#DESCRIPTION) \| [SEE ALSO](#SEE_ALSO) \| [AUTHOR](#AUTHOR) \| [COLOPHON](#COLOPHON) |                                   |
+---------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                     |                                   |
+---------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    semanage.conf(5)       Linux System Administration       semanage.conf(5)

## [](#NAME)NAME

           semanage.conf - global configuration file for the SELinux
           Management library

## [](#DESCRIPTION)DESCRIPTION

           The semanage.conf file is usually located under the directory
           /etc/selinux and it is used for run-time configuration of the
           behavior of the SELinux Management library.

           Each line should contain a configuration parameter followed by the
           equal sign ("=") and then followed by the configuration value for
           that parameter. Anything after the "#" symbol is ignored similarly
           to empty lines.

           The following parameters are allowed:

                  module-store
                         Specify how the SELinux Management library should
                         interact with the SELinux policy store. When set to
                         "direct", the SELinux Management library writes to
                         the SELinux policy module store directly (this is
                         the default setting).  Otherwise a socket path or a
                         server name can be used for the argument.  If the
                         argument begins with "/" (as in "/foo/bar"), it
                         represents the path to a named socket that should be
                         used to connect the policy management server.  If
                         the argument does not begin with a "/" (as in
                         "example.com:4242"), it should be interpreted as the
                         name of a remote policy management server to be used
                         through a TCP connection (default port is 4242
                         unless a different one is specified after the server
                         name using the colon to separate the two fields).

                  root   Specify an alternative root path to use for the
                         store. The default is "/"

                  store-root
                         Specify an alternative store_root path to use. The
                         default is "/var/lib/selinux"

                  compiler-directory
                         Specify an alternative directory that contains HLL
                         to CIL compilers. The default value is
                         "/usr/libexec/selinux/hll".

                  ignore-module-cache
                         Whether or not to ignore the cache of CIL modules
                         compiled from HLL. It can be set to either "true" or
                         "false" and is set to "false" by default.  If the
                         cache is ignored, then all CIL modules are
                         recompiled from their HLL modules.

                  policy-version
                         When generating the policy, by default semanage will
                         set the policy version to POLICYDB_VERSION_MAX, as
                         defined in <sepol/policydb/policydb.h>. Change this
                         setting if a different version needs to be set for
                         the policy.

                  target-platform
                         The target platform to generate policies for. Valid
                         values are "selinux" and "xen", and is set to
                         "selinux" by default.

                  expand-check
                         Whether or not to check "neverallow" rules when
                         executing all semanage command. It can be set to
                         either "0" / "false" (disabled) or "1" / "true"
                         (enabled) and by default it is enabled. There might
                         be a large penalty in execution time if this option
                         is enabled.

                  file-mode
                         By default the permission mode for the run-time
                         policy files is set to 0644.

                  save-previous
                         It controls whether the previous module directory is
                         saved after a successful commit to the policy store
                         and it can be set to either "true" or "false". By
                         default it is set to "false" (the previous version
                         is deleted).

                  save-linked
                         It controls whether the previously linked module is
                         saved (with name "base.linked") after a successful
                         commit to the policy store.  It can be set to either
                         "true" or "false" and by default it is set to
                         "false" (the previous module is deleted).

                  ignoredirs
                         List, separated by ";",  of directories to ignore
                         when setting up users homedirs.  Some distributions
                         use this to stop labeling /root as a homedir.

                  usepasswd
                         Whether or not to enable the use getpwent() to
                         obtain a list of home directories to label. It can
                         be set to either "true" or "false".  By default it
                         is set to "true".

                  disable-genhomedircon
                         It controls whether or not the genhomedircon
                         function is executed when using the semanage command
                         and it can be set to either "false" or "true". By
                         default the genhomedircon functionality is enabled
                         (equivalent to this option set to "false").

                  handle-unknown
                         This option overrides the kernel behavior for
                         handling permissions defined in the kernel but
                         missing from the actual policy.  It can be set to
                         "deny", "reject" or "allow". By default the setting
                         from the policy is taken.

                  bzip-blocksize
                         It should be in the range 0-9. A value of 0 means no
                         compression. By default the bzip block size is set
                         to 9 (actual block size value is obtained after
                         multiplication by 100000).

                  bzip-small
                         When set to "true", the bzip algorithm shall try to
                         reduce its system memory usage. It can be set to
                         either "true" or "false" and by default it is set to
                         "false".

                  remove-hll
                         When set to "true", HLL files will be removed after
                         compilation into CIL. In order to delete HLL files
                         already compiled into CIL, modules will need to be
                         recompiled with the ignore-module-cache option set
                         to 'true' or using the ignore-module-cache option
                         with semodule. The remove-hll option can be set to
                         either "true" or "false" and by default it is set to
                         "false".

                         Please note that since this option deletes all HLL
                         files, an updated HLL compiler will not be able to
                         recompile the original HLL file into CIL.  In order
                         to compile the original HLL file into CIL, the same
                         HLL file will need to be reinstalled.

                  optimize-policy
                         When set to "true", the kernel policy will be
                         optimized upon rebuilds.  It can be set to either
                         "true" or "false" and by default it is set to
                         "true".

                  multiple-decls
                         When set to "true", duplicate type, type attribute,
                         and role declarations will be allowed.  It can be
                         set to either "true" or "false" and by default it is
                         set to "true".

           For certain tasks the SELinux Management library resorts to
           running external commands.  For the following commands their path
           and arguments can be overridden:

                         load_policy
                                Command to load a kernel policy.  Requires no
                                argument.  Defaults to /sbin/load_policy with
                                no arguments.

                         setfiles
                                Command to verify file context definitions.
                                Requires two arguments, the path to the
                                kernel policy and the path to the file
                                context definition file.  Defaults to
                                /sbin/setfiles with the arguments '-q -c $@
                                $<'.

                         sefcontext_compile
                                Command to compile a file context definition
                                file.  Requires one argument, the path to the
                                to be compiled file context definition file.
                                Defaults to /sbin/sefcontext_compile with the
                                argument '$@'.

                  Either path or args can be omitted.  The argument string
                  must contain '$@' for the first required argument, and '$<'
                  for the second one.  The syntax for overriding an external
                  command property is:

                         [name]
                         path = /path/to/command
                         args = --flag
                         [end]

                  Example

                         [sefcontext_compile]
                         path = /usr/sbin/sefcontext_compile
                         args = -r $@
                         [end]

                  Optionally the SELinux Management library can invoke
                  external commands to verify source modules (verify module),
                  linked modules (verify linked), and kernel policies (verify
                  kernel).  The syntax is identical to the above command
                  overrides.  The program should exit with a value of 0 on
                  success, and non zero on failure.

## [](#SEE_ALSO)SEE ALSO

           semanage(8)

## [](#AUTHOR)AUTHOR

           This manual page was written by Guido Trentalancia
           <guido@trentalancia.com>.

           The SELinux management library was written by Tresys Technology
           LLC and Red Hat Inc.

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

    semanage.conf                 September 2011             semanage.conf(5)

------------------------------------------------------------------------

Pages that refer to this page: [genhomedircon(8)](../man8/genhomedircon.8.html)

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
