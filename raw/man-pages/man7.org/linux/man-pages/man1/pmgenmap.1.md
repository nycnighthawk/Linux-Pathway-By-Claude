---
{"title": "pmgenmap(1) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/pmgenmap.1.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# pmgenmap(1) --- Linux manual page

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [EXAMPLES](#EXAMPLES) \| [FILES](#FILES) \| [PCP ENVIRONMENT](#PCP_ENVIRONMENT) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                            |                                   |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    PMGENMAP(1)              General Commands Manual              PMGENMAP(1)

## [](#NAME)NAME

           pmgenmap - generate C code to simplify handling of performance
           metrics

## [](#SYNOPSIS)SYNOPSIS

           pmgenmap [infile]

## [](#DESCRIPTION)DESCRIPTION

           Given one or more lists of metric names in infile or on standard
           input, pmgenmap generates C declarations and cpp(1) macros
           suitable for use across the Performance Metrics Programming
           Interface (PMAPI) on standard output.

           The declarations produced by pmgenmap simplify the coding for
           client applications using the PMAPI.

           The input should consist of one or more lists of metric names of
           the form

                listname {
                    metricname1 symbolname1
                    metricname2 symbolname2
                    ...
                }

           which will generate C and cpp(1) declarations of the form

                char *listname[] = {
                #define symbolname1 0
                    "metricname1",
                #define symbolname2 1
                    "metricname2",
                    ...
                };

           The array declarations produced are suitable as parameters to
           pmLookupName(3) and the #defined constants may be used to index
           the vsets in the pmResult structure returned by a pmFetch(3) call.

           Obviously, listname must conform to the C identifier naming rules,
           each symbolname must conform to the cpp(1) macro naming rules, and
           each metricname is expected to be a valid performance metrics name
           (see PMNS(5) for more details).

           The input may include sh-style comment lines, i.e. with a `#' as
           the first non-blank character of a line, and these are translated
           on output to either single line or multi-line C comments in the
           K&R style.  For example, the input:

                # leading block of multi-line comments
                # initialization group
                foo {
                        a.b.c   ONE
                        d.e.f.g TWO
                        # embedded block of multi-lines
                        # comments and boring pad text
                        xx.yy.zz        THREE
                }

                # trailing single line comment

           Produces the output:

                /*
                 * leading block of multi-line comments
                 * initialization group
                 */
                char *foo[] = {
                #define ONE 0
                        "a.b.c",
                #define TWO 1
                        "d.e.f.g",
                /*
                 * embedded block of multi-lines
                 * comments and boring pad text
                 */
                #define THREE 2
                        "xx.yy.zz",

                };

                /* trailing single line comment */

## [](#EXAMPLES)EXAMPLES

           For brevity we have removed the error handling code, and assumed
           the chosen metrics do not have multiple values.

           The input file

                mystats {
                    kernel.percpu.cpu.idle     IDLE
                    kernel.percpu.cpu.sys      SYS
                    kernel.percpu.cpu.user     USER
                    hinv.ncpu                       NCPU
                }

           produces the following C code, suitable for #include-ing

                /*
                 * Performance Metrics Name Space Map
                 * Built by pmgenmap from the file
                 * mystats.metrics
                 * on Wed Dec 28 19:44:17 EST 1994
                 *
                 * Do not edit this file!
                 */

                char *mystats[] = {
                #define IDLE    0
                        "kernel.percpu.cpu.idle",
                #define SYS     1
                        "kernel.percpu.cpu.sys",
                #define USER    2
                        "kernel.percpu.cpu.user",
                #define NCPU    3
                        "hinv.ncpu",

                };

           Using the code generated by pmgenmap, we are now able to easily
           obtain metrics from the Performance Metrics Collection Subsystem
           (PMCS) as follows:

                #define MAX_PMID 4

                    int         trip = 0;
                    int         numpmid = sizeof(mystats)/sizeof(mystats[0]);
                    double      duration;
                    pmResult    *resp;
                    pmResult    *prev;
                    pmID        pmidlist[MAX_PMID];

                    pmNewContext(PM_CONTEXT_HOST, "localhost");
                    pmLookupName(numpmid, mystats, pmidlist);
                    pmFetch(numpmid, pmidlist, &resp);

                    printf("%d CPUs: %d usr   %d sys   %d   idle0,
                           resp->vset[NCPU]->vlist[0].value.lval,
                           resp->vset[USER]->vlist[0].value.lval,
                           resp->vset[SYS]->vlist[0].value.lval,
                           resp->vset[IDLE]->vlist[0].value.lval);

           Some calls to ensure portability have been removed from the code
           above for the sake of clarity - the example above should not be
           used as a template for programming.  In particular, the raw values
           of the metrics were used when pmLookupDesc(3) should have been
           called to determine the semantics of each metric.

           More complete examples that demonstrate the use of pmgenmap which
           may be used as a basis for program development are included in the
           PCP demos, e.g.  $PCP_DEMOS_DIR/pmclient.

## [](#FILES)FILES

           $PCP_VAR_DIR/pmns/*
                default PMNS specification files

## [](#PCP_ENVIRONMENT)PCP ENVIRONMENT

           Environment variables with the prefix PCP_ are used to
           parameterize the file and directory names used by PCP.  On each
           installation, the file /etc/pcp.conf contains the local values for
           these variables.  The $PCP_CONF variable may be used to specify an
           alternative configuration file, as described in pcp.conf(5).

## [](#SEE_ALSO)SEE ALSO

           cpp(1), PMAPI(3), pmFetch(3), pmLookupName(3), pmNewContext(3),
           pcp.conf(5), pcp.env(5) and PMNS(5).

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

    Performance Co-Pilot               PCP                        PMGENMAP(1)

------------------------------------------------------------------------

Pages that refer to this page: [pmcd(1)](../man1/pmcd.1.html),  [pmclient(1)](../man1/pmclient.1.html)

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
