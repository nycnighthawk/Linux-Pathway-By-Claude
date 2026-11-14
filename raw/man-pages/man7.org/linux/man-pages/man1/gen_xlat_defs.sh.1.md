---
{"title": "gen_xlat_defs.sh(1) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/gen_xlat_defs.sh.1.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# gen_xlat_defs.sh(1) --- Linux manual page

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [INPUT FORMAT](#INPUT_FORMAT) \| [OUTPUT FORMAT](#OUTPUT_FORMAT) \| [EXAMPLES](#EXAMPLES) \| [ARCHITECTURE HANDLING](#ARCHITECTURE_HANDLING) \| [EXIT STATUS](#EXIT_STATUS) \| [NOTES](#NOTES) \| [SEE ALSO](#SEE_ALSO) \| [AUTHORS](#AUTHORS) \| [COLOPHON](#COLOPHON) |                                   |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                                                                                                                                                         |                                   |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    GEN_XLAT_DEFS.SH(1)      General Commands Manual      GEN_XLAT_DEFS.SH(1)

## [](#NAME)NAME

           maint/gen_xlat_defs.sh - generate xlat .in files from Linux UAPI
           headers

## [](#SYNOPSIS)SYNOPSIS

           maint/gen_xlat_defs.sh

           maint/gen_xlat_defs.sh  < xlat_file_name.in

## [](#DESCRIPTION)DESCRIPTION

           maint/gen_xlat_defs.sh generates xlat .in files based on existing
           files and Linux UAPI headers.  It extracts constant definitions
           from the Linux kernel source code and produces architecture-aware
           xlat definition files suitable for use by strace's xlat system.

           The script reads an existing xlat .in file from standard input,
           extracts constant names matching the specified pattern, looks up
           their values in the Linux kernel UAPI headers, and outputs an
           updated .in file that includes architecture-specific value
           differences where applicable.

           The script automatically detects when a constant has different
           numeric values across different architectures and generates
           appropriate preprocessor directives (#if, #elif, #else, #endif) to
           handle these differences.  It also preserves existing comments and
           directives from the input file (except for the generated-by
           comment line).

## [](#OPTIONS)OPTIONS

           -f VAL_PRINT_FMT
                  Specifies the printf format string for printing numeric
                  values in the output.  Common formats include:

                  d      Decimal format (e.g., 42)

                  #x     Hexadecimal format with 0x prefix (e.g., 0x2a)

                  #o     Octal format with 0 prefix (e.g., 052)

                  u      Unsigned decimal format (e.g., 42)

           -p REGEXP_PATTERN
                  Specifies a regular expression pattern used to match
                  constant names in the input file.  Only lines matching this
                  pattern will be processed.  The pattern should match the
                  prefix or naming convention of the constants being
                  extracted (e.g., MADV_, _?MAP_, SO_).

           -d LINUX_SRC_DIR
                  Specifies the path to the Linux kernel source directory.
                  This directory should contain the standard Linux kernel
                  source tree structure with include/uapi/ subdirectories.

           -c COMMON_DEFS_GLOB_PATTERN
                  Specifies a glob pattern for locating common (architecture-
                  independent) definitions in the Linux UAPI headers.  The
                  pattern is relative to include/uapi/ in the Linux source
                  directory.  Examples: asm-generic/mman-common.h, asm-
                  generic/socket.h, asm-generic/fcntl.h.

           -a ARCH_DEFS_FILE
                  Specifies the architecture-specific definitions file name.
                  The script searches for this file in arch/*/include/uapi/
                  subdirectories of the Linux source directory.  Examples:
                  asm/mman.h, asm/socket.h, asm/fcntl.h.

## [](#INPUT_FORMAT)INPUT FORMAT

           The script reads an xlat .in file from standard input.  The input
           file can contain:

                  Constant name lines
                         Lines containing constant names (optionally with
                         trailing whitespace) that match the specified regex
                         pattern.  These will be looked up in the kernel
                         headers.

                  Comments
                         Lines starting with # or containing /* ... */ style
                         comments.  These are preserved in the output.

                  Blank lines
                         Empty lines are preserved to maintain formatting.

                  Directives
                         Special directives like #sorted, #unconditional,
                         etc. are preserved.

## [](#OUTPUT_FORMAT)OUTPUT FORMAT

           The script outputs an updated xlat .in file with the following
           features:

                  Generated-by header
                         The first line contains a comment indicating how the
                         file was generated, including all the command-line
                         options used.

                  Architecture-specific conditionals
                         When a constant has different values across
                         architectures, the script generates preprocessor
                         conditionals like:

                             #if defined __arch1__ || defined __arch2__
                             CONSTANT_NAME  value1
                             #elif defined __arch3__
                             CONSTANT_NAME  value2
                             #else
                             CONSTANT_NAME  value3
                             #endif

                  Preserved content
                         All comments, blank lines, and directives from the
                         input are preserved (except the old generated-by
                         line).

## [](#EXAMPLES)EXAMPLES

           The following examples demonstrate common usage patterns:

           Generate madvise command constants:
                  maint/gen_xlat_defs.sh -f 'd' -p 'MADV_' -d /path/to/linux \
                      -c 'asm-generic/mman-common.h' -a 'asm/mman.h' \
                      < src/xlat/madvise_cmds.in > src/xlat/madvise_cmds.in.new

           Generate mmap flag constants with hexadecimal output:
                  maint/gen_xlat_defs.sh -f '#x' -p '_?MAP_' -d /path/to/linux \
                      -c 'asm-generic/mman*.h' -a 'asm/mman.h' \
                      < src/xlat/mmap_flags.in > src/xlat/mmap_flags.in.new

           Generate open mode flag constants with octal output:
                  maint/gen_xlat_defs.sh -f '#o' -p '[_OF]' -d /path/to/linux \
                      -c 'asm-generic/fcntl.h' -a 'asm/fcntl.h' \
                      < src/xlat/open_mode_flags.in > src/xlat/open_mode_flags.in.new

           Generate socket option constants:
                  maint/gen_xlat_defs.sh -f 'u' -p 'SO_' -d /path/to/linux \
                      -c 'asm-generic/socket.h' -a 'asm/socket.h' \
                      < src/xlat/sock_options.in > src/xlat/sock_options.in.new

## [](#ARCHITECTURE_HANDLING)ARCHITECTURE HANDLING

           The script automatically handles architecture-specific differences
           in constant values.  It:

                  1.     First looks up the constant in the common
                         (architecture-independent) headers to determine the
                         default value.

                  2.     Then searches all architecture-specific header files
                         for different definitions of the same constant.

                  3.     Groups architectures with the same value together
                         using logical OR conditions.

                  4.     Generates appropriate #if / #elif / #else / #endif
                         blocks to handle all variations.

           The script also performs special handling for certain architecture
           aliases:

                  parisc Mapped to hppa in the output

                  arm64  Included when aarch64 is defined

                  x86    Expanded to x86_64 or i386

## [](#EXIT_STATUS)EXIT STATUS

           0      Success.

           1      An error occurred.  This can be due to:

                  Missing required command-line options
                         All five options (-f, -p, -d, -c, -a) are required.

                  Invalid Linux source directory
                         The specified directory does not exist or lacks the
                         expected structure.

                  Pattern matching failures
                         No constants were found matching the specified
                         pattern.

## [](#NOTES)NOTES

           The script is designed to work with the standard Linux kernel
           source tree layout where UAPI headers are located in include/uapi/
           and architecture-specific headers are in arch/*/include/uapi/.

           When a constant is not found in the common headers, the script
           issues a warning but continues processing.  The constant will
           appear in the output without a default value, and only
           architecture-specific definitions will be included if found.

           The script preserves the existing structure and formatting of the
           input file as much as possible, only updating the constant
           definitions and adding architecture-specific conditionals where
           needed.

## [](#SEE_ALSO)SEE ALSO

           strace(1)

           The xlat file format documentation in doc/README-xlat.md provides
           additional information about how generated .in files are used.

## [](#AUTHORS)AUTHORS

           The strace developers.

## [](#COLOPHON)COLOPHON

           This page is part of the strace (system call tracer) project.
           Information about the project can be found at ⟨http://strace.io/⟩.
           If you have a bug report for this manual page, send it to
           strace-devel@lists.sourceforge.net.  This page was obtained from
           the project's upstream Git repository
           ⟨https://github.com/strace/strace.git⟩ on 2026-08-04.  (At that
           time, the date of the most recent commit that was found in the
           repository was 2026-07-15.)  If you discover any rendering
           problems in this HTML version of the page, or you believe there is
           a better or more up-to-date source for the page, or you have
           corrections or improvements to the information in this COLOPHON
           (which is not part of the original manual page), send a mail to
           man-pages@man7.org

                                                          GEN_XLAT_DEFS.SH(1)

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
