---
{"title": "slapo-dds(5) — Linux manual page", "url": "https://man7.org/linux/man-pages/man5/slapo-dds.5.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# slapo-dds(5) --- Linux manual page

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [ACCESS CONTROL](#ACCESS_CONTROL) \| [REPLICATION](#REPLICATION) \| [FILES](#FILES) \| [SEE ALSO](#SEE_ALSO) \| [AUTHOR](#AUTHOR) \| [COLOPHON](#COLOPHON) |                                   |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                     |                                   |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    SLAPO-DDS(5)               File Formats Manual               SLAPO-DDS(5)

## [](#NAME)NAME

           slapo-dds - Dynamic Directory Services overlay to slapd

## [](#SYNOPSIS)SYNOPSIS

           ETCDIR/slapd.conf

## [](#DESCRIPTION)DESCRIPTION

           The dds overlay to slapd(8) implements dynamic objects as per RFC
           2589.  The name dds stands for Dynamic Directory Services.  It
           allows one to define dynamic objects, characterized by the
           dynamicObject objectClass.

           Dynamic objects have a limited lifetime, determined by a time-to-
           live (TTL) that can be refreshed by means of a specific refresh
           extended operation.  This operation allows one to set the Client
           Refresh Period (CRP), namely the period between refreshes that is
           required to preserve the dynamic object from expiration.  The
           expiration time is computed by adding the requested TTL to the
           current time.  When dynamic objects reach the end of their
           lifetime without being further refreshed, they are automatically
           deleted.  There is no guarantee of immediate deletion, so clients
           should not count on it.

           Dynamic objects can have subordinates, provided these also are
           dynamic objects.  RFC 2589 does not specify what the behavior of a
           dynamic directory service should be when a dynamic object with
           (dynamic) subordinates expires.  In this implementation, the
           lifetime of dynamic objects with subordinates is prolonged until
           all the dynamic subordinates expire.

           This slapd.conf(5) directive adds the dds overlay to the current
           database:

           overlay dds

           The database must have a rootdn specified, otherwise, the dds
           overlay will not be able to delete expired objects. The dds
           overlay may be used with any backend that implements the add,
           modify, search, and delete operations.  Since its use may result
           in many internal entry lookups, adds and deletes, it should be
           best used in conjunction with backends that have reasonably good
           write performances.

           The config directives that are specific to the dds overlay are
           prefixed by dds-, to avoid potential conflicts with directives
           specific to the underlying database or to other stacked overlays.

           dds-max-ttl <time>
                  Specifies the max TTL value.  This is also the default TTL
                  newly created dynamic objects receive, unless
                  dds-default-ttl is set.  When the client with a refresh
                  extended operation requests a TTL higher than it,
                  sizeLimitExceeded is returned.  This value must be between
                  86400 (1 day, the default) and 31557600 (1 year plus 6
                  hours, as per RFC 2589).

           dds-min-ttl <time>
                  Specifies the min TTL value; clients requesting a lower TTL
                  by means of the refresh extended operation actually obtain
                  this value as CRP.  If set to 0 (the default), no lower
                  limit is set.

           dds-default-ttl <time>
                  Specifies the default TTL value that newly created dynamic
                  objects get.  If set to 0 (the default), the dds-max-ttl is
                  used.

           dds-interval <time>
                  Specifies the interval between expiration checks; defaults
                  to 1 hour.

           dds-tolerance <time>
                  Specifies an extra time that is added to the timer that
                  actually wakes up the thread that will delete an expired
                  dynamic object.  So the nominal lifetime of the entry is
                  that specified in the entryTtl attribute, but its lifetime
                  will actually be entryTtl + tolerance.  Note that there is
                  no guarantee that the lifetime of a dynamic object will be
                  exactly the requested TTL; due to implementation details,
                  it may be longer, which is allowed by RFC 2589.  By
                  default, tolerance is 0.

           dds-max-dynamicObjects <num>
                  Specifies the maximum number of dynamic objects that can
                  simultaneously exist within a naming context.  This allows
                  one to limit the amount of resources (mostly in terms of
                  run-queue size) that are used by dynamic objects.  By
                  default, no limit is set.

           dds-state {TRUE|false}
                  Specifies if the Dynamic Directory Services feature is
                  enabled or not.  By default it is; however, a proxy does
                  not need to keep track of dynamic objects itself, it only
                  needs to inform the frontend that support for dynamic
                  objects is available.

## [](#ACCESS_CONTROL)ACCESS CONTROL

           The dds overlay restricts the refresh operation by requiring
           manage access to the entryTtl attribute (see slapd.access(5) for
           details about the manage access privilege).  Since the entryTtl is
           an operational, NO-USER-MODIFICATION attribute, no direct write
           access to it is possible.  So the dds overlay turns refresh
           extended operation into an internal modification to the value of
           the entryTtl attribute with the relax control set.

           RFC 2589 recommends that anonymous clients should not be allowed
           to refresh a dynamic object.  This can be implemented by
           appropriately crafting access control to obtain the desired
           effect.

           Example: restrict refresh to authenticated clients

                  access to attrs=entryTtl
                       by users manage
                       by * read

           Example: restrict refresh to the creator of the dynamic object

                  access to attrs=entryTtl
                       by dnattr=creatorsName manage
                       by * read

           Another suggested usage of dynamic objects is to implement dynamic
           meetings; in this case, all the participants to the meeting are
           allowed to refresh the meeting object, but only the creator can
           delete it (otherwise it will be deleted when the TTL expires)

           Example: assuming participant is a valid DN-valued attribute,
           allow users to start a meeting and to join it; restrict refresh to
           the participants; restrict delete to the creator

                  access to dn.base="cn=Meetings"
                            attrs=children
                       by users write

                  access to dn.onelevel="cn=Meetings"
                            attrs=entry
                       by dnattr=creatorsName write
                       by * read

                  access to dn.onelevel="cn=Meetings"
                            attrs=participant
                       by dnattr=creatorsName write
                       by users selfwrite
                       by * read

                  access to dn.onelevel="cn=Meetings"
                            attrs=entryTtl
                       by dnattr=participant manage
                       by * read

## [](#REPLICATION)REPLICATION

           This implementation of RFC 2589 provides a restricted
           interpretation of how dynamic objects replicate.  Only the
           provider takes care of handling dynamic object expiration, while
           consumers simply see the dynamic object as a plain object.

           When replicating these objects, one needs to explicitly exclude
           the dynamicObject class and the entryTtl attribute.  This
           implementation of RFC 2589 introduces a new operational attribute,
           entryExpireTimestamp, that contains the expiration timestamp.
           This must be excluded from replication as well.

           The quick and dirty solution is to set schemacheck=off in the
           syncrepl configuration and, optionally, exclude the operational
           attributes from replication, using

                  syncrepl ...
                       exattrs=entryTtl,entryExpireTimestamp

           In any case the overlay must be either statically built in or run-
           time loaded by the consumer, so that it is aware of the
           entryExpireTimestamp operational attribute; however, it must not
           be configured in the shadow database.  Currently, there is no
           means to remove the dynamicObject class from the entry; this may
           be seen as a feature, since it allows one to see the dynamic
           properties of the object.

## [](#FILES)FILES

           ETCDIR/slapd.conf
                  default slapd configuration file

## [](#SEE_ALSO)SEE ALSO

           slapd.conf(5), slapd-config(5), slapd(8).

## [](#AUTHOR)AUTHOR

           Implemented by Pierangelo Masarati.

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

    OpenLDAP LDVERSION             RELEASEDATE                   SLAPO-DDS(5)

------------------------------------------------------------------------

Pages that refer to this page: [slapd.overlays(5)](../man5/slapd.overlays.5.html)

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
