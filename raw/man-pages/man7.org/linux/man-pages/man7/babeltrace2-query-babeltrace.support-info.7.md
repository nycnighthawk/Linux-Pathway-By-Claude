---
{"title": "babeltrace2-query-babeltrace.support-info(7) — Linux manual page", "url": "https://man7.org/linux/man-pages/man7/babeltrace2-query-babeltrace.support-info.7.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# babeltrace2-query-babeltrace.support-info(7) --- Linux manual page

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [DESCRIPTION](#DESCRIPTION) \| [PARAMETERS](#PARAMETERS) \| [RESULT OBJECT](#RESULT_OBJECT) \| [EXAMPLES](#EXAMPLES) \| [BUGS](#BUGS) \| [RESOURCES](#RESOURCES) \| [AUTHORS](#AUTHORS) \| [COPYRIGHT](#COPYRIGHT) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                                                                       |                                   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    BABELTRACE2-QUERY-(7)      Babeltrace 2 manual      BABELTRACE2-QUERY-(7)

## [](#NAME)NAME

           babeltrace2-query-babeltrace.support-info - Babeltrace 2: Support
           info query object

## [](#DESCRIPTION)DESCRIPTION

           The babeltrace.support-info Babeltrace 2 query object indicates,
           for a given source component class, whether or not its instance
           can handle a given input, and if so, what’s the confidence of this
           support.

           Said input can be a simple string, an existing file path, or an
           existing directory path. Components which expect some form of URI
           can handle a string input, while components which expect an
           existing file or directory can handle a file/directory path input.

           When the query method of the source component class replies that
           its component can handle a given input, it can also specify the
           name of a group in which to put that input. All the inputs of a
           given group, for a given component class, should be passed when
           instantiating the component class as its inputs initialization
           parameter (array of strings).

           The babeltrace2-convert(1) command queries this object from
           specific source component classes to find the most appropriate for
           a given non-option argument.

## [](#PARAMETERS)PARAMETERS

           input=INPUT [string]
               Check input INPUT.

               Depending on the type parameter, this is a simple string, a
               file path, or a directory path.

           type=(string | file | directory) [string]
               Input type, one of:

               string
                   input parameter is a simple string.

               file
                   input parameter is a file path.

               directory
                   input parameter is a directory path.

                   It’s expected that the query method don’t recurse into
                   this directory: the result object indicates whether or not
                   the component class supports this specific directory
                   (input).

## [](#RESULT_OBJECT)RESULT OBJECT

           The result object can be one of:

           •   A simple real value which is the weight, between 0 and 1, of
               the support by the component class for the given input.

               A weight of 0 means the input is unsupported while a weight
               of 1 means it’s fully supported. Any value in between shows
               how confident the component class is about the support of the
               given input.

           •   A map with a weight and an optional group name.

           When it’s a map, the expected entries are:

           group=GROUP-NAME [optional string]
               Put the given input into a group named GROUP-NAME for this
               component class.

               If this entry is missing, then the given input gets its own,
               unique group.

           weight=WEIGHT [real]
               Weight, between 0 and 1, of the support by the component class
               for the given input.

               The semantics are the same as when the result object is a
               simple real value.

## [](#EXAMPLES)EXAMPLES

       Query parameters
           Example 1. String input.

               input: net://relayd177/host/node23/active
               type: string

           Example 2. File path input.

               input: /home/user/traces/2019-08-26/quad.tr
               type: file

       Result object
           Example 3. Simple weight (unique group).

               0.5

           Example 4. Weight and specific group.

               group: 63a4b7e5-37f0-4254-a048-a0cff9e5b761
               weight: 0.75

           Example 5. Weight within a map (unique group).

               weight: 0.6

## [](#BUGS)BUGS

           If you encounter any issue or usability problem, please report it
           on the Babeltrace bug tracker (see
           <https://bugs.lttng.org/projects/babeltrace>).

## [](#RESOURCES)RESOURCES

           The Babeltrace project shares some communication channels with the
           LTTng project (see <https://lttng.org/>).

           •   Babeltrace website (see <https://babeltrace.org/>)

           •   Mailing list (see <https://lists.lttng.org>) for support and
               development: lttng-dev@lists.lttng.org

           •   IRC channel (see <irc://irc.oftc.net/lttng>): #lttng on
               irc.oftc.net

           •   Bug tracker (see <https://bugs.lttng.org/projects/babeltrace>)

           •   Git repository (see
               <https://git.efficios.com/?p=babeltrace.git>)

           •   GitHub project (see <https://github.com/efficios/babeltrace>)

           •   Continuous integration (see
               <https://ci.lttng.org/view/Babeltrace/>)

           •   Code review (see
               <https://review.lttng.org/q/project:babeltrace>)

## [](#AUTHORS)AUTHORS

           The Babeltrace 2 project is the result of hard work by many
           regular developers and occasional contributors.

           The current project maintainer is Jérémie Galarneau
           <mailto:jeremie.galarneau@efficios.com>.

## [](#COPYRIGHT)COPYRIGHT

           This query object is part of the Babeltrace 2 project.

           Babeltrace is distributed under the MIT license (see
           <https://opensource.org/licenses/MIT>).

## [](#SEE_ALSO)SEE ALSO

           babeltrace2-intro(7), babeltrace2-query(1), babeltrace2-convert(1)

## [](#COLOPHON)COLOPHON

           This page is part of the babeltrace (trace read and write
           libraries and a trace converter) project.  Information about the
           project can be found at ⟨http://www.efficios.com/babeltrace⟩.  If
           you have a bug report for this manual page, send it to
           lttng-dev@lists.lttng.org.  This page was obtained from the
           project's upstream Git repository
           ⟨git://git.efficios.com/babeltrace.git⟩ on 2026-08-03.  (At that
           time, the date of the most recent commit that was found in the
           repository was 2026-07-17.)  If you discover any rendering
           problems in this HTML version of the page, or you believe there is
           a better or more up-to-date source for the page, or you have
           corrections or improvements to the information in this COLOPHON
           (which is not part of the original manual page), send a mail to
           man-pages@man7.org

    Babeltrace 2.2.0rc1         14 September 2019       BABELTRACE2-QUERY-(7)

------------------------------------------------------------------------

Pages that refer to this page: [babeltrace2-convert(1)](../man1/babeltrace2-convert.1.html),  [babeltrace2-source.ctf.fs(7)](../man7/babeltrace2-source.ctf.fs.7.html),  [babeltrace2-source.ctf.lttng-live(7)](../man7/babeltrace2-source.ctf.lttng-live.7.html)

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
