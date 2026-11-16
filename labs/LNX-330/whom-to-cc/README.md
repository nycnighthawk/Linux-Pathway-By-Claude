# Lab: work out who to send a patch to

`setup` writes `MAINTAINERS.mini`, a small copy of the kernel's MAINTAINERS format, and `patch.diff`, a patch that touches four files. `scripts/get_maintainer.pl` does this job in a real tree; here you apply the rules by hand.

## Rules (the same ones the real file documents; to verify against your tree's MAINTAINERS header)

- Sections are separated by blank lines. `M:` maintainer, `R:` designated reviewer, `L:` mailing list, `S:` status, `F:` file pattern, `X:` exclusion.
- `F:` ending in `/` matches everything below that directory. `*` matches within one path component only. A plain path matches that file.
- A file matched by an `X:` pattern of a section is excluded from that section.
- A file can match several sections. Every matching section contributes its `M:`, `R:` and `L:` entries.

## Your task

Edit `recipients.txt`: one line per recipient, `maintainer`, `reviewer` or `list` followed by the address (angle brackets removed). No duplicates, nobody who does not match.

Think about which of the four files falls under each section, and what the `X:` line does.
