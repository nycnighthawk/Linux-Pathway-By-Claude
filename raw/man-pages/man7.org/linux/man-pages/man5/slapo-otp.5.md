---
{"title": "slapo-otp(5) — Linux manual page", "url": "https://man7.org/linux/man-pages/man5/slapo-otp.5.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# slapo-otp(5) --- Linux manual page

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [CONFIGURATION](#CONFIGURATION) \| [SEE ALSO](#SEE_ALSO) \| [ACKNOWLEDGEMENT](#ACKNOWLEDGEMENT) \| [COLOPHON](#COLOPHON) |                                   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                   |                                   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    SLAPO_OTP(5)               File Formats Manual               SLAPO_OTP(5)

## [](#NAME)NAME

           slapo-otp - OATH One-Time Password module

## [](#SYNOPSIS)SYNOPSIS

           moduleload otp.la

## [](#DESCRIPTION)DESCRIPTION

           The otp module allows time-based one-time password, AKA
           "authenticator-style", and HMAC-based one-time password
           authentication to be used in conjunction with a standard LDAP
           password for two-factor authentication.

           With this module, users would use their password, followed with
           the one-time password in the password prompt to authenticate.

           The password needed for a user to authenticate is calculated based
           on a counter (current time in case of TOTP) and a key that is
           referenced in the user's LDAP entry. Since the password is based
           on the time or number of uses, it changes periodically. Once used,
           it cannot be used again so keyloggers and shoulder-surfers are
           thwarted. A mobile phone application, such as the Google
           Authenticator or YubiKey (a prover), can be used to calculate the
           user's current one-time password, which is expressed as a (usually
           six-digit) number.

           Alternatively, the value can be calculated by some other
           application with access to the user's key and delivered to the
           user through SMS or some other channel. When prompted to
           authenticate, the user merely appends the code provided by the
           prover at the end of their password when authenticating.

           This implementation complies with RFC 4226 HOTP HMAC-Based One
           Time Passwords and RFC 6238 TOTP Time-based One Time Passwords and
           includes support for the SHA-1, SHA-256, and SHA-512 HMAC
           algorithms.

           The HMAC key used in the OTP computation is stored in the
           oathOTPToken entry referenced in the user's LDAP entry and the
           parameters are stored in the oathOTPParams LDAP entry referenced
           in the token.

## [](#CONFIGURATION)CONFIGURATION

           Once the module is configured on the database, it will intercept
           LDAP simple binds for users whose LDAP entry has any of the
           oathOTPUser derived objectlasses attached to it. The attributes
           linking the user and the shared secret are:

                  oathTOTPToken: <dn>
                         Mandatory for oathTOTPUser, indicates that the named
                         entry is designated to hold the time-based one-time
                         password shared secret and the last password used.

                  oathHOTPToken: <dn>
                         Mandatory for oathHOTPUser, indicates that the named
                         entry is designated to hold the one-time password
                         shared secret and the last password used.

                  oathTOTPParams: <dn>
                         Mandatory for oathTOTPToken, indicates that the
                         named entry is designated to hold the parameters to
                         generate time-based one-time password shared secret:
                         its length and algorithm to use as well as the
                         length of each time step and the grace period.

                  oathHOTPParams: <dn>
                         Mandatory for oathHOTPToken, indicates that the
                         named entry is designated to hold the parameters to
                         generate one-time password shared secret: its length
                         and algorithm to use as well as the permitted number
                         of passwords to skip.

           The overlay also intercepts LDAP Compare requests against the
           oathSecret attribute of an oathTOTPToken or oathHOTPToken entry
           and checks the asserted value against the configured secret. This
           is subject to compare access to the attribute.

           The following parts of the OATH-LDAP schema are implemented.

           General attributes:

                  oathSecret: <data>
                         The shared secret is stored here as raw bytes.

                  oathOTPLength: <length>
                         The password length, usually 6.

                  oathHMACAlgorithm: <OID>
                         The OID of the hash algorithm to use as defined in
                         RFC 8018.  Supported algorithms include SHA1,
                         SHA224, SHA256, SHA384 and SHA512.

           The HOTP attributes:

                  oathHOTPLookAhead: <number>
                         The number of successive HOTP tokens that can be
                         skipped.

                  oathHOTPCounter: <number>
                         The order of the last HOTP token successfully
                         redeemed by the user.

           The TOTP attributes:

                  oathTOTPTimeStepPeriod: <seconds>
                         The length of the time-step period for TOTP
                         calculation.

                  oathTOTPLastTimeStep: <number>
                         The order of the last TOTP token successfully
                         redeemed by the user.

                  oathTOTPTimeStepWindow: <number>
                         The number of time periods around the current time
                         to try when checking the password provided by the
                         user.

                  oathTOTPTimeStepDrift: <number>
                         If the client didn't provide the correct token but
                         it still fit with oathTOTPTimeStepWindow above, this
                         attribute records the current offset to provide for
                         slow clock drift of the client device.

## [](#SEE_ALSO)SEE ALSO

           slapd-config(5).

## [](#ACKNOWLEDGEMENT)ACKNOWLEDGEMENT

           This work was developed by Ondřej Kuzník and Howard Chu of Symas
           Corporation for inclusion in OpenLDAP Software.

           This work reuses the OATH-LDAP schema developed by Michael
           Ströder.

## [](#COLOPHON)COLOPHON

           This page is part of the OpenLDAP (an open source implementation
           of the Lightweight Directory Access Protocol) project.
           Information about the project can be found at 
           ⟨http://www.openldap.org/⟩.  If you have a bug report for this
           manual page, see ⟨http://www.openldap.org/its/⟩.  This page was
           obtained from the project's upstream Git repository
           ⟨https://git.openldap.org/openldap/openldap.git⟩ on 2026-08-04.
           (At that time, the date of the most recent commit that was found
           in the repository was 2026-08-03.)  If you discover any rendering
           problems in this HTML version of the page, or you believe there is
           a better or more up-to-date source for the page, or you have
           corrections or improvements to the information in this COLOPHON
           (which is not part of the original manual page), send a mail to
           man-pages@man7.org

    SLAPO-OTP                       2018/6/29                    SLAPO_OTP(5)

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
