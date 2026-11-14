---
{"title": "slapo-pcache(5) — Linux manual page", "url": "https://man7.org/linux/man-pages/man5/slapo-pcache.5.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# slapo-pcache(5) --- Linux manual page

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [BACKWARD COMPATIBILITY](#BACKWARD_COMPATIBILITY) \| [CAVEATS](#CAVEATS) \| [FILES](#FILES) \| [SEE ALSO](#SEE_ALSO) \| [AUTHOR](#AUTHOR) \| [COLOPHON](#COLOPHON) |                                   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                             |                                   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    SLAPO-PCACHE(5)            File Formats Manual            SLAPO-PCACHE(5)

## [](#NAME)NAME

           slapo-pcache - proxy cache overlay to slapd

## [](#SYNOPSIS)SYNOPSIS

           ETCDIR/slapd.conf

## [](#DESCRIPTION)DESCRIPTION

           The pcache overlay to slapd(8) allows caching of LDAP search
           requests (queries) in a local database.  For an incoming query,
           the proxy cache determines its corresponding template. If the
           template was specified as cacheable using the pcacheTemplate
           directive and the request is contained in a cached request, it is
           answered from the proxy cache.  Otherwise, the search is performed
           as usual and cacheable search results are saved in the cache for
           use in future queries.

           A template is defined by a filter string and an index identifying
           a set of attributes. The template string for a query can be
           obtained by removing assertion values from the RFC 4515
           representation of its search filter. A query belongs to a template
           if its template string and set of projected attributes correspond
           to a cacheable template.  Examples of template strings are
           (mail=), (|(sn=)(cn=)), (&(sn=)(givenName=)).

           The config directives that are specific to the pcache overlay can
           be prefixed by pcache-, to avoid conflicts with directives
           specific to the underlying database or to other stacked overlays.
           This may be particularly useful for those directives that refer to
           the backend used for local storage.  The following cache specific
           directives can be used to configure the proxy cache:

           overlay pcache
                  This directive adds the proxy cache overlay to the current
                  backend. The proxy cache overlay may be used with any
                  backend but is intended for use with the ldap, meta, and
                  sql backends. Please note that the underlying backend must
                  have a configured rootdn.

           pcache <database> <max_entries> <numattrsets> <entry_limit>
           <cc_period>
                  The directive enables proxy caching in the current backend
                  and sets general cache parameters. A <database> backend
                  will be used internally to maintain the cached entries. The
                  chosen database will need to be configured as well, as
                  shown below. Cache replacement is invoked when the cache
                  size grows to <max_entries> entries and continues till the
                  cache size drops below this size.  <numattrsets> should be
                  equal to the number of following pcacheAttrset directives.
                  Queries are cached only if they correspond to a cacheable
                  template (specified by the pcacheTemplate directive) and
                  the number of entries returned is less than <entry_limit>.
                  Consistency check is performed every <cc_period> duration
                  (specified in secs). In each cycle queries with expired
                  "time to live(TTL)" are removed. A sample cache
                  configuration is:

                  pcache mdb 10000 1 50 100

           pcacheAttrset <index> <attrs...>
                  Used to associate a set of attributes <attrs..> with an
                  <index>. Each attribute set is associated with an integer
                  from 0 to <numattrsets>-1. These indices are used by the
                  pcacheTemplate directive to define cacheable templates.  A
                  set of attributes cannot be empty.  A set of attributes can
                  contain the special attributes "*" (all user attributes),
                  "+" (all operational attributes) or both; in the latter
                  case, any other attribute is redundant and should be
                  avoided for clarity.  A set of attributes can contain "1.1"
                  as the only attribute; in this case, only the presence of
                  the entries is cached.  Attributes prefixed by "undef:"
                  need not be present in the schema.  The "undef" keyword
                  cannot be used with the slapd-mdb(5) backend as it requires
                  all schema elements be fully defined.

           pcacheMaxQueries <queries>
                  Specify the maximum number of queries to cache. The default
                  is 10000.

           pcacheValidate { TRUE | FALSE }
                  Check whether the results of a query being cached can
                  actually be returned from the cache by the proxy DSA.  When
                  enabled, the entries being returned while caching the
                  results of a query are checked to ensure consistency with
                  the schema known to the proxy DSA.  In case of failure, the
                  query is not cached.  By default, the check is off.

           pcacheOffline { TRUE | FALSE }
                  Set the cache to offline mode. While offline, the
                  consistency checker will be stopped and no expirations will
                  occur. This allows the cache contents to be used
                  indefinitely while the proxy is cut off from network access
                  to the remote DSA.  The default is FALSE, i.e. consistency
                  checks and expirations will be performed.

           pcachePersist { TRUE | FALSE }
                  Specify whether the cached queries should be saved across
                  restarts of the caching proxy, to provide hot startup of
                  the cache.  Only non-expired queries are reloaded.  The
                  default is FALSE.

                  CAVEAT: of course, the configuration of the proxy cache
                  must not change across restarts; the pcache overlay does
                  not perform any consistency checks in this sense.  In
                  detail, this option should be disabled unless the existing
                  pcacheAttrset and pcacheTemplate directives are not changed
                  neither in order nor in contents.  If new sets and
                  templates are added, or if other details of the pcache
                  overlay configuration changed, this feature should not be
                  affected.

           pcacheTemplate <template_string> <attrset_index> <ttl> [<negttl>
           [<limitttl> [<ttr>]]]
                  Specifies a cacheable template and "time to live" <ttl> of
                  queries belonging to the template. An optional <negttl> can
                  be used to specify that negative results (i.e., queries
                  that returned zero entries) should also be cached for the
                  specified amount of time. Negative results are not cached
                  by default (<negttl> set to 0).  An optional <limitttl> can
                  be used to specify that results hitting a sizelimit should
                  also be cached for the specified amount of time.  Results
                  hitting a sizelimit are not cached by default (<limitttl>
                  set to 0).  An optional <ttr> "time to refresh" can be used
                  to specify that cached entries should be automatically
                  refreshed after a certain time. Entries will only be
                  refreshed while they have not expired, so the <ttl> should
                  be larger than the <ttr> for this option to be useful.
                  Entries are not refreshed by default (<ttr> set to 0).

           pcacheBind <filter_template> <attrset_index> <ttr> <scope> <base>
                  Specifies a template for caching Simple Bind credentials
                  based on an already defined pcacheTemplate. The
                  <filter_template> is similar to a <template_string> except
                  that it may have some values present. Its purpose is to
                  allow the overlay to generate filters similar to what other
                  applications do when they do a Search immediately before a
                  Bind. E.g., if a client like nss_ldap is configured to
                  search for a user with the filter
                  "(&(objectClass=posixAccount)(uid=<username>))" then the
                  corresponding template
                  "(&(objectClass=posixAccount)(uid=))" should be used here.
                  When converted to a regular template e.g.
                  "(&(objectClass=)(uid=))" this template and the
                  <attrset_index> must match an already defined
                  pcacheTemplate clause. The "time to refresh" <ttr>
                  determines the time interval after which the cached
                  credentials may be refreshed. The first Bind request that
                  occurs after that time will trigger the refresh attempt.
                  Refreshes are not performed when the overlay is Offline.
                  There is no "time to live" parameter for the Bind
                  credentials; the credentials will expire according to the
                  pcacheTemplate ttl. The <scope> and <base> should match the
                  search scope and base used by the authentication clients.
                  The cached credentials are not stored in cleartext, they
                  are hashed using the default password hash.  By default
                  Bind caching is not enabled.

           pcachePosition { head | tail }
                  Specifies whether the response callback should be placed at
                  the tail (the default) or at the head (actually, wherever
                  the stacking sequence would make it appear) of the callback
                  list.  This affects how the overlay interacts with other
                  overlays, since the proxycache overlay should be executed
                  as early as possible (and thus configured as late as
                  possible), to get a chance to return the cached results;
                  however, if executed early at response, it would cache
                  entries that may be later "massaged" by other databases and
                  thus returned after massaging the first time, and before
                  massaging when cached.

           There are some constraints:

                  all values must be positive;

                  <entry_limit> must be less than or equal to <max_entries>;

                  <numattrsets> attribute sets SHOULD be defined by using the
                  directive pcacheAttrset;

                  all attribute sets SHOULD be referenced by (at least) one
                  pcacheTemplate directive;

           The following adds a template with filter string
           (&(sn=)(givenName=)) and attributes mail, postaladdress,
           telephonenumber and a TTL of 1 hour.

                  pcacheAttrset 0 mail postaladdress telephonenumber
                  pcacheTemplate (&(sn=)(givenName=)) 0 3600

           Directives for configuring the underlying database must also be
           given, as shown here:

                  directory /var/tmp/cache
                  maxsize   1073741824

           Any valid directives for the chosen database type may be used.
           Indexing should be used as appropriate for the queries being
           handled. In addition, an equality index on the pcacheQueryid
           attribute should be configured, to assist in the removal of
           expired query data.

## [](#BACKWARD_COMPATIBILITY)BACKWARD COMPATIBILITY

           The configuration keywords have been renamed and the older form is
           deprecated. These older keywords are still recognized but may
           disappear in future releases.

           proxycache
                  use pcache

           proxyattrset
                  use pcacheAttrset

           proxycachequeries
                  use pcacheMaxQueries

           proxycheckcacheability
                  use pcacheValidate

           proxysavequeries
                  use pcachePersist

           proxytemplate
                  use pcacheTemplate

           response-callback
                  use pcachePosition

## [](#CAVEATS)CAVEATS

           Caching data is prone to inconsistencies because updates on the
           remote server will not be reflected in the response of the cache
           at least (and at most) for the duration of the pcacheTemplate TTL.
           These inconsistencies can be minimized by careful use of the TTR.

           The proxy cache overlay requires a full result set of data to
           properly function. Therefore it will strip out the paged results
           control if it is requested by the client.

           The remote server should expose the objectClass attribute because
           the underlying database that actually caches the entries may need
           it for optimal local processing of the queries.

           The proxy server should contain all the schema information
           required for caching.  Significantly, it needs the schema of
           attributes used in the query templates.  If the objectClass
           attribute is used in a query template, it needs the definition of
           the objectClasses of the entries it is supposed to cache.  It is
           the responsibility of the proxy administrator to keep the proxy
           schema lined up with that of the proxied server.

           Another potential (and subtle) inconsistency may occur when data
           is retrieved with different identities and specific per-identity
           access control is enforced by the remote server.  If data was
           retrieved with an identity that collected only partial results
           because of access rules enforcement on the remote server, other
           users with different access privileges on the remote server will
           get different results from the remote server and from the cache.
           If those users have higher access privileges on the remote server,
           they will get from the cache only a subset of the results they
           would get directly from the remote server; but if they have lower
           access privileges, they will get from the cache a superset of the
           results they would get directly from the remote server.  Either
           occurrence may or may not be acceptable, based on the security
           policy of the cache and of the remote server.  It is important to
           note that in this case the proxy is violating the security of the
           remote server by disclosing to an identity data that was collected
           by another identity.  For this reason, it is suggested that, when
           using back-ldap, proxy caching be used in conjunction with the
           identity assertion feature of slapd-ldap(5) (see the idassert-bind
           and the idassert-authz statements), so that remote server
           interrogation occurs with a vanilla identity that has some
           relatively high search and read access privileges, and the "real"
           access control is delegated to the proxy's ACLs.  Beware that
           since only the cached fraction of the real datum is available to
           the cache, it may not be possible to enforce the same access rules
           that are defined on the remote server.  When security is a
           concern, cached proxy access must be carefully tailored.

## [](#FILES)FILES

           ETCDIR/slapd.conf
                  default slapd configuration file

## [](#SEE_ALSO)SEE ALSO

           slapd.conf(5), slapd-config(5), slapd-ldap(5), slapd-meta(5),
           slapd-sql(5), slapd(8).

## [](#AUTHOR)AUTHOR

           Originally implemented by Apurva Kumar as an extension to back-
           meta; turned into an overlay by Howard Chu.

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

    OpenLDAP LDVERSION             RELEASEDATE                SLAPO-PCACHE(5)

------------------------------------------------------------------------

Pages that refer to this page: [slapd-asyncmeta(5)](../man5/slapd-asyncmeta.5.html),  [slapd-ldap(5)](../man5/slapd-ldap.5.html),  [slapd-meta(5)](../man5/slapd-meta.5.html),  [slapd.overlays(5)](../man5/slapd.overlays.5.html),  [slapd-sql(5)](../man5/slapd-sql.5.html)

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
