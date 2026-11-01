---
{"title": "Identity management", "url": "https://wiki.archlinux.org/title/Identity_management", "retrieved": "2026-11-01", "license": "GFDL-1.3-or-later"}
---

# Identity management

Related articles

-   [LDAP authentication](../en/LDAP_authentication.html "LDAP authentication")
-   [Security](../en/Security.html "Security")

[Identity management](https://en.wikipedia.org/wiki/Identity_management "wikipedia:Identity management") (IDM), sometimes also identity and access management (IAM), deals with how users gain a digital identity, the roles, and sometimes the permission granted to this identity.

## Software {#Software}

There is a number of software which helps doing identity management. Amongst, in alphabetical order, tools and related:

-   [Google Authenticator](../en/Google_Authenticator.html "Google Authenticator"), two-step authentication, using one time passwords.
-   [Initiative for Open Authentication](../en/Initiative_for_Open_Authentication.html "Initiative for Open Authentication"), standardization on how to get an access token for a web API call. Includes passwords, but will in future use WebAuthn.
-   kanidm, some [info here](https://fy.blackhats.net.au/blog/html/2019/09/18/announcing_kanidm_a_new_idm_project.html). Successor of LDAP, Kerberos. Server side of WebAuthn.
-   [Kerberos](../en/Kerberos.html "Kerberos"), with [Active Directory integration](../en/Active_Directory_integration.html "Active Directory integration"), [FreeIPA](../en/FreeIPA.html "FreeIPA")
-   [LDAP authentication](../en/LDAP_authentication.html "LDAP authentication"), passwords in a central server.
-   [PAM](../en/PAM.html "PAM"), Linux pluggable authentication modules. Kerberos, LDAP, kanidm, etc. can be plugged into Linux.
-   [Universal 2nd Factor](../en/Universal_2nd_Factor.html "Universal 2nd Factor"), replaced by WebAuthn.
-   [Users and groups](../en/Users_and_groups.html "Users and groups"). can be stored on a system or centrally via LDAP, kanidm.
-   [WebAuthn](../en/WebAuthn.html "WebAuthn"), browser web authentication API, replacement for password authentication, backwards compatible with Universal 2nd Factor.
