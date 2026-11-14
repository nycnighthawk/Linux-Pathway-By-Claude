---
{"title": "systemd.mstack(7) — Linux manual page", "url": "https://man7.org/linux/man-pages/man7/systemd.mstack.7.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# systemd.mstack(7) --- Linux manual page

+-------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [DESCRIPTION](#DESCRIPTION) \| [EXAMPLES](#EXAMPLES) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+-------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                         |                                   |
+-------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    SYSTEMD.MSTACK(7)             systemd.mstack            SYSTEMD.MSTACK(7)

## [](#NAME)NAME

           systemd.mstack - Mount stacks in self descriptive directories

## [](#DESCRIPTION)DESCRIPTION

           Directories with the ".mstack/" suffix may encode 'mount stacks'
           for assembling OS mount hierarchies based on bind and overlay
           mounts, for use in systemd-nspawn(1)'s --mstack= switch or the
           service manager's RootMStack= setting for services.  ".mstack/"
           directories may contain various files and subdirectories, where
           each will effect one layer of an "overlayfs" mount, or a bind
           mount. The name of the file or subdirectory indicates how it shall
           be used in the mount hierarchy. Specifically, the following names
           are defined:

            1. A layer@id/ directory will be turned into a layer of an
               overlayfs mount. The "id" identifier is used to define the
               order of the layers: a version sort is executed, with the
               first entry being the bottom layer in the "overlayfs" stack,
               and the last entry becoming the highest layer (precisely:
               highest "lowerdir") in the "overlayfs" stack.

            2. Similar, a layer@id.raw regular file will be mounted as a DDI,
               and the resulting mount will be turned into an overlayfs
               layer, following the same sorting rules.

            3. An rw directory will be turned into a writable layer at the
               very top of the "overlayfs" stack. A subdirectory data of it
               will become the "upperdir", a subdirectory work will become
               the "workdir". Note that these two subdirectories do not need
               to be created explicitly, they are created automatically on
               first use should they be missing.

            4. A bind@location/ directory will be bind mounted to the mount
               point indicated by the location identifier, in read-write
               fashion. The location is encoded via the same escaping logic
               used for naming ".mount" units, i.e. slashes become dashes.

            5. Similar, a bind@location.raw file will be mounted as a DDI,
               and the resulting mount bind mounted to the specified
               location.

            6. A robind@location/ is treated very similar to bind@location/,
               but the resulting bind mount is read-only.

            7. Similar, robind@location.raw creates a read-only bind mount
               from a DDI.

            8. If a root/ subdirectory exists, it is used as root of the
               resulting mount hierarchy, and only the usr/ subtree of the
               overlayfs mount will be bound to usr/ in the hierarchy.

           Note that each of the entry types above may be a symbolic link
           pointing to a directory or image file, instead a directory or
           image file itself.

           On each listed file or subdirectory type the systemd.v(7)
           functionality may be used, for automatic selection of versioned
           resources.

           Use the systemd-mstack(1) tool to process or mount .mstack/
           directories from the command line.

## [](#EXAMPLES)EXAMPLES

           The following .mstack/ consists of two read-only overlayfs layers
           as DDI, plus one writable directory on top. The read-only layers
           are symlinked:

            1. foobar.mstack/layer@0.raw → ../base.raw

            2. foobar.mstack/layer@1.raw → ../app.raw

            3. foobar.mstack/rw/

           The following .mstack/ consists of a read-only DDI mounted to
           "/usr/" and writable root:

            1. waldo.mstack/layer@0.raw → ../vendor.raw

            2. waldo.mstack/root/

           The following .mstack/ consists of a read-only DDI mounted as
           root, but a writable /var/ mounted on top:

            1. quux.mstack/layer@0.raw → ../myapp1.raw

            2. quux.mstack/bind:var → ../myapp1-var/

## [](#SEE_ALSO)SEE ALSO

           systemd(1), systemd-mstack(1), systemd-nspawn(1), systemd.exec(5),
           systemd.v(7), systemd-vpick(1)

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

    systemd 262~devel                                       SYSTEMD.MSTACK(7)

------------------------------------------------------------------------

Pages that refer to this page: [systemd-mstack(1)](../man1/systemd-mstack.1.html),  [systemd-nspawn(1)](../man1/systemd-nspawn.1.html),  [org.freedesktop.import1(5)](../man5/org.freedesktop.import1.5.html),  [systemd.exec(5)](../man5/systemd.exec.5.html),  [systemd.directives(7)](../man7/systemd.directives.7.html),  [systemd.index(7)](../man7/systemd.index.7.html)

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
