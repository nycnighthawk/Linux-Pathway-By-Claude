---
{"title": "ovsdb-server(5) — Linux manual page", "url": "https://man7.org/linux/man-pages/man5/ovsdb-server.5.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# ovsdb-server(5) --- Linux manual page

+----------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [TABLE SUMMARY](#TABLE_SUMMARY) \| [Database TABLE](#Database_TABLE) \| [COLOPHON](#COLOPHON) |                                   |
+----------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                |                                   |
+----------------------------------------------------------------------------------------------------------------+-----------------------------------+

    ovsdb-server(5)            Open vSwitch Manual            ovsdb-server(5)

## [](#NAME)NAME

           ovsdb-server - _Server database schema

           Every ovsdb-server (version 2.9 or later) always hosts an instance
           of this schema, which holds information on the status and
           configuration of the server itself. This database is read-only.
           This manpage describes the schema for this database.

## [](#TABLE_SUMMARY)TABLE SUMMARY

           The following list summarizes the purpose of each of the tables in
           the _Server database.  Each table is described in more detail on a
           later page.

           Table     Purpose
           Database  Databases.

## [](#Database_TABLE)Database TABLE

           This table describes the databases hosted by the database server,
           with one row per database. As its database configuration and
           status changes, the server automatically and immediately updates
           the table to match.

           The OVSDB protocol specified in RFC 7047 does not provide a way
           for an OVSDB client to find out about some kinds of configuration
           changes, such as about databases added or removed while a client
           is connected to the server, or databases changing between
           read/write and read-only due to a transition between active and
           backup roles. This table provides a solution: clients can monitor
           the table’s contents to find out about important changes.

           Traditionally, ovsdb-server disconnects all of its clients when a
           significant configuration change occurs, because this prompts a
           well-written client to reassess what is available from the server
           when it reconnects. Because this table provides an alternative and
           more efficient way to find out about those changes, OVS 2.9 also
           introduces the set_db_change_aware RPC, documented in
           ovsdb-server(7), to allow clients to suppress this disconnection
           behavior.

           When a database is removed from the server, in addition to
           Database table updates, the server sends canceled messages, as
           described in RFC 7047 section 4.1.4, in reply to outstanding
           transactions for the removed database. The server also cancels any
           outstanding monitoring initiated by monitor or monitor_cond
           requested on the removed database, sending the monitor_canceled
           RPC described in ovsdb-server(7). Only clients that disable
           disconnection with set_db_change_aware receive these messages.

           Clients can use the _uuid column in this table as a generation
           number. The server generates a fresh _uuid every time it adds a
           database, so that removing and then re-adding a database to the
           server causes its row _uuid to change.

       Summary:
           name                          string
           model                         string, one of clustered, relay, or
                                         standalone
           schema                        optional string
           connected                     boolean
           Clustered Databases:
             leader                      boolean
             cid                         optional uuid
             sid                         optional uuid
             index                       optional integer

       Details:
           name: string
                  The database’s name, as specified in its schema.

           model: string, one of clustered, relay, or standalone
                  The storage model: standalone for a standalone or active-
                  backup database, clustered for a clustered database, relay
                  for a relay database.

           schema: optional string
                  The database schema, as a JSON string. In the case of a
                  clustered database, this is empty until it finishes joining
                  its cluster. In the case of a relay database, this is empty
                  until it connects to the relay source.

           connected: boolean
                  True if the database is connected to its storage. A
                  standalone database is always connected. A clustered
                  database is connected if the server is in contact with a
                  majority of its cluster. A relay database is connected if
                  the server is in contact with the relay source, i.e. is
                  connected to the server it syncs from. An unconnected
                  database cannot be modified and its data might be
                  unavailable or stale.

         Clustered Databases:

           These columns are most interesting and in some cases only relevant
           for clustered databases, that is, those where the model column is
           clustered.

           leader: boolean
                  True if the database is the leader in its cluster. For a
                  standalone or active-backup database, this is always true.
                  For a relay database, this is always false.

           cid: optional uuid
                  The cluster ID for this database, which is the same for all
                  of the servers that host this particular clustered
                  database. For a standalone, active-backup or relay
                  database, this is empty.

           sid: optional uuid
                  The server ID for this database, different for each server
                  that hosts a particular clustered database. A server that
                  hosts more than one clustered database will have a
                  different sid in each one. For a standalone, active-backup
                  or relay database, this is empty.

           index: optional integer
                  For a clustered database, the index of the log entry
                  currently exposed to clients. For a given server, this
                  increases monotonically. When a client switches from one
                  server to another in a cluster, it can ensure that it never
                  sees an older snapshot of data by avoiding servers that
                  have index less than the largest value they have already
                  observed.

                  For a standalone, active-backup or relay database, this is
                  empty.

## [](#COLOPHON)COLOPHON

           This page is part of the Open vSwitch (a distributed virtual
           multilayer switch) project.  Information about the project can be
           found at ⟨http://openvswitch.org/⟩.  If you have a bug report for
           this manual page, send it to bugs@openvswitch.org.  This page was
           obtained from the project's upstream Git repository
           ⟨https://github.com/openvswitch/ovs.git⟩ on 2026-08-04.  (At that
           time, the date of the most recent commit that was found in the
           repository was 2026-07-23.)  If you discover any rendering
           problems in this HTML version of the page, or you believe there is
           a better or more up-to-date source for the page, or you have
           corrections or improvements to the information in this COLOPHON
           (which is not part of the original manual page), send a mail to
           man-pages@man7.org

    Open vSwitch 3.3.90           DB Schema 1.2.0             ovsdb-server(5)

------------------------------------------------------------------------

Pages that refer to this page: [ovsdb-server(1)](../man1/ovsdb-server.1.html),  [ovsdb-server(7)](../man7/ovsdb-server.7.html)

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
