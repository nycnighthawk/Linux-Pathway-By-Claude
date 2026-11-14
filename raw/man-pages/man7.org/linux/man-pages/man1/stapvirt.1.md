---
{"title": "stapvirt(1) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/stapvirt.1.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# stapvirt(1) --- Linux manual page

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [COMMANDS](#COMMANDS) \| [TUTORIAL](#TUTORIAL) \| [SEE ALSO](#SEE_ALSO) \| [BUGS](#BUGS) \| [COLOPHON](#COLOPHON) |                                   |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                   |                                   |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    STAPVIRT(1)              General Commands Manual              STAPVIRT(1)

## [](#NAME)NAME

           stapvirt - prepare libvirt domains for systemtap probing

## [](#SYNOPSIS)SYNOPSIS

           stapvirt [-c URI] [-d PATH] [-v] COMMAND ARGUMENTS

## [](#DESCRIPTION)DESCRIPTION

           The stapvirt program can be used to add ports to domains managed
           by libvirt (see <http://libvirt.org/>).  These ports can then be
           used by stap to run scripts inside the domains (see the '--remote'
           option in stap(1) for more information).

           Ports are added to the definition of the domain using the port-add
           command.  These ports can later be removed using the port-remove
           command.  Note that there can only be as many simultaneous stap
           sessions as there are ports.

           Starting from libvirt v1.1.1 and QEMU v0.10.0, SystemTap ports can
           be hotplugged and thus do not need to be added first using the
           port-add command.  However, you need to ensure that there is a
           virtio-serial controller in place so that hotplugged ports can be
           connected. If creating a domain using virt-install, you can do
           this by adding this option:

                  $ virt-install [...] --controller=virtio-serial

           If the domain has already been created, you can simply do port-add
           followed immediately by port-remove, and then power off and
           restart the domain. The port will be removed, but the controller
           will remain.

## [](#OPTIONS)OPTIONS

           The following options are supported. Any other option prints a
           short help message.

           -c URI Specify the libvirt driver URI to which to connect (e.g.
                  'qemu:///system'). The default value is NULL, which indi‐
                  cates to libvirt to connect to the default driver. See the
                  page at <http://libvirt.org/uri.html> for supported values.

           -d PATH
                  Specify the directory in which UNIX sockets should be cre‐
                  ated when SystemTap ports are added. The default directory
                  is '/var/lib/libvirt/qemu'.

           -v     Increase verbosity. This option may be repeated for more
                  verbosity.

## [](#COMMANDS)COMMANDS

           The following commands are recognized by stapvirt. Any other com‐
           mand prints a short help message.

           help   Display the help message.

           list   List available domains.

           port-add DOMAIN
                  Add a permanent SystemTap port to the domain's definition.
                  If the domain is currently running, it must be powered off
                  before changes take effect.

           port-list DOMAIN
                  List the UNIX socket paths of the permanent SystemTap ports
                  in the domain's definition.

           port-remove DOMAIN
                  Remove a permanent SystemTap port from the domain's defini‐
                  tion. If the domain is currently running, it must be pow‐
                  ered off before changes take effect.

           query DOMAIN
                  Display the following information about the domain: its
                  name, its UUID, its state, the number of permanent System‐
                  Tap ports installed, and whether hotplugging is supported.

## [](#TUTORIAL)TUTORIAL

           This tutorial will help you get started with stapvirt. Let's start
           by listing all the privileged domains on the machine with the list
           command:

                  $ stapvirt -c 'qemu:///system' list
                  Available domains on URI 'qemu:///system':
                  ID      State     Type        Name
                  2       running   persistent  TestVM

           Note that we specified the libvirt URI using the -c switch. Other‐
           wise libvirt might have defaulted to e.g. 'qemu:///session'.

           Rather than typing the URI everytime, it might be easier to in‐
           stead set the LIBVIRT_DEFAULT_URI environment variable and omit
           the -c switch. Note that this is a libvirt functionality (see
           <libvirt.org/uri.html> for more details).

           The list command indicates that we have a running domain named
           'TestVM' with ID 2. Let's use the query command to retrieve more
           information:

                  $ stapvirt query TestVM # by name
                  $ stapvirt query 2      # by ID

                                Name:  TestVM
                                UUID:  905951c0-fa4f-409b-079c-c91ddda27028
                               State:  running
                                  ID:  2
                                Type:  persistent
                     Permanent Ports:  0
                         Hotplugging:  not supported

           The query command gives us some basic information about the do‐
           main, such as its name, UUID, and state. More importantly, it
           gives us two pieces of information: the number of permanent ports
           installed, and whether hotplugging is supported.  Technically,
           hotplugging support depends on libvirt and qemu, and is not relat‐
           ed to the domain in itself.

           If hotplugging were supported, we could stop here and run stap di‐
           rectly (assuming we have a virtio-serial controller already in
           place, see DESCRIPTION). Since in our case hotplugging is not sup‐
           ported, we need to add SystemTap ports. To do this, we use the
           port-add command:

                  $ stapvirt port-add TestVM
                  Added new port org.systemtap.stapsh.0
                  The domain must be powered off before changes take effect.

           We can confirm that a port was added by running the query command
           again:

                  $ stapvirt query TestVM
                  ...
                     Permanent Ports:  1
                         Hotplugging:  not supported

           It now indicates that there is 1 permanent port. We can also use
           the port-list command to know exactly where the port will be cre‐
           ated:

                  $ stapvirt port-list TestVM
                  /var/lib/libvirt/qemu/TestVM.org.systemtap.stapsh.0.sock

           After powering off and restarting the domain, we are now ready to
           use the port with stap:

                  $ stap -e 'probe begin { printf("Hello from TestVM!\n"); exit() }' \
                         --remote=libvirt://TestVM
                  Hello from TestVM!

           Finally, if we'd like to remove the port, we can use the port-re‐
           move command:

                  $ stapvirt port-remove TestVM
                  Removed port org.systemtap.stapsh.0
                  The domain must be powered off before changes take effect.

           And that's all there is to it!

## [](#SEE_ALSO)SEE ALSO

           stap(1),
           virt-install(1)

## [](#BUGS)BUGS

           Use the Bugzilla link of the project web page or our mailing list.
           http://sourceware.org/systemtap/ ,<systemtap@sourceware.org>.

## [](#COLOPHON)COLOPHON

           This page is part of the systemtap (a tracing and live-system
           analysis tool) project.  Information about the project can be
           found at ⟨https://sourceware.org/systemtap/⟩.  If you have a bug
           report for this manual page, send it to systemtap@sourceware.org.
           This page was obtained from the project's upstream Git repository
           ⟨git://sourceware.org/git/systemtap.git⟩ on 2026-08-04.  (At that
           time, the date of the most recent commit that was found in the
           repository was 2026-07-30.)  If you discover any rendering
           problems in this HTML version of the page, or you believe there is
           a better or more up-to-date source for the page, or you have
           corrections or improvements to the information in this COLOPHON
           (which is not part of the original manual page), send a mail to
           man-pages@man7.org

                                                                  STAPVIRT(1)

------------------------------------------------------------------------

Pages that refer to this page: [stap(1)](../man1/stap.1.html)

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
