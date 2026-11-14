---
{"title": "trace-cmd(1) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/trace-cmd.1.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# trace-cmd(1) --- Linux manual page

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [COMMANDS](#COMMANDS) \| [OPTIONS](#OPTIONS) \| [SEE ALSO](#SEE_ALSO) \| [AUTHOR](#AUTHOR) \| [RESOURCES](#RESOURCES) \| [COPYING](#COPYING) \| [NOTES](#NOTES) \| [COLOPHON](#COLOPHON) |                                   |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                                                   |                                   |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    TRACE-CMD(1)                libtracefs Manual                TRACE-CMD(1)

## [](#NAME)NAME

           trace-cmd - interacts with Ftrace Linux kernel internal tracer

## [](#SYNOPSIS)SYNOPSIS

           trace-cmd COMMAND [OPTIONS]

## [](#DESCRIPTION)DESCRIPTION

           The trace-cmd(1) command interacts with the Ftrace tracer that is
           built inside the Linux kernel. It interfaces with the Ftrace
           specific files found in the debugfs file system under the tracing
           directory. A COMMAND must be specified to tell trace-cmd what to
           do.

## [](#COMMANDS)COMMANDS

               record  - record a live trace and write a trace.dat file to the
                         local disk or to the network.

               set     - set a ftrace configuration parameter.

               report  - reads a trace.dat file and converts the binary data to a
                         ASCII text readable format.

               stream  - Start tracing and read the output directly

               profile - Start profiling and read the output directly

               hist    - show a histogram of the events.

               stat    - show tracing (ftrace) status of the running system

               options - list the plugin options that are available to *report*

               start   - start the tracing without recording to a trace.dat file.

               stop    - stop tracing (only disables recording, overhead of tracer
                         is still in effect)

               restart - restart tracing from a previous stop (only effects recording)

               extract - extract the data from the kernel buffer and create a trace.dat
                         file.

               show    - display the contents of one of the Ftrace Linux kernel tracing files

               reset   - disables all tracing and gives back the system performance.
                         (clears all data from the kernel buffers)

               clear   - clear the content of the Ftrace ring buffers.

               split   - splits a trace.dat file into smaller files.

               list    - list the available plugins or events that can be recorded.

               listen  - open up a port to listen for remote tracing connections.

               agent   - listen on a vsocket for trace clients

               setup-guest - create FIFOs for tracing guest VMs

               restore - restore the data files of a crashed run of trace-cmd record

               snapshot- take snapshot of running trace

               stack   - run and display the stack tracer

               check-events - parse format strings for all trace events and return
                              whether all formats are parseable

               convert   - convert trace files

               attach   - attach a host trace.dat file to a guest trace.dat file

               dump    - read out the meta data from a trace file

## [](#OPTIONS)OPTIONS

           -h, --help
               Display the help text.

           Other options see the man page for the corresponding command.

## [](#SEE_ALSO)SEE ALSO

           trace-cmd-record(1), trace-cmd-report(1), trace-cmd-hist(1),
           trace-cmd-start(1), trace-cmd-stop(1), trace-cmd-extract(1),
           trace-cmd-reset(1), trace-cmd-restore(1), trace-cmd-stack(1),
           trace-cmd-convert(1), trace-cmd-split(1), trace-cmd-list(1),
           trace-cmd-listen(1), trace-cmd.dat(5), trace-cmd-check-events(1),
           trace-cmd-stat(1), trace-cmd-attach(1)

## [](#AUTHOR)AUTHOR

           Written by Steven Rostedt, <rostedt@goodmis.org[1]>

## [](#RESOURCES)RESOURCES

           https://git.kernel.org/pub/scm/utils/trace-cmd/trace-cmd.git/ 

## [](#COPYING)COPYING

           Copyright (C) 2010 Red Hat, Inc. Free use of this software is
           granted under the terms of the GNU Public License (GPL).

## [](#NOTES)NOTES

            1. rostedt@goodmis.org
               mailto:rostedt@goodmis.org

## [](#COLOPHON)COLOPHON

           This page is part of the trace-cmd (a front-end for Ftrace)
           project.  Information about the project can be found at 
           ⟨https://www.trace-cmd.org/⟩.  If you have a bug report for this
           manual page, see ⟨https://www.trace-cmd.org/⟩.  This page was
           obtained from the project's upstream Git repository
           ⟨https://git.kernel.org/pub/scm/utils/trace-cmd/trace-cmd.git⟩ on
           2026-08-04.  (At that time, the date of the most recent commit
           that was found in the repository was 2026-05-29.)  If you discover
           any rendering problems in this HTML version of the page, or you
           believe there is a better or more up-to-date source for the page,
           or you have corrections or improvements to the information in this
           COLOPHON (which is not part of the original manual page), send a
           mail to man-pages@man7.org

    libtracefs                      09/24/2023                   TRACE-CMD(1)

------------------------------------------------------------------------

Pages that refer to this page: [sqlhist(1)](../man1/sqlhist.1.html),  [strace(1)](../man1/strace.1.html),  [trace-cmd-agent(1)](../man1/trace-cmd-agent.1.html),  [trace-cmd-attach(1)](../man1/trace-cmd-attach.1.html),  [trace-cmd-check-events(1)](../man1/trace-cmd-check-events.1.html),  [trace-cmd-clear(1)](../man1/trace-cmd-clear.1.html),  [trace-cmd-convert(1)](../man1/trace-cmd-convert.1.html),  [trace-cmd-dump(1)](../man1/trace-cmd-dump.1.html),  [trace-cmd-extract(1)](../man1/trace-cmd-extract.1.html),  [trace-cmd-hist(1)](../man1/trace-cmd-hist.1.html),  [trace-cmd-list(1)](../man1/trace-cmd-list.1.html),  [trace-cmd-listen(1)](../man1/trace-cmd-listen.1.html),  [trace-cmd-mem(1)](../man1/trace-cmd-mem.1.html),  [trace-cmd-options(1)](../man1/trace-cmd-options.1.html),  [trace-cmd-profile(1)](../man1/trace-cmd-profile.1.html),  [trace-cmd-record(1)](../man1/trace-cmd-record.1.html),  [trace-cmd-report(1)](../man1/trace-cmd-report.1.html),  [trace-cmd-reset(1)](../man1/trace-cmd-reset.1.html),  [trace-cmd-restore(1)](../man1/trace-cmd-restore.1.html),  [trace-cmd-set(1)](../man1/trace-cmd-set.1.html),  [trace-cmd-show(1)](../man1/trace-cmd-show.1.html),  [trace-cmd-snapshot(1)](../man1/trace-cmd-snapshot.1.html),  [trace-cmd-split(1)](../man1/trace-cmd-split.1.html),  [trace-cmd-sqlhist(1)](../man1/trace-cmd-sqlhist.1.html),  [trace-cmd-stack(1)](../man1/trace-cmd-stack.1.html),  [trace-cmd-start(1)](../man1/trace-cmd-start.1.html),  [trace-cmd-stat(1)](../man1/trace-cmd-stat.1.html),  [trace-cmd-stop(1)](../man1/trace-cmd-stop.1.html),  [trace-cmd-stream(1)](../man1/trace-cmd-stream.1.html),  [kbuffer_alloc(3)](../man3/kbuffer_alloc.3.html),  [kbuffer_read_event(3)](../man3/kbuffer_read_event.3.html),  [kbuffer_timestamp(3)](../man3/kbuffer_timestamp.3.html),  [libtraceevent(3)](../man3/libtraceevent.3.html),  [libtracefs(3)](../man3/libtracefs.3.html),  [tep_alloc(3)](../man3/tep_alloc.3.html),  [tep_btf_list_args(3)](../man3/tep_btf_list_args.3.html),  [tep_data_type(3)](../man3/tep_data_type.3.html),  [tep_event_common_fields(3)](../man3/tep_event_common_fields.3.html),  [tep_filter_alloc(3)](../man3/tep_filter_alloc.3.html),  [tep_find_common_field(3)](../man3/tep_find_common_field.3.html),  [tep_find_event(3)](../man3/tep_find_event.3.html),  [tep_find_function(3)](../man3/tep_find_function.3.html),  [tep_get_any_field_val(3)](../man3/tep_get_any_field_val.3.html),  [tep_get_cpus(3)](../man3/tep_get_cpus.3.html),  [tep_get_event(3)](../man3/tep_get_event.3.html),  [tep_get_header_page_size(3)](../man3/tep_get_header_page_size.3.html),  [tep_get_long_size(3)](../man3/tep_get_long_size.3.html),  [tep_get_page_size(3)](../man3/tep_get_page_size.3.html),  [tep_is_bigendian(3)](../man3/tep_is_bigendian.3.html),  [tep_is_file_bigendian(3)](../man3/tep_is_file_bigendian.3.html),  [tep_list_events(3)](../man3/tep_list_events.3.html),  [tep_load_btf(3)](../man3/tep_load_btf.3.html),  [tep_load_plugins(3)](../man3/tep_load_plugins.3.html),  [tep_parse_event(3)](../man3/tep_parse_event.3.html),  [tep_parse_header_page(3)](../man3/tep_parse_header_page.3.html),  [tep_parse_saved_cmdlines(3)](../man3/tep_parse_saved_cmdlines.3.html),  [tep_plugin_kvm_get_func(3)](../man3/tep_plugin_kvm_get_func.3.html),  [tep_print_event(3)](../man3/tep_print_event.3.html),  [tep_print_field_content(3)](../man3/tep_print_field_content.3.html),  [tep_print_printk(3)](../man3/tep_print_printk.3.html),  [tep_read_number(3)](../man3/tep_read_number.3.html),  [tep_read_number_field(3)](../man3/tep_read_number_field.3.html),  [tep_register_comm(3)](../man3/tep_register_comm.3.html),  [tep_register_event_handler(3)](../man3/tep_register_event_handler.3.html),  [tep_register_print_function(3)](../man3/tep_register_print_function.3.html),  [tep_set_flag(3)](../man3/tep_set_flag.3.html),  [tep_set_function_resolver(3)](../man3/tep_set_function_resolver.3.html),  [tep_set_loglevel(3)](../man3/tep_set_loglevel.3.html),  [tep_strerror(3)](../man3/tep_strerror.3.html),  [tracefs_binary_init(3)](../man3/tracefs_binary_init.3.html),  [tracefs_cpu_open(3)](../man3/tracefs_cpu_open.3.html),  [tracefs_cpu_open_mapped(3)](../man3/tracefs_cpu_open_mapped.3.html),  [tracefs_cpu_read_buf(3)](../man3/tracefs_cpu_read_buf.3.html),  [tracefs_cpu_read_size(3)](../man3/tracefs_cpu_read_size.3.html),  [tracefs_dynevent_create(3)](../man3/tracefs_dynevent_create.3.html),  [tracefs_eprobe_alloc(3)](../man3/tracefs_eprobe_alloc.3.html),  [tracefs_error_last(3)](../man3/tracefs_error_last.3.html),  [tracefs_event_get_file(3)](../man3/tracefs_event_get_file.3.html),  [tracefs_event_systems(3)](../man3/tracefs_event_systems.3.html),  [tracefs_file_exists(3)](../man3/tracefs_file_exists.3.html),  [tracefs_filter_pid_function(3)](../man3/tracefs_filter_pid_function.3.html),  [tracefs_filter_string_append(3)](../man3/tracefs_filter_string_append.3.html),  [tracefs_find_cid_pid(3)](../man3/tracefs_find_cid_pid.3.html),  [tracefs_function_filter(3)](../man3/tracefs_function_filter.3.html),  [tracefs_get_tracing_file(3)](../man3/tracefs_get_tracing_file.3.html),  [tracefs_hist_add_sort_key(3)](../man3/tracefs_hist_add_sort_key.3.html),  [tracefs_hist_alloc(3)](../man3/tracefs_hist_alloc.3.html),  [tracefs_hist_start(3)](../man3/tracefs_hist_start.3.html),  [tracefs_instance_create(3)](../man3/tracefs_instance_create.3.html),  [tracefs_instance_file_open(3)](../man3/tracefs_instance_file_open.3.html),  [tracefs_instance_get_name(3)](../man3/tracefs_instance_get_name.3.html),  [tracefs_instance_get_stat(3)](../man3/tracefs_instance_get_stat.3.html),  [tracefs_instance_get_subbuf_size(3)](../man3/tracefs_instance_get_subbuf_size.3.html),  [tracefs_instance_set_affinity(3)](../man3/tracefs_instance_set_affinity.3.html),  [tracefs_instance_tracers(3)](../man3/tracefs_instance_tracers.3.html),  [tracefs_iterate_raw_events(3)](../man3/tracefs_iterate_raw_events.3.html),  [tracefs_kprobe_alloc(3)](../man3/tracefs_kprobe_alloc.3.html),  [tracefs_local_events(3)](../man3/tracefs_local_events.3.html),  [tracefs_option_enable(3)](../man3/tracefs_option_enable.3.html),  [tracefs_options(3)](../man3/tracefs_options.3.html),  [tracefs_options_get_supported(3)](../man3/tracefs_options_get_supported.3.html),  [tracefs_print_init(3)](../man3/tracefs_print_init.3.html),  [tracefs_set_loglevel(3)](../man3/tracefs_set_loglevel.3.html),  [tracefs_snapshot_snap(3)](../man3/tracefs_snapshot_snap.3.html),  [tracefs_sql(3)](../man3/tracefs_sql.3.html),  [tracefs_synth_alloc(3)](../man3/tracefs_synth_alloc.3.html),  [tracefs_synth_create(3)](../man3/tracefs_synth_create.3.html),  [tracefs_synth_echo_cmd(3)](../man3/tracefs_synth_echo_cmd.3.html),  [tracefs_trace_is_on(3)](../man3/tracefs_trace_is_on.3.html),  [tracefs_trace_pipe_stream(3)](../man3/tracefs_trace_pipe_stream.3.html),  [tracefs_tracers(3)](../man3/tracefs_tracers.3.html),  [tracefs_uprobe_alloc(3)](../man3/tracefs_uprobe_alloc.3.html),  [trace_seq_init(3)](../man3/trace_seq_init.3.html),  [trace-cmd.dat.v6(5)](../man5/trace-cmd.dat.v6.5.html),  [trace-cmd.dat.v7(5)](../man5/trace-cmd.dat.v7.5.html)

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
