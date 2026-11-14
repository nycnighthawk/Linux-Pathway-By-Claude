---
{"title": "queue(7) — Linux manual page", "url": "https://man7.org/linux/man-pages/man7/queue.7.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# queue(7) --- Linux manual page

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [DESCRIPTION](#DESCRIPTION) \| [STANDARDS](#STANDARDS) \| [HISTORY](#HISTORY) \| [NOTES](#NOTES) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                     |                                   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    queue(7)             Miscellaneous Information Manual            queue(7)

## [](#NAME)NAME

           queue - implementations of linked lists and queues

## [](#DESCRIPTION)DESCRIPTION

           The <sys/queue.h> header file provides a set of macros that define
           and operate on the following data structures:

           SLIST  singly linked lists

           LIST   doubly linked lists

           STAILQ singly linked tail queues

           TAILQ  doubly linked tail queues

           CIRCLEQ
                  doubly linked circular queues

           All structures support the following functionality:

           •  Insertion of a new entry at the head of the list.

           •  Insertion of a new entry after any element in the list.

           •  O(1) removal of an entry from the head of the list.

           •  Forward traversal through the list.

           Code size and execution time depend on the complexity of the data
           structure being used, so programmers should take care to choose
           the appropriate one.

       Singly linked lists (SLIST)
           Singly linked lists are the simplest and support only the above
           functionality.  Singly linked lists are ideal for applications
           with large datasets and few or no removals, or for implementing a
           LIFO queue.  Singly linked lists add the following functionality:

           •  O(n) removal of any entry in the list.

       Singly linked tail queues (STAILQ)
           Singly linked tail queues add the following functionality:

           •  Entries can be added at the end of a list.

           •  O(n) removal of any entry in the list.

           •  They may be concatenated.

           However:

           •  All list insertions must specify the head of the list.

           •  Each head entry requires two pointers rather than one.

           Singly linked tail queues are ideal for applications with large
           datasets and few or no removals, or for implementing a FIFO queue.

       Doubly linked data structures
           All doubly linked types of data structures (lists and tail queues)
           additionally allow:

           •  Insertion of a new entry before any element in the list.

           •  O(1) removal of any entry in the list.

           However:

           •  Each element requires two pointers rather than one.

       Doubly linked lists (LIST)
           Linked lists are the simplest of the doubly linked data
           structures.  They add the following functionality over the above:

           •  They may be traversed backwards.

           However:

           •  To traverse backwards, an entry to begin the traversal and the
              list in which it is contained must be specified.

       Doubly linked tail queues (TAILQ)
           Tail queues add the following functionality:

           •  Entries can be added at the end of a list.

           •  They may be traversed backwards, from tail to head.

           •  They may be concatenated.

           However:

           •  All list insertions and removals must specify the head of the
              list.

           •  Each head entry requires two pointers rather than one.

       Doubly linked circular queues (CIRCLEQ)
           Circular queues add the following functionality over the above:

           •  The first and last entries are connected.

           However:

           •  The termination condition for traversal is more complex.

## [](#STANDARDS)STANDARDS

           BSD.

## [](#HISTORY)HISTORY

           <sys/queue.h> macros first appeared in 4.4BSD.

## [](#NOTES)NOTES

           Some BSDs provide SIMPLEQ instead of STAILQ.  They are identical,
           but for historical reasons they were named differently on
           different BSDs.  STAILQ originated on FreeBSD, and SIMPLEQ
           originated on NetBSD.  For compatibility reasons, some systems
           provide both sets of macros.  glibc provides both STAILQ and
           SIMPLEQ, which are identical except for a missing SIMPLEQ
           equivalent to STAILQ_CONCAT().

## [](#SEE_ALSO)SEE ALSO

           circleq(3), insque(3), list(3), slist(3), stailq(3), tailq(3)

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

    Linux man-pages 6.19            2025-05-17                       queue(7)

------------------------------------------------------------------------

Pages that refer to this page: [circleq(3)](../man3/circleq.3.html),  [insque(3)](../man3/insque.3.html),  [list(3)](../man3/list.3.html),  [slist(3)](../man3/slist.3.html),  [stailq(3)](../man3/stailq.3.html),  [tailq(3)](../man3/tailq.3.html)

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
