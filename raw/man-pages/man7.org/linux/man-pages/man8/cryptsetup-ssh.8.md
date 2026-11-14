---
{"title": "cryptsetup-ssh(8) — Linux manual page", "url": "https://man7.org/linux/man-pages/man8/cryptsetup-ssh.8.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# cryptsetup-ssh(8) --- Linux manual page

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [NOTES](#NOTES) \| [AUTHORS](#AUTHORS) \| [REPORTING BUGS](#REPORTING_BUGS) \| [SEE ALSO](#SEE_ALSO) \| [CRYPTSETUP](#CRYPTSETUP) |                                   |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                   |                                   |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    CRYPTSETUP-SSH(8)          Maintenance Commands         CRYPTSETUP-SSH(8)

## [](#NAME)NAME

           cryptsetup-ssh - manage LUKS2 SSH token

## [](#SYNOPSIS)SYNOPSIS

           cryptsetup-ssh <action> [<options>] <action args>

## [](#DESCRIPTION)DESCRIPTION

           Experimental cryptsetup plugin for unlocking LUKS2 devices with a
           token connected to an SSH server.

           This plugin currently allows only adding a token to an existing
           keyslot. See cryptsetup(8) for instructions on how to remove,
           import or export the token.

       Add operation
           add <options> <device>

           Adds the SSH token to <device>.

           The specified SSH server must contain a key file on the specified
           path with a passphrase for an existing keyslot on the device.
           Provided credentials will be used by cryptsetup to get the
           password when opening the device using the token.

           Options --ssh-server, --ssh-user, --ssh-keypath and --ssh-path are
           required for this operation.

## [](#OPTIONS)OPTIONS

           --debug
               Show debug messages

           --debug-json
               Show debug messages including JSON metadata

           --help, -?
               Show help

           --key-slot number
               Keyslot to assign the token to. If not specified, the token
               will be assigned to the first keyslot matching the provided
               passphrase.

           --ssh-keypath string
               Path to the SSH key for connecting to the remote server.

           --ssh-path string
               Path to the key file on the remote server.

           --ssh-server string
               IP address/URL of the remote server for this token.

           --ssh-user string
               The username used for the remote server.

           --verbose, -v
               Shows more detailed error messages

           --version, -V
               Print program version

## [](#NOTES)NOTES

           The information provided when adding the token (SSH server
           address, user and paths) will be stored in the LUKS2 header in
           plaintext.

## [](#AUTHORS)AUTHORS

           The cryptsetup-ssh tool is written by Vojtech Trefny.

## [](#REPORTING_BUGS)REPORTING BUGS

           Report bugs at cryptsetup mailing list
           <cryptsetup@lists.linux.dev> or in Issues project section
           <https://gitlab.com/cryptsetup/cryptsetup/-/issues/new>.

           Please attach the output of the failed command with --debug option
           added.

## [](#SEE_ALSO)SEE ALSO

           Cryptsetup FAQ
           <https://gitlab.com/cryptsetup/cryptsetup/wikis/FrequentlyAskedQuestions>

           cryptsetup(8), integritysetup(8) and veritysetup(8)

## [](#CRYPTSETUP)CRYPTSETUP

           Part of cryptsetup project
           <https://gitlab.com/cryptsetup/cryptsetup/>. This page is part of
           the Cryptsetup ((open-source disk encryption)) project.
           Information about the project can be found at 
           ⟨https://gitlab.com/cryptsetup/cryptsetup⟩. If you have a bug
           report for this manual page, send it to dm-crypt@saout.de. This
           page was obtained from the project's upstream Git repository
           ⟨https://gitlab.com/cryptsetup/cryptsetup.git⟩ on 2026-08-03. (At
           that time, the date of the most recent commit that was found in
           the repository was 2026-07-21.) If you discover any rendering
           problems in this HTML version of the page, or you believe there is
           a better or more up-to-date source for the page, or you have
           corrections or improvements to the information in this COLOPHON
           (which is not part of the original manual page), send a mail to
           man-pages@man7.org

    cryptsetup-ssh 2.9.0-git        2025-08-09              CRYPTSETUP-SSH(8)

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
