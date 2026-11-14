---
{"title": "random(7) — Linux manual page", "url": "https://man7.org/linux/man-pages/man7/random.7.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# random(7) --- Linux manual page

+------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [DESCRIPTION](#DESCRIPTION) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                |                                   |
+------------------------------------------------------------------------------------------------+-----------------------------------+

    random(7)            Miscellaneous Information Manual           random(7)

## [](#NAME)NAME

           random - overview of interfaces for obtaining randomness

## [](#DESCRIPTION)DESCRIPTION

           The kernel random-number generator relies on entropy gathered from
           device drivers and other sources of environmental noise to seed a
           cryptographically secure pseudorandom number generator (CSPRNG).
           It is designed for security, rather than speed.

           The following interfaces provide access to output from the kernel
           CSPRNG:

           •  The /dev/urandom and /dev/random devices, both described in
              random(4).  These devices have been present on Linux since
              early times, and are also available on many other systems.

           •  The Linux-specific getrandom(2) system call, available since
              Linux 3.17.  This system call provides access either to the
              same source as /dev/urandom (called the urandom source in this
              page) or to the same source as /dev/random (called the random
              source in this page).  The default is the urandom source; the
              random source is selected by specifying the GRND_RANDOM flag to
              the system call.  (The getentropy(3) function provides a
              slightly more portable interface on top of getrandom(2).)

       Initialization of the entropy pool
           The kernel collects bits of entropy from the environment.  When a
           sufficient number of random bits has been collected, the entropy
           pool is considered to be initialized.

       Choice of random source
           Unless you are doing long-term key generation (and most likely not
           even then), you probably shouldn't be reading from the /dev/random
           device or employing getrandom(2) with the GRND_RANDOM flag.
           Instead, either read from the /dev/urandom device or employ
           getrandom(2) without the GRND_RANDOM flag.  The cryptographic
           algorithms used for the urandom source are quite conservative, and
           so should be sufficient for all purposes.

           The disadvantage of GRND_RANDOM and reads from /dev/random is that
           the operation can block for an indefinite period of time.
           Furthermore, dealing with the partially fulfilled requests that
           can occur when using GRND_RANDOM or when reading from /dev/random
           increases code complexity.

       Monte Carlo and other probabilistic sampling applications
           Using these interfaces to provide large quantities of data for
           Monte Carlo simulations or other programs/algorithms which are
           doing probabilistic sampling will be slow.  Furthermore, it is
           unnecessary, because such applications do not need
           cryptographically secure random numbers.  Instead, use the
           interfaces described in this page to obtain a small amount of data
           to seed a user-space pseudorandom number generator for use by such
           applications.

       Comparison between getrandom, /dev/urandom, and /dev/random
           The following table summarizes the behavior of the various
           interfaces that can be used to obtain randomness.  GRND_NONBLOCK
           is a flag that can be used to control the blocking behavior of
           getrandom(2).  The final column of the table considers the case
           that can occur in early boot time when the entropy pool is not yet
           initialized.
           ┌───────────────┬──────────────┬────────────────┬────────────────────┐
           │ Interface     │ Pool         │ Blocking       │ Behavior when pool │
           │               │              │ behavior       │ is not yet ready   │
           ├───────────────┼──────────────┼────────────────┼────────────────────┤
           │ /dev/random   │ Blocking     │ If entropy too │ Blocks until       │
           │               │ pool         │ low, blocks    │ enough entropy     │
           │               │              │ until there is │ gathered           │
           │               │              │ enough entropy │                    │
           │               │              │ again          │                    │
           ├───────────────┼──────────────┼────────────────┼────────────────────┤
           │ /dev/urandom  │ CSPRNG       │ Never blocks   │ Returns output     │
           │               │ output       │                │ from uninitialized │
           │               │              │                │ CSPRNG (may be low │
           │               │              │                │ entropy and        │
           │               │              │                │ unsuitable for     │
           │               │              │                │ cryptography)      │
           ├───────────────┼──────────────┼────────────────┼────────────────────┤
           │ getrandom()   │ Same as      │ Does not block │ Blocks until pool  │
           │               │ /dev/urandom │ once pool is   │ ready              │
           │               │              │ ready          │                    │
           ├───────────────┼──────────────┼────────────────┼────────────────────┤
           │ getrandom()   │ Same as      │ If entropy too │ Blocks until pool  │
           │ GRND_RANDOM   │ /dev/random  │ low, blocks    │ ready              │
           │               │              │ until there is │                    │
           │               │              │ enough entropy │                    │
           │               │              │ again          │                    │
           ├───────────────┼──────────────┼────────────────┼────────────────────┤
           │ getrandom()   │ Same as      │ Does not block │ EAGAIN             │
           │ GRND_NONBLOCK │ /dev/urandom │ once pool is   │                    │
           │               │              │ ready          │                    │
           ├───────────────┼──────────────┼────────────────┼────────────────────┤
           │ getrandom()   │ Same as      │ EAGAIN if not  │ EAGAIN             │
           │ GRND_RANDOM + │ /dev/random  │ enough entropy │                    │
           │ GRND_NONBLOCK │              │ available      │                    │
           └───────────────┴──────────────┴────────────────┴────────────────────┘

       Generating cryptographic keys
           The  amount  of seed material required to generate a cryptographic
           key equals the effective key size of  the  key.   For  example,  a
           3072-bit  RSA  or  Diffie-Hellman private key has an effective key
           size of 128 bits (it requires about 2^128 operations to break)  so
           a  key  generator  needs only 128 bits (16 bytes) of seed material
           from /dev/random.

           While some safety margin above that minimum is  reasonable,  as  a
           guard  against  flaws  in  the  CSPRNG algorithm, no cryptographic
           primitive available today can hope to promise more than  256  bits
           of security, so if any program reads more than 256 bits (32 bytes)
           from  the  kernel  random  pool  per invocation, or per reasonable
           reseed interval (not less than one minute), that should  be  taken
           as a sign that its cryptography is not skillfully implemented.

## [](#SEE_ALSO)SEE ALSO

           getrandom(2),  getauxval(3), getentropy(3), random(4), urandom(4),
           signal(7)

           ⟨http://www.2uo.de/myths-about-urandom/⟩

## [](#COLOPHON)COLOPHON

           This page is part of the man-pages (Linux  kernel  and  C  library
           user-space  interface  documentation)  project.  Information about
           the       project       can       be       found       at       
           ⟨https://www.kernel.org/doc/man-pages/⟩.   If you have a bug report
           for           this           manual           page,            see
           ⟨https://git.kernel.org/pub/scm/docs/man-pages/man-pages.git/tree/CONTRIBUTING⟩.
           This  page  was  obtained  from  the tarball man-pages-6.19.tar.gz
           fetched                                                       from
           ⟨https://mirrors.edge.kernel.org/pub/linux/docs/man-pages/⟩     on
           2026-09-09.  If you discover any rendering problems in  this  HTML
           version  of the page, or you believe there is a better or more up-
           to-date  source  for  the  page,  or  you  have   corrections   or
           improvements  to  the  information  in this COLOPHON (which is not
           part  of   the   original   manual   page),   send   a   mail   to
           man-pages@man7.org

    Linux man-pages 6.19            2026-02-08                      random(7)

------------------------------------------------------------------------

Pages that refer to this page: [getrandom(2)](../man2/getrandom.2.html),  [arc4random(3)](../man3/arc4random.3.html),  [getentropy(3)](../man3/getentropy.3.html),  [random(4)](../man4/random.4.html)

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
