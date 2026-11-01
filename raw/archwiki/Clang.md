---
{"title": "Clang", "url": "https://wiki.archlinux.org/title/Clang", "retrieved": "2026-11-01", "license": "GFDL-1.3-or-later"}
---

# Clang

[Clang](https://clang.llvm.org/) is a [C](../en/C.html "C")/C++/Objective C/[CUDA](../en/General-purpose_computing_on_graphics_processing_units.html#CUDA "CUDA") compiler based on [LLVM](../en/LLVM.html "LLVM"). The most recent iteration is distributed under the \"Apache 2.0 License with LLVM exceptions\".

## Installation {#Installation}

[Install](../en/Help:Reading.html#Installation_of_packages "Install") the [clang](https://archlinux.org/packages/?name=clang) package.

## Build packages with Clang {#Build_packages_with_Clang}

**This article or section is a candidate for merging with [makepkg](../en/Makepkg.html "Makepkg").**

**Notes:** compiler flags for use with [makepkg](../en/Makepkg.html "Makepkg") (Discuss in [Talk:Clang](../en/Talk:Clang.html))

### Generic setup {#Generic_setup}

To change the default compiler for building packages, [edit](../en/Help:Reading.html#Append,_add,_create,_edit "Textedit"):

``` {style="margin-bottom: 0; border-bottom:none; padding-bottom:0.8em;"}
/etc/makepkg.conf
```

``` {style="margin-top: 0; border-top-style:dashed; padding-top: 0.8em;"}
...
export CC=clang
export CXX=clang++
```

To use `libc++` as the [C++ Standard Library](https://en.wikipedia.org/wiki/C%2B%2B_Standard_Library "wikipedia:C++ Standard Library") instead of [GCC](../en/GNU_Compiler_Collection.html "GCC")\'s `libstdc++`: install the [libc++](https://archlinux.org/packages/?name=libc%2B%2B) package, then add `-stdlib=libc++` to `CXXFLAGS` in your `/etc/makepkg.conf`.

For LTO support: [install](../en/Help:Reading.html#Installation_of_packages "Install") the [lld](https://archlinux.org/packages/?name=lld) package, then add `-fuse-ld=lld` to `LDFLAGS` in your `/etc/makepkg.conf`.

If you are building with `debug`, you also need to remove `-fvar-tracking-assignments` from `DEBUG_CFLAGS` and `DEBUG_CXXFLAGS`, as Clang does not support it.

**Note** For packages that specify GCC-specific build options, there may be build errors that require either editing the source package, the [PKGBUILD](../en/PKGBUILD.html "PKGBUILD") or commenting out the Clang lines in `makepkg.conf`.

### Qt packages {#Qt_packages}

[Qt](../en/Qt.html "Qt") packages may require extra setup. Qt has predefined build configurations called *mkspecs*, defaulting to [GCC](../en/GNU_Compiler_Collection.html "GCC") for Linux.

In some cases, the *mkspec* will be automatically set to `linux-clang` based on `CC`/`CXX` variables. But in other cases (e.g. packages with direct call of `qmake`) it will not, so we can set it explicitly:

``` {style="margin-bottom: 0; border-bottom:none; padding-bottom:0.8em;"}
/etc/makepkg.conf
```

``` {style="margin-top: 0; border-top-style:dashed; padding-top: 0.8em;"}
export QMAKESPEC=linux-clang
```

**Note** Some packages will require [llvm](https://archlinux.org/packages/?name=llvm) to be installed because `linux-clang` is configured to use tools like `llvm-ar`.

### Rust packages {#Rust_packages}

Whenever clang is set as the system default compiler, Rust needs to be configured to use clang as the linker for C code often compiled as a part of the process for building Rust applications.

To do so, clang (and optionally lld) needs to be specified in `/etc/makepkg.conf.d/rust.conf`.

For example, to use clang and lld:

``` {style="margin-bottom: 0; border-bottom:none; padding-bottom:0.8em;"}
/etc/makepkg.conf.d/rust.conf
```

``` {style="margin-top: 0; border-top-style:dashed; padding-top: 0.8em;"}
RUSTFLAGS="-Cforce-frame-pointers=yes -Clinker=clang -Clink-arg=-fuse-ld=lld"
```

## Using the Static Analyzer {#Using_the_Static_Analyzer}

To analyze a project, simply place the word `scan-build` in front of your build command. For example:

    $ scan-build make

If your project is already compiled, `scan-build` will not rebuild and will not analyse it. To force recompilation and analysis, use `-B` switch:

    $ scan-build make -B

It is also possible to analyze specific files:

    $ scan-build gcc -c t1.c t2.c

## Tips and tricks {#Tips_and_tricks}

**This article or section needs expansion.**

**Reason:** Describe the basic usage of [ClangFormat](https://clang.llvm.org/docs/ClangFormat.html), [Clang-Tidy](https://clang.llvm.org/extra/clang-tidy/index.html), and [Clang-Include-Fixer](https://clang.llvm.org/extra/clang-include-fixer.html). (Discuss in [Talk:Clang](../en/Talk:Clang.html))

### Bash completion {#Bash_completion}

In order to enable Bash completion, install [bash-completion](https://archlinux.org/packages/?name=bash-completion).

## Troubleshooting {#Troubleshooting}

### Stack protector {#Stack_protector}

The [clang](https://archlinux.org/packages/?name=clang) package enables `-fstack-protector-strong` on default. This practice should not cause any problem for compiling most programs and improve the overall security and robustness with a minimal cost. However, there are situations where the stack protector canary is uninitialized in TLS (for example, when you are implementing the `_start` function on yourself). In such cases, compiling with `-fstack-protector-strong` may lead to segmentation faults or other unexpected errors. One should be aware of the divergence between the [clang](https://archlinux.org/packages/?name=clang) package and upstream.

## See also {#See_also}

-   [Wikipedia:Clang](https://en.wikipedia.org/wiki/Clang "wikipedia:Clang")
-   [scan-build: running the analyzer from the command line](https://clang-analyzer.llvm.org/scan-build.html)
-   [Compiling CUDA with clang](https://llvm.org/docs/CompileCudaWithLLVM.html)
