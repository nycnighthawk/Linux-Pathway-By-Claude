---
{"title": "AWK", "url": "https://wiki.archlinux.org/title/AWK", "retrieved": "2026-11-01", "license": "GFDL-1.3-or-later"}
---

# AWK

Related articles

-   [List of programming languages](../en/List_of_programming_languages.html "List of programming languages")

[AWK](https://en.wikipedia.org/wiki/AWK "wikipedia:AWK") is a small programming language designed for text processing. Its name is derived from the surnames of its authors: [Alfred Aho](https://en.wikipedia.org/wiki/Alfred_Aho "wikipedia:Alfred Aho"), [Peter Weinberger](https://en.wikipedia.org/wiki/Peter_J._Weinberger "wikipedia:Peter J. Weinberger"), and [Brian Kernighan](https://en.wikipedia.org/wiki/Brian_Kernighan "wikipedia:Brian Kernighan"). The language is [standardized and widely available](https://lwn.net/Articles/820829/) on Unix-like systems.

## Installation {#Installation}

On Arch, the [awk(1p)](https://man.archlinux.org/man/awk.1p) command is provided by [gawk](https://archlinux.org/packages/?name=gawk), which is [installed by default](../en/Base_meta_package.html "Base meta package"), with native Unicode support and a load of [extra](https://www.gnu.org/software/gawk/manual/html_node/POSIX_002fGNU.html)[features](https://www.gnu.org/software/gawk/manual/html_node/Advanced-Features.html#Part-III_003a-Moving-Beyond-Standard-awk-with-gawk).

**Note** [gawk](https://archlinux.org/packages/?name=gawk) is designed to be able to gain additional language features at runtime by dynamically loading the so-called *extensions* \-- [extensions that were bundled within](https://www.gnu.org/software/gawk/manual/html_node/Extension-Samples.html) the software distribution are out-of-box to use, but the separately maintained [gawkextlib](https://aur.archlinux.org/packages/gawkextlib/)^AUR^-\* plugins do require manual installation.

### Alternative implementations {#Alternative_implementations}

Like many other [core utilities](../en/Core_utilities.html "Core utilities"), there are several more-or-less compliant [implementations](https://www.gnu.org/software/gawk/manual/html_node/Other-Versions.html) available:

-   **[BusyBox](../en/BusyBox.html "BusyBox")** --- The BusyBox implementation is not that well performant but has a smaller footprint suitable for memory strained environment.

[https://git.busybox.net/busybox/tree/editors/awk.c](https://git.busybox.net/busybox/tree/editors/awk.c) \|\| [busybox](https://archlinux.org/packages/?name=busybox)

-   **GoAWK** --- AWK implementation in Go language.

[https://github.com/benhoyt/goawk](https://github.com/benhoyt/goawk) \|\| [goawk](https://aur.archlinux.org/packages/goawk/)^AUR^

-   **nawk** --- The \"new\" AWK as described in *The AWK Programming Language*, a.k.a. BWK AWK or the One-True-AWK, is now co-maintained by Arnold Robbins and B. W. Kernighan, featuring UTF-8 and csv support.

[https://awk.dev/](https://awk.dev/) \|\| [nawk](https://archlinux.org/packages/?name=nawk)

-   **mawk** --- A rather performant AWK implementation.

[https://invisible-island.net/mawk/](https://invisible-island.net/mawk/) \|\| [mawk](https://aur.archlinux.org/packages/mawk/)^AUR^

## Troubleshooting {#Troubleshooting}

### Assignment to `ARGC` variable via `-v` option does not preserve in runtime {#Assignment_to_ARGC_variable_via_-v_option_does_not_preserve_in_runtime}

Although undocumented, [it appears](https://groups.google.com/g/comp.lang.awk/c/WDFnplISdgw/) that many implementations will reset the `ARGC` variable internally after processing the variable assignment of `-v` options specified on command line. Therefore, to get desired value of `ARGC` variable in runtime (e.g. `BEGIN` code blocks), it\'s required to set the variable in code block directly:

    BEGIN {
      ARGC=1;
      ...
    }

**Note** An upcoming update to POSIX has [documented this issue specifically](https://austingroupbugs.net/view.php?id=974#c3231).

## See also {#See_also}

-   [nawk(1)](https://man.archlinux.org/man/nawk.1): a refcard-style man page of [nawk](https://archlinux.org/packages/?name=nawk)
-   [The GNU AWK manual](https://www.gnu.org/software/gawk/manual/gawk.html): both a comprehensive tutorial and a canonical reference text on [gawk(1)](https://man.archlinux.org/man/gawk.1)
-   [Alpine Linux\'s community wiki article on AWK](https://wiki.alpinelinux.org/wiki/Awk): has some notes on implementation difference between BusyBox and other AWKs
-   [AWK tech notes](https://maximullaris.com/awk_tech_notes.html): language gotchas and design difference compared to other modern programming languages
-   [Idiomatic AWK](https://backreference.org/category/awk/): how concise an AWK program could be
-   [awk1line.txt](https://www.pement.org/awk/awk1line.txt): handy one-line scripts for AWK
