---
{"title": "request-key.conf(5) — Linux manual page", "url": "https://man7.org/linux/man-pages/man5/request-key.conf.5.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# request-key.conf(5) --- Linux manual page

+------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [DESCRIPTION](#DESCRIPTION) \| [EXAMPLE](#EXAMPLE) \| [FILES](#FILES) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                          |                                   |
+------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    REQUEST-KEY.CONF(5)   Linux Key Management Utilities  REQUEST-KEY.CONF(5)

## [](#NAME)NAME

           request-key.conf - Instantiation handler configuration file

## [](#DESCRIPTION)DESCRIPTION

           These files are used by the /sbin/request-key program to determine
           which program it should run to instantiate a key.

           request-key looks for the best match, reading all the following
           files:

                       /etc/request-key.d/*.conf
                       /etc/request-key.conf

           If it doesn't find a match, it will return an error and the kernel
           will automatically negate the key.

           The best match is defined as the line with the shortest wildcard
           skips, ranking the columns in order left to right.  If two lines
           have the same length skips, then the first read is the one taken.

           In the files, any blank line or line beginning with a hash mark
           '#' is considered to be a comment and ignored.

           All other lines are assumed to be command lines with a number of
           white space separated fields:

           <op> <type> <description> <callout-info> <prog> <arg1> <arg2> ...

           The first four fields are used to match the parameters passed to
           request-key by the kernel. op is the operation type; currently the
           only supported operation is "create".

           type, description and callout-info match the three parameters
           passed to keyctl request2 or the request_key() system call.  Each
           of these may contain one asterisk '*' character as a wildcard
           anywhere within the string.

           Should a match be made, the program specified by <prog> will be
           exec'd. This must have a fully qualified path name. argv[0] will
           be set from the part of the program name that follows the last
           slash '/' character.

           If the program name is prefixed with a pipe bar character '|',
           then the program will be forked and exec'd attached to three
           pipes. The callout information will be piped to it on it's stdin
           and the intended payload data will be retrieved from its stdout.
           Anything sent to stderr will be posted in syslog. If the program
           exits 0, then /sbin/request-key will attempt to instantiate the
           key with the data read from stdout. If it fails in any other way,
           then request-key will attempt to execute the appropriate 'negate'
           operation command.

           The program arguments can be substituted with various macros. Only
           complete argument substitution is supported - macro substitutions
           can't be embedded. All macros begin with a percent character '%'.
           An argument beginning with two percent characters will have one of
           them discarded.

           The following macros are supported:

                  %o    Operation type
                  %k    Key ID
                  %t    Key type
                  %d    Key description
                  %c    Callout information
                  %u    Key UID
                  %g    Key GID
                  %T    Requestor's thread keyring
                  %P    Requestor's process keyring
                  %S    Requestor's session keyring

           There's another macro substitution too that permits the
           interpolation of the contents of a key:

                  %{<type>:<description>}

           This performs a lookup for a key of the given type and description
           on the requestor's keyrings, and if found, substitutes the
           contents for the macro. If not found an error will be logged and
           the key under construction will be negated.

## [](#EXAMPLE)EXAMPLE

           A basic file will be installed in the /etc. This will contain two
           debugging lines that can be used to test the installation:

                  create user debug:* negate /bin/keyctl negate %k 30 %S
                  create user debug:loop:* * |/bin/cat
                  create user debug:* *
                  /usr/share/keyutils/request-key-debug.sh %k %d %c %S
                  negate * * * /bin/keyctl negate %k 30 %S

           This is set up so that something like:

                  keyctl request2 user debug:xxxx negate

           will create a negative user-defined key, something like:

                  keyctl request2 user debug:yyyy spoon

           will create an instantiated user-defined key with "Debug spoon" as
           the payload, and something like:

                  keyctl request2 user debug:loop:zzzz abcdefghijkl

           will create an instantiated user-defined key with the callout
           information as the payload.

## [](#FILES)FILES

           /etc/request-key.conf
           /etc/request-key.d/*.conf

## [](#SEE_ALSO)SEE ALSO

           keyctl(1), request-key.conf(5)

## [](#COLOPHON)COLOPHON

           This page is part of the keyutils (key management utilities)
           project.  Information about the project can be found at [unknown
           -- if you know, please contact man-pages@man7.org] If you have a
           bug report for this manual page, send it to
           keyrings@linux-nfs.org.  This page was obtained from the project's
           upstream Git repository
           ⟨http://git.kernel.org/pub/scm/linux/kernel/git/dhowells/keyutils.git⟩
           on 2026-08-04.  (At that time, the date of the most recent commit
           that was found in the repository was 2023-03-20.)  If you discover
           any rendering problems in this HTML version of the page, or you
           believe there is a better or more up-to-date source for the page,
           or you have corrections or improvements to the information in this
           COLOPHON (which is not part of the original manual page), send a
           mail to man-pages@man7.org

    Linux                        15 November 2011         REQUEST-KEY.CONF(5)

------------------------------------------------------------------------

Pages that refer to this page: [keyctl(1)](../man1/keyctl.1.html),  [request_key(2)](../man2/request_key.2.html),  [request-key.conf(5)](../man5/request-key.conf.5.html),  [keyrings(7)](../man7/keyrings.7.html),  [keyutils(7)](../man7/keyutils.7.html),  [cifs.idmap(8)](../man8/cifs.idmap.8.html),  [cifs.upcall(8)](../man8/cifs.upcall.8.html),  [key.dns_resolver(8)](../man8/key.dns_resolver.8.html),  [request-key(8)](../man8/request-key.8.html)

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
