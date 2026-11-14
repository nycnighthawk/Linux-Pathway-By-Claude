---
{"title": "labels.conf(5) — Linux manual page", "url": "https://man7.org/linux/man-pages/man5/labels.conf.5.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# labels.conf(5) --- Linux manual page

+-------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+-------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                         |                                   |
+-------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    LABELS.CONF(5)             File Formats Manual             LABELS.CONF(5)

## [](#NAME)NAME

           labels.conf - Performance Co-Pilot labels configuration

## [](#SYNOPSIS)SYNOPSIS

           /etc/pcp/labels.conf

## [](#DESCRIPTION)DESCRIPTION

           Several Performance Co-Pilot (PCP) tools and utilities support the
           use of metric labels.  This functionality applied a hierarchical
           set of labels to each instance of every metric, as described in
           pmLookupLabels(3).

           The pmcd(1) and pmproxy(1) daemons are particularly important to
           the labels system, respectively providing the labels in real-time
           and then discovering recorded (archive) labels and indexing these
           for pmseries(1) queries using a distributed key-value service such
           as https://valkey.io/ .

           The /etc/pcp/labels.conf file is a single point of configuration
           for behaviour affecting all labels exported by pmcd or through
           tools using PMAPI local context services.  It uses the common
           ``ini'' file format and any variable it specifies that is not in
           an explicit square-bracket enclosed section is considered a
           [global] variable.

           The available configuration variables are as follows :

           machineid_hash=none|sha256
                When specified in the [global] section, controls the manner
                in which the local machine-id(5) is exported as a label.  The
                default setting (none) exports a "machineid" context label
                with value reflecting the contents of the /etc/machine-id
                file, on any platforms that provide this file.  The
                alternative (sha256) exports a "machineid_sha256" label,
                instead, and the value is the SHA256 (one-way) hash of the
                file.

## [](#SEE_ALSO)SEE ALSO

           pmcd(1), pmproxy(1), pmseries(1), PMAPI(3), pmLookupLabels(3) and
           machine-id(5).

## [](#COLOPHON)COLOPHON

           This page is part of the PCP (Performance Co-Pilot) project.
           Information about the project can be found at 
           ⟨http://www.pcp.io/⟩.  If you have a bug report for this manual
           page, send it to pcp@groups.io.  This page was obtained from the
           project's upstream Git repository
           ⟨https://github.com/performancecopilot/pcp.git⟩ on 2026-08-04.
           (At that time, the date of the most recent commit that was found
           in the repository was 2026-08-04.)  If you discover any rendering
           problems in this HTML version of the page, or you believe there is
           a better or more up-to-date source for the page, or you have
           corrections or improvements to the information in this COLOPHON
           (which is not part of the original manual page), send a mail to
           man-pages@man7.org

    Performance Co-Pilot               PCP                     LABELS.CONF(5)

------------------------------------------------------------------------

Pages that refer to this page: [pmcd(1)](../man1/pmcd.1.html),  [pmlookuplabels(3)](../man3/pmlookuplabels.3.html)

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
