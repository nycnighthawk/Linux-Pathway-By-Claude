---
{"title": "lttng-event-rule(7) — Linux manual page", "url": "https://man7.org/linux/man-pages/man7/lttng-event-rule.7.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# lttng-event-rule(7) --- Linux manual page

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [RESOURCES](#RESOURCES) \| [COPYRIGHT](#COPYRIGHT) \| [THANKS](#THANKS) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                           |                                   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    LTTNG-EVENT-RULE(7)            LTTng Manual           LTTNG-EVENT-RULE(7)

## [](#NAME)NAME

           lttng-event-rule - Common LTTng event rule specification

## [](#SYNOPSIS)SYNOPSIS

           Specify an event rule to match Linux kernel tracepoint or system
           call events:

           --type=(kernel:tracepoint | kernel:syscall[:entry|:exit|:entry+exit])]
           [--name=NAME] [--filter=EXPR]

           Specify an event rule to match Linux kernel kprobe or user space
           probe events:

           --type=(kernel:kprobe | kernel:uprobe) --location=LOC
           [--event-name=EVENTNAME]

           Specify an event rule to match user space tracepoint events:

           --type=user:tracepoint [--name=NAME] [--exclude-name=XNAME]...
           [--log-level=(LOGLEVEL | LOGLEVEL.. | ..)] [--filter=EXPR]

           Specify an event rule to match Java/Python logging events:

           --type=(jul | log4j | log4j2 | python):logging [--name=NAME]
           [--log-level=(LOGLEVEL | LOGLEVEL.. | ..)] [--filter=EXPR]

## [](#DESCRIPTION)DESCRIPTION

           This manual page shows how to specify an LTTng event rule on the
           command line.

           As of LTTng 2.15.1, the command-line options documented here only
           apply to the event-rule-matches trigger condition specifier (see
           lttng-add-trigger(1)).

           See lttng-concepts(7) to learn more about instrumentation points,
           events, and event rules.

           Note

               This manual page only describes the common event rule options.
               The lttng(1) commands which require an event rule
               specification may accept or require other options and
               arguments, depending on the context.

               For example, the lttng-add-trigger(1) command also accepts
               --capture options with the event-rule-matches trigger
               condition.

       Overview of event rule condtions
           For LTTng to emit an event E, E must satisfy all the conditions of
           an event rule, that is:

           •   The instrumentation point from which LTTng creates E has a
               specific type.

               See the “Instrumentation point type condition” section below.

           •   A pattern matches the name of E while another pattern doesn’t.

               See the “Event name condition” section below.

           •   The log level of the instrumentation point from which LTTng
               creates E is at least as severe as some value, or is exactly
               some value.

               See the “Instrumentation point log level condition” section
               below.

           •   The fields of the payload of E and the current context fields
               satisfy a filter expression.

               See the “Event payload and context filter condition” section
               below.

           The dedicated command-line options of most conditions are
           optional: if you don’t specify the option, the associated
           condition is always satisfied.

       Instrumentation point type condition
           An event E satisfies the instrumentation point type condition of
           an event rule if the instrumentation point from which LTTng
           creates E is, depending on the argument of the --type option:

           kernel:tracepoint
               An LTTng kernel tracepoint, that is, a statically defined
               point in the source code of the kernel image or of a kernel
               module with LTTng kernel tracer macros.

               List the available Linux kernel tracepoints with lttng list
               --kernel. See lttng-list(1) to learn more.

           kernel:syscall:entry, kernel:syscall:exit,
           kernel:syscall:entry+exit
               The entry, exit, or entry and exit of a Linux kernel system
               call.

               List the available Linux kernel system call instrumentation
               points with lttng list --kernel --syscall. See lttng-list(1)
               to learn more.

           kernel:kprobe
               A Linux kprobe, that is, a single probe dynamically placed in
               the compiled kernel code.

               You must specify the kprobe location with the --location
               option.

               The payload of a Linux kprobe event is empty.

           kernel:uprobe
               A Linux user space probe, that is, a single probe dynamically
               placed at the entry of a compiled user space
               application/library function through the kernel.

               LTTng 2.15.1 supports the ELF and SystemTap User-level
               Statically Defined Tracing (USDT; a DTrace-style marker)
               probing methods. LTTng only supports USDT probes which are NOT
               reference-counted.

               You must specify the user space probe location with the
               --location option.

               The payload of a Linux user space probe event is empty.

           user:tracepoint
               An LTTng user space tracepoint, that is, a statically defined
               point in the source code of a C/C++ application/library with
               LTTng user space tracer macros.

               List the available user space tracepoints with lttng list
               --userspace. See lttng-list(1) to learn more.

           jul:logging
               A java.util.logging logging statement.

               List the available java.util.logging loggers with lttng list
               --jul. See lttng-list(1) to learn more.

           log4j:logging
               An Apache log4j 1.x logging statement.

               List the available Apache log4j 1.x loggers with lttng list
               --log4j. See lttng-list(1) to learn more.

           log4j2:logging
               An Apache Log4j 2 logging statement.

               List the available Apache Log4j 2 loggers with lttng list
               --log4j2. See lttng-list(1) to learn more.

           python:logging
               A Python logging statement.

               List the available Python loggers with lttng list --python.
               See lttng-list(1) to learn more.

       Event name condition
           An event E satisfies the event name condition of an event rule ER
           if the two following statements are true:

           •   You don’t specify the --name=NAME option or, depending on the
               instrumentation type condition (see the “Instrumentation point
               type condition” section above) of ER, NAME matches:

               kernel:tracepoint, user:tracepoint
                   The full name of the tracepoint from which LTTng
                   creates E.

                   Note that the full name of a user space tracepoint is
                   PROVIDER:NAME, where PROVIDER is the tracepoint provider
                   name and NAME is the tracepoint name.

               jul:logging, log4j:logging, log4j2:logging, python:logging
                   The name of the Java or Python logger from which LTTng
                   creates E.

               kernel:syscall:entry, kernel:syscall:exit,
               kernel:syscall:entry+exit
                   The name of the system call, without any sys_ prefix, from
                   which LTTng creates E.

           •   You don’t specify any --exclude-name=XNAME option or none of
               the XNAME arguments matches the full name of the user space
               tracepoint from which LTTng creates E.

               The --exclude-name option is only available with the
               --type=user:tracepoint option.

           This condition is only meaningful for the LTTng tracepoint,
           logging statement, and Linux system call instrumentation point
           types: it’s always satisfied for the other types.

           In all cases, NAME and XNAME are globbing patterns: the *
           character means “match anything”. To match a literal * character,
           use \*.

           Important

               Make sure to single-quote NAME and XNAME when they contain the
               * character and when you run an lttng(1) command from a shell.

           As of LTTng 2.15.1, not specifying the --name option is equivalent
           to specifying --name='*´, but this default may change in the
           future.

       Instrumentation point log level condition
           An event E satisfies the instrumentation point log level condition
           of an event rule if either:

           •   You specify the --log-level=..  option or you don’t specify
               the --log-level option.

               Defaulting to --log-level=..  when you don’t specify the
               --log-level option is specific to LTTng 2.15.1 and may change
               in the future.

           •   The log level of the LTTng user space tracepoint or logging
               statement from which LTTng creates E is:

               With the --log-level=LOGLEVEL.. option
                   At least as severe as LOGLEVEL.

               With the --log-level=LOGLEVEL option
                   Exactly LOGLEVEL.

           As of LTTng 2.15.1, the ..LOGLEVEL and LOGLEVEL..LOGLEVEL formats
           are NOT supported.

           This condition is only meaningful for the LTTng user space
           tracepoint and logging statement instrumentation point types: it’s
           always satisfied for other types.

           The available values of LOGLEVEL are, depending on the argument of
           the --type option, from the most to the least severe:

           user:tracepoint

               •   EMERG (0)

               •   ALERT (1)

               •   CRIT (2)

               •   ERR (3)

               •   WARNING (4)

               •   NOTICE (5)

               •   INFO (6)

               •   DEBUG_SYSTEM (7)

               •   DEBUG_PROGRAM (8)

               •   DEBUG_PROCESS (9)

               •   DEBUG_MODULE (10)

               •   DEBUG_UNIT (11)

               •   DEBUG_FUNCTION (12)

               •   DEBUG_LINE (13)

               •   DEBUG (14)

           jul:logging

               •   OFF (INT32_MAX)

               •   SEVERE (1000)

               •   WARNING (900)

               •   INFO (800)

               •   CONFIG (700)

               •   FINE (500)

               •   FINER (400)

               •   FINEST (300)

               •   ALL (INT32_MIN)

           log4j:logging

               •   OFF (INT32_MAX)

               •   FATAL (50000)

               •   ERROR (40000)

               •   WARN (30000)

               •   INFO (20000)

               •   DEBUG (10000)

               •   TRACE (5000)

               •   ALL (INT32_MIN)

           log4j2:logging

               •   OFF (0)

               •   FATAL (100)

               •   ERROR (200)

               •   WARN (300)

               •   INFO (400)

               •   DEBUG (500)

               •   TRACE (600)

               •   ALL (INT32_MAX)

           python:logging

               •   CRITICAL (50)

               •   ERROR (40)

               •   WARNING (30)

               •   INFO (20)

               •   DEBUG (10)

               •   NOTSET (0)

       Event payload and context filter condition
           An event E satisfies the event payload and context filter
           condition of an event rule if the --filter=EXPR option is missing
           or if EXPR is true.

           This condition is only meaningful for the LTTng tracepoint and
           Linux system call instrumentation point types: it’s always
           satisfied for other types.

           EXPR can contain references to the payload fields of E and to the
           current context fields.

           Important

               Make sure to single-quote EXPR when you run an lttng(1)
               command from a shell, as filter expressions typically include
               characters having a special meaning for most shells.

           The expected syntax of EXPR is similar to the syntax of a
           C language conditional expression (an expression which an if
           statement can evaluate), but there are a few differences:

           •   A NAME expression identifies an event payload field named NAME
               (a C identifier).

               Use the C language dot and square bracket notations to access
               nested structure and array/sequence fields. You can only use a
               constant, positive integer number within square brackets. If
               the index is out of bounds, EXPR is false.

               The value of an enumeration field is an integer.

               When a field expression doesn’t exist, EXPR is false.

               Examples: my_field, target_cpu, seq[7],
               msg.user[1].data[2][17].

           •   A $ctx.TYPE expression identifies the statically-known context
               field having the type TYPE (a C identifier).

               List the available statically-known context field names with
               the lttng-add-context(1) command. As of LTTng 2.15.1, context
               field names starting with perf: aren’t supported.

               When a field expression doesn’t exist, EXPR is false.

               Examples: $ctx.prio, $ctx.gid, $ctx.preemptible.

           •   A $app.PROVIDER:TYPE expression identifies the
               application-specific context field having the type TYPE (a
               C identifier) from the provider PROVIDER (a C identifier).

               When a field expression doesn’t exist, EXPR is false.

               Example: $app.server:cur_user.

           •   Compare strings, either string fields or string literals
               (double-quoted), with the == and != operators.

               When comparing to a string literal, the * character means
               “match anything”. To match a literal * character, use \*.

               Examples: my_field == "user34", my_field == my_other_field,
               my_field == "192.168.*".

           •   The precedence table of the operators which are supported in
               EXPR is as follows. In this table, the highest precedence
               is 1:
               ┌────────────┬──────────┬─────────────────┬───────────────┐
               │ Precedence │ Operator │ Description     │ Associativity │
               ├────────────┼──────────┼─────────────────┼───────────────┤
               │ 1          │ -        │ Unary minus     │ Right-to-left │
               ├────────────┼──────────┼─────────────────┼───────────────┤
               │ 1          │ +        │ Unary plus      │ Right-to-left │
               ├────────────┼──────────┼─────────────────┼───────────────┤
               │ 1          │ !        │ Logical NOT     │ Right-to-left │
               ├────────────┼──────────┼─────────────────┼───────────────┤
               │ 1          │ ~        │ Bitwise NOT     │ Right-to-left │
               ├────────────┼──────────┼─────────────────┼───────────────┤
               │ 2          │ <<       │ Bitwise left    │ Left-to-right │
               │            │          │ shift           │               │
               ├────────────┼──────────┼─────────────────┼───────────────┤
               │ 2          │ >>       │ Bitwise right   │ Left-to-right │
               │            │          │ shift           │               │
               ├────────────┼──────────┼─────────────────┼───────────────┤
               │ 3          │ &        │ Bitwise AND     │ Left-to-right │
               ├────────────┼──────────┼─────────────────┼───────────────┤
               │ 4          │ ^        │ Bitwise XOR     │ Left-to-right │
               ├────────────┼──────────┼─────────────────┼───────────────┤
               │ 5          │ |        │ Bitwise OR      │ Left-to-right │
               ├────────────┼──────────┼─────────────────┼───────────────┤
               │ 6          │ <        │ Less than       │ Left-to-right │
               ├────────────┼──────────┼─────────────────┼───────────────┤
               │ 6          │ <=       │ Less than or    │ Left-to-right │
               │            │          │ equal to        │               │
               ├────────────┼──────────┼─────────────────┼───────────────┤
               │ 6          │ >        │ Greater than    │ Left-to-right │
               ├────────────┼──────────┼─────────────────┼───────────────┤
               │ 6          │ >=       │ Greater than or │ Left-to-right │
               │            │          │ equal to        │               │
               ├────────────┼──────────┼─────────────────┼───────────────┤
               │ 7          │ ==       │ Equal to        │ Left-to-right │
               ├────────────┼──────────┼─────────────────┼───────────────┤
               │ 7          │ !=       │ Not equal to    │ Left-to-right │
               ├────────────┼──────────┼─────────────────┼───────────────┤
               │ 8          │ &&       │ Logical AND     │ Left-to-right │
               ├────────────┼──────────┼─────────────────┼───────────────┤
               │ 9          │ ||       │ Logical OR      │ Left-to-right │
               └────────────┴──────────┴─────────────────┴───────────────┘

               Parentheses are supported to bypass the default order.

               Important
                   Unlike the C language, the bitwise AND and OR operators (&
                   and |) in EXPR take precedence over relational operators
                   (<, <=, >, >=, ==, and !=). This means the expression 2 &
                   2 == 2 is true while the equivalent C expression is false.
               The arithmetic operators are NOT supported.

               LTTng first casts all integer constants and fields to signed
               64-bit integers. The representation of negative integers is
               two’s complement. This means that, for example, the signed
               8-bit integer field 0xff (-1) becomes 0xffffffffffffffff
               (still -1) once casted.

               Before a bitwise operator is applied, LTTng casts all its
               operands to unsigned 64-bit integers, and then casts the
               result back to a signed 64-bit integer. For the bitwise NOT
               operator, it’s the equivalent of this C expression:

                   (int64_t) ~((uint64_t) val)

               For the binary bitwise operators, it’s the equivalent of those
               C expressions:

                   (int64_t) ((uint64_t) lhs >> (uint64_t) rhs)
                   (int64_t) ((uint64_t) lhs << (uint64_t) rhs)
                   (int64_t) ((uint64_t) lhs & (uint64_t) rhs)
                   (int64_t) ((uint64_t) lhs ^ (uint64_t) rhs)
                   (int64_t) ((uint64_t) lhs | (uint64_t) rhs)

               If the right-hand side of a bitwise shift operator (<< and >>)
               is not in the [0, 63] range, then EXPR is false.

           EXPR examples:

               msg_id == 23 && size >= 2048

               $ctx.procname == "lttng*" && (!flag || poel < 34)

               $app.my_provider:my_context == 17.34e9 || some_enum >= 14

               $ctx.cpu_id == 2 && filename != "*.log"

               eax_reg & 0xff7 == 0x240 && x[4] >> 12 <= 0x1234

       Migration from a recording event rule specification
           Since LTTng 2.13, what this manual page documents is the standard,
           common way to specify an LTTng event rule.

           With the lttng-enable-event(1) command, you also specify an event
           rule, but with deprecated options and arguments.

           The following table shows how to translate from the
           lttng-enable-event(1) options and arguments to the common event
           rule specification options:
           ┌────────────────────────────┬──────────────────────────────────┐
           │ Recording event rule       │ Common event rule                │
           │ option(s)/argument(s)      │ option(s)                        │
           ├────────────────────────────┼──────────────────────────────────┤
           │                            │                                  │
           │ --kernel and               │ --type=kernel:tracepoint         │
           │ --tracepoint               │                                  │
           ├────────────────────────────┼──────────────────────────────────┤
           │                            │                                  │
           │ --kernel and --syscall     │ --type=kernel:syscall:entry+exit │
           ├────────────────────────────┼──────────────────────────────────┤
           │                            │                                  │
           │ --probe=LOC and            │ --type=kernel:kprobe,            │
           │ RECORDNAME (non-option)    │ --location=LOC, and --event-     │
           │                            │ name=RECORDNAME                  │
           ├────────────────────────────┼──────────────────────────────────┤
           │                            │                                  │
           │ --userspace-probe=LOC      │ --type=kernel:uprobe,            │
           │ and RECORDNAME             │ --location=LOC, and --event-     │
           │ (non-option)               │ name=RECORDNAME                  │
           ├────────────────────────────┼──────────────────────────────────┤
           │                            │                                  │
           │ --function=LOC and         │ Not available as of LTTng 2.15.1 │
           │ RECORDNAME (non-option)    │                                  │
           ├────────────────────────────┼──────────────────────────────────┤
           │                            │                                  │
           │ --userspace and            │ --type=user:tracepoint           │
           │ --tracepoint               │                                  │
           ├────────────────────────────┼──────────────────────────────────┤
           │                            │                                  │
           │ --jul and --tracepoint     │ --type=jul:logging               │
           ├────────────────────────────┼──────────────────────────────────┤
           │                            │                                  │
           │ --log4j and --tracepoint   │ --type=log4j:logging             │
           ├────────────────────────────┼──────────────────────────────────┤
           │                            │                                  │
           │ --log4j2 and               │ --type=log4j2:logging            │
           │ --tracepoint               │                                  │
           ├────────────────────────────┼──────────────────────────────────┤
           │                            │                                  │
           │ --python and               │ --type=python:logging            │
           │ --tracepoint               │                                  │
           ├────────────────────────────┼──────────────────────────────────┤
           │                            │                                  │
           │ NAME (non-option)          │ --name=NAME                      │
           ├────────────────────────────┼──────────────────────────────────┤
           │                            │                                  │
           │ --all                      │ --name='*´ or no --name option   │
           ├────────────────────────────┼──────────────────────────────────┤
           │                            │                                  │
           │ --exclude=XNAME[,XNAME]... │ --exclude-name=XNAME for each    │
           │                            │ XNAME                            │
           ├────────────────────────────┼──────────────────────────────────┤
           │                            │                                  │
           │ --loglevel=LOGLEVEL        │ --log-level=LOGLEVEL..           │
           ├────────────────────────────┼──────────────────────────────────┤
           │                            │                                  │
           │ --loglevel-only=LOGLEVEL   │ --log-level=LOGLEVEL             │
           ├────────────────────────────┼──────────────────────────────────┤
           │                            │                                  │
           │ --filter=EXPR              │ --filter=EXPR                    │
           └────────────────────────────┴──────────────────────────────────┘

## [](#OPTIONS)OPTIONS

       Instrumentation point type condition
           See the “Instrumentation point type condition” section above.

           -E NAME, --event-name=NAME
               With the --type=kernel:kprobe or --type=kernel:uprobe option,
               set the name of the emitted events to NAME instead of the LOC
               argument of the --location=LOC option.

               Defaulting to LOC is specific to LTTng 2.15.1 and may change
               in the future.

           -L LOC, --location=LOC

               With the --type=kernel:kprobe option
                   Set the location of the Linux kprobe to insert to LOC.

                   LOC is one of:

                   •   An address (0x hexadecimal prefix supported).

                   •   A symbol name.

                   •   A symbol name and an offset (SYMBOL+OFFSET format).

               With the --type=kernel:uprobe option
                   Set the location of the user space probe to insert to LOC.

                   LOC is one of:

                   [elf:]PATH:SYMBOL
                       An available symbol within a user space application or
                       library.

                       PATH
                           Application or library path.

                           One of:

                           •   An absolute path.

                           •   A relative path.

                           •   The name of an application as found in the
                               directories listed in the PATH environment
                               variable.

                       SYMBOL
                           Symbol name of the function of which to instrument
                           the entry.

                           SYMBOL can be any defined code symbol in the
                           output of the nm(1) command, including with its
                           --dynamic option, which lists dynamic symbols.

                       As of LTTng 2.15.1, not specifying elf: is equivalent
                       to specifying it, but this default may change in the
                       future.

                       Examples:

                       •   /usr/lib/libc.so.6:malloc

                       •   ./myapp:createUser

                       •   elf:httpd:ap_run_open_htaccess

                   sdt:PATH:PROVIDER:NAME
                       A SystemTap User-level Statically Defined Tracing
                       (USDT) probe within a user space application or
                       library.

                       PATH
                           Application or library path.

                           This can be:

                           •   An absolute path.

                           •   A relative path.

                           •   The name of an application as found in the
                               directories listed in the PATH environment
                               variable.

                       PROVIDER, NAME
                           USDT provider and probe names.

                           For example, with the following USDT probe:

                               DTRACE_PROBE2("server", "accept_request",
                                             request_id, ip_addr);

                           The provider/probe name pair is
                           server:accept_request.

                       Example: sdt:./build/server:server:accept_request

           -t TYPE, --type=TYPE
               Only match events which LTTng creates from an instrumentation
               point having the type TYPE.

               TYPE is one of:

               kernel:tracepoint
                   LTTng kernel tracepoint.

                   As of LTTng 2.15.1, kernel is an alias, but this may
                   change in the future.

               user:tracepoint
                   LTTng user space tracepoint.

                   As of LTTng 2.15.1, user is an alias, but this may change
                   in the future.

               kernel:syscall:entry
                   Linux system call entry.

                   As of LTTng 2.15.1, syscall:entry is an alias, but this
                   may change in the future.

               kernel:syscall:exit
                   Linux system call exit.

                   As of LTTng 2.15.1, syscall:exit is an alias, but this may
                   change in the future.

               kernel:syscall:entry+exit
                   Linux system call entry and exit (two distinct
                   instrumentation points).

                   As of LTTng 2.15.1, the following are aliases, but this
                   may change in the future:

                   •   syscall:entry+exit

                   •   kernel:syscall

                   •   syscall

               kernel:kprobe
                   Linux kprobe.

                   As of LTTng 2.15.1, kprobe is an alias, but this may
                   change in the future.

                   You must specify the location of the kprobe to insert with
                   the --location option.

                   You may specify the name of the emitted events with the
                   --event-name option.

               kernel:uprobe
                   Linux user space probe.

                   You must specify the location of the user space probe to
                   insert with the --location option.

                   You may specify the name of the emitted events with the
                   --event-name option.

               jul:logging
                   java.util.logging logging statement.

                   As of LTTng 2.15.1, jul is an alias, but this may change
                   in the future.

               log4j:logging
                   Apache log4j 1.x logging statement.

                   As of LTTng 2.15.1, log4j is an alias, but this may change
                   in the future.

               log4j2:logging
                   Apache Log4j 2 logging statement.

                   As of LTTng 2.15.1, log4j2 is an alias, but this may
                   change in the future.

               python:logging
                   Python logging statement.

                   As of LTTng 2.15.1, python is an alias, but this may
                   change in the future.

       Event name condition
           See the “Event name condition” section above.

           -n NAME, --name=NAME
               Only match events of which NAME matches, depending on the
               argument of the --type option:

               kernel:tracepoint, user:tracepoint
                   The full name of the LTTng tracepoint.

               jul:logging, log4j:logging, log4j2:logging, python:logging
                   The Java or Python logger name.

               kernel:syscall:entry, kernel:syscall:exit,
               kernel:syscall:entry+exit
                   The name of the system call, without any sys_ prefix.

               This option is NOT available with other instrumentation point
               types.

               As of LTTng 2.15.1, not specifying this option is equivalent
               to specifying --name='*´ (when it applies), but this default
               may change in the future.

           -x XNAME, --exclude-name=XNAME
               Only match events of which XNAME does NOT match the full name
               of the LTTng user space tracepoint.

               Only available with the --type=user:tracepoint option.

           NAME and XNAME are globbing patterns: the * character means “match
           anything”. To match a literal * character, use \*.

       Instrumentation point log level condition
           See the “Instrumentation point log level condition” section above.

           -l LOGLEVELSPEC, --log-level=LOGLEVELSPEC
               Only match events of which the log level of the LTTng
               tracepoint or logging statement is, depending on the format of
               LOGLEVELSPEC:

               LOGLEVEL..
                   At least as severe as LOGLEVEL.

               LOGLEVEL
                   Exactly LOGLEVEL.

               ..
                   Anything.

               This option is NOT available with the following options:

               •   --type=kernel:tracepoint

               •   --type=kernel:syscall:entry

               •   --type=kernel:syscall:exit

               •   --type=kernel:syscall:entry+exit

               •   --type=kernel:kprobe

               •   --type=kernel:uprobe

                   As of LTTng 2.15.1, not specifying this option is
                   equivalent to specifying --log-level=..  (when it
                   applies), but this default may change in the future.

       Event payload and context filter condition
           See the “Event payload and context filter condition” section
           above.

           -f EXPR, --filter=EXPR
               Only match events of which EXPR, which can contain references
               to event payload and current context fields, is true.

               This option is only available with the following options:

               •   --type=kernel:tracepoint

               •   --type=kernel:syscall:entry

               •   --type=kernel:syscall:exit

               •   --type=kernel:syscall:entry+exit

## [](#RESOURCES)RESOURCES

           •   LTTng project website <https://lttng.org>

           •   LTTng documentation <https://lttng.org/docs>

           •   LTTng bug tracker <https://bugs.lttng.org>

           •   Git repositories <https://git.lttng.org>

           •   GitHub organization <https://github.com/lttng>

           •   Continuous integration <https://ci.lttng.org/>

           •   Mailing list <https://lists.lttng.org/> for support and
               development: lttng-dev@lists.lttng.org

           •   IRC channel <irc://irc.oftc.net/lttng>: #lttng on irc.oftc.net

           •   Mastodon <https://mastodon.social/@lttng>

## [](#COPYRIGHT)COPYRIGHT

           This program is part of the LTTng-tools project.

           LTTng-tools is distributed under the GNU General Public License
           version 2 <http://www.gnu.org/licenses/old-
           licenses/gpl-2.0.en.html>. See the LICENSE
           <https://github.com/lttng/lttng-tools/blob/master/LICENSE> file
           for details.

## [](#THANKS)THANKS

           Special thanks to Michel Dagenais and the DORSAL laboratory
           <http://www.dorsal.polymtl.ca/> at École Polytechnique de Montréal
           for the LTTng journey.

           Also thanks to the Ericsson teams working on tracing which helped
           us greatly with detailed bug reports and unusual test cases.

## [](#SEE_ALSO)SEE ALSO

           lttng(1), lttng-add-trigger(1), lttng-list(1), lttng-concepts(7)

## [](#COLOPHON)COLOPHON

           This page is part of the LTTng-Tools (LTTng tools) project.
           Information about the project can be found at ⟨http://lttng.org/⟩.
           It is not known how to report bugs for this man page; if you know,
           please send a mail to man-pages@man7.org.  This page was obtained
           from the project's upstream Git repository
           ⟨https://github.com/lttng/lttng-tools.git⟩ on 2026-08-04.  (At
           that time, the date of the most recent commit that was found in
           the repository was 2026-07-30.)  If you discover any rendering
           problems in this HTML version of the page, or you believe there is
           a better or more up-to-date source for the page, or you have
           corrections or improvements to the information in this COLOPHON
           (which is not part of the original manual page), send a mail to
           man-pages@man7.org

    LTTng 2.15.1                   1 April 2025           LTTNG-EVENT-RULE(7)

------------------------------------------------------------------------

Pages that refer to this page: [lttng-add-trigger(1)](../man1/lttng-add-trigger.1.html),  [lttng-concepts(7)](../man7/lttng-concepts.7.html)

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
