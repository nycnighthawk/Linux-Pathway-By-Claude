---
{"title": "gawk(1) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/gawk.1.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# gawk(1) --- Linux manual page

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [README FIRST](#README_FIRST) \| [DESCRIPTION](#DESCRIPTION) \| [OPTION FORMAT](#OPTION_FORMAT) \| [OPTIONS](#OPTIONS) \| [AWK PROGRAM EXECUTION](#AWK_PROGRAM_EXECUTION) \| [VARIABLES, RECORDS AND FIELDS](#VARIABLES,_RECORDS_AND_FIELDS) \| [PATTERNS AND ACTIONS](#PATTERNS_AND_ACTIONS) \| [USER-DEFINED FUNCTIONS](#USER-DEFINED_FUNCTIONS) \| [DYNAMICALLY LOADING NEW FUNCTIONS](#DYNAMICALLY_LOADING_NEW_FUNCTIONS) \| [SIGNALS](#SIGNALS) \| [INTERNATIONALIZATION](#INTERNATIONALIZATION) \| [GNU EXTENSIONS](#GNU_EXTENSIONS) \| [ENVIRONMENT VARIABLES](#ENVIRONMENT_VARIABLES) \| [EXIT STATUS](#EXIT_STATUS) \| [VERSION INFORMATION](#VERSION_INFORMATION) \| [AUTHORS](#AUTHORS) \| [BUG REPORTS AND QUESTIONS](#BUG_REPORTS_AND_QUESTIONS) \| [BUGS](#BUGS) \| [SEE ALSO](#SEE_ALSO) \| [EXAMPLES](#EXAMPLES) \| [COPYING PERMISSIONS](#COPYING_PERMISSIONS) \| [COLOPHON](#COLOPHON) |                                   |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |                                   |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    GAWK(1)                      Utility Commands                     GAWK(1)

## [](#NAME)NAME

           gawk - pattern scanning and processing language

## [](#SYNOPSIS)SYNOPSIS

           gawk [ POSIX or GNU style options ] -f program-file [ -- ] file
           ...
           gawk [ POSIX or GNU style options ] [ -- ] program-text file ...

## [](#README_FIRST)README FIRST

           This manual page is provided as a courtesy.  Please note that the
           One Source Of Truth for gawk is the Texinfo manual, GAWK:
           Effective AWK Programming, available online in several formats at
           this link ⟨https://www.gnu.org/software/gawk/manual⟩.  The Texinfo
           manual should always be considered to be authoritative.

           This manual page is intentionally as terse as possible.  Full
           details are provided in in the manual, and you should look there
           for the full story on any specific feature.  Where possible, links
           to the online version of the manual are provided.

           Furthermore, the gawk maintainer reserves the right in the future
           to remove this manual page from the distribution in order to ease
           his maintenance burden.

## [](#DESCRIPTION)DESCRIPTION

           Gawk is the GNU Project's implementation of the AWK programming
           language.  It conforms to the definition of the language in the
           POSIX 1003.1 standard.  This version in turn is based on the
           description in the first edition (1987) of The AWK Programming
           Language, by Aho, Kernighan, and Weinberger.  Gawk provides the
           additional features found in the current version of Brian
           Kernighan's awk and numerous GNU-specific extensions.

           The command line consists of options to gawk itself, the AWK
           program text (if not supplied via the -f or --include options),
           and values to be made available in the ARGC and ARGV pre-defined
           AWK variables.

## [](#OPTION_FORMAT)OPTION FORMAT

           Gawk options may be either traditional POSIX-style one letter
           options, or GNU-style long options.  POSIX options start with a
           single “-”, while long options start with “--”.

## [](#OPTIONS)OPTIONS

           Gawk accepts the following options.  Standard options are listed
           first, followed by options for gawk extensions, listed
           alphabetically by short option.  A full description of the options
           is provided at this link 
           ⟨https://www.gnu.org/software/gawk/manual/html_node/Options⟩.

           -f program-file, --file program-file
                  Read the AWK program source from the file program-file,
                  instead of from the first command line argument.  Multiple
                  -f options may be used.

           -F fs, --field-separator fs
                  Use fs for the input field separator (the value of the FS
                  predefined variable).

           -v var=val, --assign var=val
                  Assign the value val to the variable var, before execution
                  of the program begins.

           -b, --characters-as-bytes
                  Treat all input data as single-byte characters.  The
                  --posix option overrides this one.

           -c, --traditional
                  Run in compatibility mode.

           -C, --copyright
                  Print the short version of the GNU copyright information
                  message on the standard output and exit successfully.

           -d[file], --dump-variables[=file]
                  Print a sorted list of global variables, their types and
                  final values to file.  The default file is awkvars.out in
                  the current directory.

           -D[file], --debug[=file]
                  Enable debugging of AWK programs.  For details about the
                  debugger, see this link 
                  ⟨https://www.gnu.org/software/gawk/manual/html_node/Debugger⟩.

           -e program-text, --source program-text
                  Use program-text as AWK program source code.

           -E file, --exec file
                  Similar to -f, however, this option is the last one
                  processed.  This should be used with #! scripts,
                  particularly for CGI applications, to avoid passing in
                  options or source code (!) on the command line from a URL.
                  This option disables command-line variable assignments.

           -g, --gen-pot
                  Scan and parse the AWK program, and generate a GNU .pot
                  (Portable Object Template) format file on standard output
                  with entries for all localizable strings in the program.
                  The program itself doesn't run.

           -h, --help
                  Print a relatively short summary of the available options
                  on the standard output.  Per the GNU Coding Standards,
                  these options cause an immediate, successful exit.

           -i include-file, --include include-file
                  Load an awk source library.  For more information, see this
                  link 
                  ⟨https://www.gnu.org/software/gawk/manual/html_node/AWKPATH-
                  Variable⟩.

           -I, --trace
                  Print to standard error the internal byte code names as
                  they are executed when running the program.

           -k, --csv
                  Enable CSV special processing.  See Comma Separated Values,
                  below, for more information.

           -l lib, --load lib
                  Load a gawk extension from the shared library lib.  For
                  more information, see this link 
                  ⟨https://www.gnu.org/software/gawk/manual/html_node/AWKLIBPATH-
                  Variable⟩.

           -L [value], --lint[=value]
                  Provide warnings about constructs that are dubious or non-
                  portable to other AWK implementations.  See this link 
                  ⟨https://www.gnu.org/software/gawk/manual/html_node/Options⟩
                  for the list of possible values for value.

           -M, --bignum
                  Force arbitrary precision arithmetic on numbers.  This
                  option has no effect if gawk is not compiled to use the GNU
                  MPFR and GMP libraries.  (In such a case, gawk issues a
                  warning.)

           -n, --non-decimal-data
                  Recognize octal and hexadecimal values in input data.  Use
                  this option with great caution!

           -N, --use-lc-numeric
                  Force gawk to use the locale's decimal point character when
                  parsing input data.

           -o[file], --pretty-print[=file]
                  Output a pretty printed version of the program to file.
                  The default file is awkprof.out in the current directory.
                  This option implies --no-optimize.

           -O, --optimize
                  Apply gawk's default optimizations to the program's
                  internal representation.  This is the default.

           -p[prof-file], --profile[=prof-file]
                  Start a profiling session, and send the profiling data to
                  prof-file.  The default is awkprof.out in the current
                  directory.  This option implies --no-optimize.

           -P, --posix
                  Turn on compatibility mode, and disable a number of common
                  extensions.

           -s, --no-optimize
                  Disable gawk's default optimizations upon the internal
                  representation of the program.

           -S, --sandbox
                  Run gawk in sandbox mode.

           -V, --version
                  Print version information for this particular copy of gawk
                  on the standard output.  This is useful when reporting
                  bugs.  Per the GNU Coding Standards, these options cause an
                  immediate, successful exit.

           --     Signal the end of options.  This is useful to allow further
                  arguments to the AWK program itself to start with a “-”.

           In compatibility mode, any other options are flagged as invalid,
           but are otherwise ignored.  In normal operation, as long as
           program text has been supplied, unknown options are passed on to
           the AWK program in the ARGV array for processing.

           For POSIX compatibility, the -W option may be used, followed by
           the name of a long option.

## [](#AWK_PROGRAM_EXECUTION)AWK PROGRAM EXECUTION

           An AWK program consists of a sequence of optional directives,
           pattern-action statements, and optional function definitions.

                  @include "filename"
                  @nsinclude "filename"
                  @load "filename"
                  @namespace "name"
                  pattern   { action statements }
                  function name(parameter list) { statements }

           Gawk first reads the program source from the program-file(s) if
           specified, from arguments to --source, or from the first non-
           option argument on the command line.  Gawk reads the program text
           as if all the program-files and command line source texts had been
           concatenated together.

           In addition, lines beginning with @include may be used to include
           other source files into your program.  This is equivalent to using
           the --include option.  Lines beginning with @nsinclude also
           include files, but with two differences.  First, the namespace in
           the included file is not reset to the default of awk, and such
           files may be included multiple times.

           Lines beginning with @load may be used to load extension functions
           into your program.  This is equivalent to using the --load option.

           The environment variable AWKPATH specifies a search path to use
           when finding source files named with the -f and --include options.
           See this link 
           ⟨https://www.gnu.org/software/gawk/manual/html_node/AWKPATH-
           Variable⟩.

           The environment variable AWKLIBPATH specifies a search path to use
           when finding source files named with the --load option.  See this
           link 
           ⟨https://www.gnu.org/software/gawk/manual/html_node/AWKLIBPATH-
           Variable⟩.

           Gawk executes AWK programs as follows: First, all variable
           assignments specified via the -v option are performed.  Next, gawk
           compiles the program into an internal form.  Then, gawk executes
           the code in the BEGIN rule(s) (if any), and then proceeds to read
           each file named in the ARGV array (up to ARGV[ARGC-1]).  If there
           are no files named on the command line, gawk reads the standard
           input.

           A filename on the command line of the form var=val is treated as a
           variable assignment.  The variable var is assigned the value val.
           (This happens after any BEGIN rule(s) have been run.)

           If the value of a particular element of ARGV is empty (""), gawk
           skips over it.

           For each input file, if a BEGINFILE rule exists, gawk executes the
           associated code before processing the contents of the file.
           Similarly, gawk executes the code associated with ENDFILE rules
           after processing the file.

           For each record in the input, gawk tests to see if it matches any
           pattern in the AWK program.  For each pattern that the record
           matches, gawk executes the associated action.  The patterns are
           tested in the order they occur in the program.

           Finally, after all the input is exhausted, gawk executes the code
           in the END rule(s) (if any).

## [](#VARIABLES,_RECORDS_AND_FIELDS)VARIABLES, RECORDS AND FIELDS

           AWK variables are dynamic; they come into existence when they are
           first used.  Their values are either floating-point numbers or
           strings, or both, depending upon how they are used.  Additionally,
           gawk allows variables to have regular-expression type.  AWK also
           has one dimensional arrays; arrays with multiple dimensions may be
           simulated.  However, gawk provides true arrays of arrays.  Several
           pre-defined variables are set as a program runs; these are
           described as needed and summarized below.

       Records
           You control how records are separated by assigning values to the
           built-in variable RS.  See this link 
           ⟨https://www.gnu.org/software/gawk/manual/html_node/Records⟩ for
           the details.  Normally, records are separated by newline
           characters.

       Fields
           As each input record is read, gawk splits the record into fields,
           using the value of the FS variable as the field separator.
           Additionally, FIELDWIDTHS and FPAT may be used to control input
           field splitting.  See the details, starting at this link 
           ⟨https://www.gnu.org/software/gawk/manual/html_node/Fields⟩.

           Each field in the input record may be referenced by its position:
           $1, $2, and so on.  $0 is the whole record, including leading and
           trailing whitespace.

           The variable NF is set to the total number of fields in the input
           record.

           Assigning a value to an existing field causes the whole record to
           be rebuilt when $0 is referenced.  Similarly, assigning a value to
           $0 causes the record to be resplit, creating new values for the
           fields.

       Comma Separated Values
           When invoked with either the -k or the --csv option, gawk record
           determination and field splitting are different: records are
           terminated by unquoted newlines, and fields are separated by
           commas.  Double-quotes may be used to enclose fields containing
           commas, newlines, or doubled double-quotes.  See this link 
           ⟨https://www.gnu.org/software/gawk/manual/html_node/Comma-
           Separated-Fields⟩ for more details.

       Built-in Variables
           Gawk's built-in variables are listed below.  This list is
           purposely terse.  For details, see this link 
           ⟨https://www.gnu.org/software/gawk/manual/html_node/Built_002din-
           Variables⟩.

           ARGC   The number of command line arguments.

           ARGIND The index in ARGV of the current file being processed.

           ARGV   Array of command line arguments.  The array is indexed from
                  0 to ARGC - 1.

           BINMODE
                  On non-POSIX systems, specifies use of “binary” mode for
                  all file I/O.  See this link 
                  ⟨https://www.gnu.org/software/gawk/manual/html_node/PC-
                  Using⟩ for the details.

           CONVFMT
                  The conversion format for numbers, "%.6g", by default.

           ENVIRON
                  An array containing the values of the current environment.

           ERRNO  A string describing the problem if a system error occurs
                  doing a redirection for getline, during a read for getline,
                  or during a close().

           FIELDWIDTHS
                  A whitespace-separated list of field widths.  See this link
                  
                  ⟨https://www.gnu.org/software/gawk/manual/html_node/Constant-
                  Size⟩.

           FILENAME
                  The name of the current input file.  If no files are
                  specified on the command line, the value of FILENAME is
                  “-”.  However, FILENAME is undefined inside the BEGIN rule
                  (unless set by getline).

           FNR    The input record number in the current input file.

           FPAT   A regular expression describing the contents of the fields
                  in a record. See this link 
                  ⟨https://www.gnu.org/software/gawk/manual/html_node/Splitting-
                  By-Content⟩.

           FS     The input field separator, a space by default.  See this
                  link 
                  ⟨https://www.gnu.org/software/gawk/manual/html_node/Field-
                  Separators⟩.

           FUNCTAB
                  An array whose indices and corresponding values are the
                  names of all the user-defined or extension functions in the
                  program.

           IGNORECASE
                  Controls the case-sensitivity of all regular expression and
                  string operations.  See this link 
                  ⟨https://www.gnu.org/software/gawk/manual/html_node/Case_002dsensitivity⟩.

           LINT   Provides dynamic control of the --lint option from within
                  an AWK program.

           NF     The number of fields in the current input record.

           NR     The total number of input records seen so far.

           OFMT   The output format for numbers, "%.6g", by default.

           OFS    The output field separator, a space by default.

           ORS    The output record separator, by default a newline.

           PREC   The working precision of arbitrary precision floating-point
                  numbers, 53 by default.

           PROCINFO
                  The elements of this array provide access to information
                  about the running AWK program.  See this link 
                  ⟨https://www.gnu.org/software/gawk/manual/html_node/Auto_002dset⟩.

           ROUNDMODE
                  The rounding mode to use for arbitrary precision arithmetic
                  on numbers, by default "N" (IEEE-754 roundTiesToEven mode).
                  See this link 
                  ⟨https://www.gnu.org/software/gawk/manual/html_node/Setting-
                  the-rounding-mode⟩.

           RS     The input record separator, by default a newline.

           RT     The record terminator.  Gawk sets RT to the input text that
                  matched the character or regular expression specified by
                  RS.

           RSTART The index of the first character matched by match(); 0 if
                  no match.

           RLENGTH
                  The length of the string matched by match(); -1 if no
                  match.

           SUBSEP The string used to separate multiple subscripts in array
                  elements, by default "\034".

           SYMTAB An array whose indices are the names of all currently
                  defined global variables and arrays in the program.

           TEXTDOMAIN
                  The text domain of the AWK program; used to find the
                  localized translations for the program's strings.

       Arrays
           Arrays are subscripted with an expression between square brackets
           ([ and ]).  If the expression is an expression list (expr, expr
           ...)  then the array subscript is a string consisting of the
           concatenation of the (string) value of each expression, separated
           by the value of the SUBSEP variable.  This facility simulates
           multidimensional arrays.  For example:

                  i = "A"; j = "B"; k = "C"
                  x[i, j, k] = "hello, world\n"

           assigns the string "hello, world\n" to the element of the array x
           which is indexed by the string "A\034B\034C".  All arrays in AWK
           are associative, i.e., indexed by string values.

           The special operator in may be used to test if an array has an
           index consisting of a particular value:

                  if (val in array)
                       print array[val]

           If the array has multiple subscripts, use (i, j) in array.

           The in construct may also be used in a for loop to iterate over
           all the elements of an array.  However, the (i, j) in array
           construct only works in tests, not in for loops.

           An element may be deleted from an array using the delete
           statement.  The delete statement may also be used to delete the
           entire contents of an array, just by specifying the array name
           without a subscript.

           gawk supports true multidimensional arrays.  See this link 
           ⟨https://www.gnu.org/software/gawk/manual/html_node/Arrays⟩.

       Namespaces
           Gawk provides a simple namespace facility to help work around the
           fact that all variables in AWK are global.  For more details, see
           this link 
           ⟨https://www.gnu.org/software/gawk/manual/html_node/Namespaces⟩.

       Variable Typing And Conversion
           Variables and fields may be (floating point) numbers, or strings,
           or both.  They may also be regular expressions.  How the value of
           a variable is interpreted depends upon its context.  If used in a
           numeric expression, it will be treated as a number; if used as a
           string it will be treated as a string.

           To force a variable to be treated as a number, add zero to it; to
           force it to be treated as a string, concatenate it with the null
           string.

           Uninitialized variables have the numeric value zero and the string
           value "" (the null, or empty, string).

           Much more (important!) detail may be found in the manual. See this
           link 
           ⟨https://www.gnu.org/software/gawk/manual/html_node/Typing-and-
           Comparison⟩.

       Octal and Hexadecimal Constants
           You may use C-style octal and hexadecimal constants in your AWK
           program source code.

       String Constants
           String constants in AWK are sequences of characters enclosed
           between double quotes (like "value").  Within strings, certain
           escape sequences are recognized, as in C.  See this link 
           ⟨https://www.gnu.org/software/gawk/manual/html_node/Escape-
           Sequences⟩ for the details.

       Regexp Constants
           A regular expression constant is a sequence of characters enclosed
           between forward slashes (like /value/).  The escape sequences
           described in the manual may also be used inside constant regular
           expressions.

           Gawk provides strongly typed regular expression constants.  These
           are written with a leading @ symbol like so: @/value/.  Such
           constants may be assigned to scalars (variables, array elements)
           and passed to user-defined functions.  Variables that have been so
           assigned have regular expression type.

## [](#PATTERNS_AND_ACTIONS)PATTERNS AND ACTIONS

           AWK is a line-oriented language.  The pattern comes first, and
           then the action.  Action statements are enclosed in { and }.
           Either the pattern may be missing, or the action may be missing,
           but, of course, not both.  If the pattern is missing, the action
           executes for every single record of input.  A missing action is
           equivalent to { print } which prints the entire record.

           Comments begin with the # character, and continue until the end of
           the line.  Empty lines may be used to separate statements.  See
           this link 
           ⟨https://www.gnu.org/software/gawk/manual/html_node/Statements_002fLines⟩
           for the rules about when statements continue across lines.

       Patterns
           AWK patterns may be one of the following:

                  BEGIN
                  END
                  BEGINFILE
                  ENDFILE
                  /regular expression/
                  relational expression
                  pattern && pattern
                  pattern || pattern
                  pattern ? pattern : pattern
                  (pattern)
                  ! pattern
                  pattern1, pattern2

           BEGIN and END are two special kinds of patterns which are not
           tested against the input.  The action parts of all BEGIN patterns
           execute in order as if all the statements had been written in a
           single BEGIN rule.  They execute before any of the input is read.
           Similarly, all the END rule statements execute when all the input
           is exhausted (or when an exit statement is executed).  BEGIN and
           END patterns cannot be combined with other patterns in pattern
           expressions, nor may they have missing action parts.

           BEGINFILE and ENDFILE are additional special patterns whose
           actions execute before reading the first record of each command-
           line input file and after reading the last record of each file.
           See this link 
           ⟨https://www.gnu.org/software/gawk/manual/html_node/BEGINFILE_002fENDFILE⟩.

           For more information on patterns and their constituent elements,
           see this link 
           ⟨https://www.gnu.org/software/gawk/manual/html_node/Pattern-
           Overview⟩.

       Actions
           Action statements are enclosed in braces, { and }.  Action
           statements consist of the usual assignment, conditional, and
           looping statements found in most languages.  The operators,
           control statements, and input/output statements available are
           patterned after those in C.

       Operators
           The operators in AWK, in order of decreasing precedence, are:

           (...)  Grouping

           $      Field reference.

           ++ --  Increment and decrement, both prefix and postfix.

           ^      Exponentiation.

           + - !  Unary plus, unary minus, and logical negation.

           * / %  Multiplication, division, and modulus.

           + -    Addition and subtraction.

           space  String concatenation.

           |   |& Piped I/O for getline, print, and printf.

           < > <= >= == !=
                  The regular relational operators.

           ~ !~   Regular expression match, negated match.

           in     Array membership.

           &&     Logical AND.

           ||     Logical OR.

           ?:     The C conditional expression, of the form expr1 ? expr2 :
                  expr3.  If expr1 is true, the value of the expression is
                  expr2, otherwise it is expr3.  Only one of expr2 and expr3
                  is evaluated.

           = += -= *= /= %= ^=
                  Assignment.  Both absolute assignment (var = value) and
                  operator-assignment (the other forms) are supported.

       Control Statements
           The control statements are as follows:

                  if (condition) statement [ else statement ]
                  while (condition) statement
                  do statement while (condition)
                  for (expr1; expr2; expr3) statement
                  for (var in array) statement
                  break
                  continue
                  delete array[index]
                  delete array
                  exit [ expression ]
                  { statements }
                  switch (expression) {
                  case value|regex : statement
                  ...
                  [ default: statement ]
                  }

       I/O Statements
           The input/output statements are as follows:

           close(file [, how])
                  Close an open file, pipe or coprocess.  See this link 
                  ⟨https://www.gnu.org/software/gawk/manual/html_node/I_002fO-
                  Functions⟩.

           getline
                  Set $0 from the next input record; set NF, NR, FNR, RT.

           getline <file
                  Set $0 from the next record of file; set NF, RT.

           getline var
                  Set var from the next input record; set NR, FNR, RT.

           getline var <file
                  Set var from the next record of file; set RT.

           command | getline [var]
                  Run command, piping the output either into $0 or var, as
                  above, and RT.

           command |& getline [var]
                  Run command as a coprocess piping the output either into $0
                  or var, as above, and RT.  (The command can also be a
                  socket.  See the subsection Special File Names, below.)

           fflush([file])
                  Flush any buffers associated with the open output file or
                  pipe file.  If file is missing or if it is the null string,
                  then flush all open output files and pipes.

           next   Stop processing the current input record.  Read the next
                  input record and start processing over with the first
                  pattern in the AWK program.  Upon reaching the end of the
                  input data, execute any END rule(s).

           nextfile
                  Stop processing the current input file.  The next input
                  record read comes from the next input file.  Update
                  FILENAME and ARGIND, reset FNR to 1, and start processing
                  over with the first pattern in the AWK program.  Upon
                  reaching the end of the input data, execute any ENDFILE and
                  END rule(s).

           print  Print the current record.  The output record is terminated
                  with the value of ORS.

           print expr-list
                  Print expressions.  Each expression is separated by the
                  value of OFS.  The output record is terminated with the
                  value of ORS.

           print expr-list >file
                  Print expressions on file.

           printf fmt, expr-list
                  Format and print.

           printf fmt, expr-list >file
                  Format and print on file.

           system(cmd-line)
                  Execute the command cmd-line, and return the exit status.
                  See this link 
                  ⟨https://www.gnu.org/software/gawk/manual/html_node/I_002fO-
                  Functions⟩ for more details.

           Additional output redirections are allowed for print and printf:

           print ... >> file
                  Append output to the file.

           print ... | command
                  Write on a pipe.

           print ... |& command
                  Send data to a coprocess or socket.  (See also the
                  subsection Special File Names, below.)

           The getline function returns 1 on success, zero on end of file,
           and -1 on an error.  Upon an error, ERRNO describes the problem.
           It may be possible to retry failing I/O; see this link 
           ⟨https://www.gnu.org/software/gawk/manual/html_node/Retrying-
           Input⟩.

           NOTE: Failure in opening a two-way socket results in a non-fatal
           error being returned to the calling function.  If using a pipe,
           coprocess, or socket to getline, or from print or printf within a
           loop, you must use close() to create new instances of the command
           or socket.  AWK does not automatically close pipes, sockets, or
           coprocesses when they return EOF.

           The AWK versions of the printf statement and sprintf() function
           are similar to those of C.  See this link 
           ⟨https://www.gnu.org/software/gawk/manual/html_node/Printf⟩.

       Special File Names
           When doing I/O redirection from either print or printf into a
           file, or via getline from a file, gawk recognizes certain special
           filenames internally.  These filenames allow access to open file
           descriptors inherited from gawk's parent process (usually the
           shell).  These file names may also be used on the command line to
           name data files.  The filenames are:

           -      The standard input.

           /dev/stdin
                  The standard input.

           /dev/stdout
                  The standard output.

           /dev/stderr
                  The standard error output.

           /dev/fd/n
                  The file associated with the open file descriptor n.

           The following special filenames may be used with the |& coprocess
           operator for creating TCP/IP network connections:

           /inet/tcp/lport/rhost/rport
           /inet4/tcp/lport/rhost/rport
           /inet6/tcp/lport/rhost/rport
                  Files for a TCP/IP connection on local port lport to remote
                  host rhost on remote port rport.  Use a port of 0 to have
                  the system pick a port.  Use /inet4 to force an IPv4
                  connection, and /inet6 to force an IPv6 connection.  Plain
                  /inet uses the system default (most likely IPv4).  Usable
                  only with the |& two-way I/O operator.

       Numeric Functions
           AWK has the following built-in arithmetic functions:

           atan2(y, x)
                  Return the arctangent of y/x in radians.

           cos(expr)
                  Return the cosine of expr, which is in radians.

           exp(expr)
                  The exponential function.

           int(expr)
                  Truncate to integer.

           log(expr)
                  The natural logarithm function.

           rand() Return a random number N, between zero and one, such that 0
                  ≤ N < 1.

           sin(expr)
                  Return the sine of expr, which is in radians.

           sqrt(expr)
                  Return the square root of expr.

           srand([expr])
                  Use expr as the new seed for the random number generator.
                  If no expr is provided, use the time of day.  Return the
                  previous seed for the random number generator.

       String Functions
           Gawk has the following built-in string functions; details are
           provided in this link 
           ⟨https://www.gnu.org/software/gawk/manual/html_node/String-
           Functions⟩.

           asort(s [, d [, how] ])
                  Return the number of elements in the source array s.  Sort
                  the contents of s, replacing the indices of the sorted
                  values with integers starting with 1.  If given the
                  destination array d, duplicate s into d, and then sort d,
                  leaving the indices of s unchanged.  The optional string
                  how controls the direction and the comparison mode.  See
                  this link 
                  ⟨https://www.gnu.org/software/gawk/manual/html_node/String-
                  Functions⟩ for valid values for how.  s and d may be the
                  same array; this only makes sense when supplying the third
                  argument as well.

           asorti(s [, d [, how] ])
                  Return the number of elements in the source array s.  Like
                  asort(), except that the array indices are used for
                  sorting.

           gensub(r, s, h [, t])
                  Search the target string t for matches of the regular
                  expression r.  See this link 
                  ⟨https://www.gnu.org/software/gawk/manual/html_node/String-
                  Functions⟩.

           gsub(r, s [, t])
                  For each substring matching the regular expression r in the
                  string t, substitute the string s, and return the number of
                  substitutions.  If t is not supplied, use $0.  An & in the
                  replacement text is replaced with the text that was
                  actually matched.  Use \& to get a literal &.

           index(s, t)
                  Return the index of the string t in the string s, or zero
                  if t is not present.

           length([s])
                  Return the length of the string s, or the length of $0 if s
                  is not supplied.  With an array argument, length() returns
                  the number of elements in the array.

           match(s, r [, a])
                  Return the position in s where the regular expression r
                  occurs, or zero if r is not present, and set the values of
                  RSTART and RLENGTH.

           patsplit(s, a [, r [, seps] ])
                  Split the string s into the array a and the separators
                  array seps on the regular expression r, and return the
                  number of fields.  Splitting behaves identically to field
                  splitting with FPAT.

           split(s, a [, r [, seps] ])
                  Split the string s into the array a and the separators
                  array seps on the regular expression r, and return the
                  number of fields.  If r is omitted, FS is used instead.
                  The arrays a and seps are cleared first.  Splitting behaves
                  identically to field splitting.

           sprintf(fmt, expr-list)
                  Print expr-list according to fmt, and return the resulting
                  string.

           strtonum(str)
                  Examine str, and return its numeric value.  See the manual
                  for the details.

           sub(r, s [, t])
                  Like gsub(), but replace only the first matching substring.
                  Return either zero or one.

           substr(s, i [, n])
                  Return the at-most n-character substring of s starting at
                  i.  If n is omitted, use the rest of s.

           tolower(str)
                  Return a copy of the string str, with all the uppercase
                  characters in str translated to their corresponding
                  lowercase counterparts.  Non-alphabetic characters are left
                  unchanged.

           toupper(str)
                  Return a copy of the string str, with all the lowercase
                  characters in str translated to their corresponding
                  uppercase counterparts.  Non-alphabetic characters are left
                  unchanged.

           Gawk is multibyte aware.  This means that index(), length(),
           substr() and match() all work in terms of characters, not bytes.
           toupper() and tolower() are locale-aware.

       Time Functions
           Gawk provides the following functions for obtaining time stamps
           and formatting them.  Details are provided in this link 
           ⟨https://www.gnu.org/software/gawk/manual/html_node/Time-
           Functions⟩.

           mktime(datespec [, utc-flag])
                  Turn datespec into a time stamp of the same form as
                  returned by systime(), and return the result.

           strftime([format [, timestamp[, utc-flag]]])
                  Format timestamp according to the specification in format.

           systime()
                  Return the current time of day as the number of seconds
                  since the Epoch (1970-01-01 00:00:00 UTC on POSIX systems).

       Bit Manipulations Functions
           Gawk supplies the following bit manipulation functions.  Passing
           negative operands to any of these functions causes a fatal error.
           The functions are:

           and(v1, v2 [, ...])
                  Return the bitwise AND of the values provided in the
                  argument list.  There must be at least two.

           compl(val)
                  Return the bitwise complement of val.

           lshift(val, count)
                  Return the value of val, shifted left by count bits.

           or(v1, v2 [, ...])
                  Return the bitwise OR of the values provided in the
                  argument list.  There must be at least two.

           rshift(val, count)
                  Return the value of val, shifted right by count bits.

           xor(v1, v2 [, ...])
                  Return the bitwise XOR of the values provided in the
                  argument list.  There must be at least two.

       Type Functions
           The following functions provide type related information about
           their arguments.

           isarray(x)
                  Return true if x is an array, false otherwise.

           typeof(x)
                  Return a string indicating the type of x.  The string will
                  be one of "array", "number", "number|bool", "regexp",
                  "string", "strnum", "unassigned", or "untyped".

       Internationalization Functions
           The following functions may be used from within your AWK program
           for translating strings at run-time.  For full details, see this
           link 
           ⟨https://www.gnu.org/software/gawk/manual/html_node/I18N-
           Functions⟩.

           bindtextdomain(directory [, domain])
                  Specify the directory where gawk looks for the .gmo files,
                  in case they will not or cannot be placed in the “standard”
                  locations.  It returns the directory where domain is
                  “bound.”

           dcgettext(string [, domain [, category]])
                  Return the translation of string in text domain domain for
                  locale category category.

           dcngettext(string1, string2, number [, domain [, category]])
                  Return the plural form used for number of the translation
                  of string1 and string2 in text domain domain for locale
                  category category.

       Boolean Valued Functions
           You can create special Boolean-typed values; see this link 
           ⟨https://www.gnu.org/software/gawk/manual/html_node/Boolean-
           Functions⟩ for how they work and why they exist.

           mkbool(expression)
                  Based on the boolean value of expression return either a
                  true value or a false value.  True values have numeric
                  value one.  False values have numeric value zero.

## [](#USER-DEFINED_FUNCTIONS)USER-DEFINED FUNCTIONS

           Functions in AWK are defined as follows:

                  function name(parameter list) { statements }

           Functions execute when they are called from within expressions in
           either patterns or actions.  Actual parameters supplied in the
           function call are used to instantiate the formal parameters
           declared in the function.  Arrays are passed by reference, other
           variables are passed by value.  Local variables are declared as
           extra parameters in the parameter list.  Functions may be called
           indirectly; see this link 
           ⟨https://www.gnu.org/software/gawk/manual/html_node/Indirect-Calls⟩
           for the details.

           The left parenthesis in a function call is required to immediately
           follow the function name, without any intervening whitespace.

           Use return expr to return a value from a function.  The return
           value is undefined if no value is provided, or if the function
           returns by “falling off” the end.

## [](#DYNAMICALLY_LOADING_NEW_FUNCTIONS)DYNAMICALLY LOADING NEW FUNCTIONS

           You can dynamically add new functions written in C or C++ to the
           running gawk interpreter with the @load statement.  The full
           details are beyond the scope of this manual page; see this link 
           ⟨https://www.gnu.org/software/gawk/manual/html_node/Dynamic-
           Extensions⟩.

## [](#SIGNALS)SIGNALS

           The gawk profiler accepts two signals.  SIGUSR1 causes it to dump
           a profile and function call stack to the profile file, which is
           either awkprof.out, or whatever file was named with the --profile
           option.  It then continues to run.  SIGHUP causes gawk to dump the
           profile and function call stack and then exit.

## [](#INTERNATIONALIZATION)INTERNATIONALIZATION

           String constants are sequences of characters enclosed in double
           quotes.  In non-English speaking environments, it is possible to
           mark strings in the AWK program as requiring translation to the
           local natural language.  Such strings are marked in the AWK
           program with a leading underscore (“_”).  See this link 
           ⟨https://www.gnu.org/software/gawk/manual/html_node/Internationalization⟩
           for the steps involved in producing and running a localizable AWK
           program.

## [](#GNU_EXTENSIONS)GNU EXTENSIONS

           Gawk has a too-large number of extensions to POSIX awk.  They are
           described in this link 
           ⟨https://www.gnu.org/software/gawk/manual/html_node/POSIX_002fGNU⟩.
           All the extensions can be disabled by invoking gawk with the
           --traditional or --posix options.

## [](#ENVIRONMENT_VARIABLES)ENVIRONMENT VARIABLES

           AWKPATH provides a list of directories that gawk searches when
           looking for files named via the -f, --file, -i and --include
           options, and the @include and @nsinclude directives.  If the
           initial search fails, the path is searched again after appending
           .awk to the filename.

           AWKLIBPATH provides a list of directories that gawk searches when
           looking for files named via the -l and --load options and the
           @load directive.

           GAWK_PERSIST_FILE, if present, specifies a file to use as the
           backing store for persistent memory.  See this link 
           ⟨https://www.gnu.org/software/gawk/manual/html_node/Persistent-
           Memory⟩.

           GAWK_READ_TIMEOUT specifies a timeout in milliseconds for reading
           input from a terminal, pipe or two-way communication including
           sockets.

           For connection to a remote host via socket, GAWK_SOCK_RETRIES
           controls the number of retries, and GAWK_MSEC_SLEEP the interval
           between retries.  The interval is in milliseconds.  On systems
           that do not support usleep(3), the value is rounded up to an
           integral number of seconds.

           If POSIXLY_CORRECT exists in the environment, gawk behaves exactly
           as if --posix had been specified on the command line.  With
           --lint, gawk issues a warning message to this effect.

## [](#EXIT_STATUS)EXIT STATUS

           If the exit statement is used with a value, then gawk exits with
           the numeric value given to it.  Otherwise, if there were no
           problems during execution, gawk exits with the value of the C
           constant EXIT_SUCCESS.  This is usually zero.

           If an error occurs, gawk exits with the value of the C constant
           EXIT_FAILURE.  This is usually one.  If gawk exits because of a
           fatal error, the exit status is 2.  On non-POSIX systems, this
           value may be mapped to EXIT_FAILURE.

## [](#VERSION_INFORMATION)VERSION INFORMATION

           This man page documents gawk, version 5.4.

## [](#AUTHORS)AUTHORS

           The original version of UNIX awk was designed and implemented by
           Alfred Aho, Peter Weinberger, and Brian Kernighan of Bell
           Laboratories.  Ozan Yigit is the current maintainer.  Brian
           Kernighan occasionally dabbles in its development.

           Paul Rubin and Jay Fenlason, of the Free Software Foundation,
           wrote gawk, to be compatible with the original version of awk
           distributed in Seventh Edition UNIX.  John Woods contributed a
           number of bug fixes.  David Trueman, with contributions from
           Arnold Robbins, made gawk compatible with the new version of UNIX
           awk.  Arnold Robbins is the current maintainer.

           See this link 
           ⟨https://www.gnu.org/software/gawk/manual/html_node/Contributors⟩
           for a full list of the contributors to gawk and its documentation.

           See the README file in the gawk distribution for up-to-date
           information about maintainers and which ports are currently
           supported.

## [](#BUG_REPORTS_AND_QUESTIONS)BUG REPORTS AND QUESTIONS

           If you find a bug in gawk, please use the gawkbug(1) program to
           report it.

           Full instructions for reporting a bug are provided in this link 
           ⟨https://www.gnu.org/software/gawk/manual/html_node/Bugs⟩.  Please
           carefully read and follow the instructions given there.  This will
           make bug reporting and resolution much easier for everyone
           involved.  Really.

           On the other hand, if you have a question as to how to accomplish
           a particular task using awk or gawk, send an email to help-
           gawk@gnu.org with your request for help.

## [](#BUGS)BUGS

           The -F option is not necessary given the command line variable
           assignment feature; it remains only for backwards compatibility.

           This manual page is too long; gawk has too many features.

## [](#SEE_ALSO)SEE ALSO

           egrep(1), sed(1), gawkbug(1), printf(3), and strftime(3).

           The AWK Programming Language, second edition, Alfred V. Aho, Brian
           W. Kernighan, Peter J. Weinberger, Addison-Wesley, 2023.  ISBN
           9-780138-269722.

           GAWK: Effective AWK Programming, Edition 5.4, shipped with the
           gawk source.  The current version of this document is available
           online at this link ⟨https://www.gnu.org/software/gawk/manual⟩.

           The GNU gettext documentation, available online at this link 
           ⟨https://www.gnu.org/software/gettext⟩.

## [](#EXAMPLES)EXAMPLES

           Print and sort the login names of all users:

                BEGIN     { FS = ":" }
                     { print $1 | "sort" }

           Count lines in a file:

                     { nlines++ }
                END  { print nlines }

           Precede each line by its number in the file:

                { print FNR, $0 }

           Concatenate and line number (a variation on a theme):

                { print NR, $0 }

           Run an external command for particular lines of data:

                tail -f access_log |
                awk '/myhome.html/ { system("nmap " $1 ">> logdir/myhome.html") }'

## [](#COPYING_PERMISSIONS)COPYING PERMISSIONS

           Copyright © 1989, 1991–1999, 2001–2005, 2007, 2009–2026, Free
           Software Foundation, Inc.

           Permission is granted to make and distribute verbatim copies of
           this manual page provided the copyright notice and this permission
           notice are preserved on all copies.

           Permission is granted to copy and distribute modified versions of
           this manual page under the conditions for verbatim copying,
           provided that the entire resulting derived work is distributed
           under the terms of a permission notice identical to this one.

           Permission is granted to copy and distribute translations of this
           manual page into another language, under the above conditions for
           modified versions, except that this permission notice may be
           stated in a translation approved by the Foundation.

## [](#COLOPHON)COLOPHON

           This page is part of the gawk (GNU awk) project.  Information
           about the project can be found at 
           ⟨http://www.gnu.org/software/gawk/⟩.  If you have a bug report for
           this manual page, see
           ⟨http://pkg-shadow.alioth.debian.org/getinvolved.php⟩.  This page
           was obtained from the project's upstream Git repository
           ⟨git://git.savannah.gnu.org/gawk.git⟩ on 2026-08-03.  (At that
           time, the date of the most recent commit that was found in the
           repository was 2026-08-01.)  If you discover any rendering
           problems in this HTML version of the page, or you believe there is
           a better or more up-to-date source for the page, or you have
           corrections or improvements to the information in this COLOPHON
           (which is not part of the original manual page), send a mail to
           man-pages@man7.org

    Free Software Foundation       June 25 2026                       GAWK(1)

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
