---
{"title": "PR_RISCV_SET_ICACHE_FLUSH_CTX(2const) — Linux manual page", "url": "https://man7.org/linux/man-pages/man2/pr_riscv_set_icache_flush_ctx.2const.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# PR_RISCV_SET_ICACHE_FLUSH_CTX(2const) --- Linux manual page

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [LIBRARY](#LIBRARY) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [EXAMPLES](#EXAMPLES) \| [STANDARDS](#STANDARDS) \| [HISTORY](#HISTORY) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                           |                                   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    PR_RISCV_SET...CHE_FLUSH_CTX(2const) PR_RISCV_SET...CHE_FLUSH_CTX(2const)

## [](#NAME)NAME

           PR_RISCV_SET_ICACHE_FLUSH_CTX - enable/disable icache flushing
           instructions in userspace

## [](#LIBRARY)LIBRARY

           Standard C library (libc, -lc)

## [](#SYNOPSIS)SYNOPSIS

           #include <linux/prctl.h>  /* Definition of PR_* constants */
           #include <sys/prctl.h>

           int prctl(PR_RISCV_SET_ICACHE_FLUSH_CTX, unsigned long ctx,
                     unsigned long scope);

## [](#DESCRIPTION)DESCRIPTION

           The context and the scope can be provided using ctx and scope
           respectively.

           When scope is set to PR_RISCV_SCOPE_PER_PROCESS all threads in the
           process are permitted to emit icache flushing instructions.
           Whenever any thread in the process is migrated, the corresponding
           hart's icache will be guaranteed to be consistent with instruction
           storage.  This does not enforce any guarantees outside of
           migration.  If a thread modifies an instruction that another
           thread may attempt to execute, the other thread must still emit an
           icache flushing instruction before attempting to execute the
           potentially modified instruction.  This must be performed by the
           user-space program.

           In per-thread context (i.e., scope is set to
           PR_RISCV_SCOPE_PER_THREAD) only the thread calling this function
           is permitted to emit icache flushing instructions.  When the
           thread is migrated, the corresponding hart's icache will be
           guaranteed to be consistent with instruction storage.

           On kernels configured without SMP, this prctl
           PR_RISCV_SET_ICACHE_FLUSH_CTX is a nop as migrations across harts
           will not occur.

           The following values for ctx can be specified:

           PR_RISCV_CTX_SW_FENCEI_ON (since Linux 6.10)
                  Allow fence.i in user space.

           PR_RISCV_CTX_SW_FENCEI_OFF (since Linux 6.10)
                  Disallow fence.i in user space.  All threads in a process
                  will be affected when scope is set to
                  PR_RISCV_SCOPE_PER_PROCESS.  Therefore, caution must be
                  taken; use this flag only when you can guarantee that no
                  thread in the process will emit fence.i from this point
                  onward.

           The following values for scope can be specified:

           PR_RISCV_SCOPE_PER_PROCESS (since Linux 6.10)
                  Ensure the icache of any thread in this process is coherent
                  with instruction storage upon migration.

           PR_RISCV_SCOPE_PER_THREAD (since Linux 6.10)
                  Ensure the icache of the current thread is coherent with
                  instruction storage upon migration.

## [](#EXAMPLES)EXAMPLES

           The following files are meant to be compiled and linked with each
           other.  The modify_instruction() function replaces an add with
           zero with an add with one, causing the instruction sequence in
           get_value() to change from returning a zero to returning a one.

       Program source: cmodx.c
           #include <stdio.h>
           #include <sys/prctl.h>

           extern int get_value(void);
           extern void modify_instruction(void);

           int
           main(void)
           {
               int value = get_value();

               printf("Value before cmodx: %d\n", value);

               // Call prctl before first fence.i is called
               prctl(PR_RISCV_SET_ICACHE_FLUSH_CTX, PR_RISCV_CTX_SW_FENCEI_ON,
                     PR_RISCV_SCOPE_PER_PROCESS);

               modify_instruction();

               // Call prctl after final fence.i is called in process
               prctl(PR_RISCV_SET_ICACHE_FLUSH_CTX, PR_RISCV_CTX_SW_FENCEI_OFF,
                     PR_RISCV_SCOPE_PER_PROCESS);

               value = get_value();
               printf("Value after cmodx: %d\n", value);
               return 0;
           }

       Program source: cmodx.S
           .option norvc

           .text
           .global modify_instruction
           modify_instruction:
           lw a0, new_insn
           lui a5,%hi(old_insn)
           sw  a0,%lo(old_insn)(a5)
           fence.i
           ret

           .section modifiable, "awx"
           .global get_value
           get_value:
           li a0, 0
           old_insn:
           addi a0, a0, 0
           ret

           .data
           new_insn:
           addi a0, a0, 1

       Expected result
           Value before cmodx: 0
           Value after cmodx: 1

## [](#STANDARDS)STANDARDS

           Linux.  RISC-V only.

## [](#HISTORY)HISTORY

           Linux 6.10 (RISC-V).

## [](#SEE_ALSO)SEE ALSO

           prctl(2)

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

    Linux man-pages 6.19            2026-0P2R-_0R8ISCV_SET...CHE_FLUSH_CTX(2const)

------------------------------------------------------------------------

Pages that refer to this page: [prctl(2)](../man2/prctl.2.html)

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
