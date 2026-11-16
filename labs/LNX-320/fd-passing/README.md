# Lab: pass a file descriptor over a Unix socket

`setup` writes `fdpass.c` with stub `send_fd` and `recv_fd`.

## Your task

1. `int send_fd(int sock, int fd)`: send one byte of data and the descriptor in `SCM_RIGHTS` control data with `sendmsg`; return 0, or -1 with `errno`.
2. `int recv_fd(int sock)`: receive with `recvmsg`, using `CMSG_SPACE(sizeof(int))` for the control buffer and `MSG_CMSG_CLOEXEC`; return the new descriptor, or -1 if the message carried none (also when the peer closed).
3. Use the `CMSG_*` macros; do not index the buffer by hand.

## Success criteria

The check passes a descriptor of a temporary file over a `socketpair` in a forked child, reads the file through the received descriptor, checks that the descriptor has `FD_CLOEXEC`, and that a plain byte with no descriptor makes `recv_fd` return -1. Needs `gcc`.

## Grade it

```bash
mkdir -p ~/lab && cd ~/lab && LAB_DIR=$PWD /path/to/repo/labs/LNX-320/fd-passing/setup
LAB_DIR=$PWD /path/to/repo/labs/LNX-320/fd-passing/check
```

Reading: [the lesson](lesson:LNX-320-T07); then [the quiz](quiz:LNX-320-T07).
