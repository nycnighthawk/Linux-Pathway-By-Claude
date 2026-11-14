---
{"title": "systemd.environment-generator(7) — Linux manual page", "url": "https://man7.org/linux/man-pages/man7/systemd.environment-generator.7.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# systemd.environment-generator(7) --- Linux manual page

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [EXAMPLES](#EXAMPLES) \| [SEE ALSO](#SEE_ALSO) \| [NOTES](#NOTES) \| [COLOPHON](#COLOPHON) |                                   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                     |                                   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    SYSTEMD...ENERATOR(7) systemd.environment-generator SYSTEMD...ENERATOR(7)

## [](#NAME)NAME

           systemd.environment-generator - systemd environment file
           generators

## [](#SYNOPSIS)SYNOPSIS

           /usr/lib/systemd/system-environment-generators/some-generator

           /usr/lib/systemd/user-environment-generators/some-generator

               /run/systemd/system-environment-generators/*
               /etc/systemd/system-environment-generators/*
               /usr/local/lib/systemd/system-environment-generators/*
               /usr/lib/systemd/system-environment-generators/*

               /run/systemd/user-environment-generators/*
               /etc/systemd/user-environment-generators/*
               /usr/local/lib/systemd/user-environment-generators/*
               /usr/lib/systemd/user-environment-generators/*

## [](#DESCRIPTION)DESCRIPTION

           Generators are small executables that live in
           /usr/lib/systemd/system-environment-generators/ and other
           directories listed above.  systemd(1) will execute those binaries
           very early at the startup of each manager and at configuration
           reload time, before running the generators described in
           systemd.generator(7) and before starting any units. Environment
           generators can override the environment that the manager exports
           to services and other processes.

           Generators are loaded from a set of paths determined during
           compilation, as listed above. System and user environment
           generators are loaded from directories with names ending in
           system-environment-generators/ and user-environment-generators/,
           respectively. Generators found in directories listed earlier
           override the ones with the same name in directories lower in the
           list [1]. A symlink to /dev/null or an empty file can be used to
           mask a generator, thereby preventing it from running. Please note
           that the order of the two directories with the highest priority is
           reversed with respect to the unit load path, and generators in
           /run/ overwrite those in /etc/.

           After installing new generators or updating the configuration,
           systemctl daemon-reload may be executed. This will re-run all
           generators, updating environment configuration. It will be used
           for any services that are started subsequently.

           Environment file generators are executed similarly to unit file
           generators described in systemd.generator(7), with the following
           differences:

           •   Generators are executed sequentially in the alphanumerical
               order of the final component of their name. The output of each
               generator output is immediately parsed and used to update the
               environment for generators that run after that. Thus, later
               generators can use and/or modify the output of earlier
               generators.

           •   Generators are run by every manager instance, their output can
               be different for each user.

           It is recommended to use numerical prefixes for generator names to
           simplify ordering.

## [](#EXAMPLES)EXAMPLES

           Example 1. A simple generator that extends an environment variable
           if a directory exists in the file system

               # 50-xdg-data-dirs.sh

               #!/bin/sh
               # SPDX-License-Identifier: MIT-0

               # set the default value
               XDG_DATA_DIRS="${XDG_DATA_DIRS:-/usr/local/share/:/usr/share}"

               # add a directory if it exists
               if [ -d /opt/foo/share ]; then
                   XDG_DATA_DIRS="/opt/foo/share:${XDG_DATA_DIRS}"
               fi

               # write our output
               echo "XDG_DATA_DIRS=${XDG_DATA_DIRS}"

           Example 2. A more complicated generator which reads existing
           configuration and mutates one variable

               # 90-rearrange-path.py

               #!/usr/bin/python
               # SPDX-License-Identifier: MIT-0

               """

               Proof-of-concept systemd environment generator that makes sure that bin dirs
               are always after matching sbin dirs in the path.
               (Changes /sbin:/bin:/foo/bar to /bin:/sbin:/foo/bar.)

               This generator shows how to override the configuration possibly created by
               earlier generators. It would be easier to write in bash, but let's have it
               in Python just to prove that we can, and to serve as a template for more
               interesting generators.

               """

               import os
               import pathlib

               def rearrange_bin_sbin(path):
                   """Make sure any pair of .../bin, .../sbin directories is in this order

                   >>> rearrange_bin_sbin('/bin:/sbin:/usr/sbin:/usr/bin')
                   '/bin:/sbin:/usr/bin:/usr/sbin'
                   """
                   items = [pathlib.Path(p) for p in path.split(':')]
                   for i in range(len(items)):
                       if 'sbin' in items[i].parts:
                           ind = items[i].parts.index('sbin')
                           bin = pathlib.Path(*items[i].parts[:ind], 'bin', *items[i].parts[ind + 1 :])
                           if bin in items[i + 1 :]:
                               j = i + 1 + items[i + 1 :].index(bin)
                               items[i], items[j] = items[j], items[i]
                   return ':'.join(p.as_posix() for p in items)

               if __name__ == '__main__':
                   # This should be always set. If it is not, we will just crash, which is OK too.
                   path = os.environ['PATH']
                   new = rearrange_bin_sbin(path)
                   if new != path:
                       print(f'PATH={new}')

           Example 3. Debugging a generator

               SYSTEMD_LOG_LEVEL=debug VAR_A=something VAR_B="something else" \
               /usr/lib/systemd/system-environment-generators/path-to-generator

## [](#SEE_ALSO)SEE ALSO

           systemd-environment-d-generator(8), systemd.generator(7),
           systemd(1), systemctl(1)

## [](#NOTES)NOTES

            1. 💣💥🧨💥💥💣 Please note that those configuration files must
               be available at all times. If /usr/local/ is a separate
               partition, it may not be available during early boot, and must
               not be used for configuration.

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

    systemd 262~devel                                   SYSTEMD...ENERATOR(7)

------------------------------------------------------------------------

Pages that refer to this page: [environment.d(5)](../man5/environment.d.5.html),  [systemd.unit(5)](../man5/systemd.unit.5.html),  [systemd.directives(7)](../man7/systemd.directives.7.html),  [systemd.generator(7)](../man7/systemd.generator.7.html),  [systemd.index(7)](../man7/systemd.index.7.html),  [systemd-environment-d-generator(8)](../man8/systemd-environment-d-generator.8.html)

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
