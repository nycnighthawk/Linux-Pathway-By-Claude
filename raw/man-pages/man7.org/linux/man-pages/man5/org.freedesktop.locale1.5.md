---
{"title": "org.freedesktop.locale1(5) — Linux manual page", "url": "https://man7.org/linux/man-pages/man5/org.freedesktop.locale1.5.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# org.freedesktop.locale1(5) --- Linux manual page

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [INTRODUCTION](#INTRODUCTION) \| [THE D-BUS API](#THE_D-BUS_API) \| [EXAMPLES](#EXAMPLES) \| [VERSIONING](#VERSIONING) \| [SEE ALSO](#SEE_ALSO) \| [NOTES](#NOTES) \| [COLOPHON](#COLOPHON) |                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                              |                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    ORG.FREE...P.LOCALE1(5)  org.freedesktop.locale1  ORG.FREE...P.LOCALE1(5)

## [](#NAME)NAME

           org.freedesktop.locale1 - The D-Bus interface of systemd-localed

## [](#INTRODUCTION)INTRODUCTION

           systemd-localed.service(8) is a system service that can be used to
           control the system locale and keyboard mapping from user programs.
           This page describes the D-Bus interface.

## [](#THE_D-BUS_API)THE D-BUS API

           The service exposes the following interfaces on the bus:

               node /org/freedesktop/locale1 {
                 interface org.freedesktop.locale1 {
                   methods:
                     SetLocale(in  as locale,
                               in  b interactive);
                     SetVConsoleKeyboard(in  s keymap,
                                         in  s keymap_toggle,
                                         in  b convert,
                                         in  b interactive);
                     SetX11Keyboard(in  s layout,
                                    in  s model,
                                    in  s variant,
                                    in  s options,
                                    in  b convert,
                                    in  b interactive);
                   properties:
                     readonly as Locale = ['...', ...];
                     readonly s X11Layout = '...';
                     readonly s X11Model = '...';
                     readonly s X11Variant = '...';
                     readonly s X11Options = '...';
                     readonly s VConsoleKeymap = '...';
                     readonly s VConsoleKeymapToggle = '...';
                 };
                 interface org.freedesktop.DBus.Peer { ... };
                 interface org.freedesktop.DBus.Introspectable { ... };
                 interface org.freedesktop.DBus.Properties { ... };
               };

       Methods
           If you set a new system locale all old system locale settings will
           be dropped and the new settings will be saved to disk. The locale
           will also be passed to the system manager, and subsequently
           started daemons will inherit the new system locale. Note that
           already running daemons will not learn about the new value.

           The SetVConsoleKeyboard() method may be used to set the key
           mapping for the virtual console. Similarly, SetX11Keyboard() may
           be used to set the default key mapping of any X11 servers.

           Note that SetVConsoleKeyboard() instantly applies the new key
           mapping to the console, while SetX11Keyboard() simply sets a
           default that may be used by later sessions.

           The boolean argument convert may be set to optionally convert the
           console keyboard configuration to X11 keyboard mappings and vice
           versa. If true and SetVConsoleKeyboard() is used, the nearest X11
           keyboard setting for the chosen console setting is set. If true
           and SetX11Keyboard() is used, the nearest console keyboard setting
           for the chosen X11 setting is set. Hence, it is usually sufficient
           to call only one of the two functions.

           For graphical UIs that need to set the system keyboard mapping
           simply invoke SetX11Keyboard(), set convert=true and ignore
           SetVConsoleKeyboard().

           Use the empty string for the keymap parameters you wish not to
           set.

           The interactive boolean parameters can be used to control whether
           polkit[1] should interactively ask the user for authentication
           credentials if required.

       Signals
           Whenever the system locale or keymap is changed via the daemon,
           PropertyChanged signals are sent out to clients which have
           subscribed.

       Properties
           The system locale is shown in the Locale property. It is an array
           containing environment-variable-assignment-like strings. The
           following strings are known: LANG=, LC_CTYPE=, LC_NUMERIC=,
           LC_TIME=, LC_COLLATE=, LC_MONETARY=, LC_MESSAGES=, LC_PAPER=,
           LC_NAME=, LC_ADDRESS=, LC_TELEPHONE=, LC_MEASUREMENT=,
           LC_IDENTIFICATION=.

           The X11Layout, X11Model, X11Variant, and X11Options properties
           show values configurable with SetX11Keyboard() described above (or
           SetVConsoleKeyboard() with convert=true). The VConsoleKeymap and
           VConsoleKeymapToggle properties show values configurable with
           SetVConsoleKeyboard() (or SetX11Keyboard() with convert=true).

       Security
           Changing the system locale or keymap using this interface is
           authenticated via polkit. The polkit action for SetLocale() is
           org.freedesktop.locale1.set-locale. The polkit action for
           SetX11Keyboard() and SetVConsoleKeyboard() is
           org.freedesktop.locale1.set-keyboard.

## [](#EXAMPLES)EXAMPLES

           Example 1. Introspect org.freedesktop.locale1 on the bus

               $ gdbus introspect --system \
                 --dest org.freedesktop.locale1 \
                 --object-path /org/freedesktop/locale1

## [](#VERSIONING)VERSIONING

           These D-Bus interfaces follow the usual interface versioning
           guidelines[2].

## [](#SEE_ALSO)SEE ALSO

           systemd(1), systemd-localed.service(8), localectl(1)

## [](#NOTES)NOTES

            1. polkit
               https://www.freedesktop.org/software/polkit/docs/latest/

            2. the usual interface versioning guidelines
               https://0pointer.de/blog/projects/versioning-dbus.html

## [](#COLOPHON)COLOPHON

           This page is part of the systemd (systemd system and service
           manager) project.  Information about the project can be found at
           ⟨http://www.freedesktop.org/wiki/Software/systemd⟩.  If you have a
           bug report for this manual page, see
           ⟨http://www.freedesktop.org/wiki/Software/systemd/#bugreports⟩.
           This page was obtained from the project's upstream Git repository
           ⟨https://github.com/systemd/systemd.git⟩ on 2026-08-04.  (At that
           time, the date of the most recent commit that was found in the
           repository was 2026-08-03.)  If you discover any rendering
           problems in this HTML version of the page, or you believe there is
           a better or more up-to-date source for the page, or you have
           corrections or improvements to the information in this COLOPHON
           (which is not part of the original manual page), send a mail to
           man-pages@man7.org

    systemd 262~devel                                 ORG.FREE...P.LOCALE1(5)

------------------------------------------------------------------------

Pages that refer to this page: [systemd.directives(7)](../man7/systemd.directives.7.html),  [systemd.index(7)](../man7/systemd.index.7.html),  [systemd-localed.service(8)](../man8/systemd-localed.service.8.html)

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
