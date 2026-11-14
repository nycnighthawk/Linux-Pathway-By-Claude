---
{"title": "dumpcalls(1) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/dumpcalls.1.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# dumpcalls(1) --- Linux manual page

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [EXAMPLES](#EXAMPLES) \| [SEE ALSO](#SEE_ALSO) \| [NOTES](#NOTES) \| [AUTHORS](#AUTHORS) |                                   |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                          |                                   |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    DUMPCALLS(1)                                                 DUMPCALLS(1)

## [](#NAME)NAME

           dumpcalls - Dump system calls to a file.

## [](#SYNOPSIS)SYNOPSIS

           Options
           dumpcalls [ --help ] [ --version ] [ --extcap-interfaces ] [
           --extcap-dlts ] [ --extcap-interface=<interface> ] [
           --extcap-config ] [ --extcap-capture-filter=<capture filter> ] [
           --capture ] [ --fifo=<path to file or pipe> ] [ --log-level=<log
           level> ] [ --log-file=<path to file> ] [
           --include-capture-processes=<TRUE or FALSE> ] [
           --include-switch-calls=<TRUE or FALSE> ]

## [](#DESCRIPTION)DESCRIPTION

           dumpcalls is an extcap tool that allows one to capture system
           calls on a Linux system.

## [](#OPTIONS)OPTIONS

           --help
               Print program arguments. This will also list the configuration
               arguments for each plugin.

           --version
               Print the program version.

           --extcap-interfaces
               List the available interfaces.

           --extcap-interface=<interface>
               Use the specified interface.

           --extcap-dlts
               List the DLTs of the specified interface.

           --extcap-config
               List the configuration options of specified interface.

           --extcap-capture-filter=<capture filter>
               The capture filter. Must be a valid Sysdig / Falco filter.

           --capture
               Start capturing from the source specified by --plugin-source
               via the specified interface and write raw packet data to the
               location specified by --fifo.

           --fifo=<path to file or pipe>
               Save captured packet to file or send it through pipe.

           --log-level
               Set the log level

           --log-file
               Set a log file to log messages in addition to the console

           --include-capture-processes
               Include system calls for capture processes (dumpcalls,
               dumpcap, and Stratoshark) if TRUE. Defaults to FALSE.

           --include-switch-calls
               Include "switch" calls if TRUE. Defaults to FALSE.

## [](#EXAMPLES)EXAMPLES

           To see program arguments:

               dumpcalls --help

           To see program version:

               dumpcalls --version

           To see interfaces:

               dumpcalls --extcap-interfaces

           Only one interface (dumpcalls) is supported.

           Example output

               interface {value=dumpcalls}{display=Falco plugin}

           To see interface DLTs:

               dumpcalls --extcap-interface=cloudtrail --extcap-dlts

           Example output

               dlt {number=147}{name=cloudtrail}{display=USER0}

           To see interface configuration options:

               dumpcalls --extcap-interface=cloudtrail --extcap-config

           Example output

               arg {number=0}{call=--plugin-source}{display=Plugin source}{type=string}{tooltip=The plugin data source. This us usually a URL.}{placeholder=Enter a source URL…}{required=true}{group=Capture}
               arg {number=1}{call=cloudtrail-s3downloadconcurrency}{display=s3DownloadConcurrency}{type=integer}{default=1}{tooltip=Controls the number of background goroutines used to download S3 files (Default: 1)}{group=Capture}
               arg {number=2}{call=cloudtrail-sqsdelete}{display=sqsDelete}{type=boolean}{default=true}{tooltip=If true then the plugin will delete sqs messages from the queue immediately after receiving them (Default: true)}{group=Capture}
               arg {number=3}{call=cloudtrail-useasync}{display=useAsync}{type=boolean}{default=true}{tooltip=If true then async extraction optimization is enabled (Default: true)}{group=Capture}

           To capture AWS CloudTrail events from an S3 bucket:

               dumpcalls --extcap-interface=cloudtrail --fifo=/tmp/cloudtrail.pcap --plugin-source=s3://aws-cloudtrail-logs.../CloudTrail/us-east-2/... --capture

           or:

               dumpcalls --capture --extcap-interface cloudtrail --fifo ~/cloudtrail.pcap --plugin-source s3://my-cloudtrail-bucket/AWSLogs/o-abc12345/123456789012/ --cloudtrail-s3downloadconcurrency 32 --cloudtrail-s3interval 5d-2d --cloudtrail-aws-region eu-west-1

               Note

               CTRL + C should be used to stop the capture in order to ensure
               clean termination.

## [](#SEE_ALSO)SEE ALSO

           stratoshark(1), strato(1), dumpcap(1), extcap(4)

## [](#NOTES)NOTES

           dumpcalls is part of the Stratoshark distribution. The latest
           version of Stratoshark can be found at https://www.wireshark.org.

           HTML versions of the Wireshark project man pages are available at
           https://www.wireshark.org/docs/man-pages.

## [](#AUTHORS)AUTHORS

           Original Author
           Gerald Combs <gerald[AT]wireshark.org>.SH COLOPHON This page is
           part of the wireshark (Interactively dump and analyze network
           traffic) project. Information about the project can be found at 
           ⟨https://www.wireshark.org/⟩. If you have a bug report for this
           manual page, see
           ⟨https://gitlab.com/wireshark/wireshark/-/issues⟩. This page was
           obtained from the project's upstream Git repository
           ⟨https://gitlab.com/wireshark/wireshark.git⟩ on 2026-08-04. (At
           that time, the date of the most recent commit that was found in
           the repository was 2026-08-03.) If you discover any rendering
           problems in this HTML version of the page, or you believe there is
           a better or more up-to-date source for the page, or you have
           corrections or improvements to the information in this COLOPHON
           (which is not part of the original manual page), send a mail to
           man-pages@man7.org

                                    2026-01-15                   DUMPCALLS(1)

------------------------------------------------------------------------

Pages that refer to this page: [falcodump(1)](../man1/falcodump.1.html)

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
