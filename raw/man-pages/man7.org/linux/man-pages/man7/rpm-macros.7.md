---
{"title": "rpm-macros(7) — Linux manual page", "url": "https://man7.org/linux/man-pages/man7/rpm-macros.7.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# rpm-macros(7) --- Linux manual page

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [EXPANSION](#EXPANSION) \| [PARAMETRIC MACROS](#PARAMETRIC_MACROS) \| [BUILT-IN MACROS](#BUILT-IN_MACROS) \| [EXAMPLES](#EXAMPLES) \| [DEBUGGING](#DEBUGGING) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                                                                          |                                   |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    RPM-MACROS(7)        Miscellaneous Information Manual       RPM-MACROS(7)

## [](#NAME)NAME

           rpm-macros - RPM macro processor

## [](#SYNOPSIS)SYNOPSIS

       Defining
           %NAME[<MODIFIERS>] BODY

           %NAME([OPTIONS])[<MODIFIERS>] BODY

       Expanding
           %NAME

           %NAME [OPTIONS] [ARGUMENTS]

           %{NAME}

           %{NAME [OPTIONS] ARGUMENTS}

           %{NAME:ARGUMENT}

           %{?NAME}

           %{?NAME:VALUE-IF-DEFINED}

           %{!?NAME:VALUE-IF-NOT-DEFINED}

           %(SHELL-COMMAND)

           %[EXPRESSION]

           %[EXPRESSION ? VALUE-IF-TRUE : VALUE-IF-FALSE]

           %{lua:LUA-CODE}

## [](#DESCRIPTION)DESCRIPTION

           RPM has a powerful built-in macro processor. The primary uses of
           macros are configuration and other utility functions for RPM
           itself, and as a packaging aid in spec files.

           In addition to simple text substitution, the macro processor
           supports the following facilities:
           •   function-like PARAMETRIC MACROS with options and arguments
               processing and locally scoped automatic and user-defined
               macros
           •   Shell expansion
           •   Expression expansion
           •   Lua expansion for embedded Lua processing
           •   various BUILT-IN MACROS for string processing and OS
               interaction

           The syntax for defining simple macros is:

               NAME BODY

           All whitespace surrounding BODY is removed.  NAME may be composed
           of alphanumeric characters and the underscore (_), and must be at
           least two characters in length. By default, the body is
           (re-)expanded on each macro invocation. Macro names and options
           are case-sensitive.

           Macro behavior can be altered by supplying modifiers: (Added:
           6.1.0)

               NAME<MODIFIERS> BODY

           Supported modifiers are:
           •   l: Literal expansion. % is not processed when expanding.
           •   o: One-shot expansion. The macro is expanded on first use and
               the literal result is pushed on top of the original macro.

           Literal macros can simplify dealing with content that may contain
           percent signs (%) which otherwise would need to be escaped.

           One-shot macros are useful for caching expansion results, for
           example to guard a result against underlying changes, or to
           perform an expensive shell invocation just once. The one-shot
           expansion can be re-armed by undefining the macro once.

           See PARAMETRIC MACROS for the more advanced macro variant with
           options and arguments processing.

           Macros can be defined via rpm-macrofile(5) files, and fully
           managed with macro primitives %define, %global and %undefine, RPM
           command-line described in rpm-common(8) and the API (C, Python,
           Lua).

           Except for those defined inside parametric macros, macros are
           always global in scope.

           RPM macros are stacked, ie. when redefining an already existing
           macro, the new definition is pushed on top of the previous one,
           shadowing it. Conversely, undefining a macro only pops the topmost
           definition, reactivating the previous macro definition if there is
           one.

           Note that this manual only describes the macro processor engine
           itself. On a normal RPM based system, there are a vast number of
           other macros defined through rpm-macrofile(5) files that will not
           be covered here.

## [](#EXPANSION)EXPANSION

           To expand a macro, place % in front of it. Several forms are
           supported:

           %NAME
               Expand the macro NAME.

           %{NAME}
               Expand the macro NAME, allowing placement adjacent to other
               text (similar to ${ENV} in shell).

           %NAME [OPTIONS] [ARGUMENTS]
               Expand the parametric/built-in macro NAME, using options and
               arguments parsed up to the string end or next newline.

               -- can be used to separate options from arguments.

           %{NAME [OPTIONS] [ARGUMENTS]}
               Expand the parametric/built-in macro NAME, using options and
               arguments parsed up to the closing }. Allows usage adjacent to
               other text.

           %{NAME:ARGUMENT}
               Expand the parametric/built-in macro NAME, using the string
               after : as the sole argument. Allows usage adjacent to other
               text.

           Note: The syntaxes for calling parametric and built-in macros are
           generally interchangeable now, but prior to 4.18, the
           %{NAME:ARGUMENT} syntax was exclusive to built-in macros.

           Macro expansion can be escaped by placing a second % in front of
           the macro, for example %%{name} would be expanded to %{name}.

           Attempting to expand an undefined macro expands to the literal
           invocation, e.g. %_undefined expands to %_undefined. If this is
           not desired, use conditionals.

           Macro expansions can recurse up to 64 levels.

       Shell expansion
           Shell expansion can be performed using %(shell command).
           shell_command is expanded before executing it with /bin/sh, whose
           output becomes the expansion of the macro. The trailing newline is
           deleted.

           Example:
               %(echo aa-bb-cc | tr '-' '.')

       Conditional expansion
           The macro processor supports testing whether a macro is defined or
           not.

           %{?NAME:VALUE}
               Expands to the expansion of VALUE if NAME is defined,
               otherwise to an empty string.

           %{!?NAME:VALUE}
               Expands to the expansion of VALUE if NAME is not defined,
               otherwise it expands to an empty string.

           %{?NAME}
               Shorthand for %{?NAME:%{NAME}}.

           For more complex tests, use Expression expansion or Lua expansion.
           Note that %if, %ifarch and the like are not macros, they are spec
           directives and only usable in that context.

           Note that in RPM >= 4.17, conditionals on built-in macros simply
           test for existence of that built-in, just like with any other
           macros. In older versions, the behavior of conditionals on built-
           ins is undefined.

       Expression expansion
           Expression expansion can be performed using %[EXPRESSION].  An
           expression consists of terms that can be combined using operators.

           RPM supports three kinds of terms:
           •   numbers made up from digits
           •   strings enclosed in double quotes (e.g "somestring")
           •   versions enclosed in double quotes preceded by v (e.g
               v"3:1.2-1")

           RPM will expand macros when evaluating terms.

           You can use the standard operators to combine terms:
           •   logical operators &&, ||, !
           •   relational operators !=, ==, <, >, <=, >=
           •   arithmetic operators +, -, /, *,
           •   the ternary operator ? :
           •   parentheses

           For example, %[ 3 + 4 * (1 + %two) ] will expand to 15 if %two
           expands to 2. Version terms are compared using RPM version
           ([epoch:]version[-release]) comparison algorithm, rather than
           regular string comparison.

           Note that the %[EXPRESSION] expansion is different to the
           %{expr:EXPRESSION} macro.  With the latter, the macros in the
           expression are expanded first and then the expression is evaluated
           (without re-expanding the terms).  Thus

               rpm --define 'foo 1 + 2' --eval '%{expr:%foo}'

           will print 3.  Using %[%foo] instead will result in the error that
           "1 + 2" is not a number.

           Doing the macro expansion when evaluating the terms has two
           advantages.  First, it allows RPM to do correct short-circuit
           processing when evaluating logical operators.  Second, the
           expansion result does not influence the expression parsing, e.g.
           %["%file"] will even work if the %file macro expands to a string
           that contains a double quote.

           Added: 4.16.0

       Lua expansion
           The most powerful of the macro expansion methods is using RPM's
           embedded Lua interpreter:

           %{lua:LUA-CODE}
               Execute LUA-CODE using RPM's embedded Lua interpreter,
               expanding to the code's print()'ed output.

           See rpm-lua(7) for the details.

## [](#PARAMETRIC_MACROS)PARAMETRIC MACROS

           Parametric macros are a powerful mechanism that allows building
           function-like utility macros with option processing and accepting
           a variable number of arguments, much like common shell tools.

           The syntax for defining parametric macros is:

               NAME([OPTIONS])[<MODIFIERS>] BODY

           If present, the OPTIONS (i.e. the string between parentheses) are
           passed exactly as is to getopt(3) for argc/argv processing at the
           beginning of a macro invocation. Only short options are supported.

           - as the sole OPTIONS field disables RPM's option processing. This
           allows macros to fully decide how to handle their input, e.g. if
           the arguments of the macro only/mostly consist of items starting
           with -, the default processing only gets in the way.

           A modifier field may be present, but currently there are no
           modifiers compatible with parametric macros.

       Automatic macros
           While a parameterized macro is being expanded, the following
           shell-like automatic macros are available:

           ┌─────────────┬──────────────────────────────────────────────────┐
           │ Macro       │ Description                                      │
           ├─────────────┼──────────────────────────────────────────────────┤
           │ %0          │ the name of the macro being invoked              │
           ├─────────────┼──────────────────────────────────────────────────┤
           │ %*          │ all arguments (unlike shell, not including any   │
           │             │ processed flags)                                 │
           ├─────────────┼──────────────────────────────────────────────────┤
           │ %**         │ all arguments (including any processed flags)    │
           ├─────────────┼──────────────────────────────────────────────────┤
           │ %#          │ the number of arguments                          │
           ├─────────────┼──────────────────────────────────────────────────┤
           │ %{-f}       │ if present at invocation, the last occurrence of │
           │             │ flag f (flag and argument)                       │
           ├─────────────┼──────────────────────────────────────────────────┤
           │ %{-f*}      │ if present at invocation, the argument to the    │
           │             │ last occurrence of flag f                        │
           ├─────────────┼──────────────────────────────────────────────────┤
           │ %1, %2, ... │ the arguments themselves (after getopt(3)        │
           │             │ processing)                                      │
           └─────────────┴──────────────────────────────────────────────────┘

           If the built-in option processing was disabled with - as the
           OPTIONS field, only the following automatic macros are available:

           ┌─────────────┬──────────────────────────────────────────────────┐
           │ Macro       │ Description                                      │
           ├─────────────┼──────────────────────────────────────────────────┤
           │ %0          │ the name of the macro being invoked              │
           ├─────────────┼──────────────────────────────────────────────────┤
           │ %*, %**     │ all arguments                                    │
           ├─────────────┼──────────────────────────────────────────────────┤
           │ %#          │  the number of arguments                         │
           ├─────────────┼──────────────────────────────────────────────────┤
           │ %1, %2, ... │ the arguments themselves                         │
           └─────────────┴──────────────────────────────────────────────────┘

           Automatic macros are automatically defined and undefined on
           parametric macro entry and exit.

       Accessing options
           Within the body of a parametric macro, there are several
           constructs that permit testing for the presence of optional
           parameters. The simplest construct is %{-f} which expands
           (literally) to -f if -f was mentioned when the macro was invoked.
           There are also provisions for including text if a flag was present
           using %{-f:X}. This macro expands to (the expansion of) X if the
           flag was present. The negative form, %{!-f:Y}, expanding to (the
           expansion of) Y if -f was not present, is also supported.

       Scope and visibility
           In general, macros have a global scope, regardless of where and
           how they were defined. However, macros defined inside parametric
           macros have non-global scope as follows:
           •   automatic macros have local scope, ie. are only visible on the
               call-level of the macro itself
           •   user-defined local macros have nested scope, ie. are visible
               on the call-level of the macro itself and deeper

           That is, a parametric macro cannot see the options or arguments of
           another one, but a user-defined local macro in a calling macro can
           be accessed in the callee(s).

           To define a global macro inside a parametric macro, you must use
           %global instead of %define. Also note that because such a macro
           may be referring to other macros only visible in the current
           scope, %global expands the macro body once at the time of
           definition, unless it's a literal macro. Note that the body of a
           one-shot macro defined via %global is actually expanded twice:
           once at the time of definition, and the result of that expansion
           is expanded again on first use.

       Calling convention
           When a parametric macro is expanded, the following calling
           convention is used:
           1.  any arguments to the macro are expanded on the call-level of
               the callee
           2.  any options to the macro are processed
           3.  automatic macros are set up for the options and the arguments
           4.  the macro body is recursively expanded
           5.  all macros defined on this call-level are discarded

## [](#BUILT-IN_MACROS)BUILT-IN MACROS

           RPM supports the following built-in macros for various operations.
           Built-in macros cannot be undefined or overridden.

           Note: The %{name:arg} style is used here as it's the most
           backwards compatible and does not require quoting for whitespace,
           but it can generally be replaced with the other expansion forms
           too. Built-ins taking multiple arguments must use other styles, as
           indicated below.

       Macro manipulation
           The macro primitives are used for macro manipulation in spec files
           and other macros. Note that all these operate on the macro name
           without the preceding %-character.

           %define [DEFOPTS] NAME[([OPTIONS])] BODY
               This is the primary way to define macros. By default, a
               %define is declarative: no macro expansion takes place and it
               has no side-effects. Macros are placed in the current scope by
               default: local inside parametric macros, otherwise global.

               The %define macro accepts the following options (DEFOPTS):

               -e
                   Expand body at the time of definition, making the result
                   the actual macro body.
               -g
                   Place macro in the global context. Has no effect outside
                   parametric macros.

               %define -eg is identical to using %global.

               Example:
                   %define mypath /usr/bin/mine

           %global NAME[([OPTIONS])] BODY
               The %global primitive is identical in syntax to %define, but
               has two critically important behavioral differences: as it's
               name suggests, a macro defined with %global always has a
               global scope regardless of where it's used.

               The second difference is that the BODY is expanded once at the
               time of definition and the expansion becomes the actual macro
               body. Thus, arbitrary code execution and side-effects may
               occur when %global is used, depending on the contents and the
               other macros used in BODY. The latter can be handy for
               avoiding redundant, possibly expensive macro expansions if the
               value does not change, but be aware of the side-effects.

               Note that while %global technically accepts an OPTIONS field,
               it is ill-suited for defining parametric macros because of the
               BODY expansion behavior.

               Example:
                   %global snapver 0-0.48.20240616git

           %undefine NAME
               Note that %undefine only pops a macro definition from the
               stack, so using it does not guarantee that NAME is undefined
               after calling %undefine on it. Automatic macros and built-in
               macros cannot be undefined.

               Example:
                   %undefine mypath

           %{load:FILE}
               Load an rpm-macrofile(5) file. (Added: 4.12.0)

               Example:
                   %{load:/some/dir/macros.foo}

       Macro expansion
           %{expand:BODY}
               Expand BODY as if it were a macro body. Useful for increased
               indirection, such as to expand a macro name constructed from
               two or more macros.

               Example:
                   %{expand:%{foo_prefix}%{foo_suffix}}

           %{expr:EXPRESSION}
               Expand EXPRESSION. See Expression expansion. (Added: 4.15.0)

               Example:
                   %{expr:5*1024}

           %{lua:LUA-CODE}
               Expand to output of LUA-CODE using the embedded Lua
               interpreter. See Lua expansion.

               Example:
                   %{lua:for i=65,90 do print(string.char(i)) end}

           %{macrobody:NAME}
               Expand to the literal body of the macro NAME. (Added: 4.16.0)

               Example:
                   %{macrobody:_libdir}

       String operations
           %dnl
               Discard to next line (without expanding anything). %dnl is the
               recommended way to comment out things in spec files because it
               works everywhere and disables macro processing for that line.
               (Added: 4.15.0)

               Example:
                   %dnl This is a comment on %{mymacro} behavior

           %{gsub STRING, PATTERN, REPL [,N]}
               Replace all (or N first if given) occurrences of PATTERN in
               STRING by REPL.

               Added: 4.19.0

               Example:
                   %{gsub aabbaacc aa dd 1}

           %{len:STRING}
               Expand to length of STRING. (Added: 4.19.0)

               Example:
                   %{len:9bf7da058a7c582878310e75be3d56a5a8b67f95}

           %{lower:STRING}
               Expand to lowercase STRING. (Added: 4.19.0)

               Example:
                   %{lower:CamelCase}'

           %{quote:STRING}
               Quote arguments for passing empty strings and strings with
               embedded whitespace as parametric macro arguments. (Added:
               4.14.0)

               Example:
                   %myzip -x %{quote:empty spaces.zip}

           %{rep STRING, N [,SEP]}
               Expand to a string that is the concatenation of N copies of
               STRING, separated by SEP (if specified).

               Added: 4.19.0

               Example:
                   %{rep a 5}

           %{reverse:STRING}
               Reverse a string. (Added: 4.19.0)

               Example:
                   %{reverse:tac}

           %{shescape:STRING}
               Single quote STRING with escapes for use in shell. (Added:
               4.18.0)

               Example:
                   %{shescape:foo's}

           %{shrink:STRING}
               Trim leading and trailing whitespace from STRING, reduce
               intermediate whitespace to a single space. (Added: 4.14.0)

               Example:
                   %{shrink:aa  bb   ccc   }

           %{span:STRING}
               As-is string, handy for wrapping multiline macros. (Added:
               6.0.0)

               Example:
                   %{span:
                        %one thing
                        %another thing
                   }

           %{sub STRING, I, [,J]}
               Expand to substring of STRING that starts at I and continues
               until J. I and J can be negative to index from the string's
               end. If J is absent, then it is assumed to be equal to -1 (ie.
               string end).

               Added: 4.19.0

               Example:
                   *%{sub myfile.zip 3 6}*

           %{upper:STRING}
               Expand to uppercase STRING. (Added: 4.19.0)

               Example:
                   %{upper:CamelCase}'

       File and path operations
           %{basename:PATH}
               basename(1) macro analogue.

               Example:
                   %{basename:/some/dir/file.suf}

           %{dirname:PATH}
               dirname(1) macro analogue.

               Example:
                   %{dirname:/some/dir/file.suf}

           %{exists:PATH}
               Test file existence, expands to 1/0. (Added: 4.18.0)

               Example:
                   %{exists:%{builddir}/myflag.txt}

           %{suffix:PATH}
               Expand to suffix part of a filename.

               Example:
                   %{suffix:myfile.zip}

           %{url2path:URL}
               Convert url to a local path.

               Example:
                   %{url2path:http://rpm.org/not/there}

           %{uncompress:PATH}
               Expand to a command for outputting argument PATH to standard
               output, uncompressing as needed.

               Note: for unpackaging sources in rpm-spec(5) files, consider
               calling rpmuncompress(1) directly instead.

               Example:
                   %{uncompress /my/source.tar.gz}

           %{xdg:KIND}
               Expand to XDG base directory paths. Supported values for KIND
               are:
               •   cache: user-specific non-essential (cached) data
               •   config: user-specific configuration files
               •   data: user-specific data files
               •   state: user-specific state data

               Added: 6.0.0

               Example:
                   %{xdg config}

       Environment info
           %getncpus
               Expand to the number of available CPUs. (Added: 4.15.0)

           %{getncpus:KIND}
               Expand to the number of available CPUs, supported valued for
               KIND are
               •   total: total number of available CPUs (same as %getncpus)
               •   proc: number of available CPUs for processes
               •   thread: number of available CPUs for threads

               proc and thread account for available memory, including
               address space limitations for threads.

               Added: 4.19.0.

               Example:
                   %{getncpus proc}

           %getconfdir
               Expand to RPM "home" directory (typically /usr/lib/rpm).

           %{getenv:NAME}
               getenv(3) macro analogue.

               Example:
                   %{getenv:HOME}

           %rpmversion
               Expand to running RPM version.

       Output
           %{echo:STRING}
               Print STRING to process standard output.

               Example:
                   %{echo:Building with foo}

           %{warn:STRING}
               Print STRING prefixed with "warning: " to process standard
               error.

               Example:
                   %{warning:Foo is deprecated}

           %{error:STRING}
               Print STRING prefixed with "error: " to process standard error
               and flag an error in the macro processor.

               Example:
                   %{error:Invalid argument}

           %verbose
               Expand to 1/0 whether RPM is in verbose mode or not. (Added:
               4.17.1)

           %{verbose:STRING}
               Expand to STRING if RPM is in verbose mode, the empty string
               if not. (Added: 4.17.1)

               Example:
                   %{verbose:-x}

       Diagnostics
           %trace
               Toggle print of debugging information before/after expansion.

           %dump
               Print the active (i.e. non-covered) macro table.

           %__file_name
               Expand to current filename (if parsing a file). (Added: 4.15)

           %__file_lineno
               Expand to current line number in current file (if parsing a
               file). (Added: 4.15)

## [](#EXAMPLES)EXAMPLES

       Example 1. Define a simple macro
           Define macro mylib to a path relative to %{_libdir} macro in a
           spec:

               %define mylib %{_libdir}/mine

       Example 2. Define a parametric macro
           Define parametric macro myhelper which executes the program
           specified by %myprog with it's first argument and always passing
           the option --some-opt to it, and additionally the --xtra option if
           it received the -x option itself:

               %define myhelper(x) %{myprog} --some-opt %{?-x:--xtra} %{1}

       Example 3. Define a macro utilizing shell expansion
           Define macro %today that expands to the current date in YYMMDD
           format by calling the date(1) shell utility. Note the 2nd % needed
           to escape the arguments to date(1):

               %define today %(date +%%y%%m%%d)

       Example 4. Define a macro conditionally
           Define macro mypath if it wasn't previously defined:

               %{!?mypath: %define mypath /some/where}

       Example 5. Conditional expansion
           Expands to 1 if use_foo is defined and 0 otherwise:

               %{?use_foo:1}%{!?use_foo:0}

       Example 6. Expressions
           Calculate 5 * 1024:

               %[5 * 1024]

           Expand to literal true or false depending on a condition:

               %[1 < 2 ? "true" : "false"]

           Compare versions, expanding to 1 or 0 on true/false:

               %[ v"3.1.0-1" < v"1.0~alpha-2" ? 1 : 0]

           Expands to 1 if %aa expands to 5, otherwise expands to 2:

               %[ "%{aa}" == "5" ? 1 : 2]

       Example 7. Literal macros
           Define a macro whose body contains literal % characters, possibly
           overlapping with other macros:

               %mymacro 1.2.3
               %aa %mymacro
               %bb<l> %mymacro

           %aa expands to 1.2.3, whereas %bb expands to %mymacro.

               %cc some%%thing
               %dd<l> some%%thing

           %cc expands to some%thing, whereas %dd expands to some%%thing.

       Example 8. One-shot macros
           Define a one-shot _python_platlib macro to output Python platform
           library path:

               %_python_platlib<o> %(python -c "import sysconfig; print(sysconfig.get_path('platlib'))")

           The Python interpreter will only be invoked on the first use of
           this macro, the result of that expansion is pushed as a literal
           macro on top of the original.

## [](#DEBUGGING)DEBUGGING

           Some useful tools for working with and troubleshooting macros:

           rpm --eval "VALUE"
               Expand VALUE on the command line.

           rpm --define "aa 11" --eval "%aa"
               Define and evaluate a macro on the command line.

           rpm --eval "%global unamer %(uname -r)" --eval
           "%{macrobody:unamer}"
               Define and examine macro body using %global on the command
               line.

           rpm --eval "%define unamer %(uname -r)" --eval
           "%{macrobody:unamer}"
               Define and examine macro body using %define on the command
               line.

           rpmlua
               Run an interactive shell in the embedded Lua environment.

           rpmlua -e 'print(macros.defined("_libdir"))'
               Using the embedded Lua interpreter in standalone form, print
               print 1/0 whether macro _libdir is defined or not.

           rpmspec --shell
               Run an interactive shell in the macro environment.

           rpmspec --shell telnet.spec
               Run an interactive shell in the macro environment after
               parsing telnet.spec.

## [](#SEE_ALSO)SEE ALSO

           rpm(8) rpm-common(8) rpm-macrofile(5) rpm-config(5) rpm-lua(7)
           rpmspec(1) rpmlua(1)

## [](#COLOPHON)COLOPHON

           This page is part of the rpm (RPM Package Manager) project.
           Information about the project can be found at 
           ⟨https://github.com/rpm-software-management/rpm⟩.  It is not known
           how to report bugs for this man page; if you know, please send a
           mail to man-pages@man7.org.  This page was obtained from the
           project's upstream Git repository
           ⟨https://github.com/rpm-software-management/rpm.git⟩ on
           2026-08-04.  (At that time, the date of the most recent commit
           that was found in the repository was 2026-07-27.)  If you discover
           any rendering problems in this HTML version of the page, or you
           believe there is a better or more up-to-date source for the page,
           or you have corrections or improvements to the information in this
           COLOPHON (which is not part of the original manual page), send a
           mail to man-pages@man7.org

    RPM 6.1.90                      2026-08-03                  RPM-MACROS(7)

------------------------------------------------------------------------

Pages that refer to this page: [rpmbuild(1)](../man1/rpmbuild.1.html),  [rpmspec(1)](../man1/rpmspec.1.html),  [rpmbuild-config(5)](../man5/rpmbuild-config.5.html),  [rpm-config(5)](../man5/rpm-config.5.html),  [rpm-macrofile(5)](../man5/rpm-macrofile.5.html),  [rpm-rpmrc(5)](../man5/rpm-rpmrc.5.html),  [rpm-spec(5)](../man5/rpm-spec.5.html),  [rpm-dependency-generators(7)](../man7/rpm-dependency-generators.7.html),  [rpm-design(7)](../man7/rpm-design.7.html),  [rpm-lua(7)](../man7/rpm-lua.7.html),  [rpm-scriptlets(7)](../man7/rpm-scriptlets.7.html),  [rpm-spec-macros(7)](../man7/rpm-spec-macros.7.html),  [rpm-common(8)](../man8/rpm-common.8.html)

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
