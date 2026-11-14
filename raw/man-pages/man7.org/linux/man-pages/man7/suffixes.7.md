---
{"title": "suffixes(7) — Linux manual page", "url": "https://man7.org/linux/man-pages/man7/suffixes.7.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# suffixes(7) --- Linux manual page

+--------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [DESCRIPTION](#DESCRIPTION) \| [STANDARDS](#STANDARDS) \| [BUGS](#BUGS) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                            |                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    SUFFIXES(7)          Miscellaneous Information Manual         SUFFIXES(7)

## [](#NAME)NAME

           suffixes - list of file suffixes

## [](#DESCRIPTION)DESCRIPTION

           It is customary to indicate the contents of a file with the file
           suffix, which (typically) consists of a period, followed by one or
           more letters.  Many standard utilities, such as compilers, use
           this to recognize the type of file they are dealing with.  The
           make(1) utility is driven by rules based on file suffix.

           Following is a list of suffixes which are likely to be found on a
           Linux system.

           Suffix         File type
           ───────────────────────────────────────────────────────────────────
           ,v             files for RCS (Revision Control System)
           -              backup file
           .C             C++ source code, equivalent to .cc
           .F             Fortran source with cpp(1) directives
                          or file compressed using freeze
           .S             assembler source with cpp(1) directives
           .Y             file compressed using yabba
           .Z             file compressed using compress(1)
           .[0-9]+gf      TeX generic font files
           .[0-9]+pk      TeX packed font files
           .[1-9]         manual page for the corresponding section
           .[1-9][a-z]    manual page for section plus subsection
           .a             static object code library
           .ad            X application default resource file
           .ada           Ada source (may be body, spec, or combination)
           .adb           Ada body source
           .ads           Ada spec source
           .afm           PostScript font metrics
           .al            Perl autoload file
           .am            automake(1) input file
           .arc           arc(1) archive
           .arj           arj(1) archive
           .asc           OpenPGP ASCII-armored data
           .asm           (GNU) assembler source file
           .au            Audio sound file
           .aux           LaTeX auxiliary file
           .avi           (msvideo) movie
           .awk           AWK language program
           .b             LILO boot loader image
           .bak           backup file
           .bash          bash(1) shell script
           .bb            basic block list data produced by
                          gcc -ftest-coverage
           .bbg           basic block graph data produced by
                          gcc -ftest-coverage
           .bbl           BibTeX output
           .bdf           X font file
           .bib           TeX bibliographic database, BibTeX input
           .bm            bitmap source
           .bmp           bitmap
           .bz2           file compressed using bzip2(1)
           .c             C source
           .cat           message catalog files
           .cc            C++ source
           .cf            configuration file
           .cfg           configuration file
           .cgi           WWW content generating script or program
           .cls           LaTeX Class definition
           .class         Java compiled byte-code
           .conf          configuration file
           .config        configuration file
           .cpp           equivalent to .cc
           .csh           csh(1) shell script
           .cxx           equivalent to .cc
           .dat           data file
           .deb           Debian binary package (deb(5))
           .def           Modula-2 source for definition modules
           .def           other definition files
           .desc          initial part of mail message unpacked with
                          munpack(1)
           .diff          file differences (diff(1) command output)
           .dir           dbm data base directory file
           .doc           documentation file
           .dsc           Debian source package control file (dsc(5))
           .dtx           LaTeX package source file
           .dvi           TeX's device independent output
           .el            Emacs-Lisp source
           .elc           compiled Emacs-Lisp source
           .eps           encapsulated PostScript
           .exp           Expect source code
           .f             Fortran source
           .f77           Fortran 77 source
           .f90           Fortran 90 source
           .fas           precompiled Common-Lisp
           .fi            Fortran include files
           .fig           FIG image file (used by xfig(1))
           .fmt           TeX format file
           .gif           Compuserve Graphics Image File format
           .gmo           GNU format message catalog
           .gsf           Ghostscript fonts
           .gz            file compressed using gzip(1)
           .h             C or C++ header files
           .help          help file
           .hf            equivalent to .help
           .hlp           equivalent to .help
           .htm           poor man's .html
           .html          HTML document used with the World Wide Web
           .hqx           7-bit encoded Macintosh file
           .i             C source after preprocessing
           .icon          bitmap source
           .idx           reference or datum-index file for hypertext
                          or database system
           .image         bitmap source
           .in            configuration template, especially for GNU Autoconf
           .info          files for the Emacs info browser
           .info-[0-9]+   split info files
           .ins           LaTeX package install file for docstrip
           .itcl          itcl source code;
                          itcl ([incr Tcl]) is an OO extension of tcl
           .java          a Java source file
           .jpeg          Joint Photographic Experts Group format
           .jpg           poor man's .jpeg
           .js            JavaScript source code
           .jsx           JSX (JavaScript XML-like extension) source code
           .kmap          lyx(1) keymap
           .l             equivalent to .lex or .lisp
           .lex           lex(1) or flex(1) files
           .lha           lharc archive
           .lib           Common-Lisp library
           .lisp          Lisp source
           .ln            files for use with lint(1)
           .log           log file, in particular produced by TeX
           .lsm           Linux Software Map entry
           .lsp           Common-Lisp source
           .lzh           lharc archive
           .m             Objective-C source code
           .m4            m4(1) source
           .mac           macro files for various programs
           .man           manual page (usually source rather than formatted)
           .map           map files for various programs
           .me            Nroff source using the me macro package
           .mf            Metafont (font generator for TeX) source
           .mgp           MagicPoint file
           .mm            sources for groff(1) in mm - format
           .mo            Message catalog binary file
           .mod           Modula-2 source for implementation modules
           .mov           (quicktime) movie
           .mp            Metapost source
           .mp2           MPEG Layer 2 (audio) file
           .mp3           MPEG Layer 3 (audio) file
           .mpeg          movie file
           .o             object file
           .old           old or backup file
           .orig          backup (original) version of a file, from patch(1)
           .out           output file, often executable program (a.out)
           .p             Pascal source
           .pag           dbm data base data file
           .patch         file differences for patch(1)
           .pbm           portable bitmap format
           .pcf           X11 font files
           .pdf           Adobe Portable Data Format
                          (use Acrobat/acroread or xpdf)
           .perl          Perl source (see .ph, .pl, and .pm)
           .pfa           PostScript font definition files, ASCII format
           .pfb           PostScript font definition files, binary format
           .pgm           portable greymap format
           .pgp           OpenPGP binary data
           .ph            Perl header file
           .php           PHP program file
           .php3          PHP3 program file
           .pid           File to store daemon PID (e.g., crond.pid)
           .pl            TeX property list file or Perl library file
           .pm            Perl module
           .png           Portable Network Graphics file
           .po            Message catalog source
           .pod           perldoc(1) file
           .ppm           portable pixmap format
           .pr            bitmap source
           .ps            PostScript file
           .py            Python source
           .pyc           compiled python
           .qt            quicktime movie
           .r             RATFOR source (obsolete)
           .rej           patches that patch(1) couldn't apply
           .rpm           RPM software package
           .rtf           Rich Text Format file
           .rules         rules for something
           .s             assembler source
           .sa            stub libraries for a.out shared libraries
           .sc            sc(1) spreadsheet commands
           .scm           Scheme source code
           .sed           sed source file
           .sgml          SGML source file
           .sh            sh(1) scripts
           .shar          archive created by the shar(1) utility
           .shtml         HTML using Server Side Includes
           .so            Shared library or dynamically loadable object
           .sql           SQL source
           .sqml          SQML schema or query program
           .sty           LaTeX style files
           .sym           Modula-2 compiled definition modules
           .tar           archive created by the tar(1) utility
           .tar.Z         tar(1) archive compressed with compress(1)
           .tar.bz2       tar(1) archive compressed with bzip2(1)
           .tar.gz        tar(1) archive compressed with gzip(1)
           .tar.xz        tar(1) archive compressed with xz(1)
           .taz           tar(1) archive compressed with compress(1)
           .tcl           tcl source code
           .tex           TeX or LaTeX source
           .texi          equivalent to .texinfo
           .texinfo       Texinfo documentation source
           .text          text file
           .tfm           TeX font metric file
           .tgz           tar(1) archive compressed with gzip(1)
           .tif           poor man's .tiff
           .tiff          Tagged Image File Format
           .tk            tcl/tk script
           .tmp           temporary file
           .tmpl          template files
           .ts            TypeScript source code
           .tsx           TypeScript with JSX source code (.ts + .jsx)
           .txt         │ equivalent to .text
           .uu          │ equivalent to .uue
           .uue         │ binary file encoded with uuencode(1)
           .vf          │ TeX virtual font file
           .vpl         │ TeX virtual property list file
           .w           │ Silvio Levi's CWEB
           .wav         │ wave sound file
           .web         │ Donald Knuth's WEB
           .wml         │ Source file for Web Meta Language
           .xbm         │ X11 bitmap source
           .xcf         │ GIMP graphic
           .xml         │ eXtended Markup Language file
           .xpm         │ X11 pixmap source
           .xs          │ Perl xsub file produced by h2xs
           .xsl         │ XSL stylesheet
           .xz          │ file compressed with xz(1)
           .y           │ yacc(1) or bison(1) (parser generator) files
           .z           │ File compressed using pack(1) (or an old gzip(1))
           .zip         │ zip(1) archive
           .zoo         │ zoo(1) archive
           .zst         │ File compressed using zstd(1) format
           ~            │ Emacs or patch(1) backup file
           rc           │ startup (`run control') file, e.g., .newsrc

## [](#STANDARDS)STANDARDS

           General UNIX conventions.

## [](#BUGS)BUGS

           This list is not exhaustive.

## [](#SEE_ALSO)SEE ALSO

           file(1), make(1)

## [](#COLOPHON)COLOPHON

           This page is part of the man-pages (Linux kernel and C library
           user-space interface documentation) project.  Information about
           the project can be found at 
           ⟨https://www.kernel.org/doc/man-pages/⟩.  If you have a bug report
           for this manual page, see
           ⟨https://git.kernel.org/pub/scm/docs/man-pages/man-pages.git/tree/CONTRIBUTING⟩.
           This page was obtained from the tarball man-pages-6.19.tar.gz
           fetched from
           ⟨https://mirrors.edge.kernel.org/pub/linux/docs/man-pages/⟩ on
           2026-09-09.  If you discover any rendering problems in this HTML
           version of the page, or you believe there is a better or more up-
           to-date source for the page, or you have corrections or
           improvements to the information in this COLOPHON (which is not
           part of the original manual page), send a mail to
           man-pages@man7.org

    Linux man-pages 6.19            2026-05-11                    SUFFIXES(7)

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
