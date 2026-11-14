---
{"title": "stap-jupyter(1) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/stap-jupyter.1.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# stap-jupyter(1) --- Linux manual page

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [INSTALL OPTIONS](#INSTALL_OPTIONS) \| [CONTAINER OPTIONS](#CONTAINER_OPTIONS) \| [CONTAINER COMMANDS](#CONTAINER_COMMANDS) \| [SEE ALSO](#SEE_ALSO) \| [BUGS](#BUGS) \| [COLOPHON](#COLOPHON) |                                   |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                                                         |                                   |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    STAP-JUPYTER-*(1)        General Commands Manual        STAP-JUPYTER-*(1)

## [](#NAME)NAME

           stap-jupyter-install   - locally install isystemtap

           stap-jupyter-container - manage an isystemtap container image

## [](#SYNOPSIS)SYNOPSIS

           stap-jupyter-install [--remove] [--container-install PREFIX]

           stap-jupyter-container [--repo REPOSITORY] [--image IMAGE] [--tag
           TAG] [--keyname KEYNAME] --{run, pull, build, publish, remove}

## [](#DESCRIPTION)DESCRIPTION

           ISystemtap is an interactive jupyter interface for the incremental
           writing and running of Systemtap scripts.

           The stap-jupyter-install program can be used to locally install
           the ISystemtap jupyter kernel, language-server and jupyter-lab
           extension in ~/.systemtap/jupyter.  Once installed, the kernel can
           be used with jupyter-lab.

           Alternatively the stap-jupyter-container program can be used to
           run ISystemtap within a container, preventing the need for any
           local jupyter kernel installation.

## [](#INSTALL_OPTIONS)INSTALL OPTIONS

           The following options are supported by stap-jupyter-install. Any
           other option prints a short help message.

           --remove
                  Uninstall the local ISystemtap files.

           --container-install PREFIX
                  [Intended For Maintainers Only] This is used to specify the
                  PREFIX of the install directory for stap. It is called
                  within the container build process, and should not be used
                  otherwise.

## [](#CONTAINER_OPTIONS)CONTAINER OPTIONS

           The following options are supported by stap-jupyter-container. Any
           other option prints a short help message.

           --repo REPOSITORY
                  Specify which repository to use, defaults to "quay.io".

           --image IMAGE
                  Specify the image name. Defaults to "systemtap/isystemtap"

           --tag TAG
                  Specify the image tag. Defaults to "latest"

           --keyname KEYNAME
                  In order for the container to run stap it needs to ssh to
                  the host. It requires an ssh key pair, and is specified by
                  KEYNAME, which is by default "id_rsa".

## [](#CONTAINER_COMMANDS)CONTAINER COMMANDS

           The following commands are recognized by stap-jupyter-container.
           One of the following is required.

           --run
                   Run the image. Pulls if not done already.

           --pull
                   Pulls the image.

           --build
                   Builds a local copy of the image. The repo will be
                  "localhost". See podman images.

           --remove
                   Removes the image.

           --publish
                   [Intended For Maintainers Only] This is used to publish
                  the built image. It requires write permissions to
                  https://quay.io/systemtap/isystemtap.

## [](#SEE_ALSO)SEE ALSO

           stap(1),
           podman(1)
           ssh(1)

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

                                                            STAP-JUPYTER-*(1)

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
