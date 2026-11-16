# Lab: finish an edge-triggered epoll echo server

`setup` writes `echo.c`, a TCP echo server on `127.0.0.1` (port from `argv[1]`) whose event loop is missing. The listener and client handling functions exist, but `run_loop` is a stub.

## Your task

1. Implement `run_loop(int lfd)` with `epoll`: add the listener, then loop with `epoll_wait`.
2. On the listener: accept until `EAGAIN`, make each client non-blocking, and register it with `EPOLLIN | EPOLLET`.
3. On a client: call `handle_client(fd)` (it drains the socket and echoes) and close the client when it returns non-zero.
4. The server must handle at least 200 simultaneous idle connections plus active ones in one thread.

## Success criteria

The check starts your server and drives it with a Python client: 200 idle connections, then 20 concurrent echo exchanges with large payloads. Needs `gcc` and `python3`.

## Grade it

```bash
mkdir -p ~/lab && cd ~/lab && LAB_DIR=$PWD /path/to/repo/labs/LNX-320/epoll-echo/setup
LAB_DIR=$PWD /path/to/repo/labs/LNX-320/epoll-echo/check
```

Reading: [the lesson](lesson:LNX-320-T03); then [the quiz](quiz:LNX-320-T03).
