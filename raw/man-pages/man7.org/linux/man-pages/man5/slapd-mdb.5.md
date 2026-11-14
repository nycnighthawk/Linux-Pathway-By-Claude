---
{"title": "slapd-mdb(5) — Linux manual page", "url": "https://man7.org/linux/man-pages/man5/slapd-mdb.5.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# slapd-mdb(5) --- Linux manual page

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [CONFIGURATION](#CONFIGURATION) \| [ACCESS CONTROL](#ACCESS_CONTROL) \| [FILES](#FILES) \| [SEE ALSO](#SEE_ALSO) \| [ACKNOWLEDGEMENTS](#ACKNOWLEDGEMENTS) \| [COLOPHON](#COLOPHON) |                                   |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                                             |                                   |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    SLAPD-MDB(5)               File Formats Manual               SLAPD-MDB(5)

## [](#NAME)NAME

           slapd-mdb - Memory-Mapped DB backend to slapd

## [](#SYNOPSIS)SYNOPSIS

           ETCDIR/slapd.conf

## [](#DESCRIPTION)DESCRIPTION

           The mdb backend to slapd(8) uses OpenLDAP's Lightning Memory-
           Mapped DB (LMDB) library to store data.  It relies completely on
           the underlying operating system for memory management and does no
           caching of its own. It is the recommended primary database
           backend.

           The mdb backend uses a hierarchical database layout which supports
           subtree renames.

## [](#CONFIGURATION)CONFIGURATION

           These slapd.conf options apply to the mdb backend.  That is, they
           must follow a "backend mdb" line and come before any subsequent
           "backend" or "database" lines.

           idlexp <exp>
                  Specify a power of 2 for the maximum size of an index slot.
                  The default is 16, yielding a maximum slot size of 2^16 or
                  65536.  Once set, this option applies to every mdb database
                  instance.  The specified value must be in the range of
                  16-30.

           These slapd.conf options apply to the mdb backend database.  That
           is, they must follow a "database mdb" line and come before any
           subsequent "backend" or "database" lines.  Other database options
           are described in the slapd.conf(5) manual page.

           checkpoint <kbyte> <min>
                  Specify the frequency for flushing the database disk
                  buffers.  This setting is only needed if the dbnosync
                  option is used.  The checkpoint will occur if either
                  <kbyte> data has been written or <min> minutes have passed
                  since the last checkpoint.  Both arguments default to zero,
                  in which case they are ignored. When the <min> argument is
                  non-zero, an internal task will run every <min> minutes to
                  perform the checkpoint.  Note: currently the <kbyte>
                  setting is unimplemented.

           dbnosync
                  Specify that on-disk database contents should not be
                  immediately synchronized with in memory changes.  Enabling
                  this option may improve performance at the expense of data
                  security. In particular, if the operating system crashes
                  before changes are flushed, some number of transactions may
                  be lost.  By default, a full data flush/sync is performed
                  when each transaction is committed.

           dbpagesize  <bytes>
                  Specify the page size to use for the database, in bytes.
                  The default depends on the underlying filesystem's block
                  size (typically 4096 or 8192).  The value must be a power
                  of two and the maximum is 65536.  This setting usually
                  should not need to be changed, but setting a larger
                  pagesize also increases the maximum length of keys so it
                  may be useful to support longer values when multival is
                  used.  This setting only takes effect when a database is
                  being newly created.

           directory <directory>
                  Specify the directory where the LMDB files containing this
                  database and associated indexes live.  A separate directory
                  must be specified for each database.  The default is
                  LOCALSTATEDIR/openldap-data.

           envflags {nosync,nometasync,writemap,mapasync,nordahead}
                  Specify flags for finer-grained control of the LMDB
                  library's operation.

                  nosync This is exactly the same as the dbnosync directive.

                  nometasync
                         Flush the data on a commit, but skip the sync of the
                         meta page. This mode is slightly faster than doing a
                         full sync, but can potentially lose the last
                         committed transaction if the operating system
                         crashes. If both nometasync and nosync are set, the
                         nosync flag takes precedence.

                  writemap
                         Use a writable memory map instead of just read-only.
                         This speeds up write operations but makes the
                         database vulnerable to corruption in case any bugs
                         in slapd cause stray writes into the mmap region.

                  mapasync
                         When using a writable memory map and performing
                         flushes on each commit, use an asynchronous flush
                         instead of a synchronous flush (the default). This
                         option has no effect if writemap has not been set.
                         It also has no effect if nosync is set.

                  nordahead
                         Turn off file readahead. Usually the OS performs
                         readahead on every read request. This usually boosts
                         read performance but can be harmful to random access
                         read performance if the system's memory is full and
                         the DB is larger than RAM. This option is not
                         implemented on Windows.

           index {<attrlist>|default} [pres,eq,approx,sub,<special>]
                  Specify the indexes to maintain for the given attribute (or
                  list of attributes).  Some attributes only support a subset
                  of indexes.  If only an <attr> is given, the indices
                  specified for default are maintained.  Note that setting a
                  default does not imply that all attributes will be indexed.
                  Also, an eq index is always implicitly configured for the
                  objectClass attribute and any attempts to change this index
                  are ignored.

                  A number of special index parameters may be specified.  The
                  index type sub can be decomposed into subinitial,
                  subany, and subfinal indices.  The special type nolang may
                  be specified to disallow use of this index by language
                  subtypes.  The special type nosubtypes may be specified to
                  disallow use of this index by named subtypes.  Note:
                  changing index settings in slapd.conf(5) requires
                  rebuilding indices, see slapindex(8); changing index
                  settings dynamically by LDAPModifying "cn=config"
                  automatically causes rebuilding of the indices online in a
                  background task.

           maxentrysize <bytes>
                  Specify the maximum size of an entry in bytes. Attempts to
                  store an entry larger than this size will be rejected with
                  the error LDAP_ADMINLIMIT_EXCEEDED. The default is 0, which
                  is unlimited.

           maxreaders <integer>
                  Specify the maximum number of threads that may have
                  concurrent read access to the database. Tools such as
                  slapcat count as a single thread, in addition to threads in
                  any active slapd processes. The default is 126.

           maxsize <bytes>
                  Specify the maximum size of the database in bytes. A memory
                  map of this size is allocated at startup time and the
                  database will not be allowed to grow beyond this size. The
                  default is 10485760 bytes. This setting may be changed
                  upward if the configured limit needs to be increased.

                  Note: It is important to set this to as large a value as
                  possible, (relative to anticipated growth of the actual
                  data over time) since growing the size later may not be
                  practical when the system is under heavy load.

           mode <integer>
                  Specify the file protection mode that newly created
                  database files should have.  The default is 0600.

           multival {<attrlist>|default} <integer hi>,<integer lo>
                  Specify the number of values for which a multivalued
                  attribute is stored in a separate table. Normally entries
                  are stored as a single blob inside the database. When an
                  entry gets very large or contains attributes with a very
                  large number of values, modifications on that entry may get
                  very slow. Splitting the large attributes out to a separate
                  table can improve the performance of modification
                  operations.  The threshold is specified as a pair of
                  integers. If the number of values exceeds the hi threshold
                  the values will be split out. If a modification deletes
                  enough values to bring an attribute below the lo threshold
                  the values will be removed from the separate table and
                  merged back into the main entry blob.  The threshold can be
                  set for a specific list of attributes, or the default can
                  be configured for all other attributes.  The default value
                  for both hi and lo thresholds is UINT_MAX, which keeps all
                  attributes in the main blob.

           rtxnsize <entries>
                  Specify the maximum number of entries to process in a
                  single read transaction when executing a large search.
                  Long-lived read transactions prevent old database pages
                  from being reused in write transactions, and so can cause
                  significant growth of the database file when there is heavy
                  write traffic. This setting causes the read transaction in
                  large searches to be released and reacquired after the
                  given number of entries has been read, to give writers the
                  opportunity to reclaim old database pages. The default is
                  10000.

           searchstack <depth>
                  Specify the depth of the stack used for search filter
                  evaluation.  Search filters are evaluated on a stack to
                  accommodate nested AND / OR clauses. An individual stack is
                  assigned to each server thread.  The depth of the stack
                  determines how complex a filter can be evaluated without
                  requiring any additional memory allocation. Filters that
                  are nested deeper than the search stack depth will cause a
                  separate stack to be allocated for that particular search
                  operation. These allocations can have a major negative
                  impact on server performance, but specifying too much stack
                  will also consume a great deal of memory.  Each search
                  stack uses 512K bytes per level. The default stack depth is
                  16, thus 8MB per thread is used.

           crypto <module>
                  Load an encryption module to use for encrypting the
                  database. The LMDB source code includes an example
                  encryption module. By default there is no encryption.

           passphrase <pass>
                  The passphrase to use for encrypting the database. The
                  crypto module must also be configured.

## [](#ACCESS_CONTROL)ACCESS CONTROL

           The mdb backend honors access control semantics as indicated in
           slapd.access(5).

## [](#FILES)FILES

           ETCDIR/slapd.conf
                  default slapd configuration file

## [](#SEE_ALSO)SEE ALSO

           slapd.conf(5), slapd-config(5), slapd(8), slapadd(8), slapcat(8),
           slapindex(8), slapmodify(8), OpenLDAP LMDB documentation.

## [](#ACKNOWLEDGEMENTS)ACKNOWLEDGEMENTS

           OpenLDAP Software is developed and maintained by The OpenLDAP
           Project <http://www.openldap.org/>.  OpenLDAP Software is derived
           from the University of Michigan LDAP 3.3 Release.  Written by
           Howard Chu.

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

    OpenLDAP LDVERSION             RELEASEDATE                   SLAPD-MDB(5)

------------------------------------------------------------------------

Pages that refer to this page: [slapd.access(5)](../man5/slapd.access.5.html),  [slapd.backends(5)](../man5/slapd.backends.5.html),  [slapd.overlays(5)](../man5/slapd.overlays.5.html),  [slapo-accesslog(5)](../man5/slapo-accesslog.5.html),  [slapo-refint(5)](../man5/slapo-refint.5.html),  [slapo-translucent(5)](../man5/slapo-translucent.5.html),  [slapo-unique(5)](../man5/slapo-unique.5.html),  [slapcat(8)](../man8/slapcat.8.html),  [slapschema(8)](../man8/slapschema.8.html)

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
