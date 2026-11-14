---
{"title": "mlx5dv(7) — Linux manual page", "url": "https://man7.org/linux/man-pages/man7/mlx5dv.7.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# mlx5dv(7) --- Linux manual page

+------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [DESCRIPTION](#DESCRIPTION) \| [NOTES](#NOTES) \| [SEE ALSO](#SEE_ALSO) \| [AUTHORS](#AUTHORS) \| [COLOPHON](#COLOPHON) |                                   |
+------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                          |                                   |
+------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    MLX5DV(7)            Miscellaneous Information Manual           MLX5DV(7)

## [](#NAME)NAME

           mlx5dv - Direct verbs for mlx5 devices
           This is low level access to mlx5 devices to perform data path
           operations, without general branching performed by
           ibv_post_send(3).

## [](#DESCRIPTION)DESCRIPTION

           The libibverbs API is an abstract one. It is agnostic to any
           underlying provider specific implementation. While this
           abstraction has the advantage of user applications portability it
           has a performance penalty. For some applications optimizing
           performance is more important than portability.

           The mlx5 direct verbs API is intended for such applications.  It
           exposes mlx5 specific low level data path
           (send/receive/completion) operations, allowing the application to
           bypass the libibverbs data path API.

           This interface consists from one hardware specific header file
           with relevant inline functions and conversion logic from ibverbs
           structures to mlx5 specific structures.

           The direct include of mlx5dv.h together with linkage to mlx5
           library will allow usage of this new interface.

           Once an application uses the direct flow the locking scheme is
           fully managed by itself. There is an expectation that no mixed
           flows in the data path for both direct/non-direct access will be
           by same application.

## [](#NOTES)NOTES

           All Mellanox NIC devices starting from Connect-IB (Connect-IB,
           ConnectX-4, ConnectX-4Lx, ConnectX-5, ...) implement the mlx5 API,
           thus using the mlx5 direct verbs does not limit the applications
           to a single NIC HW device thus keeping some level of portability.

## [](#SEE_ALSO)SEE ALSO

           ibv_post_send(3), verbs(7), mlx5dv_is_supported(3)

## [](#AUTHORS)AUTHORS

           Leon Romanovsky <leonro@mellanox.com>

## [](#COLOPHON)COLOPHON

           This page is part of the rdma-core (RDMA Core Userspace Libraries
           and Daemons) project.  Information about the project can be found
           at ⟨https://github.com/linux-rdma/rdma-core⟩.  If you have a bug
           report for this manual page, send it to
           linux-rdma@vger.kernel.org.  This page was obtained from the
           project's upstream Git repository
           ⟨https://github.com/linux-rdma/rdma-core.git⟩ on 2026-08-04.  (At
           that time, the date of the most recent commit that was found in
           the repository was 2026-07-22.)  If you discover any rendering
           problems in this HTML version of the page, or you believe there is
           a better or more up-to-date source for the page, or you have
           corrections or improvements to the information in this COLOPHON
           (which is not part of the original manual page), send a mail to
           man-pages@man7.org

    1.0.0                           2017-02-02                      MLX5DV(7)

------------------------------------------------------------------------

Pages that refer to this page: [mlx5dv_get_clock_info(3)](../man3/mlx5dv_get_clock_info.3.html),  [mlx5dv_init_obj(3)](../man3/mlx5dv_init_obj.3.html),  [mlx5dv_query_device(3)](../man3/mlx5dv_query_device.3.html),  [mlx5dv_ts_to_ns(3)](../man3/mlx5dv_ts_to_ns.3.html)

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
