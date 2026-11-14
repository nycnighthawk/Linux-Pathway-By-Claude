---
{"title": "gitprotocol-common(5) — Linux manual page", "url": "https://man7.org/linux/man-pages/man5/gitprotocol-common.5.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# gitprotocol-common(5) --- Linux manual page

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [ABNF NOTATION](#ABNF_NOTATION) \| [PKT-LINE FORMAT](#PKT-LINE_FORMAT) \| [GIT](#GIT) \| [COLOPHON](#COLOPHON) |                                   |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                         |                                   |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    GITPROTOCOL-COMMON(5)           Git Manual          GITPROTOCOL-COMMON(5)

## [](#NAME)NAME

           gitprotocol-common - Things common to various protocols

## [](#SYNOPSIS)SYNOPSIS

           <over-the-wire-protocol>

## [](#DESCRIPTION)DESCRIPTION

           This document defines things common to various over-the-wire
           protocols and file formats used in Git.

## [](#ABNF_NOTATION)ABNF NOTATION

           ABNF notation as described by RFC 5234 is used within the protocol
           documents, except the following replacement core rules are used:

                 HEXDIG    =  DIGIT / "a" / "b" / "c" / "d" / "e" / "f"

           We also define the following common rules:

                 NUL       =  %x00
                 zero-id   =  40*"0"
                 obj-id    =  40*(HEXDIGIT)

                 refname  =  "HEAD"
                 refname /=  "refs/" <see discussion below>

           A refname is a hierarchical octet string beginning with "refs/"
           and not violating the git-check-ref-format command’s validation
           rules. More specifically, they:

            1. They can include slash / for hierarchical (directory)
               grouping, but no slash-separated component can begin with a
               dot ..

            2. They must contain at least one /. This enforces the presence
               of a category like heads/, tags/ etc. but the actual names are
               not restricted.

            3. They cannot have two consecutive dots .. anywhere.

            4. They cannot have ASCII control characters (i.e. bytes whose
               values are lower than \040, or \177 DEL), space, tilde ~,
               caret ^, colon :, question-mark ?, asterisk *, or open bracket
               [ anywhere.

            5. They cannot end with a slash / or a dot ..

            6. They cannot end with the sequence .lock.

            7. They cannot contain a sequence @{.

            8. They cannot contain a \\.

## [](#PKT-LINE_FORMAT)PKT-LINE FORMAT

           Much (but not all) of the payload is described around pkt-lines.

           A pkt-line is a variable length binary string. The first four
           bytes of the line, the pkt-len, indicates the total length of the
           line, in hexadecimal. The pkt-len includes the 4 bytes used to
           contain the length’s hexadecimal representation.

           A pkt-line MAY contain binary data, so implementors MUST ensure
           pkt-line parsing/formatting routines are 8-bit clean.

           A non-binary line SHOULD BE terminated by an LF, which if present
           MUST be included in the total length. Receivers MUST treat
           pkt-lines with non-binary data the same whether or not they
           contain the trailing LF (stripping the LF if present, and not
           complaining when it is missing).

           The maximum length of a pkt-line’s data component is 65516 bytes.
           Implementations MUST NOT send pkt-line whose length exceeds 65520
           (65516 bytes of payload + 4 bytes of length data).

           Implementations SHOULD NOT send an empty pkt-line ("0004").

           A pkt-line with a length field of 0 ("0000"), called a flush-pkt,
           is a special case and MUST be handled differently than an empty
           pkt-line ("0004").

                 pkt-line     =  data-pkt / flush-pkt

                 data-pkt     =  pkt-len pkt-payload
                 pkt-len      =  4*(HEXDIG)
                 pkt-payload  =  (pkt-len - 4)*(OCTET)

                 flush-pkt    = "0000"

           Examples (as C-style strings):

                 pkt-line          actual value
                 ---------------------------------
                 "0006a\n"         "a\n"
                 "0005a"           "a"
                 "000bfoobar\n"    "foobar\n"
                 "0004"            ""

## [](#GIT)GIT

           Part of the git(1) suite

## [](#COLOPHON)COLOPHON

           This page is part of the git (Git distributed version control
           system) project.  Information about the project can be found at 
           ⟨http://git-scm.com/⟩.  If you have a bug report for this manual
           page, see ⟨http://git-scm.com/community⟩.  This page was obtained
           from the project's upstream Git repository
           ⟨https://github.com/git/git.git⟩ on 2026-08-04.  (At that time,
           the date of the most recent commit that was found in the
           repository was 2026-08-03.)  If you discover any rendering
           problems in this HTML version of the page, or you believe there is
           a better or more up-to-date source for the page, or you have
           corrections or improvements to the information in this COLOPHON
           (which is not part of the original manual page), send a mail to
           man-pages@man7.org

    Git 2.55.0.493.g5b2471          2026-08-03          GITPROTOCOL-COMMON(5)

------------------------------------------------------------------------

Pages that refer to this page: [git(1)](../man1/git.1.html),  [gitformat-bundle(5)](../man5/gitformat-bundle.5.html),  [gitprotocol-pack(5)](../man5/gitprotocol-pack.5.html),  [gitprotocol-v2(5)](../man5/gitprotocol-v2.5.html)

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
