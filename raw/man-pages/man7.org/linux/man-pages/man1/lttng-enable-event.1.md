---
{"title": "lttng-enable-event(1) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/lttng-enable-event.1.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# lttng-enable-event(1) --- Linux manual page

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [EXIT STATUS](#EXIT_STATUS) \| [ENVIRONMENT](#ENVIRONMENT) \| [FILES](#FILES) \| [EXAMPLES](#EXAMPLES) \| [RESOURCES](#RESOURCES) \| [COPYRIGHT](#COPYRIGHT) \| [THANKS](#THANKS) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                                                                                                                     |                                   |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    LTTNG-ENABLE-EVENT(1)          LTTng Manual         LTTNG-ENABLE-EVENT(1)

## [](#NAME)NAME

           lttng-enable-event - Create or enable LTTng recording event rules

## [](#SYNOPSIS)SYNOPSIS

           Create or enable one or more recording event rules to match Linux
           kernel tracepoint or system call events:

           lttng [GENERAL OPTIONS] enable-event --kernel [--tracepoint | --syscall]
                 (--all | NAME[,NAME]...) [--filter=EXPR]
                 [--session=SESSION] [--channel=CHANNEL]

           Create or enable a recording event rule to match Linux kernel
           events created from a dynamic instrumentation point:

           lttng [GENERAL OPTIONS] enable-event --kernel
                 (--probe=LOC | --function=LOC | --userspace-probe=LOC) RECORDNAME
                 [--session=SESSION] [--channel=CHANNEL]

           Create or enable one or more recording event rules to match user
           space tracepoint events:

           lttng [GENERAL OPTIONS] enable-event --userspace [--tracepoint]
                 (--all | NAME[,NAME]...) [--exclude=XNAME[,XNAME]...]
                 [--loglevel=LOGLEVEL | --loglevel-only=LOGLEVEL] [--filter=EXPR]
                 [--session=SESSION] [--channel=CHANNEL]

           Create or enable one or more recording event rules to match
           Java/Python logging events:

           lttng [GENERAL OPTIONS] enable-event (--jul | --log4j | --log4j2 |
                                                 --python)
                 [--tracepoint] (--all | NAME[,NAME]...)
                 [--loglevel=LOGLEVEL | --loglevel-only=LOGLEVEL] [--filter=EXPR]
                 [--session=SESSION] [--channel=CHANNEL]

## [](#DESCRIPTION)DESCRIPTION

           The lttng enable-event command does one of:

           •   Create one or more recording event rules.

           •   Enable one or more disabled recording event rules.

               See the “Enable a disabled recording event rule” section
               below.

           See lttng-concepts(7) to learn more about instrumentation points,
           events, recording event rules, and event records.

           The recording event rule(s) to create or enable belong to:

           With the --session=SESSION option
               The recording session named SESSION.

           Without the --session option
               The current recording session (see lttng-concepts(7) to learn
               more about the current recording session).

           With the --channel=CHANNEL option
               The channel named CHANNEL.

           Without the --channel option
               The channel named channel0.

               If there’s already a channel for the selected recording
               session and domain which isn’t named channel0, the enable-
               event command fails. Otherwise, it automatically creates it.

           See the “EXAMPLES” section below for usage examples.

           List the recording event rules of a specific recording session
           and/or channel with the lttng-list(1) and lttng-status(1)
           commands.

           Disable an enabled recording event rule with the
           lttng-disable-event(1) command.

       Overview of recording event rule conditions
           For LTTng to emit and record an event E, E must satisfy all the
           conditions of a recording event rule ER, that is:

           Explicit conditions
               You set the following conditions when you create or enable ER
               with the enable-event command:

               •   The instrumentation point type from which LTTng creates E
                   has a specific type.

                   See the “Instrumentation point type condition” section
                   below.

               •   A pattern matches the name of E while another pattern
                   doesn’t.

                   See the “Event name condition” section below.

               •   The log level of the instrumentation point from which
                   LTTng creates E is at least as severe as some value, or is
                   exactly some value.

                   See the “Instrumentation point log level condition”
                   section below.

               •   The fields of the payload of E and the current context
                   fields satisfy a filter expression.

                   See the “Event payload and context filter condition”
                   section below.

           Implicit conditions

               •   ER itself is enabled.

                   A recording event rule is enabled on creation.

                   Enable a disabled recording event rule with the enable-
                   event command.

               •   The channel to which ER is attached is enabled.

                   A channel is enabled on creation.

                   Enable a disabled channel with the lttng-enable-channel(1)
                   command.

               •   The recording session of ER is active (started).

                   A recording session is inactive (stopped) on creation.

                   Start an inactive recording session with the
                   lttng-start(1) command.

               •   The process for which LTTng creates E is allowed to record
                   events.

                   All processes are allowed to record events on recording
                   session creation.

                   Use the lttng-track(1) and lttng-untrack(1) commands to
                   select which processes are allowed to record events based
                   on specific process attributes.

           The dedicated command-line options of most conditions are
           optional: if you don’t specify the option, the associated
           condition is always satisfied.

       Instrumentation point type condition
           An event E satisfies the instrumentation point type condition of a
           recording event rule if the instrumentation point from which LTTng
           creates E is:

           For the Linux kernel tracing domain (--kernel option)

               With the --tracepoint option or without any other
               instrumentation point type option
                   An LTTng kernel tracepoint, that is, a statically defined
                   point in the source code of the kernel image or of a
                   kernel module with LTTng kernel tracer macros.

                   As of LTTng 2.15.1, this is the default instrumentation
                   point type of the Linux kernel tracing domain, but this
                   may change in the future.

                   List the available Linux kernel tracepoints with lttng
                   list --kernel. See lttng-list(1) to learn more.

               With the --syscall option
                   The entry and exit of a Linux kernel system call.

                   List the available Linux kernel system call
                   instrumentation points with lttng list --kernel --syscall.
                   See lttng-list(1) to learn more.

               With the --probe option
                   A Linux kprobe, that is, a single probe dynamically placed
                   in the compiled kernel code.

                   The argument of the --probe option is the location of the
                   kprobe to insert, either a symbol or a memory address,
                   while RECORDNAME is the name of the record of E (see the
                   “Event record name” section below).

                   The payload of a Linux kprobe event is empty.

               With the --userspace-probe option
                   A Linux user space probe, that is, a single probe
                   dynamically placed at the entry of a compiled user space
                   application/library function through the kernel.

                   The argument of the --userspace-probe option is the
                   location of the user space probe to insert, one of:

                   •   A path and symbol (ELF method).

                   •   A path, provider name, and probe name (SystemTap
                       User-level Statically Defined Tracing (USDT) method; a
                       DTrace-style marker).

                       As of LTTng 2.15.1, LTTng only supports USDT probes
                       which are NOT reference-counted.

                   RECORDNAME is the name of the record of E (see the “Event
                   record name” section below).

                   The payload of a Linux user space probe event is empty.

               With the --function option
                   A Linux kretprobe, that is, two probes dynamically placed
                   at the entry and exit of a function in the compiled kernel
                   code.

                   The argument of the --function option is the location of
                   the Linux kretprobe to insert, either a symbol or a memory
                   address, while RECORDNAME is the name of the record of E
                   (see the “Event record name” section below).

                   The payload of a Linux kretprobe event is empty.

           For the user space tracing domain (--userspace option)

               With or without the --tracepoint option
                   An LTTng user space tracepoint, that is, a statically
                   defined point in the source code of a C/C++
                   application/library with LTTng user space tracer macros.

                   As of LTTng 2.15.1, this is the default and sole
                   instrumentation point type of the user space tracing
                   domain, but this may change in the future.

                   List the available user space tracepoints with lttng list
                   --userspace. See lttng-list(1) to learn more.

           For the java.util.logging (--jul option), Apache log4j 1.x
           (--log4j option), Apache Log4j 2 (--log4j2 option), and Python
           (--python option) tracing domains

               With or without the --tracepoint option
                   A logging statement.

                   As of LTTng 2.15.1, this is the default and sole
                   instrumentation point type of the java.util.logging,
                   Apache log4j 1.x, Apache Log4j 2, and Python tracing
                   domains, but this may change in the future.

                   List the available Java and Python loggers with lttng list
                   --jul, lttng list --log4j, lttng list --log4j2, and lttng
                   list --python. See lttng-list(1) to learn more.

       Event name condition
           An event E satisfies the event name condition of a recording event
           rule ER if the two following statements are true:

           •   You specify the --all option or, depending on the
               instrumentation type condition (see the “Instrumentation point
               type condition” section above) of ER, NAME matches:

               LTTng tracepoint
                   The full name of the tracepoint from which LTTng
                   creates E.

                   Note that the full name of a user space tracepoint is
                   PROVIDER:NAME, where PROVIDER is the tracepoint provider
                   name and NAME is the tracepoint name.

               Logging statement
                   The name of the Java or Python logger from which LTTng
                   creates E.

               Linux system call
                   The name of the system call, without any sys_ prefix, from
                   which LTTng creates E.

           •   You don’t specify the --exclude=XNAME[,XNAME]... option or,
               depending on the instrumentation type condition of ER, none of
               the XNAME arguments matches the full name of the user space
               tracepoint from which LTTng creates E.

               The --exclude option is only available with the --userspace
               option.

           This condition is only meaningful for the LTTng tracepoint,
           logging statement, and Linux system call instrumentation point
           types: it’s always satisfied for the other types.

           In all cases, NAME and XNAME are globbing patterns: the *
           character means “match anything”. To match a literal * character,
           use \*. To match a literal , character, use \,.

           Important

               Make sure to single-quote NAME and XNAME when they contain the
               * character and when you run the enable-event command from a
               shell.

           With the LTTng tracepoint, logging statement, and Linux system
           call instrumentation point types, the enable-event command creates
           or enables one independent recording event rule per NAME argument
           (non-option, comma-separated). With the --all option, the enable-
           event command creates or enables a single recording event rule.

       Instrumentation point log level condition
           An event E satisfies the instrumentation point log level condition
           of a recording event rule if either:

           •   The --loglevel and --loglevel-only options are missing.

           •   The log level of the LTTng user space tracepoint or logging
               statement which creates E is:

               With the --loglevel=LOGLEVEL option
                   At least as severe as LOGLEVEL.

               With the --loglevel-only=LOGLEVEL option
                   Exactly LOGLEVEL.

           This condition is only meaningful for the LTTng user space
           tracepoint and logging statement instrumentation point types: it’s
           always satisfied for other types.

           The available values of LOGLEVEL are, depending on the tracing
           domain, from the most to the least severe:

           User space (--userspace option)

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

           java.util.logging (--jul option)

               •   OFF (INT32_MAX)

               •   SEVERE (1000)

               •   WARNING (900)

               •   INFO (800)

               •   CONFIG (700)

               •   FINE (500)

               •   FINER (400)

               •   FINEST (300)

               •   ALL (INT32_MIN)

           Apache log4j 1.x (--log4j option)

               •   OFF (INT32_MAX)

               •   FATAL (50000)

               •   ERROR (40000)

               •   WARN (30000)

               •   INFO (20000)

               •   DEBUG (10000)

               •   TRACE (5000)

               •   ALL (INT32_MIN)

           Apache Log4j 2 (--log4j2 option)

               •   OFF (0)

               •   FATAL (100)

               •   ERROR (200)

               •   WARN (300)

               •   INFO (400)

               •   DEBUG (500)

               •   TRACE (600)

               •   ALL (INT32_MAX)

           Python (--python option)

               •   CRITICAL (50)

               •   ERROR (40)

               •   WARNING (30)

               •   INFO (20)

               •   DEBUG (10)

               •   NOTSET (0)

       Event payload and context filter condition
           An event E satisfies the event payload and context filter
           condition of a recording event rule if the --filter=EXPR option is
           missing or if EXPR is true.

           This condition is only meaningful for the LTTng tracepoint and
           Linux system call instrumentation point types: it’s always
           satisfied for other types.

           EXPR can contain references to the payload fields of E and to the
           current context fields.

           Important

               Make sure to single-quote EXPR when you run the enable-event
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

           Note

               Use the lttng-track(1) and lttng-untrack(1) commands to allow
               or disallow processes to record LTTng events based on their
               attributes instead of using equivalent statically-known
               context fields in EXPR like $ctx.pid.

               The former method is much more efficient.

           EXPR examples:

               msg_id == 23 && size >= 2048

               $ctx.procname == "lttng*" && (!flag || poel < 34)

               $app.my_provider:my_context == 17.34e9 || some_enum >= 14

               $ctx.cpu_id == 2 && filename != "*.log"

               eax_reg & 0xff7 == 0x240 && x[4] >> 12 <= 0x1234

       Event record name
           When LTTng records an event E, the resulting event record has a
           name which depends on the instrumentation point type condition
           (see the “Instrumentation point type condition” section above) of
           the recording event rule which matched E:

           LTTng tracepoint (--kernel/--userspace and --tracepoint options)
               Full name of the tracepoint from which LTTng creates E.

               Note that the full name of a user space tracepoint is
               PROVIDER:NAME, where PROVIDER is the tracepoint provider name
               and NAME is the tracepoint name.

           java.util.logging logging statement (--jul and --tracepoint
           options)
               lttng_jul:event

               Such an event record has a string field logger_name which
               contains the name of the java.util.logging logger from which
               LTTng creates E.

           Apache log4j 1.x logging statement (--log4j and --tracepoint
           options)
               lttng_log4j:event

               Such an event record has a string field logger_name which
               contains the name of the Apache log4j 1.x logger from which
               LTTng creates E.

           Apache Log4j 2 logging statement (--log4j2 and --tracepoint
           options)
               lttng_log4j2:event

               Such an event record has a string field logger_name which
               contains the name of the Apache Log4j 2 logger from which
               LTTng creates E.

           Python logging statement (--python and --tracepoint options)
               lttng_python:event

               Such an event record has a string field logger_name which
               contains the name of the Python logger from which LTTng
               creates E.

           Linux system call (--kernel and --syscall options)

               Entry
                   syscall_entry_NAME, where NAME is the name of the system
                   call from which LTTng creates E, without any sys_ prefix.

               Exit
                   syscall_exit_NAME, where NAME is the name of the system
                   call from which LTTng creates E, without any sys_ prefix.

           Linux kprobe (--kernel and --probe options), Linux user space
           probe (--kernel and --userspace-probe options)
               RECORDNAME (first non-option argument).

           Linux kretprobe (--kernel and --function options)

               Entry
                   RECORDNAME_entry

               Exit
                   RECORDNAME_exit

       Enable a disabled recording event rule
           The enable-event command can enable a disabled recording event
           rule, as listed in the output of the lttng-list(1) command.

           You may enable a disabled recording event rule regardless of the
           activity (started or stopped) of its recording session (see
           lttng-start(1) and lttng-stop(1)).

           To enable a disabled recording event rule, run the enable-event
           command with the exact same options and arguments that you used to
           create it. In particular, with the --filter=EXPR option, EXPR must
           be the exact same string as the one you used on creation.

## [](#OPTIONS)OPTIONS

           See lttng(1) for GENERAL OPTIONS.

       Tracing domain
           One of:

           -j, --jul
               Create or enable recording event rules in the
               java.util.logging (JUL) tracing domain.

           -k, --kernel
               Create or enable recording event rules in the Linux kernel
               tracing domain.

           -l, --log4j
               Create or enable recording event rules in the Apache log4j 1.x
               tracing domain.

           --log4j2
               Create or enable recording event rules in the Apache Log4j 2
               tracing domain.

           -p, --python
               Create or enable recording event rules in the Python tracing
               domain.

           -u, --userspace
               Create or enable recording event rules in the user space
               tracing domain.

       Recording target
           -c CHANNEL, --channel=CHANNEL
               Create or enable recording event rules attached to the channel
               named CHANNEL instead of channel0.

           -s SESSION, --session=SESSION
               Create or enable recording event rules in the recording
               session named SESSION instead of the current recording
               session.

       Instrumentation point type condition
           See the “Instrumentation point type condition” section above.

           At most one of:

           --function=LOC
               Only match Linux kretprobe events.

               Only available with the --kernel option.

               LOC is one of:

               •   A function address (0x hexadecimal prefix supported).

               •   A function symbol name.

               •   A function symbol name and an offset (SYMBOL+OFFSET
                   format).

               You must specify the event record name with RECORDNAME. See
               the “Event record name” section above to learn more.

           --probe=LOC
               Only match Linux kprobe events.

               Only available with the --kernel option.

               LOC is one of:

               •   An address (0x hexadecimal prefix supported).

               •   A symbol name.

               •   A symbol name and an offset (SYMBOL+OFFSET format).

               You must specify the event record name with RECORDNAME. See
               the “Event record name” section above to learn more.

           --userspace-probe=LOC
               Only match Linux user space probe events.

               Only available with the --kernel option.

               LOC is one of:

               [elf:]PATH:SYMBOL
                   Probe an available symbol within a user space application
                   or library.

                   PATH
                       Application or library path.

                       One of:

                       •   An absolute path.

                       •   A relative path.

                       •   The name of an application as found in the
                           directories listed in the PATH environment
                           variable.

                   SYMBOL
                       Symbol name of the function of which to instrument the
                       entry.

                       SYMBOL can be any defined code symbol in the output of
                       the nm(1) command, including with its --dynamic
                       option, which lists dynamic symbols.

                   As of LTTng 2.15.1, not specifying elf: is equivalent to
                   specifying it, but this default may change in the future.

                   Examples:

                   •   --userspace-probe=/usr/lib/libc.so.6:malloc

                   •   --userspace-probe=./myapp:createUser

                   •   --userspace-probe=elf:httpd:ap_run_open_htaccess

               sdt:PATH:PROVIDER:NAME
                   Use a SystemTap User-level Statically Defined Tracing
                   (USDT) probe within a user space application or library.

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

                       The provider/probe name pair is server:accept_request.

                   Example: --userspace-
                   probe=sdt:./build/server:server:accept_request

               You must specify the event record name with RECORDNAME. See
               the “Event record name” section above to learn more.

           --syscall
               Only match Linux system call events.

               Only available with the --kernel option.

           --tracepoint
               Only match:

               With the --kernel or --userspace option
                   LTTng tracepoint events.

               With the --jul, --log4j, --log4j2, or --python option
                   Logging events.

           With the --kernel, not specifying any of the instrumentation point
           type options is equivalent to specifying the --tracepoint option,
           but this default may change in the future.

           With the --userspace, --jul, --log4j, --log4j2, and --python
           options, not specifying the --tracepoint option is equivalent to
           specifying it, but this default may change in the future.

       Event name condition
           See the “Event name condition” section above.

           -a, --all
               Equivalent to a single NAME argument (LTTng tracepoint or
               logger name) set to * (match anything).

               You may NOT use this option with a NAME argument.

           -x XNAME[,XNAME]..., --exclude=XNAME[,XNAME]...
               Only match events of which none of the XNAME arguments matches
               the full name of the LTTng user space tracepoint.

               Only available with the --userspace option.

               XNAME is a globbing pattern: the * character means “match
               anything”. To match a literal * character, use \*. To match a
               literal , character, use \,.

       Instrumentation point log level condition
           See the “Instrumentation point log level condition” section above.

           At most one of:

           --loglevel=LOGLEVEL
               Only match events of which the log level of the LTTng
               tracepoint or logging statement is at least as severe as
               LOGLEVEL.

           --loglevel-only=LOGLEVEL
               Only match events of which the log level of the LTTng
               tracepoint or logging statement is exactly LOGLEVEL.

           The instrumentation point log level options above are NOT
           available with the --kernel option.

       Event payload and context filter condition
           See the “Event payload and context filter condition” section
           above.

           -f EXPR, --filter=EXPR
               Only match events of which EXPR, which can contain references
               to event payload and current context fields, is true.

               This option is only available with the --tracepoint or
               --syscall option.

       Program information
           -h, --help
               Show help.

               This option attempts to launch /usr/bin/man to view this
               manual page. Override the manual pager path with the
               LTTNG_MAN_BIN_PATH environment variable.

           --list-options
               List available command options and quit.

## [](#EXIT_STATUS)EXIT STATUS

           0
               Success

           1
               Command error

           2
               Undefined command

           3
               Fatal error

           4
               Command warning (something went wrong during the command)

## [](#ENVIRONMENT)ENVIRONMENT

           LTTNG_ABORT_ON_ERROR
               Set to 1 to abort the process after the first error is
               encountered.

           LTTNG_HOME
               Path to the LTTng home directory.

               Defaults to $HOME.

               Useful when the Unix user running the commands has a
               non-writable home directory.

           LTTNG_LIST_LEGACY
               Set to 1 to use the legacy output format (LTTng 2.14 and
               earlier) for the lttng-list(1) command instead of the modern
               output format.

               Note that the legacy output doesn’t show anything related to
               features introduced after LTTng 2.14.

           LTTNG_MAN_BIN_PATH
               Absolute path to the manual pager to use to read the LTTng
               command-line help (with lttng-help(1) or with the --help
               option) instead of /usr/bin/man.

           LTTNG_NO_UTF_8
               Set to 1 to NOT emit multi-byte UTF-8 sequences, even if the
               locale claims to support it.

           LTTNG_SESSION_CONFIG_XSD_PATH
               Path to the directory containing the session.xsd recording
               session configuration XML schema.

           LTTNG_SESSIOND_PATH
               Absolute path to the LTTng session daemon binary (see
               lttng-sessiond(8)) to spawn from the lttng-create(1) command.

               The --sessiond-path general option overrides this environment
               variable.

           LTTNG_TERM_COLOR
               Controls when to emit terminal SGR codes in the output.

               The NO_COLOR environment variable overrides this.

               One of:

               auto (default)
                   Only emit SGR codes when the standard output is connected
                   to a color-capable terminal.

               always
                   Always emit SGR codes.

               never
                   Never emit SGR codes.

           NO_COLOR
               If set and not empty, then it’s equivalent to setting
               LTTNG_TERM_COLOR to never.

               See NO_COLOR <https://no-color.org/> to learn more.

## [](#FILES)FILES

           $LTTNG_HOME/.lttngrc
               Unix user’s LTTng runtime configuration.

               This is where LTTng stores the name of the Unix user’s current
               recording session between executions of lttng(1).
               lttng-create(1) and lttng-set-session(1) set the current
               recording session.

           $LTTNG_HOME/lttng-traces
               Default output directory of LTTng traces in local and snapshot
               modes.

               Override this path with the --output option of the
               lttng-create(1) command.

           $LTTNG_HOME/.lttng
               Unix user’s LTTng runtime and configuration directory.

           $LTTNG_HOME/.lttng/sessions
               Default directory containing the Unix user’s saved recording
               session configurations (see lttng-save(1) and lttng-load(1)).

           /usr/local/etc/lttng/sessions
               Directory containing the system-wide saved recording session
               configurations (see lttng-save(1) and lttng-load(1)).

           Note

               $LTTNG_HOME defaults to the value of the HOME environment
               variable.

## [](#EXAMPLES)EXAMPLES

           Example 1. Create a recording event rule which matches all Linux
           system call events (current recording session, default channel).

               See the --all and --syscall options.

                   $ lttng enable-event --kernel --all --syscall

           Example 2. Create a recording event rule which matches user space
           tracepoint events named specifically (current recording session,
           default channel).

               The recording event rule below matches all user space
               tracepoint events of which the name starts with
               my_provider:msg.

                   $ lttng enable-event --userspace 'my_provider:msg*'

           Example 3. Create three recording event rules which match Python
           logging events named specifically (current recording session,
           default channel).

                   $ lttng enable-event --python server3,ui.window,user-mgmt

           Example 4. Create a recording event rule which matches Apache
           log4j 1.x logging events with a specific log level range (current
           recording session, specific channel).

               See the --channel, --all, and --loglevel options.

                   $ lttng enable-event --log4j --channel=my-loggers \
                                        --all --loglevel=INFO

           Example 5. Create a recording event rule which matches Apache
           Log4j 2 logging events with the specific WARN log level (current
           recording session, specific channel).

               See the --channel, --all, and --loglevel options.

                   $ lttng enable-event --log4j2 --channel=my-loggers \
                                        --all --loglevel-only=WARN

           Example 6. Create a recording event rule which matches specific
           Linux kprobe events (current recording session, default channel).

               The recording event rule below matches the entry of
               usb_disconnect() Linux kernel function calls. The records of
               such events are named usbd (see the “Event record name”
               section above).

               See the --probe option.

                   $ lttng enable-event --kernel --probe=usb_disconnect usbd

           Example 7. Create a recording event rule which matches Linux
           kernel tracepoint events which satisfy an event payload and
           context filter (specific recording session, default channel).

               See the --session and --filter options.

                   $ lttng enable-event --kernel --session=my-session 'sched_*' \
                           --filter='$ctx.preemptible && comm != "systemd*"'

           Example 8. Enable two Linux kernel tracepoint recording event
           rules (current recording session, specific channel).

               See the --channel option.

                   $ lttng enable-event --kernel --channel=tva ja,wendy

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

           lttng(1), lttng-disable-event(1), lttng-enable-channel(1),
           lttng-list(1), lttng-start(1), lttng-track(1), lttng-concepts(7)

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

    LTTng 2.15.1                   1 April 2025         LTTNG-ENABLE-EVENT(1)

------------------------------------------------------------------------

Pages that refer to this page: [lttng(1)](../man1/lttng.1.html),  [lttng-disable-event(1)](../man1/lttng-disable-event.1.html),  [lttng-enable-channel(1)](../man1/lttng-enable-channel.1.html),  [lttng-start(1)](../man1/lttng-start.1.html),  [lttng-stop(1)](../man1/lttng-stop.1.html),  [lttng-ust(3)](../man3/lttng-ust.3.html),  [lttng_ust_tracef(3)](../man3/lttng_ust_tracef.3.html),  [lttng_ust_tracelog(3)](../man3/lttng_ust_tracelog.3.html),  [babeltrace2-filter.lttng-utils.debug-info(7)](../man7/babeltrace2-filter.lttng-utils.debug-info.7.html),  [lttng-concepts(7)](../man7/lttng-concepts.7.html),  [lttng-event-rule(7)](../man7/lttng-event-rule.7.html)

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
