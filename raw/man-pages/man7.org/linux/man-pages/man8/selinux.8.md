---
{"title": "selinux(8) — Linux manual page", "url": "https://man7.org/linux/man-pages/man8/selinux.8.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# selinux(8) --- Linux manual page

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [DESCRIPTION](#DESCRIPTION) \| [FILE LABELING](#FILE_LABELING) \| [AUTHOR](#AUTHOR) \| [FILES](#FILES) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                           |                                   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    selinux(8)          SELinux Command Line documentation         selinux(8)

## [](#NAME)NAME

           SELinux - Security-Enhanced Linux (SELinux)

## [](#DESCRIPTION)DESCRIPTION

           Security-Enhanced Linux (SELinux) is an implementation of a
           flexible mandatory access control architecture in the Linux
           operating system.  The SELinux architecture provides general
           support for the enforcement of many kinds of mandatory access
           control policies, including those based on the concepts of Type
           Enforcement®, Role- Based Access Control, and Multi-Level
           Security.  Background information and technical documentation
           about SELinux can be found at https://github.com/SELinuxProject.

           The /etc/selinux/config configuration file controls whether
           SELinux is enabled or disabled, and if enabled, whether SELinux
           operates in permissive mode or enforcing mode.  The SELINUX
           variable may be set to any one of disabled, permissive, or
           enforcing to select one of these options.  The disabled disables
           most of the SELinux kernel and application code, leaving the
           system running without any SELinux protection.  The permissive
           option enables the SELinux code, but causes it to operate in a
           mode where accesses that would be denied by policy are permitted
           but audited.  The enforcing option enables the SELinux code and
           causes it to enforce access denials as well as auditing them.
           permissive mode may yield a different set of denials than
           enforcing mode, both because enforcing mode will prevent an
           operation from proceeding past the first denial and because some
           application code will fall back to a less privileged mode of
           operation if denied access.

           NOTE: Disabling SELinux by setting SELINUX=disabled in
           /etc/selinux/config is deprecated and depending on kernel version
           and configuration it might not lead to SELinux being completely
           disabled.  Specifically, the SELinux hooks will still be executed
           internally, but the SELinux policy will not be loaded and no
           operation will be denied.  In such state, the system will act as
           if SELinux was disabled, although some operations might behave
           slightly differently.  To properly disable SELinux, it is
           recommended to use the selinux=0 kernel boot option instead.  In
           that case SELinux will be disabled regardless of what is set in
           the /etc/selinux/config file.

           The /etc/selinux/config configuration file also controls what
           policy is active on the system.  SELinux allows for multiple
           policies to be installed on the system, but only one policy may be
           active at any given time.  At present, multiple kinds of SELinux
           policy exist: targeted, mls for example.  The targeted policy is
           designed as a policy where most user processes operate without
           restrictions, and only specific services are placed into distinct
           security domains that are confined by the policy.  For example,
           the user would run in a completely unconfined domain while the
           named daemon or apache daemon would run in a specific domain
           tailored to its operation.  The MLS (Multi-Level Security) policy
           is designed as a policy where all processes are partitioned into
           fine-grained security domains and confined by policy.  MLS also
           supports the Bell And LaPadula model, where processes are not only
           confined by the type but also the level of the data.

           You can define which policy you will run by setting the
           SELINUXTYPE environment variable within /etc/selinux/config.  You
           must reboot and possibly relabel if you change the policy type to
           have it take effect on the system.  The corresponding policy
           configuration for each such policy must be installed in the
           /etc/selinux/{SELINUXTYPE}/ directories.

           A given SELinux policy can be customized further based on a set of
           compile-time tunable options and a set of runtime policy booleans.
           system-config-selinux allows customization of these booleans and
           tunables.

           Many domains that are protected by SELinux also include SELinux
           man pages explaining how to customize their policy.

## [](#FILE_LABELING)FILE LABELING

           All files, directories, devices ... have a security context/label
           associated with them.  These context are stored in the extended
           attributes of the file system.  Problems with SELinux often arise
           from the file system being mislabeled. This can be caused by
           booting the machine with a non SELinux kernel.  If you see an
           error message containing file_t, that is usually a good indicator
           that you have a serious problem with file system labeling.

           The best way to relabel the file system is to create the flag file
           /.autorelabel and reboot.  system-config-selinux, also has this
           capability.  The restorecon/fixfiles commands are also available
           for relabeling files.

           Please note that using mount flag nosuid also disables SELinux
           domain transitions, unless permission nosuid_transition is used in
           the policy to allow this, which in turn needs also policy
           capability nnp_nosuid_transition.

## [](#AUTHOR)AUTHOR

           This manual page was written by Dan Walsh <dwalsh@redhat.com>.

## [](#FILES)FILES

           /etc/selinux/config

## [](#SEE_ALSO)SEE ALSO

           booleans(8), setsebool(8), sepolicy(8), system-config-selinux(8),
           togglesebool(8), restorecon(8), fixfiles(8), setfiles(8),
           semanage(8), sepolicy(8)

           Every confined service on the system has a man page in the
           following format:

           <servicename>_selinux(8)

           For example, httpd has the httpd_selinux(8) man page.

           man -k selinux

           Will list all SELinux man pages.

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

    dwalsh@redhat.com              29 Apr 2005                     selinux(8)

------------------------------------------------------------------------

Pages that refer to this page: [crontab(1)](../man1/crontab.1.html),  [connect(2)](../man2/connect.2.html),  [avc_add_callback(3)](../man3/avc_add_callback.3.html),  [avc_cache_stats(3)](../man3/avc_cache_stats.3.html),  [avc_compute_create(3)](../man3/avc_compute_create.3.html),  [avc_context_to_sid(3)](../man3/avc_context_to_sid.3.html),  [avc_has_perm(3)](../man3/avc_has_perm.3.html),  [avc_init(3)](../man3/avc_init.3.html),  [avc_netlink_loop(3)](../man3/avc_netlink_loop.3.html),  [avc_open(3)](../man3/avc_open.3.html),  [context_new(3)](../man3/context_new.3.html),  [getcon(3)](../man3/getcon.3.html),  [getexeccon(3)](../man3/getexeccon.3.html),  [getfilecon(3)](../man3/getfilecon.3.html),  [getfscreatecon(3)](../man3/getfscreatecon.3.html),  [getkeycreatecon(3)](../man3/getkeycreatecon.3.html),  [get_ordered_context_list(3)](../man3/get_ordered_context_list.3.html),  [getseuserbyname(3)](../man3/getseuserbyname.3.html),  [getsockcreatecon(3)](../man3/getsockcreatecon.3.html),  [init_selinuxmnt(3)](../man3/init_selinuxmnt.3.html),  [is_context_customizable(3)](../man3/is_context_customizable.3.html),  [is_selinux_enabled(3)](../man3/is_selinux_enabled.3.html),  [matchmediacon(3)](../man3/matchmediacon.3.html),  [matchpathcon(3)](../man3/matchpathcon.3.html),  [matchpathcon_checkmatches(3)](../man3/matchpathcon_checkmatches.3.html),  [security_check_context(3)](../man3/security_check_context.3.html),  [security_class_to_string(3)](../man3/security_class_to_string.3.html),  [security_compute_av(3)](../man3/security_compute_av.3.html),  [security_disable(3)](../man3/security_disable.3.html),  [security_getenforce(3)](../man3/security_getenforce.3.html),  [security_load_booleans(3)](../man3/security_load_booleans.3.html),  [security_load_policy(3)](../man3/security_load_policy.3.html),  [security_policyvers(3)](../man3/security_policyvers.3.html),  [selabel_digest(3)](../man3/selabel_digest.3.html),  [selabel_get_digests_all_partial_matches(3)](../man3/selabel_get_digests_all_partial_matches.3.html),  [selabel_lookup(3)](../man3/selabel_lookup.3.html),  [selabel_lookup_best_match(3)](../man3/selabel_lookup_best_match.3.html),  [selabel_open(3)](../man3/selabel_open.3.html),  [selabel_partial_match(3)](../man3/selabel_partial_match.3.html),  [selabel_stats(3)](../man3/selabel_stats.3.html),  [selinux_binary_policy_path(3)](../man3/selinux_binary_policy_path.3.html),  [selinux_check_securetty_context(3)](../man3/selinux_check_securetty_context.3.html),  [selinux_colors_path(3)](../man3/selinux_colors_path.3.html),  [selinux_file_context_cmp(3)](../man3/selinux_file_context_cmp.3.html),  [selinux_file_context_verify(3)](../man3/selinux_file_context_verify.3.html),  [selinux_getenforcemode(3)](../man3/selinux_getenforcemode.3.html),  [selinux_getpolicytype(3)](../man3/selinux_getpolicytype.3.html),  [selinux_lsetfilecon_default(3)](../man3/selinux_lsetfilecon_default.3.html),  [selinux_policy_root(3)](../man3/selinux_policy_root.3.html),  [selinux_raw_context_to_color(3)](../man3/selinux_raw_context_to_color.3.html),  [selinux_set_callback(3)](../man3/selinux_set_callback.3.html),  [selinux_set_mapping(3)](../man3/selinux_set_mapping.3.html),  [set_matchpathcon_flags(3)](../man3/set_matchpathcon_flags.3.html),  [crontab(5)](../man5/crontab.5.html),  [customizable_types(5)](../man5/customizable_types.5.html),  [default_contexts(5)](../man5/default_contexts.5.html),  [default_type(5)](../man5/default_type.5.html),  [failsafe_context(5)](../man5/failsafe_context.5.html),  [removable_context(5)](../man5/removable_context.5.html),  [secolor.conf(5)](../man5/secolor.conf.5.html),  [securetty_types(5)](../man5/securetty_types.5.html),  [selabel_db(5)](../man5/selabel_db.5.html),  [selabel_file(5)](../man5/selabel_file.5.html),  [selabel_media(5)](../man5/selabel_media.5.html),  [selabel_x(5)](../man5/selabel_x.5.html),  [selinux_config(5)](../man5/selinux_config.5.html),  [sepermit.conf(5)](../man5/sepermit.conf.5.html),  [service_seusers(5)](../man5/service_seusers.5.html),  [sestatus.conf(5)](../man5/sestatus.conf.5.html),  [setrans.conf(5)](../man5/setrans.conf.5.html),  [seusers(5)](../man5/seusers.5.html),  [user_contexts(5)](../man5/user_contexts.5.html),  [virtual_domain_context(5)](../man5/virtual_domain_context.5.html),  [virtual_image_context(5)](../man5/virtual_image_context.5.html),  [keyrings(7)](../man7/keyrings.7.html),  [xattr(7)](../man7/xattr.7.html),  [avcstat(8)](../man8/avcstat.8.html),  [booleans(8)](../man8/booleans.8.html),  [chcat(8)](../man8/chcat.8.html),  [getenforce(8)](../man8/getenforce.8.html),  [getsebool(8)](../man8/getsebool.8.html),  [matchpathcon(8)](../man8/matchpathcon.8.html),  [mcs(8)](../man8/mcs.8.html),  [mount(8)](../man8/mount.8.html),  [pam_selinux(8)](../man8/pam_selinux.8.html),  [pam_sepermit(8)](../man8/pam_sepermit.8.html),  [sandbox(8)](../man8/sandbox.8.html),  [sefcontext_compile(8)](../man8/sefcontext_compile.8.html),  [selinuxenabled(8)](../man8/selinuxenabled.8.html),  [semanage(8)](../man8/semanage.8.html),  [semanage-boolean(8)](../man8/semanage-boolean.8.html),  [semanage-dontaudit(8)](../man8/semanage-dontaudit.8.html),  [semanage-export(8)](../man8/semanage-export.8.html),  [semanage-fcontext(8)](../man8/semanage-fcontext.8.html),  [semanage-ibendport(8)](../man8/semanage-ibendport.8.html),  [semanage-ibpkey(8)](../man8/semanage-ibpkey.8.html),  [semanage-import(8)](../man8/semanage-import.8.html),  [semanage-interface(8)](../man8/semanage-interface.8.html),  [semanage-login(8)](../man8/semanage-login.8.html),  [semanage-module(8)](../man8/semanage-module.8.html),  [semanage-node(8)](../man8/semanage-node.8.html),  [semanage-permissive(8)](../man8/semanage-permissive.8.html),  [semanage-port(8)](../man8/semanage-port.8.html),  [semanage-user(8)](../man8/semanage-user.8.html),  [sepolicy(8)](../man8/sepolicy.8.html),  [sepolicy-booleans(8)](../man8/sepolicy-booleans.8.html),  [sepolicy-communicate(8)](../man8/sepolicy-communicate.8.html),  [sepolicy-generate(8)](../man8/sepolicy-generate.8.html),  [sepolicy-gui(8)](../man8/sepolicy-gui.8.html),  [sepolicy-interface(8)](../man8/sepolicy-interface.8.html),  [sepolicy-manpage(8)](../man8/sepolicy-manpage.8.html),  [sepolicy-network(8)](../man8/sepolicy-network.8.html),  [sepolicy-transition(8)](../man8/sepolicy-transition.8.html),  [sestatus(8)](../man8/sestatus.8.html),  [setenforce(8)](../man8/setenforce.8.html),  [seunshare(8)](../man8/seunshare.8.html),  [togglesebool(8)](../man8/togglesebool.8.html)

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
