---
{"title": "Packaging Brother printer drivers", "url": "https://wiki.archlinux.org/title/Packaging_Brother_printer_drivers", "retrieved": "2026-11-02", "license": "GFDL-1.3-or-later"}
---

# Packaging Brother printer drivers

**This article or section is out of date.**

**Reason:** This page was written before the i686 architecture stopped being supported. As such, it provides examples with i386 packages and packages them without taking [32-bit package guidelines](../en/32-bit_package_guidelines.html "32-bit package guidelines") into consideration. (Discuss in [Talk:Packaging Brother printer drivers](../en/Talk:Packaging_Brother_printer_drivers.html))

Brother supplies Linux drivers for its printers, but they are provided as *.rpm* and/or *.deb* packages only. This article explains what adjustments to the contents of the DEB and RPM packages supplied by Brother will need to be made to create a [PKGBUILD](../en/PKGBUILD.html "PKGBUILD") for the printer driver. Additional example PKGBUILDs for Brother printers can be found by searching in the [AUR](../en/Arch_User_Repository.html "AUR").

[CUPS](../en/CUPS.html "CUPS") handles printers using a *.ppd* file and a filter binary. Once those two files are installed, the printer can be [added](../en/CUPS.html#Usage "CUPS") in CUPS.

## Creating a PKGBUILD from a .deb {#Creating_a_PKGBUILD_from_a_.deb}

Brother is offering a \"Driver Install Tool\" as well as two *.deb* packages.

One is the LPR driver and the other one a CUPS wrapper (running on top of LPR driver). Both can be found on Brother\'s \"Support & Downloads\" page (e.g. for [HL-L9200CDW](https://support.brother.com/g/b/producttop.aspx?c=ca&lang=en&prod=hll9200cdw_us_as_cn)).

It is possible to create a PKGBUILD that will automatically download and install the *.deb* packages directly from the URL provided by Brother. Therefore you will need to obtain the direct download links for both *.deb* packages from brothers website (e.g. for HL-L9200CDW you have [the LPR driver](https://download.brother.com/welcome/dlf101047/hll9200cdwlpr-1.1.2-1.i386.deb) and [the CUPS wrapper](https://download.brother.com/welcome/dlf101045/hll9200cdwcupswrapper-1.1.3-1.i386.deb)).

Once you have obtained the download URLs for both *.deb* packages, use existing PKGBUILD files from [brother-hll8360cdw-lpr-bin](https://aur.archlinux.org/packages/brother-hll8360cdw-lpr-bin/)^AUR^ and [brother-hll8360cdw-cups-bin](https://aur.archlinux.org/packages/brother-hll8360cdw-cups-bin/)^AUR^ as templates. You will need to adjust the package name. Change `url=` to the URL of Brother\'s support page for your specific printer model, `source=` needs to be adjusted to the URL of the *.deb* package. The following PKGBUILD example has been based on [brother-hll8360cdw-cups-bin](https://aur.archlinux.org/packages/brother-hll8360cdw-cups-bin/)^AUR^ but has been adjusted for HL-L9200CDW LPR printer driver:

    # Maintainer: John Doe <joe@example.com>
    pkgname=brother-hll9200cdw-lpr-bin
    pkgver=1.1.2
    pkgrel=1
    pkgdesc="LPR driver for Brother HL-L9200CDW(T) printer"
    arch=("i686" "x86_64")
    url="https://support.brother.com/g/b/producttop.aspx?c=ca&lang=en&prod=hll9200cdw_us_as_cn"
    license=("EULA")
    source=("http://www.brother.com/pub/bsc/linux/packages/hll9200cdwlpr-1.1.2-1.i386.deb")
    md5sums=("30124df7d49362906a2a118eff3c710e")
    package() {
            tar -xf data.tar.gz -C "${pkgdir}"
    }

Do not forget to update the md5sum. The pkgver version should be the same version as Brother\'s printer drivers (please note versions might differ for LPR and CUPS wrapper). Create the PKGBUILD file for the CUPS wrapper, too:

    # Maintainer: John Doe <joe@example.com>
    pkgname=brother-hll9200cdw-cups-bin
    pkgver=1.1.3
    pkgrel=1
    pkgdesc="CUPS wrapper for Brother HL-L9200CDW(T) printer"
    arch=("i686" "x86_64")
    url="https://support.brother.com/g/b/producttop.aspx?c=ca&lang=en&prod=hll9200cdw_us_as_cn"
    license=("EULA")
    source=("http://www.brother.com/pub/bsc/linux/packages/hll9200cdwcupswrapper-1.1.3-1.i386.deb")
    md5sums=("0a802088aac7236a3c309b2b46b37f11")
    package() {
           tar -xf data.tar.gz -C "${pkgdir}"
    }

Finally, use [makepkg](../en/Makepkg.html "Makepkg") to test/install your newly created PKGBUILD file(s). If everything works, do not forget to publish your new driver to AUR. See [AUR submission guidelines](../en/AUR_submission_guidelines.html "AUR submission guidelines") for the details.

## Creating a PKGBUILD from a .rpm {#Creating_a_PKGBUILD_from_a_.rpm}

Unfortunately, Brother\'s drivers have some issues:

-   The CUPS driver is built on top of the lpr driver.
-   The CUPS driver package contains a single installation shell script with an embedded ppd and filter. It is executed by rpm during installation. It extracts the ppd and filter, and performs some installation procedures in a Red Hat-specific way.
-   The CUPS driver package uses paths that are not compliant with the [Arch package guidelines](../en/Arch_package_guidelines.html "Arch package guidelines").

These issues can be worked around.

-   The lpr driver does not need to be installed, so the PKGBUILD can just extract the files in the lpr driver\'s RPM package.
-   The CUPS driver\'s RPM should contain a single shell script. For instance, for the [brother-hl2030](https://aur.archlinux.org/packages/brother-hl2030/)^AUR^ package, the PKGBUILD changes three things:
    1.  The paths are changed.
    2.  All commands are disabled except \"`cat <<EOF`\" or \"`echo > ...`\" or whatever there is that emits \*.ppd or filter to separate file. It was done by wrapping irrelevant instructions by `if false; then ... fi`.
    3.  The target file names for the ppd and filter are changed so they are installed into the same directory as the PKGBUILD. Note that paths to the embedded filter where also changed.
-   To fix the paths to conform to the [Arch package guidelines](../en/Arch_package_guidelines.html "Arch package guidelines"), [sed](https://archlinux.org/packages/?name=sed) or similar can be used on all text files unpacked from both the lpr and CUPS drivers. Look at the patch in the [brother-hl2030](https://aur.archlinux.org/packages/brother-hl2030/)^AUR^ package to check which files are affected.

Effectively after the changes described above the script will just output a ppd and a filter to some known location. The PKGBUILD will then copy them to the proper directories in `$pkgdir`:

    install -m 644 -D ppd "${pkgdir}/usr/share/cups/model/HL2030.ppd"
    install -m 755 -D filter  "${pkgdir}/usr/lib/cups/filter/brlpdwrapperHL2030"

The lpr driver files will also need to be copied into `$pkgdir`!

### Other changes {#Other_changes}

Edit the installation script:

    -#PSTOPSFILTER=`which pstops`
    +PSTOPSFILTER='/usr/lib/cups/filter/pstops'

As pstops is not installed in a standard location, the path will need to be hard-coded.

**The factual accuracy of this article or section is disputed.**

**Reason:** The original author \"could not remember\" why this is needed, or whether it was required at all (Discuss in [Talk:Packaging Brother printer drivers](../en/Talk:Packaging_Brother_printer_drivers.html))

This may also need to be added.

    +[psconvert2]
    +pstops=/usr/lib/cups/filter/pstops

## x86_64

Because some of the supplied binaries are 32 bit only, on an x86_64 system some additional [multilib](../en/Official_repositories.html#multilib "Multilib") packages may need to be installed. Note, however, that few 32 bit packages, such as a 32 bit version of glibc ([lib32-glibc](https://archlinux.org/packages/?name=lib32-glibc)), are in [core](../en/Official_repositories.html#core "Core").
