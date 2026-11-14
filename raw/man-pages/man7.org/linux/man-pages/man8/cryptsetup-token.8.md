---
{"title": "cryptsetup-token(8) — Linux manual page", "url": "https://man7.org/linux/man-pages/man8/cryptsetup-token.8.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# cryptsetup-token(8) --- Linux manual page

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [REPORTING BUGS](#REPORTING_BUGS) \| [SEE ALSO](#SEE_ALSO) \| [CRYPTSETUP](#CRYPTSETUP) |                                   |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                         |                                   |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    CRYPTSETUP-TOKEN(8)        Maintenance Commands       CRYPTSETUP-TOKEN(8)

## [](#NAME)NAME

           cryptsetup-token - manage LUKS2 tokens

## [](#SYNOPSIS)SYNOPSIS

           cryptsetup token <add|remove|import|export|unassign> [<options>]
           <device>

## [](#DESCRIPTION)DESCRIPTION

           Action add creates a new keyring token to enable auto-activation
           of the device. For the auto-activation, the passphrase must be
           stored in the keyring with the specified description. Usually, the
           passphrase should be stored in the user or user-session keyring.
           The token command is supported only for LUKS2.

           For adding a new keyring token, the option --key-description is
           mandatory. Also, a new token is assigned to the keyslot specified
           with --key-slot option or to all active keyslots if the --key-slot
           option is omitted.

           To remove an existing token, specify the token ID that should be
           removed with --token-id option.

           WARNING: The action token remove removes any token type, not just
           keyring type from token slot specified by --token-id option.

           Action import can store an arbitrary valid JSON data in the LUKS2
           token. It may be passed via standard input or a file passed in
           --json-file option. If you specify --key-slot, a successfully
           imported token is also assigned to the keyslot.

           Action export writes requested token JSON to a file passed with
           --json-file or to standard output.

           Action unassign removes token binding to specified keyslot. Both
           token and keyslot must be specified by --token-id and --key-slot
           parameters.

           If --token-id is used with action add or action import and a token
           with that ID already exists, option --token-replace can replace
           the existing token.

           <options> can be [--header, --token-id, --key-slot,
           --key-description, --disable-external-tokens, --disable-locks,
           --disable-keyring, --json-file, --token-replace, --unbound,
           --external tokens-path].

## [](#OPTIONS)OPTIONS

           --batch-mode, -q
               Suppresses all confirmation questions. Use with care!

               If the --verify-passphrase option is not specified, this
               option also switches off the passphrase verification.

           --debug or --debug-json
               Run in debug mode with full diagnostic logs. Debug output
               lines are always prefixed by #.

               If --debug-json is used, additional LUKS2 JSON data structures
               are printed.

           --disable-external-tokens
               Disable loading of plugins for external LUKS2 tokens.

           --disable-keyring
               Do not load the volume key in the kernel keyring; store it
               directly in the dm-crypt target instead. This option is
               supported only for the LUKS2 type.

           --disable-locks
               Disable lock protection for metadata on disk. This option is
               valid only for LUKS2 and is ignored for other formats.

               WARNING: Do not use this option unless you run cryptsetup in a
               restricted environment where locking is impossible to perform
               (where /run directory cannot be used).

           --external-tokens-path <absolute path>
               Override the system directory path where cryptsetup searches
               for external token handlers (or token plugins). It must be an
               absolute path (starting with '/' character).

           --header <device or file storing the LUKS header>
               Use a detached (separated) metadata device or file where the
               LUKS header is stored. This option allows one to store the
               ciphertext and LUKS header on different devices.

               For commands that change the LUKS header (e.g., luksAddKey),
               specify the device or file with the LUKS header directly as
               the LUKS device.

           --help, -?
               Show help text and default parameters.

           --json-file
               Read the token JSON from a file or write the token to it.
               Option --json-file=- reads JSON from standard input or writes
               it to standard output, respectively.

           --key-description text
               Set the key description in the keyring that will be used for
               passphrase retrieval.

           --key-slot, -S <0-N>
               For LUKS operations that add key material, this option allows
               you to specify which keyslot is selected for the new key.

               The maximum number of keyslots depends on the LUKS version.
               LUKS1 can have up to 8 keyslots. LUKS2 can have up to 32
               keyslots based on keyslot area size and key size, but a valid
               keyslot ID can always be between 0 and 31 for LUKS2.

           --token-id
               Specify the token number. If omitted, the first unused token
               id is used when adding or importing a new token.

           --token-replace
               Replace an existing token when adding or importing a token
               with the --token-id option.

           --unbound
               Creates a new LUKS2 keyring token assigned to no keyslot.
               Usable only with the add action.

           --usage
               Show short option help.

           --version, -V
               Show the program version.

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

    cryptsetup 2.9.0-git            2025-08-09            CRYPTSETUP-TOKEN(8)

------------------------------------------------------------------------

Pages that refer to this page: [cryptsetup(8)](../man8/cryptsetup.8.html)

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
