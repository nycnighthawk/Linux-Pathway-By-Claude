---
{"title": "complex(7) — Linux manual page", "url": "https://man7.org/linux/man-pages/man7/complex.7.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# complex(7) --- Linux manual page

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [LIBRARY](#LIBRARY) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [EXAMPLES](#EXAMPLES) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                         |                                   |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    complex(7)           Miscellaneous Information Manual          complex(7)

## [](#NAME)NAME

           complex - basics of complex mathematics

## [](#LIBRARY)LIBRARY

           Math library (libm, -lm)

## [](#SYNOPSIS)SYNOPSIS

           #include <complex.h>

## [](#DESCRIPTION)DESCRIPTION

           Complex numbers are numbers of the form z = a+b*i, where a and b
           are real numbers and i = sqrt(-1), so that i*i = -1.

           There are other ways to represent that number.  The pair (a,b) of
           real numbers may be viewed as a point in the plane, given by X-
           and Y-coordinates.  This same point may also be described by
           giving the pair of real numbers (r,phi), where r is the distance
           to the origin O, and phi the angle between the X-axis and the line
           Oz.  Now z = r*exp(i*phi) = r*(cos(phi)+i*sin(phi)).

           The basic operations are defined on z = a+b*i and w = c+d*i as:

           addition: z+w = (a+c) + (b+d)*i

           multiplication: z*w = (a*c - b*d) + (a*d + b*c)*i

           division: z/w = ((a*c + b*d)/(c*c + d*d)) + ((b*c - a*d)/(c*c +
           d*d))*i

           Nearly all math function have a complex counterpart but there are
           some complex-only functions.

## [](#EXAMPLES)EXAMPLES

           Your C-compiler can work with complex numbers if it supports the
           C99 standard.  The imaginary unit is represented by I.

           /* check that exp(i * pi) == -1 */
           #include <math.h>        /* for atan */
           #include <stdio.h>
           #include <complex.h>

           int
           main(void)
           {
               double pi = 4 * atan(1.0);
               double complex z = cexp(I * pi);
               printf("%f + %f * i\n", creal(z), cimag(z));
           }

## [](#SEE_ALSO)SEE ALSO

           cabs(3), cacos(3), cacosh(3), carg(3), casin(3), casinh(3),
           catan(3), catanh(3), ccos(3), ccosh(3), cerf(3), cexp(3),
           cexp2(3), cimag(3), clog(3), clog10(3), clog2(3), conj(3),
           cpow(3), cproj(3), creal(3), csin(3), csinh(3), csqrt(3), ctan(3),
           ctanh(3)

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

    Linux man-pages 6.19            2026-02-08                     complex(7)

------------------------------------------------------------------------

Pages that refer to this page: [cabs(3)](../man3/cabs.3.html),  [cacos(3)](../man3/cacos.3.html),  [cacosh(3)](../man3/cacosh.3.html),  [carg(3)](../man3/carg.3.html),  [casin(3)](../man3/casin.3.html),  [casinh(3)](../man3/casinh.3.html),  [catan(3)](../man3/catan.3.html),  [catanh(3)](../man3/catanh.3.html),  [ccos(3)](../man3/ccos.3.html),  [ccosh(3)](../man3/ccosh.3.html),  [cexp2(3)](../man3/cexp2.3.html),  [cexp(3)](../man3/cexp.3.html),  [cimag(3)](../man3/cimag.3.html),  [clog10(3)](../man3/clog10.3.html),  [clog2(3)](../man3/clog2.3.html),  [clog(3)](../man3/clog.3.html),  [conj(3)](../man3/conj.3.html),  [cpow(3)](../man3/cpow.3.html),  [cproj(3)](../man3/cproj.3.html),  [creal(3)](../man3/creal.3.html),  [csin(3)](../man3/csin.3.html),  [csinh(3)](../man3/csinh.3.html),  [csqrt(3)](../man3/csqrt.3.html),  [ctan(3)](../man3/ctan.3.html),  [ctanh(3)](../man3/ctanh.3.html)

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
