---
{"title": "pmsnap(1) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/pmsnap.1.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# pmsnap(1) --- Linux manual page

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [FILES](#FILES) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                   |                                   |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    PMSNAP(1)                General Commands Manual                PMSNAP(1)

## [](#NAME)NAME

           pmsnap - generate performance summary snapshot images

## [](#SYNOPSIS)SYNOPSIS

           $PCP_BINADM_DIR/pmsnap [-NV?]  [-c configs] [-C dir] [-f format]
           [-n names] [-o dir]

## [](#DESCRIPTION)DESCRIPTION

           pmsnap is a shell script that is normally run periodically from
           crontab(1) to generate graphic images of pmchart(1) performance
           charts.  These images can be in any of the supported pmchart
           formats, including png, bmp, and jpeg, and may be incorporated
           into the content offered by the local web server.  By default
           pmsnap generates no textual output unless some error or warning
           condition is encountered.

           pmsnap generates images according to its control file,
           $PCP_PMSNAPCONTROL_PATH (or dir/control if the -C option is
           specified), and uses archives created by pmlogger(1) or PCP
           archive folios created by pmafm(1) and pmlogger_check(1).  Before
           attempting to configure pmsnap, it is strongly recommended that
           pmlogger be configured according to the descriptions in
           pmlogger_daily(1), pmlogger_check(1) and pmlogger(1).

           Once pmlogger has been configured, it is necessary to configure
           pmsnap as follows;

           1.     Edit the control file $PCP_PMSNAPCONTROL_PATH.  The syntax
                  of this file is described in the comment at the head of the
                  file and an example is supplied for one and twelve hour
                  "Summary" performance charts for the local host.  Suitable
                  arguments for pmchart are also described in the comment.
                  The user should consult pmchart for further details.  Note
                  that when pmsnap is run, it globally substitutes the string
                  LOCALHOSTNAME with the name of the local host in the
                  control file.

           2.     Test the configuration by running
                                    $PCP_BINADM_DIR/pmsnap.
                  Without any arguments pmsnap will process every non-comment
                  line in $PCP_PMSNAPCONTROL_PATH.  The output images will be
                  placed in the files named in the first field of each line
                  in the control file, with the file format appended if
                  necessary.  If these file names do not start with / or .
                  then they are assumed relative to dir, as specified with
                  the -o option.  The default dir is the current directory.
                  Note that if pmlogger has only been recently started
                  (within about the last 15 minutes), snapshot images may not
                  be produced and no error messages will be issued - the
                  reason is that pmchart can not use very short archives and
                  hence, neither can pmsnap.  For debugging purposes the -V
                  flag should be used.

           3.     Add an appropriate entry for pmsnap in the root user's
                  crontab.  An example is supplied in
                  $PCP_VAR_DIR/config/pmlogger/crontab.

           4.     Incorporate the pmsnap images into the local WWW content.
                  Usually, WWW pages use images that are relative to a
                  particular document root, so it is often convenient to use
                  the -o command line option to specify a sub-directory of
                  the local WWW content, and then create a web page in this
                  directory that shows the snapshot images with text and
                  other content appropriate to the local environment.

           A sample HTML page, suitable for the Summary snapshot may be found
           in $PCP_VAR_DIR/config/pmsnap/Summary.html.

           Although pmsnap attempts to flush stdio(3) output buffers in the
           relevant pmlogger processes before generating snapshots images,
           this may fail for assorted reasons and no error message will be
           given.

           pmsnap should not be invoked immediately after pmlogger_daily has
           rolled the logs because the new archives will be too short to
           obtain meaningful results.  Note however that pmsnap will not
           report errors from pmchart about not being able to comply with the
           -A option on very short archives.  In these cases no error will be
           reported and no output images will be produced.

## [](#OPTIONS)OPTIONS

           The available command line options are:

           -c config-pattern
                Only process lines in the control file which match the
                config-pattern regular expression in the Config column.

           -C dir
                The control file is located in the directory dir rather than
                in the default $PCP_PMSNAPCONTROL_PATH location.

           -f format
                Set output image format.  The defaults format is png.

           -n name-pattern
                Only process lines in the control file which match the name-
                pattern regular expression (see egrep(1)) in the Name column.

           -N   Enable a ``show me'' mode, where the actions are echoed, but
                not executed, in the style of ``make -n''.  Using -N in
                conjunction with -V maximizes the diagnostic capabilities for
                debugging.

           -o dir
                The output images having file names which do not start with /
                or .  will be placed in a directory relative to dir,
                otherwise the output directory is relative to the current
                directory (i.e. the default value for dir is ./).  Note that
                dir must be a writable directory path and may be on an NFS or
                CIFS file system.

           -V   Enable verbose mode.

           -?   Display usage message and exit.

           When either -n or -c are used, pmsnap will only process lines in
           the control file which match all the supplied patterns.  If no
           patterns are given, then all lines will be processed.  These
           arguments allow multiple entries for pmsnap in crontab so that
           different performance summary images can be generated at different
           times or with different frequencies.

## [](#FILES)FILES

           $PCP_PMSNAPCONTROL_PATH
                pmsnap control file

           $PCP_VAR_DIR/config/pmsnap/Summary
                summary view for pmchart

           $PCP_VAR_DIR/config/pmsnap/Summary.html
                sample HTML page for summary snapshot

           $PCP_LOG_DIR/pmlogger/<hostname>/Latest
                PCP archive folio for the host hostname, as generated by
                pmlogger_check

           $PCP_VAR_DIR/config/pmlogger/crontab
                example crontab entry

## [](#SEE_ALSO)SEE ALSO

           cron(1), crontab(1), egrep(1), pmafm(1), pmchart(1), pmlc(1),
           pmlogger(1) and pmlogger_daily(1).

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

    Performance Co-Pilot                                            PMSNAP(1)

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
