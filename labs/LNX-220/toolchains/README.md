# Lab: four toolchains, one program, and what each binary depends on

You will build the same greeting program with the C, Rust and Go toolchains, link some of the results statically, create an
isolated Python environment, and inspect with `readelf` what each result needs at run time.

## Starting state

`setup` writes `src/hello.c`, `src/hello.rs`, `src/go/hello.go` with its `go.mod`, `src/hello.py` and a blank `answers.txt`.

## Your task

1. `cc -O2 -o bin/c-dynamic src/hello.c` and `cc -O2 -static -o bin/c-static src/hello.c`. Compare
   `readelf -lW` (look for `INTERP`) and `readelf -dW` (look for `NEEDED`) on both.
2. `rustc -O -C target-feature=+crt-static -o bin/rust-static src/hello.rs`. Also build a default `bin/rust-default` and
   see how it differs.
3. `cd src/go && CGO_ENABLED=0 go build -o ../../bin/go-static .`
4. `python3 -m venv --without-pip venv`, then run `venv/bin/python src/hello.py`. Look at `venv/pyvenv.cfg`.
5. Fill in `answers.txt`.

## Grade it

```bash
mkdir -p ~/lab && cd ~/lab && LAB_DIR=$PWD /path/to/repo/labs/LNX-220/toolchains/setup
# ...do the task...
LAB_DIR=$PWD /path/to/repo/labs/LNX-220/toolchains/check
```

## Notes

- The lab needs `gcc`, `libc6-dev` (for `libc.a`), `rustc`, `golang-go`, `python3`, `binutils`.
- Reading material: [the lesson](lesson:LNX-220-T07). Afterwards, try [the quiz](quiz:LNX-220-T07).
