---
{"title": "cap_text_formats(7) — Linux manual page", "url": "https://man7.org/linux/man-pages/man7/cap_text_formats.7.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# cap_text_formats(7) --- Linux manual page

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [CAPABILITY TEXT FORMATS](#CAPABILITY_TEXT_FORMATS) \| [THE CAPABILITY SET TEXT FORMAT](#THE_CAPABILITY_SET_TEXT_FORMAT) \| [THE IAB TUPLE TEXT FORMAT](#THE_IAB_TUPLE_TEXT_FORMAT) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                       |                                   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    CAP_TEXT_FORMATS(7)     Linux Programmer's Manual     CAP_TEXT_FORMATS(7)

## [](#CAPABILITY_TEXT_FORMATS)CAPABILITY TEXT FORMATS

           The capability library libcap(3) employs two string formats for
           representing capabilities: the original text format for the
           standard capability `Set' and supported by the getcap(8),
           setcap(8) and capsh(8) command line tools; and the IAB-tuple text
           format, which is usable by the pam_cap(8) Linux-PAM module,
           captree(8)and capsh(8).  These text formats have extensive support
           in libcap(3), and the
           'kernel.org/pub/linux/libs/security/libcap/cap' Go package.

## [](#THE_CAPABILITY_SET_TEXT_FORMAT)THE CAPABILITY SET TEXT FORMAT

           This text format is specified in the defunct POSIX.1e draft [1]
           that introduced capabilities. It is able to represent both process
           and file capabilities.

           The textual representation of capability sets consists of one or
           more whitespace-separated clauses.  Each clause specifies some
           operations on a capability set; the set starts out with all
           capabilities lowered, and the meaning of the string is the state
           of the capability set after all the clauses have been applied in
           order.

           Each clause consists of a list of comma-separated capability names
           (or the word `all'), followed by an action-list.  An action-list
           consists of a sequence of operator flag pairs.  Legal operators
           are: `=', '+', and `-'.  Legal flags are: `e', `i', and `p'.
           These flags are case-sensitive and specify the Effective,
           Inheritable and Permitted sets respectively.

           In the capability name lists, all names are case-insensitive.  The
           special name `all' specifies all capabilities; it is equivalent to
           a list naming every capability individually.

           Unnamed capabilities can also be specified by number. This feature
           ensures that libcap can support capabilities that were not
           allocated at the time libcap was compiled. However, generally
           upgrading libcap will add names for recently allocated
           capabilities.

           The `=' operator indicates that the listed capabilities are first
           reset in all three capability sets.  The subsequent flags (which
           are optional when associated with this operator) indicate that the
           listed capabilities for the corresponding set are to be raised.
           For example: "all=p" means lower every capability in the Effective
           and Inheritable sets but raise all of the Permitted capabilities;
           or, "cap_fowner=ep" means raise the Effective and Permitted
           override-file-ownership capability, while lowering this
           Inheritable capability.

           In the case that the leading operator is `=', and no list of
           capabilities is provided, the action-list is assumed to refer to
           `all' capabilities.  For example, the following three clauses are
           equivalent to each other (and indicate a completely empty
           capability set): "all="; "="; "cap_chown,<every-other-
           capability>=".

           The operators, `+' and `-' both require an explicit preceding
           capability list and one or more explicit trailing flags.  The `+'
           operator will raise all of the listed capabilities in the flagged
           capability sets.  The `-' operator will lower all of the listed
           capabilities in the flagged capability sets.  For example: "all+p"
           will raise all of the Permitted capabilities and "cap_fowner-i"
           will lower the override-file-ownership in the Inheritable set.

           The action list can consist of multiple operator flag pairs; the
           actions are performed in left-to-right order.  Thus, for example,
           "cap_fowner+p-i" is equivalent to "cap_fowner+p cap_fowner-i".  As
           another example, "cap_fowner+pe-i" and "cap_fowner=+pe" are
           equivalent.

## [](#THE_IAB_TUPLE_TEXT_FORMAT)THE IAB TUPLE TEXT FORMAT

           This format is a pure Linux extension. It started out life as the
           format used by pam_cap(8) and can be employed by capsh(8).

           The IAB tuple text format is a comma separated list of capability
           values. Each capability is prefixed by nothing (or %) (Inh); !
           (Bound, but think Blocked); ^ (Amb). Or, some combination thereof.
           Since the Amb vector is constrained to be no greater than the Inh
           vector, ^ is equivalent to %^. Further, unless B is non-zero, %
           can be omitted. The following are legal text representations:
           "!%cap_chown" (Bound but Inh), "!cap_chown,^cap_chown" (Bound,
           Inh+Amb). "cap_setuid,!cap_chown" (Inh, Bound). As noted above,
           this text representation is used in the configuration file syntax
           (see capability.conf(5)) for the pam_cap(8) Linux-PAM security
           module.

## [](#SEE_ALSO)SEE ALSO

           [1] A copy of the last POSIX.1e draft for security extensions can
           be downloaded from the https://sites.google.com/site/fullycapable/
           website. Please report bugs as directed at that site.

           Related manual pages: libcap(3), capsh(1), setcap(8), getcap(8),
           captree(8), pam_cap(8), cap_from_text(3), cap_iab(3).

## [](#COLOPHON)COLOPHON

           This page is part of the libcap (capabilities commands and
           library) project.  Information about the project can be found at
           ⟨https://sites.google.com/site/fullycapable/⟩.  If you have a bug
           report for this manual page, send it to morgan@kernel.org (please
           put "libcap" in the Subject line).  This page was obtained from
           the project's upstream Git repository
           ⟨https://git.kernel.org/pub/scm/libs/libcap/libcap.git/⟩ on
           2026-08-04.  (At that time, the date of the most recent commit
           that was found in the repository was 2026-07-30.)  If you discover
           any rendering problems in this HTML version of the page, or you
           believe there is a better or more up-to-date source for the page,
           or you have corrections or improvements to the information in this
           COLOPHON (which is not part of the original manual page), send a
           mail to man-pages@man7.org

                                    2025-03-19            CAP_TEXT_FORMATS(7)

------------------------------------------------------------------------

Pages that refer to this page: [capsh(1)](../man1/capsh.1.html),  [cap_from_text(3)](../man3/cap_from_text.3.html),  [capability.conf(5)](../man5/capability.conf.5.html),  [rpm-spec(5)](../man5/rpm-spec.5.html),  [tmpfiles.d(5)](../man5/tmpfiles.d.5.html),  [captree(8)](../man8/captree.8.html),  [getpcaps(8)](../man8/getpcaps.8.html),  [pam_cap(8)](../man8/pam_cap.8.html),  [setcap(8)](../man8/setcap.8.html)

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
