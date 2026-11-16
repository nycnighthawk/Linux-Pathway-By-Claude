# Lab: a client connect with a deadline and address fallback

`setup` writes `conn.c` with a stub `connect_timeout`.

## Your task

Implement `int connect_timeout(const char *host, const char *port, int timeout_ms)`:

1. Resolve with `getaddrinfo` (`AF_UNSPEC`, `SOCK_STREAM`).
2. For each address create a non-blocking socket and `connect`. On `EINPROGRESS`, `poll` for writability within the time left, then read `SO_ERROR`. If it failed, close the socket and try the next address.
3. The total time for all addresses must not exceed `timeout_ms`.
4. On success clear `O_NONBLOCK` and return the descriptor. On failure return -1 with `errno` set to the last error, or `ETIMEDOUT` when the deadline passed.

## Success criteria

The check connects to a local listener through the name `localhost` (which may resolve to `::1` first, where nothing listens), expects a working descriptor in blocking mode, expects `ECONNREFUSED` for a closed port, and expects `ETIMEDOUT` after roughly the deadline against a listener whose accept queue is full. Needs `gcc` and `python3`.

## Grade it

```bash
mkdir -p ~/lab && cd ~/lab && LAB_DIR=$PWD /path/to/repo/labs/LNX-320/connect-timeout/setup
LAB_DIR=$PWD /path/to/repo/labs/LNX-320/connect-timeout/check
```

Reading: [the lesson](lesson:LNX-320-T08); then [the quiz](quiz:LNX-320-T08).
