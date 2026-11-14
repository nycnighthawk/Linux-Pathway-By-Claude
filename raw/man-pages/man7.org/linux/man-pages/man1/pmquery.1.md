---
{"title": "pmquery(1) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/pmquery.1.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# pmquery(1) --- Linux manual page

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [EXAMPLES](#EXAMPLES) \| [ENVIRONMENT](#ENVIRONMENT) \| [EXIT STATUS](#EXIT_STATUS) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                       |                                   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    PMQUERY(1)               General Commands Manual               PMQUERY(1)

## [](#NAME)NAME

           pmconfirm, pmmessage, pmquery - general purpose dialog box

## [](#SYNOPSIS)SYNOPSIS

           pmconfirm [-c] [-b button-name] [-B default-button-name] [-t
           string] [-file filename] [-icon icontype] [-font font] [-header
           titlebar-string] [-useslider] [-noslider] [-noframe] [-exclusive]

           pmmessage [-buttons label1[:value1][,label2[:value2][,...]]]
           [-center] [-nearmouse] [-default button] [-file filename] [-print]
           [-timeout sec] message...

           pmquery [-input] [all above options...]  [message...]

## [](#DESCRIPTION)DESCRIPTION

           pmquery provides a command-line-option compatible implementation
           of the xconfirm and xmessage tools, using a look-and-feel that is
           consistent with pmchart.  Several extensions to the functionality
           of the original tools have been made, in order to improve their
           specific utility for pmchart, but wherever possible the original
           semantics remain.

           pmconfirm displays a line of text for each -t option specified (or
           a file when the -file option is used), and a button for each -b
           option specified.  When one of the buttons is pressed, the label
           of that button is written to pmquery's standard output.  This
           provides a means of communication/feedback from within shell
           scripts and a means to display useful information to a user from
           an application.

           pmmessage displays a window containing a message from the command
           line, a file, or standard input.  It additionally allows buttons
           to be associated with an exit status, and only optionally will
           write the label of the button to standard output.

           pmquery extends the above tools to additionally support limited
           user input, as free form text.  In this -input mode, any text
           entered will be output when the default button is pressed.  A
           default text can be entered using the same mechanisms as the other
           tools.

           Command line options are available to specify font style, frame
           style, modality and one of several different icons to be presented
           for tailored visual feedback to the user.

## [](#OPTIONS)OPTIONS

           The available command line options are:

           -c, -center
                Center the window on the display.

           -nearmouse
                Pop up the window near the mouse cursor.

           -b button-name
                Displays a button with the label button-name.  If button-name
                is the empty string, the button in that position is not
                displayed.  If no -b options are present, the default is a
                button with the label Continue.  The exit status associated
                with button-name is zero.

           -B button-name
                Displays a button with the label button-name and specifies it
                as the button to be activated when enter is pressed.  The
                exit status associated with button-name is zero.

           -buttons button,button,...
                This option will create one button for each comma-separated
                button option.  Each button consists of a label optionally
                followed by a colon and an exit value.  The exit value will
                be returned if that button is selected.  The default exit
                value is 100 plus the button number.  Buttons are numbered
                from the left starting with one.

           -default label
                Defines the button with a matching label to be the default.
                If not specified there is no default.  The corresponding
                resource is defaultButton.  Pressing Return anywhere in the
                xmessage window will activate the default button.  The
                default button has a wider border than the others.

           -t message
                Displays message.  Any number of strings can be listed on the
                command line (each must be preceded with the -t option).

           -file filename
                Displays the file filename.  All -t options will be ignored.
                A filename of `-' reads from standard input.

           -icon icontype
                Displays the icon icontype where icontype is one of: info,
                error, question, warning, critical.  action is also accepted
                as a synonym for error for backward compatibility.  pmquery
                introduces the additional archive and host icon types as well
                as the original xconfirm types listed earlier.

           -font fontname
                Use fontname as the font.  This option is only available when
                using the X Window System.

           -header string
                Use string as the window title.

           -print
                This causes the program to write the label of the button
                pressed to standard output.  It is the default behaviour for
                pmconfirm and pmquery.

           -noprint
                This causes the program to not write the label of the button
                pressed to standard output.  It is the default behaviour for
                pmmessage.

           -geometry geometry-string
                This provides the tool with an X-compatible geometry string
                specification.  This option is only available when using the
                X Window System.

           -useslider
                When displaying a file, always use a slider instead of
                determining automatically whether a slider is necessary.

           -noslider
                Do not create a slider, and clip text to the window size,
                instead of determining automatically whether a slider is
                necessary..

           -noframe
                Do not display a frame around the contents.

           -exclusive
                Grab the keyboard/pointer and do not allow further input
                until a button is pressed.

           -timeout secs
                Exit with status 0 after secs seconds if the user has not
                clicked on a button yet.  The corresponding resource is
                timeout.

           -?, -h, -help
                Display usage message and exit.

## [](#EXAMPLES)EXAMPLES

           The following shell script will display a window with an
           information icon, asking the user a yes or no question with "Yes"
           as the default.

            #! /bin/sh
            case `pmquery -t "Really power down?" -b No -B Yes -icon question
            in
              Yes) shutdown;;
              No) ;;
            esac

           A second example, which prompts for a hostname then starts a
           terminal with an ssh session connected to the requested host.

            #! /bin/sh
            host=`pmquery -input -icon host -b Cancel -B OK \
                          -header "Remote Terminal - Secure Shell"
            [ "$host" = "Cancel" -o -z "$host" ] && exit
            gnome-terminal -e "ssh $host"

## [](#ENVIRONMENT)ENVIRONMENT

           pmquery is an excellent choice of utility for the
           PCP_XCONFIRM_PROG Performance Co-Pilot configuration parameter
           (refer to pcp.conf(5) for details).

           Note that PCP_XCONFIRM_PROG will be automatically set to pmquery
           inside tools like pmchart, unless PCP_XCONFIRM_PROG is already set
           in the environment.

## [](#EXIT_STATUS)EXIT STATUS

           If it detects an error, pmquery always returns 1, so this value
           should not be associated with a button.  Unless -button option has
           not been used, the return code will be zero on success.

## [](#SEE_ALSO)SEE ALSO

           pmchart(1) and pcp.conf(5).

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

    Performance Co-Pilot                                           PMQUERY(1)

------------------------------------------------------------------------

Pages that refer to this page: [pmchart(1)](../man1/pmchart.1.html),  [pmie(1)](../man1/pmie.1.html),  [pmrecord(3)](../man3/pmrecord.3.html)

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
