---
{"title": "setpci(8) — Linux manual page", "url": "https://man7.org/linux/man-pages/man8/setpci.8.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# setpci(8) --- Linux manual page

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [DEVICE SELECTION](#DEVICE_SELECTION) \| [OPERATIONS](#OPERATIONS) \| [SEE ALSO](#SEE_ALSO) \| [AUTHOR](#AUTHOR) \| [COLOPHON](#COLOPHON) |                                   |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                           |                                   |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    setpci(8)                   The PCI Utilities                   setpci(8)

## [](#NAME)NAME

           setpci - configure PCI devices

## [](#SYNOPSIS)SYNOPSIS

           setpci [options] devices operations ...

## [](#DESCRIPTION)DESCRIPTION

           setpci is a utility for querying and configuring PCI devices.

           All numbers are entered in hexadecimal notation.

           Root privileges are necessary for almost all operations, excluding
           reads of the standard header of the configuration space on some
           operating systems.  Please see lspci(8) for details on access
           rights.

## [](#OPTIONS)OPTIONS

       General options
           -v     Tells setpci to be verbose and display detailed information
                  about configuration space accesses.

           -f     Tells setpci not to complain when there's nothing to do
                  (when no devices are selected).  This option is intended
                  for use in widely-distributed configuration scripts where
                  it's uncertain whether the device in question is present in
                  the machine or not.

           -D     `Demo mode' – don't write anything to the configuration
                  registers.  It's useful to try setpci -vD to verify that
                  your complex sequence of setpci operations does what you
                  think it should do.

           -r     Avoids bus scan if each operation selects a specific device
                  (uses the -s selector with specific domain, bus, slot, and
                  function). This is faster, but if the device does not
                  exist, it fails instead of matching an empty set of
                  devices.

           --version
                  Show setpci version. This option should be used stand-
                  alone.

           --help Show detailed help on available options. This option should
                  be used stand-alone.

           --dumpregs
                  Show a list of all known PCI registers and capabilities.
                  This option should be used stand-alone.

       PCI access options
           The PCI utilities use the PCI library to talk to PCI devices (see
           pcilib(7) for details). You can use the following options to
           influence its behavior:

           -A <method>
                  The library supports a variety of methods to access the PCI
                  hardware.  By default, it uses the first access method
                  available, but you can use this option to override this
                  decision. See -A help for a list of available methods and
                  their descriptions.

           -O <param>=<value>
                  The behavior of the library is controlled by several named
                  parameters.  This option allows one to set the value of any
                  of the parameters. Use -O help for a list of known
                  parameters and their default values.

           -H1    Use direct hardware access via Intel configuration
                  mechanism 1.  (This is a shorthand for -A intel-conf1.)

           -H2    Use direct hardware access via Intel configuration
                  mechanism 2.  (This is a shorthand for -A intel-conf2.)

           -G     Increase debug level of the library.

## [](#DEVICE_SELECTION)DEVICE SELECTION

           Before each sequence of operations you need to select which
           devices you wish that operation to affect.

           -s [[[[<domain>]:]<bus>]:][<slot>][.[<func>]]
                  Consider only devices in the specified domain (in case your
                  machine has several host bridges, they can either share a
                  common bus number space or each of them can address a PCI
                  domain of its own; domains are numbered from 0 to ffff),
                  bus (0 to ff), slot (0 to 1f) and function (0 to 7).  Each
                  component of the device address can be omitted or set to
                  "*", both meaning "any value". All numbers are hexadecimal.
                  E.g., "0:" means all devices on bus 0, "0" means all
                  functions of device 0 on any bus, "0.3" selects third
                  function of device 0 on all buses and ".4" matches only the
                  fourth function of each device.

           -d [<vendor>]:[<device>][:<class>[:<prog-if>]]
                  Select devices with specified vendor, device, class ID, and
                  programming interface.  The IDs are given in hexadecimal
                  and may be omitted or given as "*", both meaning "any
                  value". The class ID can contain "x" characters which stand
                  for "any digit".

           When -s and -d are combined, only devices that match both criteria
           are selected. When the same option is used multiple times, the
           rightmost one overrides the others and a warning is produced.

## [](#OPERATIONS)OPERATIONS

           There are two kinds of operations: reads and writes. To read a
           register, just specify its name. Writes have the form
           name=value,value... where each value is either a hexadecimal
           number or an expression of type data:mask where both data and mask
           are hexadecimal numbers. In the latter case, only the bits
           corresponding to binary ones in the mask are changed (technically,
           this is a read-modify-write operation).

           There are several ways to identify a register:

           •      Tell its address in hexadecimal.

           •      Spell its name. Setpci knows the names of all registers in
                  the standard configuration headers. Use `setpci --dumpregs'
                  to get the complete list.  See PCI bus specifications for
                  the precise meaning of these registers or consult header.h
                  or /usr/include/pci/pci.h for a brief sketch.

           •      If the register is a part of a PCI capability, you can
                  specify the name of the capability to get the address of
                  its first register. See the names starting with `CAP_' or
                  `ECAP_' in the --dumpregs output.

           •      If the name of the capability is not known to setpci, you
                  can refer to it by its number in the form CAPid or ECAPid,
                  where id is the numeric identifier of the capability in
                  hexadecimal.

           •      Each of the previous formats can be followed by +offset to
                  add an offset (a hex number) to the address. This feature
                  can be useful for addressing of registers living within a
                  capability, or to modify parts of standard registers.

           •      To choose how many bytes (1, 2, or 4) should be
                  transferred, you should append a width specifier .B, .W, or
                  .L. The width can be omitted if you are referring to a
                  register by its name and the width of the register is well
                  known.

           •      Finally, if a capability exists multiple times you can
                  choose which one to target using @number. Indexing starts
                  at 0.

           All names of registers and width specifiers are case-insensitive.

    EXAMPLES
           COMMAND
                  asks for the word-sized command register.

           4.w    is a numeric address of the same register.

           COMMAND.l
                  asks for a 32-bit word starting at the location of the
                  command register, i.e., the command and status registers
                  together.

           VENDOR_ID+1.b
                  specifies the upper byte of the vendor ID register
                  (remember, PCI is little-endian).

           CAP_PM+2.w
                  corresponds to the second word of the power management
                  capability.

           ECAP108.l
                  asks for the first 32-bit word of the extended capability
                  with ID 0x108.

## [](#SEE_ALSO)SEE ALSO

           lspci(8), pcilib(7)

## [](#AUTHOR)AUTHOR

           The PCI Utilities are maintained by Martin Mares <mj@ucw.cz>.

## [](#COLOPHON)COLOPHON

           This page is part of the pciutils (PCI utilities) project.
           Information about the project can be found at 
           ⟨http://mj.ucw.cz/sw/pciutils/⟩.  If you have a bug report for this
           manual page, send it to linux-pci@vger.kernel.org.  This page was
           obtained from the project's upstream Git repository
           ⟨git://git.kernel.org/pub/scm/utils/pciutils/pciutils.git⟩ on
           2026-08-04.  (At that time, the date of the most recent commit
           that was found in the repository was 2026-07-08.)  If you discover
           any rendering problems in this HTML version of the page, or you
           believe there is a better or more up-to-date source for the page,
           or you have corrections or improvements to the information in this
           COLOPHON (which is not part of the original manual page), send a
           mail to man-pages@man7.org

    pciutils-3.15.0                 2026-04-05                      setpci(8)

------------------------------------------------------------------------

Pages that refer to this page: [proc_bus(5)](../man5/proc_bus.5.html),  [pcilib(7)](../man7/pcilib.7.html),  [lspci(8)](../man8/lspci.8.html)

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
