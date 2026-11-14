---
{"title": "slapd.plugin(5) — Linux manual page", "url": "https://man7.org/linux/man-pages/man5/slapd.plugin.5.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# slapd.plugin(5) --- Linux manual page

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [FILES](#FILES) \| [SEE ALSO](#SEE_ALSO) \| [ACKNOWLEDGEMENTS](#ACKNOWLEDGEMENTS) \| [COLOPHON](#COLOPHON) |                                   |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                     |                                   |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    SLAPD.PLUGIN(5)            File Formats Manual            SLAPD.PLUGIN(5)

## [](#NAME)NAME

           slapd.plugin - plugin configuration for slapd, the stand-alone
           LDAP daemon

## [](#SYNOPSIS)SYNOPSIS

           ETCDIR/slapd.conf

## [](#DESCRIPTION)DESCRIPTION

           The slapd.conf(5) file contains configuration information for the
           slapd(8) daemon. This configuration file is also used by the SLAPD
           tools slapadd(8), slapcat(8), slapmodify(8), and slapindex(8).

           The slapd.conf file consists of a series of global configuration
           options that apply to slapd as a whole (including all backends),
           followed by zero or more database backend definitions that contain
           information specific to a backend instance.

           The general format of slapd.conf is as follows:

               # comment - these options apply to every database
               <global configuration options>
               # first database definition & configuration options
               database    <backend 1 type>
               <configuration options specific to backend 1>
               # subsequent database definitions & configuration options
               ...

           If slapd is compiled with --enable-slapi, support for plugins
           according to Netscape's Directory Server Plug-Ins.  Version 4 of
           the API is currently implemented, with some extensions from
           version 5.

           Both global and database specific data may contain plugin
           information.  Plugins associated with a specific database are
           called before global plugins.  This manpage details the slapd(8)
           configuration statements that affect the loading of SLAPI plugins.

           Arguments that should be replaced by actual text are shown in
           brackets <>.

           The structure of the plugin directives is

           plugin <type> <lib_path> <init_function> [<arguments>]
                  Load a plugin of the specified type for the current
                  database.

           The <type> can be one of preoperation, that is executed before
           processing the operation for the specified database,
           postoperation, that is executed after the operation for the
           specified database has been processed, extendedop, that is used
           when executing an extended operation, or object.  The latter is
           used for miscellaneous types such as ACL, computed attribute and
           search filter rewriter plugins.

           The <libpath> argument specifies the path to the plugin loadable
           object; if a relative path is given, the object is looked for
           according to the underlying dynamic loading package (libtool's
           ltdl is used).

           The <init_function> argument specifies what symbol must be called
           when the plugin is first loaded.  This function should register
           the functions provided by the plugin for the desired operations.
           It should be noted that it is this init function, not the plugin
           type specified as the first argument, that determines when and for
           what operations the plugin will be invoked.  The optional
           <arguments> list is passed to the init function.

           pluginlog <file>
                  Specify an alternative path for the plugin log file
                  (default is LOCALSTATEDIR/errors).

           modulepath <pathspec>
                  This statement sets the module load path for dynamically
                  loadable backends, as described in slapd.conf(5); however,
                  since both the dynamically loadable backends and the SLAPI
                  plugins use the same underlying library (libtool's ltdl)
                  its value also affects the plugin search path.  In general
                  the search path is made of colon-separated paths; usually
                  the user-defined path is searched first; then the value of
                  the LTDL_LIBRARY_PATH environment variable, if defined, is
                  used; finally, the system-specific dynamic load path is
                  attempted (e.g. on Linux the value of the environment
                  variable LD_LIBRARY_PATH).  Please carefully read the
                  documentation of ltdl because its behavior is very platform
                  dependent.

## [](#FILES)FILES

           ETCDIR/slapd.conf
                  default slapd configuration file

           LOCALSTATEDIR/errors
                  default plugin log file

## [](#SEE_ALSO)SEE ALSO

           slapd(8),

           "OpenLDAP Administrator's Guide"
           (http://www.OpenLDAP.org/doc/admin/)

## [](#ACKNOWLEDGEMENTS)ACKNOWLEDGEMENTS

           OpenLDAP Software is developed and maintained by The OpenLDAP
           Project <http://www.openldap.org/>.  OpenLDAP Software is derived
           from the University of Michigan LDAP 3.3 Release.

## [](#COLOPHON)COLOPHON

           This page is part of the OpenLDAP (an open source implementation
           of the Lightweight Directory Access Protocol) project.
           Information about the project can be found at 
           ⟨http://www.openldap.org/⟩.  If you have a bug report for this
           manual page, see ⟨http://www.openldap.org/its/⟩.  This page was
           obtained from the project's upstream Git repository
           ⟨https://git.openldap.org/openldap/openldap.git⟩ on 2026-08-04.
           (At that time, the date of the most recent commit that was found
           in the repository was 2026-08-03.)  If you discover any rendering
           problems in this HTML version of the page, or you believe there is
           a better or more up-to-date source for the page, or you have
           corrections or improvements to the information in this COLOPHON
           (which is not part of the original manual page), send a mail to
           man-pages@man7.org

    OpenLDAP LDVERSION             RELEASEDATE                SLAPD.PLUGIN(5)

------------------------------------------------------------------------

Pages that refer to this page: [slapd.conf(5)](../man5/slapd.conf.5.html),  [slapd-config(5)](../man5/slapd-config.5.html)

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
