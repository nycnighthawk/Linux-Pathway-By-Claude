# Lab: which bug class does Rust remove?

Rust for Linux does not make drivers magically correct; it makes certain classes of mistake impossible to write in safe code, and confines the rest to small `unsafe` blocks inside abstractions. `snippets.c` has eight C fragments, each with a different bug. In `answers.txt`, give for each the mechanism that handles it (the list of keywords is at the top of the file).

One of the eight cannot be removed by the language and is the reason the kernel's Rust abstractions exist. Find it, and explain to yourself why a safe wrapper around it is still valuable.
