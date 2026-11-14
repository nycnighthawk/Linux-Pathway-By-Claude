---
{"title": "KEYCTL_DH_COMPUTE(2const) — Linux manual page", "url": "https://man7.org/linux/man-pages/man2/keyctl_dh_compute.2const.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# KEYCTL_DH_COMPUTE(2const) --- Linux manual page

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [LIBRARY](#LIBRARY) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [RETURN VALUE](#RETURN_VALUE) \| [ERRORS](#ERRORS) \| [STANDARDS](#STANDARDS) \| [HISTORY](#HISTORY) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                                        |                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    KEYCTL_DH_COMPUTE(2const)                       KEYCTL_DH_COMPUTE(2const)

## [](#NAME)NAME

           KEYCTL_DH_COMPUTE - compute a Diffie-Hellman shared secret or
           public key

## [](#LIBRARY)LIBRARY

           Standard C library (libc, -lc)

## [](#SYNOPSIS)SYNOPSIS

           #include <linux/keyctl.h>  /* Definition of KEY* constants */
           #include <sys/syscall.h>   /* Definition of SYS_* constants */
           #include <unistd.h>

           long syscall(size_t n;
                        SYS_keyctl, KEYCTL_DH_COMPUTE,
                        struct keyctl_dh_params *dh_params,
                        char buf[n], size_t n,
                        struct keyctl_kdf_params *_Nullable kdf_params);

## [](#DESCRIPTION)DESCRIPTION

           Compute a Diffie-Hellman shared secret or public key, optionally
           applying key derivation function (KDF) to the result.

           The dh_params argument is a pointer to a set of parameters
           containing serial numbers for three "user" keys used in the
           Diffie-Hellman calculation, packaged in a structure of the
           following form:

               struct keyctl_dh_params {
                   int32_t private; /* The local private key */
                   int32_t prime; /* The prime, known to both parties */
                   int32_t base;  /* The base integer: either a shared
                                     generator or the remote public key */
               };

           Each of the three keys specified in this structure must grant the
           caller read permission.  The payloads of these keys are used to
           calculate the Diffie-Hellman result as:

               base ^ private mod prime

           If the base is the shared generator, the result is the local
           public key.  If the base is the remote public key, the result is
           the shared secret.

           The buf argument points to a buffer where the result of the
           calculation is placed.  The size of that buffer is specified in n.

           The buffer must be large enough to accommodate the output data,
           otherwise an error is returned.  If n is specified zero, in which
           case the buffer is not used and the operation returns the minimum
           required buffer size (i.e., the length of the prime).

           Diffie-Hellman computations can be performed in user space, but
           require a multiple-precision integer (MPI) library.  Moving the
           implementation into the kernel gives access to the kernel MPI
           implementation, and allows access to secure or acceleration
           hardware.

           Adding support for DH computation to the keyctl() system call was
           considered a good fit due to the DH algorithm's use for deriving
           shared keys; it also allows the type of the key to determine which
           DH implementation (software or hardware) is appropriate.

           If the kdf_params argument is NULL, then the DH result itself is
           returned.  Otherwise (since Linux 4.12), it is a pointer to a
           structure which specifies parameters of the KDF operation to be
           applied:

               struct keyctl_kdf_params {
                   char *hashname;     /* Hash algorithm name */
                   char *otherinfo;    /* SP800-56A OtherInfo */
                   __u32 otherinfolen; /* Length of otherinfo data */
                   __u32 __spare[8];   /* Reserved */
               };

           The hashname field is a null-terminated string which specifies a
           hash name (available in the kernel's crypto API; the list of the
           hashes available is rather tricky to observe; please refer to the
           "Kernel Crypto API Architecture"
           ⟨https://www.kernel.org/doc/html/latest/crypto/architecture.html⟩
           documentation for the information regarding how hash names are
           constructed and your kernel's source and configuration regarding
           what ciphers and templates with type CRYPTO_ALG_TYPE_SHASH are
           available) to be applied to DH result in KDF operation.

           The otherinfo field is an OtherInfo data as described in SP800-56A
           section 5.8.1.2 and is algorithm-specific.  This data is
           concatenated with the result of DH operation and is provided as an
           input to the KDF operation.  Its size is provided in the
           otherinfolen field and is limited by KEYCTL_KDF_MAX_OI_LEN
           constant that defined in security/keys/internal.h to a value of
           64.

           The __spare field is currently unused.  It was ignored until Linux
           4.13 (but still should be user-addressable since it is copied to
           the kernel), and should contain zeros since Linux 4.13.

           The KDF implementation complies with SP800-56A as well as with
           SP800-108 (the counter KDF).

           This operation is exposed by libkeyutils (from libkeyutils 1.5.10
           onwards) via the functions keyctl_dh_compute(3) and
           keyctl_dh_compute_alloc(3).

## [](#RETURN_VALUE)RETURN VALUE

           On success, the number of bytes copied to the buffer, or, if n is
           0, the required buffer size.

           On error, -1 is returned, and errno is set to indicate the error.

## [](#ERRORS)ERRORS

           EAGAIN There was an error during crypto module initialization.

           EFAULT One of the following has failed:

                  •  copying of the struct keyctl_dh_params, provided in the
                     dh_params argument, from user space;

                  •  copying of the struct keyctl_kdf_params, provided in the
                     non-NULL kdf_params argument, from user space (in case
                     kernel supports performing KDF operation on DH operation
                     result);

                  •  copying of data pointed by the hashname field of the
                     struct keyctl_kdf_params from user space;

                  •  copying of data pointed by the otherinfo field of the
                     struct keyctl_kdf_params from user space if the
                     otherinfolen field was nonzero;

                  •  copying of the result to user space.

           EINVAL (before Linux 4.12)
                  Argument kdf_params was non-NULL.

           EINVAL The digest size of the hashing algorithm supplied is zero.

           EINVAL The buffer size provided is not enough to hold the result.
                  Provide 0 as a buffer size in order to obtain the minimum
                  buffer size.

           EINVAL The hash name provided in the hashname field of the struct
                  keyctl_kdf_params pointed by kdf_params argument is too big
                  (the limit is implementation-specific and varies between
                  kernel versions, but it is deemed big enough for all valid
                  algorithm names).

           EINVAL The __spare field of the struct keyctl_kdf_params provided
                  in the kdf_params argument contains nonzero values.

           EMSGSIZE
                  The buffer length exceeds KEYCTL_KDF_MAX_OUTPUT_LEN (which
                  is 1024 currently) or the otherinfolen field of the struct
                  keyctl_kdf_parms passed in kdf_params exceeds
                  KEYCTL_KDF_MAX_OI_LEN (which is 64 currently).

           ENOENT The hashing algorithm specified in the hashname field of
                  the struct keyctl_kdf_params pointed by kdf_params argument
                  hasn't been found.

           ETIMEDOUT
                  The initialization of crypto modules has timed out.

## [](#STANDARDS)STANDARDS

           Linux.

## [](#HISTORY)HISTORY

           Linux 4.7.

## [](#SEE_ALSO)SEE ALSO

           keyctl(2), keyctl_dh_compute(3), keyctl_dh_compute_alloc(3),
           keyctl_dh_compute_kdf(3)

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

    Linux man-pages 6.19            2026-02-08      KEYCTL_DH_COMPUTE(2const)

------------------------------------------------------------------------

Pages that refer to this page: [keyctl(2)](../man2/keyctl.2.html)

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
