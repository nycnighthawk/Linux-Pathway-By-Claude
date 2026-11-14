---
{"title": "pmdaweblog(1) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/pmdaweblog.1.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# pmdaweblog(1) --- Linux manual page

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [INSTALLATION](#INSTALLATION) \| [CONFIGURATION](#CONFIGURATION) \| [CAVEATS](#CAVEATS) \| [FILES](#FILES) \| [PCP ENVIRONMENT](#PCP_ENVIRONMENT) \| [DEBUGGING OPTIONS](#DEBUGGING_OPTIONS) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                                                                                                         |                                   |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    PMDAWEBLOG(1)            General Commands Manual            PMDAWEBLOG(1)

## [](#NAME)NAME

           pmdaweblog - performance metrics domain agent (PMDA) for Web
           server logs

## [](#SYNOPSIS)SYNOPSIS

           $PCP_PMDAS_DIR/weblog/pmdaweblog [-Cp] [-D debug] [-d domain] [-h
           helpfile] [-i port] [-l logfile] [-n idlesec] [-S num] [-t delay]
           [-u socket] [-U username] configfile

## [](#DESCRIPTION)DESCRIPTION

           pmdaweblog is a Performance Metrics Domain Agent (PMDA(3)) that
           scans Web server logs to extract metrics characterizing Web server
           activity.  These performance metrics are then made available
           through the infrastructure of the Performance Co-Pilot (PCP).

           The configfile specifies which Web servers are to be monitored,
           their associated access logs and error logs, and a regular-
           expression based scheme for extracting detailed information about
           each Web access.  This file is maintained as part of the PMDA
           installation and/or de-installation by the scripts Install and
           Remove in the directory $PCP_PMDAS_DIR/weblog.  For more details,
           refer to the section below covering installation.

           Once started, pmdaweblog monitors a set of log files and in
           response to a request for information, will process any new
           information that has been appended to the log files, similar to a
           tail(1).  There is also periodic "catch up" to process new
           information from all log files, and a scheme to detect the
           rotation of log files.

           Like all other PMDAs, pmdaweblog is launched by pmcd(1) using
           command line options specified in $PCP_PMCDCONF_PATH - the Install
           script will prompt for appropriate values for the command line
           options, and update $PCP_PMCDCONF_PATH.

           A brief description of the pmdaweblog command line options
           follows:

           -C     Check the configuration and exit.

           -d domain
                  Specify the domain number.  It is absolutely crucial that
                  the performance metrics domain number specified here is
                  unique and consistent.  That is, domain should be different
                  for every PMDA on the one host, and the same domain number
                  should be used for the pmdaweblog PMDA on all hosts.

                  For most installations, the default domain as encapsulated
                  in the file $PCP_PMDAS_DIR/weblog/domain.h will suffice.
                  For alternate values, check $PCP_PMCDCONF_PATH for the
                  domain values already in use on this host, and the file
                  $PCP_VAR_DIR/pmns/stdpmid contains a repository of ``well
                  known'' domain assignments that probably should be avoided.

           -h helpfile
                  Get the help text from the supplied helpfile rather than
                  from the default location.

           -i port
                  Communicate with pmcd(1) on the specified Internet port
                  (which may be a number or a name).

           -l logfile
                  Location of the log file.  By default, a log file named
                  weblog.log is written in the current directory of pmcd(1)
                  when pmdaweblog is started, i.e.  $PCP_LOG_DIR/pmcd.  If
                  the log file cannot be created or is not writable, output
                  is written to the standard error instead.

           -n idlesec
                  If a Web server log file has not been modified for idlesec
                  seconds, then the file will be closed and re-opened.  This
                  is the only way pmdaweblog can detect any asynchronous
                  rotation of the logs by Web server administrative scripts.
                  The default period is 20 seconds.  This value may be
                  changed dynamically using pmstore(1) to modify the value of
                  the performance metric web.config.check.

           -p     Communicate with pmcd(1) via a pipe.

           -S num Specify the maximum number of Web servers per sproc.  It
                  may be desirable (from a latency and load balancing
                  perspective) or necessary (due to file descriptor limits)
                  to delegate responsibility for scanning the Web server log
                  files to several sprocs.  pmdaweblog will ensure that each
                  sproc handles the log files for at most num Web servers.
                  The default value is 80 Web servers per sproc.

           -t delay
                  To avoid the need to scan a lot of information from the Web
                  server logs in response to a single request for performance
                  metrics, all log files will be checked at least once every
                  delay seconds.  The default is 15 seconds.  This value may
                  by changed dynamically using pmstore(1) to modify the value
                  of the performance metric web.config.catchup.

           -u socket
                  Communicate with pmcd(1) via the given Unix domain socket.

           -U     User account under which to run the agent.  The default is
                  the unprivileged "pcp" account in current versions of PCP,
                  but in older versions the superuser account ("root") was
                  used by default.

## [](#INSTALLATION)INSTALLATION

           The PCP framework allows metrics to be collected on one host and
           monitored from another.  These hosts are referred to as collector
           and monitor hosts, respectively.  A host may be both a collector
           and a monitor.

           Collector hosts require the installation of the agent, while
           monitoring hosts require no agent installation at all.

           For collector hosts do the following as root:

             # cd $PCP_PMDAS_DIR/weblog
             # ./Install

           The installation procedure prompts for a default or non-default
           installation.  A default installation will search for known server
           configurations and automatically configure the PMDA for any server
           log files that are found.  A non-default installation will step
           through each server, prompting the user for other server
           configurations and arguments to pmdaweblog.  The end result of a
           collector installation is to build a configuration file that is
           passed to pmdaweblog via the configfile argument.

           If you want to undo the installation, do the following as root:

             # cd $PCP_PMDAS_DIR/weblog
             # ./Remove

           pmdaweblog is launched by pmcd(1) and should never be executed
           directly.  The Install and Remove scripts notify pmcd(1) when the
           agent is installed or removed.

## [](#CONFIGURATION)CONFIGURATION

           The configuration file for the weblog PMDA is an ASCII file that
           can be easily modified.  Empty lines and lines beginning with '#'
           are ignored.  All other lines must be either a regular expression
           or server specification.

           Regular expressions, which are used on both the access and error
           log files, must be of the form:

             regex regexName regexp
           or

             regex_posix regexName ordering regexp_posix

           The regexName is a word which uniquely identifies the regular
           expression.  This is the reference used in the server
           specification.  The regexp for access logs is in the format
           described for regcmp(3).  The regexp_posix for access logs is in
           the format described for regcomp(3).  The argument ordering is
           explained below. The Posix form should be available on all
           platforms.

           The regular expression requires the specification of up to four
           arguments to be extracted from each line of a Web server access
           log, depending on the type of server. In the most common case
           there are two arguments representing the method and the size.

           For the non- Posix version, argument $0 should contain the method:
           GET, HEAD , POST or PUT.  The method PUT is treated as a synonym
           for POST, and anything else is categorized as OTHER.

           The second argument, $1, should contain the size of the request.
           A size of ``-'' or `` '' is treated as unknown.

           Argument $3 should contain the status code returned to the client
           browser and argument $4 should contain the status code returned to
           the server from a remote host.  These latter two arguments are
           used for caching servers and must be specified as a pair (or $3
           will be ignored). For further information on status codes, refer
           to the web site
           http://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html .

           Some legal non- Posix regex expression specifications for
           monitoring an access log are:

             # pattern for CERN, NCSA, Netscape etc Access Logs
             regex CERN ] "([A-Za-z][-A-Za-z]+)$0 .*" [-0-9]+ ([-0-9]+)$1

             # pattern for FTP Server access logs (normally in SYSLOG)
             regex SYSLOG_FTP ftpd[.*]: ([gp][-A-Za-z]+)$0( )$1

           There is 1 special types of access logs with the RegexName SQUID.
           This formats extract 4 parameters but since the Squid log file
           uses text-based status codes, it is handled as a special case.

           In the examples below, NS_PROXY parses the Netscape/W3C Common
           Extended Log Format and SQUID parses the default Squid Object
           Cache format log file.

             # pattern for Netscape Proxy Server Extended Logs
             regex NS_PROXY ] "([A-Za-z][-A-Za-z]+)$0 .*" ([-0-9]+)$2 \
                  ([-0-9]+)$1 ([-0-9]+)$3

             # pattern for Squid Cache logs
             regex SQUID [0-9]+.[0-9]+[ ]+[0-9]+ [a-zA-Z0-9.]+ \
                  ([_A-Z]+)$3([0-9]+)$2 ([0-9]+)$1 ([A-Z]+)$0

           The regexp for the error logs does not require any arguments, only
           a match.  Some legal expressions are:

             # pattern for CERN, NCSA, Netscape etc Error Logs
             regex CERN_err .

             # pattern for FTP Server error logs (normally in SYSLOG)
             regex SYSLOG_FTP_err FTP LOGIN FAILED

           If POSIX compliant regular expressions are used, additional
           information is required since the order of parameters cannot be
           specified in the regular expression.  For backwards compatibility,
           the common case of two parameters the order may be specified as
           method,size or size,method In the general case, the ordering is
           specified by one of the following methods:

           n1,n2,n3,n4
                where nX is a digit between 1 and 4. Each comma-separated
                field represents (in order) the argument number for
                method,size,client_status,server_status

           -    Used for cases like the error logs where the content is
                ignored.

           As for the non- Posix format, the SQUID RegexName is treated as a
           special case to match the non-numerical status codes.

           Some legal Posix regex expression specifications for monitoring an
           access log are:

             # pattern for CERN, NCSA, Netscape, Apache etc Access Logs
             regex_posix CERN method,size ][ \]+"([A-Za-z][-A-Za-z]+) \
                  [^"]*" [-0-9]+ ([-0-9]+)

             # pattern for CERN, NCSA, Netscape, Apache etc Access Logs
             regex_posix CERN 1,2 ][ \]+"([A-Za-z][-A-Za-z]+) \
                  [^"]*" [-0-9]+ ([-0-9]+)

             # pattern for FTP Server access logs (normally in SYSLOG)
             regex_posix SYSLOG_FTP method,size ftpd[.*]: \
                  ([gp][-A-Za-z]+)( )

             # pattern for Netscape Proxy Server Extended Logs
             regex_posix NS_PROXY 1,3,2,4 ][ ]+"([A-Za-z][-A-Za-z]+) \
                  [^"]*" ([-0-9]+) ([-0-9]+) ([-0-9]+)

             # pattern for Squid Cache logs
             regex_posix SQUID 4,3,2,1 [0-9]+.[0-9]+[ ]+[0-9]+ \
                  [a-zA-Z0-9.]+ ([_A-Z]+)([0-9]+) ([0-9]+) ([A-Z]+)

             # pattern for CERN, NCSA, Netscape etc Error Logs
             regex_posix CERN_err - .

             # pattern for FTP Server error logs (normally in SYSLOG)
             regex_posix SYSLOG_FTP_err - FTP LOGIN FAILED

           A Web server can be specified using this syntax:

             server serverName on|off accessRegex accessFile errorRegex errorFile

           The serverName must be unique for each server, and is the name
           given to the instance for the associated performance metrics.  See
           PMAPI(3) for a discussion of PCP instance domains.  The on or off
           flag indicates whether the server is to be monitored when the PMDA
           is installed.  This can altered dynamically using pmstore(1) for
           the metric web.perserver.watched, which has one instance for each
           Web server named in configfile.

           Two files are monitored for each Web server, the access and the
           error log.  Each file requires the name of a previously declared
           regular expression, and a file name.  The log files specified for
           each server do not have to exist when the weblog PMDA is
           installed.  The PMDA will continue to check for non-existent log
           files and open them when possible.  Some legal server
           specifications are:

             # Netscape Server on Port 80 at IP address 127.55.555.555
             server 127.55.555.555:80 on CERN /logs/access CERN_err /logs/errors

             # FTP Server.
             server ftpd on SYSLOG_FTP /var/log/messages SYSLOG_FTP_err /var/log/messages

## [](#CAVEATS)CAVEATS

           Specifying regular expressions with an incorrect number of
           arguments, anything other than 2 for access logs, and none for
           error logs, may cause the PMDA to behave incorrectly and even
           crash. This is due to limitations in the interface of regex(3).

## [](#FILES)FILES

           $PCP_PMDAS_DIR/weblog
                  installation directory for the weblog PMDA

           $PCP_PMDAS_DIR/weblog/Install
                  installation script for the weblog PMDA

           $PCP_PMDAS_DIR/weblog/Remove
                  de-installation script for the weblog PMDA

           $PCP_LOG_DIR/pmcd/weblog.log
                  default log file for error reporting

           $PCP_PMCDCONF_PATH
                  pmcd configuration file that specifies the command line
                  options to be used when pmdaweblog is launched

           $PCP_LOG_DIR/NOTICES
                  log of PMDA installations and removals

           $PCP_VAR_DIR/config/web/weblog.conf
                  likely location of the weblog PMDA configuration file

           $PCP_DOC_DIR/pcpweb/index.html
                  the online HTML documentation for PCPWEB

## [](#PCP_ENVIRONMENT)PCP ENVIRONMENT

           Environment variables with the prefix PCP_ are used to
           parameterize the file and directory names used by PCP.  On each
           installation, the file /etc/pcp.conf contains the local values for
           these variables.  The $PCP_CONF variable may be used to specify an
           alternative configuration file, as described in pcp.conf(5).

## [](#DEBUGGING_OPTIONS)DEBUGGING OPTIONS

           The -D or --debug option enables the output of additional
           diagnostics on stderr to help triage problems, although the
           information is sometimes cryptic and primarily intended to provide
           guidance for developers rather end-users.  debug is a comma
           separated list of debugging options; use pmdbg(1) with the -l
           option to obtain a list of the available debugging options and
           their meaning.

           Debugging options specific to pmdaweblog are as follows:
           ┌────────┬───────────────────────────────────────────────────────┐
           │ Option │ Description                                           │
           ├────────┼───────────────────────────────────────────────────────┤
           │ appl0  │ initialization, configfile parsing and log file       │
           │        │ processing                                            │
           ├────────┼───────────────────────────────────────────────────────┤
           │ appl1  │ timer operations, log file probing                    │
           ├────────┼───────────────────────────────────────────────────────┤
           │ appl2  │ IPC with worker processes, log lines processed        │
           └────────┴───────────────────────────────────────────────────────┘

## [](#SEE_ALSO)SEE ALSO

           pmcd(1), pmchart(1), pmdawebping(1), pminfo(1), pmstore(1),
           pmview(1), tail(1), weblogvis(1), webvis(1), PMAPI(3), PMDA(3) and
           regcmp(3).

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

    Performance Co-Pilot               PCP                      PMDAWEBLOG(1)

------------------------------------------------------------------------

Pages that refer to this page: [weblogvis(1)](../man1/weblogvis.1.html),  [webvis(1)](../man1/webvis.1.html)

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
