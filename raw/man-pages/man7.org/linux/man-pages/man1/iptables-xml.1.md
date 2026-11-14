---
{"title": "iptables-xml(1) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/iptables-xml.1.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# iptables-xml(1) --- Linux manual page

+---------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [BUGS](#BUGS) \| [AUTHOR](#AUTHOR) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                               |                                   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    IPTABLES-XML(1)              iptables 1.8.13              IPTABLES-XML(1)

## [](#NAME)NAME

           iptables-xml — Convert iptables-save format to XML

## [](#SYNOPSIS)SYNOPSIS

           iptables-xml [-c] [-v]

## [](#DESCRIPTION)DESCRIPTION

           iptables-xml is used to convert the output of iptables-save into
           an easily manipulatable XML format to STDOUT.  Use I/O-redirection
           provided by your shell to write to a file.

           -c, --combine
                  combine consecutive rules with the same matches but
                  different targets. iptables does not currently support more
                  than one target per match, so this simulates that by
                  collecting the targets from consecutive iptables rules into
                  one action tag, but only when the rule matches are
                  identical. Terminating actions like RETURN, DROP, ACCEPT
                  and QUEUE are not combined with subsequent targets.

           -v, --verbose
                  Output xml comments containing the iptables line from which
                  the XML is derived

           iptables-xml does a mechanistic conversion to a very expressive
           xml format; the only semantic considerations are for -g and -j
           targets in order to discriminate between <call> <goto> and <nane-
           of-target> as it helps xml processing scripts if they can tell the
           difference between a target like SNAT and another chain.

           Some sample output is:

           <iptables-rules>
             <table name="mangle">
               <chain name="PREROUTING" policy="ACCEPT" packet-count="63436"
           byte-count="7137573">
                 <rule>
                  <conditions>
                   <match>
                     <p>tcp</p>
                   </match>
                   <tcp>
                     <sport>8443</sport>
                   </tcp>
                  </conditions>
                  <actions>
                   <call>
                     <check_ip/>
                   </call>
                   <ACCEPT/>
                  </actions>
                 </rule>
               </chain>
             </table> </iptables-rules>

           Conversion from XML to iptables-save format may be done using the
           iptables.xslt script and xsltproc, or a custom program using
           libxsltproc or similar; in this fashion:

           xsltproc iptables.xslt my-iptables.xml | iptables-restore

## [](#BUGS)BUGS

           None known as of iptables-1.3.7 release

## [](#AUTHOR)AUTHOR

           Sam Liddicott <azez@ufomechanic.net>

## [](#SEE_ALSO)SEE ALSO

           iptables-save(8), iptables-restore(8), iptables(8)

## [](#COLOPHON)COLOPHON

           This page is part of the iptables (administer and maintain packet
           filter rules) project.  Information about the project can be found
           at ⟨http://www.netfilter.org/⟩.  If you have a bug report for this
           manual page, see ⟨http://bugzilla.netfilter.org/⟩.  This page was
           obtained from the project's upstream Git repository
           ⟨git://git.netfilter.org/iptables⟩ on 2026-08-04.  (At that time,
           the date of the most recent commit that was found in the
           repository was 2026-07-10.)  If you discover any rendering
           problems in this HTML version of the page, or you believe there is
           a better or more up-to-date source for the page, or you have
           corrections or improvements to the information in this COLOPHON
           (which is not part of the original manual page), send a mail to
           man-pages@man7.org

    iptables 1.8.13                                           IPTABLES-XML(1)

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
