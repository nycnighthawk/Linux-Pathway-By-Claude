---
{"title": "uname(2) — Linux manual page", "url": "https://man7.org/linux/man-pages/man2/oldolduname.2.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# uname(2) --- Linux manual page

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [LIBRARY](#LIBRARY) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [RETURN VALUE](#RETURN_VALUE) \| [ERRORS](#ERRORS) \| [VERSIONS](#VERSIONS) \| [STANDARDS](#STANDARDS) \| [HISTORY](#HISTORY) \| [NOTES](#NOTES) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                                                                                    |                                   |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    uname(2)                   System Calls Manual                   uname(2)

## [](#NAME)NAME

           uname - get name and information about current kernel

## [](#LIBRARY)LIBRARY

           Standard C library (libc, -lc)

## [](#SYNOPSIS)SYNOPSIS

           #include <sys/utsname.h>

           int uname(struct utsname *buf);

## [](#DESCRIPTION)DESCRIPTION

           uname() returns system information in the structure pointed to by
           buf.  The utsname struct is defined in <sys/utsname.h>:

               struct utsname {
                   char sysname[];    /* Operating system name (e.g., "Linux") */
                   char nodename[];   /* Name within communications network
                                         to which the node is attached, if any */
                   char release[];    /* Operating system release
                                         (e.g., "2.6.28") */
                   char version[];    /* Operating system version */
                   char machine[];    /* Hardware type identifier */
               #ifdef _GNU_SOURCE
                   char domainname[]; /* NIS or YP domain name */
               #endif
               };

           The length of the arrays in a struct utsname is unspecified (see
           VERSIONS and HISTORY); the fields are terminated by a null byte
           ('\0').

## [](#RETURN_VALUE)RETURN VALUE

           On success, zero is returned.  On error, -1 is returned, and errno
           is set to indicate the error.

## [](#ERRORS)ERRORS

           EFAULT buf is not valid.

## [](#VERSIONS)VERSIONS

           The domainname member (the NIS or YP domain name) is a GNU
           extension.

           The length of the fields in the struct varies.  Some operating
           systems or libraries use a hardcoded 9 or 33 or 65 or 257.  Other
           systems use SYS_NMLN or _SYS_NMLN or UTSLEN or _UTSNAME_LENGTH.
           Clearly, it is a bad idea to use any of these constants; just use
           sizeof(...).  SVr4 uses 257, "to support Internet hostnames" —this
           is the largest value likely to be encountered in the wild—.

## [](#STANDARDS)STANDARDS

           POSIX.1-2024.

## [](#HISTORY)HISTORY

           POSIX.1-2001, SVr4, 4.4BSD.

       C library/kernel differences
           Over time, increases in the size of the utsname structure have led
           to three successive versions of uname(): sys_olduname() (slot
           __NR_oldolduname), sys_uname() (slot __NR_olduname), and
           sys_newuname() (slot __NR_uname).  The first one used length 9 for
           all fields; the second used 65; the third also uses 65 but adds
           the domainname field.  The glibc uname() wrapper function hides
           these details from applications, invoking the most recent version
           of the system call provided by the kernel.

## [](#NOTES)NOTES

           The kernel has the name, release, version, and supported machine
           type built in.  Conversely, the nodename field is configured by
           the administrator to match the network (this is what the BSD
           historically calls the "hostname", and is set via sethostname(2)).
           Similarly, the domainname field is set via setdomainname(2).

           Part of the utsname information is also accessible via
           /proc/sys/kernel/{ostype, hostname, osrelease, version,
           domainname}.

## [](#SEE_ALSO)SEE ALSO

           uname(1), getdomainname(2), gethostname(2), uts_namespaces(7)

## [](#COLOPHON)COLOPHON

           This page is part of the man-pages (Linux kernel and C library
           user-space interface documentation) project.  Information about
           the project can be found at 
           ⟨https://www.kernel.org/doc/man-pages/⟩.  If you have a bug report
           for this manual page, see
           ⟨https://git.kernel.org/pub/scm/docs/man-pages/man-pages.git/tree/CONTRIBUTING⟩.
           This page was obtained from the tarball man-pages-6.19.tar.gz
           fetched from
           ⟨https://mirrors.edge.kernel.org/pub/linux/docs/man-pages/⟩ on
           2026-09-09.  If you discover any rendering problems in this HTML
           version of the page, or you believe there is a better or more up-
           to-date source for the page, or you have corrections or
           improvements to the information in this COLOPHON (which is not
           part of the original manual page), send a mail to
           man-pages@man7.org

    Linux man-pages 6.19            2026-02-08                       uname(2)

------------------------------------------------------------------------

Pages that refer to this page: [arch(1)](../man1/arch.1.html),  [systemd-nspawn(1)](../man1/systemd-nspawn.1.html),  [uname(1)](../man1/uname.1.html),  [getdomainname(2)](../man2/getdomainname.2.html),  [gethostname(2)](../man2/gethostname.2.html),  [personality(2)](../man2/personality.2.html),  [syscalls(2)](../man2/syscalls.2.html),  [kbuffer_alloc(3)](../man3/kbuffer_alloc.3.html),  [core(5)](../man5/core.5.html),  [org.freedesktop.hostname1(5)](../man5/org.freedesktop.hostname1.5.html),  [rpm-rpmrc(5)](../man5/rpm-rpmrc.5.html),  [systemd.exec(5)](../man5/systemd.exec.5.html),  [systemd.unit(5)](../man5/systemd.unit.5.html),  [lvmsystemid(7)](../man7/lvmsystemid.7.html),  [rpm-lua(7)](../man7/rpm-lua.7.html),  [signal-safety(7)](../man7/signal-safety.7.html),  [uts_namespaces(7)](../man7/uts_namespaces.7.html),  [lvmdevices(8)](../man8/lvmdevices.8.html),  [modprobe(8)](../man8/modprobe.8.html),  [sm-notify(8)](../man8/sm-notify.8.html),  [systemd-sysext(8)](../man8/systemd-sysext.8.html)

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
