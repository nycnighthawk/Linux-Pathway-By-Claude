---
{"title": "falcodump(1) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/falcodump.1.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# falcodump(1) --- Linux manual page

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [PLUGINS](#PLUGINS) \| [EXAMPLES](#EXAMPLES) \| [SEE ALSO](#SEE_ALSO) \| [NOTES](#NOTES) \| [AUTHORS](#AUTHORS) |                                   |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                 |                                   |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    FALCODUMP(1)                                                 FALCODUMP(1)

## [](#NAME)NAME

           falcodump - Dump log data to a file using a Falco source plugin.

## [](#SYNOPSIS)SYNOPSIS

           Common options
           falcodump [ --help ] [ --version ] [ --plugin-api-version ] [
           --extcap-interfaces ] [ --extcap-dlts ] [
           --extcap-interface=<interface> ] [ --extcap-config ] [
           --extcap-capture-filter=<capture filter> ] [ --capture ] [
           --fifo=<path to file or pipe> ] [ --plugin-source=<source path or
           URL> ] [ --log-level=<log level> ] [ --log-file=<path to file> ]

           CloudTrail plugin options
           [ --cloudtrail-s3downloadconcurrency=<number of concurrent
           downloads> ] [ --cloudtrail-s3interval=<timeframe> ] [
           --cloudtrail-s3accountlist=<comma separated account IDs> ] [
           --cloudtrail-sqsdelete=<true or false> ] [
           --cloudtrail-useasync=<true or false> ] [
           --cloudtrail-uses3sns=<true or false> ] [
           --cloudtrail-aws-region=<AWS region> ] [
           --cloudtrail-aws-profile=<AWS profile> ] [
           --cloudtrail-aws-config=<path> ] [
           --cloudtrail-aws-credentials=<path to file> ]

## [](#DESCRIPTION)DESCRIPTION

           falcodump is an extcap tool that allows one to capture log
           messages from cloud providers.

           Each plugin is listed as a separate interface. For example, the
           Kubernetes audit plugin is listed as “k8saudit” and the AWS
           CloudTrail plugin is listed as “cloudtrail”.

## [](#OPTIONS)OPTIONS

           --help
               Print program arguments. This will also list the configuration
               arguments for each plugin.

           --version
               Print the program version.

           --plugin-api-version
               Print the Falco plugin API version.

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

           --plugin-source=<source path or URL>
               Capture from the specified location.

           --log-level
               Set the log level

           --log-file
               Set a log file to log messages in addition to the console

## [](#PLUGINS)PLUGINS

       cloudtrail (AWS CloudTrail)
           --cloudtrail-s3downloadconcurrency
               Controls the number of background goroutines used to download
               S3 files (Default: 32)

           --cloudtrail-s3interval
               Download log files over the specified interval (Default: no
               interval)

           --cloudtrail-s3accountlist
               If source is an organization CloudTrail S3 bucket download log
               files for all specified account IDs (Default: no account IDs)

           --cloudtrail-sqsdelete
               If true then the plugin will delete SQS messages from the
               queue immediately after receiving them (Default: true)

           --cloudtrail-useasync
               If true then async extraction optimization is enabled
               (Default: true)

           --cloudtrail-uses3sns
               If true then the plugin will expect SNS messages to originate
               from S3 instead of directly from Cloudtrail (Default: false)

           --cloudtrail-aws-profile
               If non-empty overrides the AWS shared configuration profile
               (e.g. 'default') and environment variables such as AWS_PROFILE
               (Default: empty)

           --cloudtrail-aws-region
               If non-empty overrides the AWS region specified in the profile
               (e.g. 'us-east-1') and environment variables such as
               AWS_REGION (Default: empty)

           --cloudtrail-aws-config
               If non-empty overrides the AWS shared configuration filepath
               (e.g. ~/.aws/config) and env variables such as AWS_CONFIG_FILE
               (Default: empty)

           --cloudtrail-aws-credentials
               If non-empty overrides the AWS shared credentials filepath
               (e.g. ~/.aws/credentials) and env variables such as
               AWS_SHARED_CREDENTIALS_FILE (Default: empty)

           CloudTrail sources can be S3 buckets or SQS queue URLs. S3 bucket
           URLs have the form

           's3://bucket_name/prefix/AWSLogs/account-id/CloudTrail/region/year/month/day'

           For organization CloudTrail the S3 bucket URL can be

           's3://bucket_name/prefix/AWSLogs/org-id/account-id/CloudTrail/region/year/month/day'

           The region, year, month, and day components can be omitted in
           order to fetch more or less data. For example, the source
           's3://mybucket/AWSLogs/012345678/CloudTrail/us-west-2/2023' will
           fetch all CloudWatch logs for the year 2023.

           If the URL ends with 'account-id/' or 'account-id/CloudTrail/'
           (for example 's3://mybucket/AWSLOGS/012345678912/') the option
           '--cloudtrail-s3interval' can be used to define the time frame. A
           s3interval of '1d' for example would get all events of the last 24
           hours from all available regions. A s3interval of '2w-1w' would
           get all events from all regions from two weeks ago up to one week
           ago. The s3invterval can also be defined as a RFC 3339-style
           timestamp like '2024-02-29T18:07:17Z' or
           '2024-02-29T00:00:00Z-2024-03-01T23:59:59Z'.

           If the URL ends with 'AWSLogs/org-id' option
           '--cloudtrail-s3accountlist' can be used to specify account IDs.
           This can be combined with '--cloudtrail-s3interval'. A source like
           's3://my-org-bucket/AWSLogs/o-123abc/' with
           '--cloudstrail-s3accountlist' set to '123456789012,987654321098'
           and '--cloudtrail-s3interval' set to '30m' would get all events of
           the last 30min from all regions for accounts 123456789012 and
           987654321098.

           If source URL is the organization CloudTrail bucket (like
           's3://my-org-bucket/AWSLogs/o-123abc') and '--s3accountlist' is
           not set the plugin iterates over all accounts (limited by
           '--s3interval' if set). Attention: Depending on the size of the
           organization and the time interval, this can take a long time.

           The cloudtrail plugin uses the AWS SDK for Go, which can obtain
           profile, region, and credential settings from a set of standard
           environment variables and configuration files
           <https://aws.github.io/aws-sdk-go-v2/docs/configuring-sdk/>.
           Falcodump will show a list of locally configured profiles and the
           current regions, and will let you supply a custom value as well.

           More information is available in the README
           <https://github.com/falcosecurity/plugins/blob/master/plugins/cloudtrail/README.md>
           of the CloudTrail plugin.

## [](#EXAMPLES)EXAMPLES

           To see program arguments:

               falcodump --help

           To see program version:

               falcodump --version

           To see interfaces:

               falcodump --extcap-interfaces

           Only one interface (falcodump) is supported.

           Example output

               interface {value=cloudtrail}{display=Falco plugin}

           To see interface DLTs:

               falcodump --extcap-interface=cloudtrail --extcap-dlts

           Example output

               dlt {number=147}{name=cloudtrail}{display=USER0}

           To see interface configuration options:

               falcodump --extcap-interface=cloudtrail --extcap-config

           Example output

               arg {number=0}{call=--plugin-source}{display=Plugin source}{type=string}{tooltip=The plugin data source. This us usually a URL.}{placeholder=Enter a source URL…}{required=true}{group=Capture}
               arg {number=1}{call=cloudtrail-s3downloadconcurrency}{display=s3DownloadConcurrency}{type=integer}{default=1}{tooltip=Controls the number of background goroutines used to download S3 files (Default: 1)}{group=Capture}
               arg {number=2}{call=cloudtrail-sqsdelete}{display=sqsDelete}{type=boolean}{default=true}{tooltip=If true then the plugin will delete sqs messages from the queue immediately after receiving them (Default: true)}{group=Capture}
               arg {number=3}{call=cloudtrail-useasync}{display=useAsync}{type=boolean}{default=true}{tooltip=If true then async extraction optimization is enabled (Default: true)}{group=Capture}

           To capture AWS CloudTrail events from an S3 bucket:

               falcodump --extcap-interface=cloudtrail --fifo=/tmp/cloudtrail.pcap --plugin-source=s3://aws-cloudtrail-logs.../CloudTrail/us-east-2/... --capture

           or:

               falcodump --capture --extcap-interface cloudtrail --fifo ~/cloudtrail.pcap --plugin-source s3://my-cloudtrail-bucket/AWSLogs/o-abc12345/123456789012/ --cloudtrail-s3downloadconcurrency 32 --cloudtrail-s3interval 5d-2d --cloudtrail-aws-region eu-west-1

               Note

               CTRL + C should be used to stop the capture in order to ensure
               clean termination.

## [](#SEE_ALSO)SEE ALSO

           stratoshark(1), strato(1), dumpcalls(1), dumpcap(1), extcap(4)

## [](#NOTES)NOTES

           falcodump is part of the Stratoshark distribution. The latest
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

                                    2026-01-15                   FALCODUMP(1)

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
