# Lab: a socket-activated epoll daemon

`setup` writes `daemon.py` with a stub. Implement the contract in its docstring: adopt the listening socket passed as descriptor 3, serve many clients from one epoll loop, send the readiness message when the loop is ready and the stopping message on SIGTERM.

The grader plays the part of the init system: it opens the socket, passes it as descriptor 3 with `LISTEN_PID` and `LISTEN_FDS` set, and listens on a datagram socket for the notify messages. The same protocol is what systemd uses (`Type=notify` with a `.socket` unit). A C or Rust version follows the same steps with `epoll_create1`, `epoll_ctl` and `epoll_wait`.

## Run it

`bin/lpc course lab LNX-403 activated-daemon`, or edit `daemon.py` in your work directory and run `check` with `LAB_DIR` set to it.

## Notes

Reading material: [the milestone](lesson:LNX-403-T01).
