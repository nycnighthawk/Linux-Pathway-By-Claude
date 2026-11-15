# Lab: package a script as an RPM

`setup` creates a source tarball, `hello-site-1.0.tar.gz`, holding a script, its configuration file and a licence, and an empty `rpmbuild/` tree with the tarball already in `rpmbuild/SOURCES`. Write the spec file and build both the source and binary RPMs without root.

## Starting state

`setup` writes the tarball and the `rpmbuild/` workspace into `$LAB_DIR`.

## Your task

1. Write `hello-site.spec` (and copy it to `rpmbuild/SPECS/`): Name `hello-site`, Version `1.0`, Release `1%{?dist}`, License `MIT`, `BuildArch: noarch`, Source0 the tarball, `%autosetup`, an `%install` that puts the script in `%{_bindir}` with mode 0755 and the configuration in `%{_sysconfdir}` with mode 0644, a `%check` that runs the script, a `%files` list that marks the licence with `%license` and the configuration with `%config(noreplace)`, and a `%changelog` entry.
2. Build both packages: `rpmbuild --define "_topdir $PWD/rpmbuild" -ba rpmbuild/SPECS/hello-site.spec`.

## Grade it

```bash
mkdir -p ~/lab && cd ~/lab && LAB_DIR=$PWD /path/to/repo/labs/LNX-304/rpm-spec/setup
# ...write the spec, run rpmbuild...
LAB_DIR=$PWD /path/to/repo/labs/LNX-304/rpm-spec/check
```

## Notes

- Needs the `rpm` package (it provides `rpmbuild`) on Debian or Ubuntu, or `rpm-build` on Enterprise Linux. No root needed.
- `rpm -qpl`, `rpm -qp --scripts`, `rpm -qp --requires` and `rpmlint` (if installed) show what you built. For the clean-room version of this build, run the source RPM through `mock`.
- Reading material: [the lesson](lesson:LNX-304-T01). Afterwards, try [the quiz](quiz:LNX-304-T01).
