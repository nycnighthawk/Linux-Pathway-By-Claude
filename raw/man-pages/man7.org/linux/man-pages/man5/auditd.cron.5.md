---
{"title": "auditd.cron(5) — Linux manual page", "url": "https://man7.org/linux/man-pages/man5/auditd.cron.5.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# auditd.cron(5) --- Linux manual page

+--------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [DESCRIPTION](#DESCRIPTION) \| [CONFIGURATION](#CONFIGURATION) \| [SEE ALSO](#SEE_ALSO) \| [AUTHOR](#AUTHOR) \| [COLOPHON](#COLOPHON) |                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                        |                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    AUDITD.CRON(5)       System Administration Utilities       AUDITD.CRON(5)

## [](#NAME)NAME

           auditd.conf - time-based rotation of audit logs

## [](#DESCRIPTION)DESCRIPTION

           By default, the audit daemon (auditd) supports size-based log
           rotation, where logs are rotated once they reach a specified size,
           as configured in /etc/audit/auditd.conf.  This manual describes an
           alternative method: time-based log rotation using cron.  Using
           this approach, audit logs can be rotated at specified intervals
           (hourly, daily, weekly or on a custom date), regardless of their
           size.

## [](#CONFIGURATION)CONFIGURATION

           1.Disable Size-Based Rotation:

           To enable time-based log rotation, first disable auditd's built-in
           size-based rotation by setting the following parameter in
           /etc/audit/auditd.conf:

                  max_log_file_action = ignore

           2. Configure Log Retention:

           The num_logs parameter determines the number of rotated log files
           to keep. For daily rotation, setting

                  num_logs = 7

           ensures that logs from the last seven days are retained. However,
           on busy systems, audit logs may grow rapidly, potentially leading
           to a lack of disk space. To prevent this, ensure that the
           space_left_action parameter is configured to handle low-disk-space
           situations appropriately.

           3. Apply Configuration Changes:

           After modifying the main auditd configuration file, reload auditd
           to apply the changes:

                  auditctl --signal reload

           4. Deploy the Rotation Script:

           Copy the provided auditd.cron script to the appropriate cron
           directory ( cron.daily or cron.hourly or cron.weekly , depending
           on your rotation preference). Then, ensure the file has the
           correct SELinux labels:

                  cp /usr/share/doc/audit/auditd.cron /etc/cron.daily

## [](#SEE_ALSO)SEE ALSO

           auditd.conf(5), auditd(8), cron(8).

## [](#AUTHOR)AUTHOR

           Attila Lakatos

## [](#COLOPHON)COLOPHON

           This page is part of the audit (Linux Audit) project.  Information
           about the project can be found at 
           ⟨http://people.redhat.com/sgrubb/audit/⟩.  If you have a bug report
           for this manual page, send it to linux-audit@redhat.com.  This
           page was obtained from the project's upstream Git repository
           ⟨https://github.com/linux-audit/audit-userspace.git⟩ on
           2026-08-03.  (At that time, the date of the most recent commit
           that was found in the repository was 2026-07-29.)  If you discover
           any rendering problems in this HTML version of the page, or you
           believe there is a better or more up-to-date source for the page,
           or you have corrections or improvements to the information in this
           COLOPHON (which is not part of the original manual page), send a
           mail to man-pages@man7.org

    Red Hat                          Feb 2025                  AUDITD.CRON(5)

------------------------------------------------------------------------

Pages that refer to this page: [auditd.conf(5)](../man5/auditd.conf.5.html)

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
