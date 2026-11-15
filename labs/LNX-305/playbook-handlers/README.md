# Lab: a playbook with a loop, a template and a handler

You will finish a small playbook that creates files in a loop, renders a Jinja2 template from a list of upstream servers,
and reloads a service only when the configuration really changed. The "service" is a log file, so no real daemon is needed.

## Starting state

`setup` writes `ansible.cfg`, an inventory with `localhost` over a local connection, `vars.yml` (the data),
`site.yml` (a skeleton with four TODO comments and a ready-made handler named `Reload app`), an empty template
`templates/app.conf.j2` and a blank `answers.txt`. Output goes to `out/` in your working directory.

## Your task

1. Create `out/conf.d` and `out/users` with one looping task.
2. With one loop over `admins`, create `out/users/<name>`; each file holds the name and a newline.
3. Render `templates/app.conf.j2` to `out/conf.d/app.conf` and notify the handler. The file must read, in this order:
   the comment line `# Managed by Ansible`; a block `upstream <app_name> {` that holds one line
   `    server HOST:PORT weight=N;` per upstream, then `}`; and a last line `listen <app_port>;`. Blank lines are ignored by the grader.
4. Only when `app_port` is below 1024, create the empty file `out/conf.d/privileged.flag`.
5. Fill in `answers.txt`.

Run it with `ansible-playbook site.yml` and also try `--check --diff`. A second run must report `changed=0`, and the
handler must not run again until the rendered file changes.

## Grade it

```bash
mkdir -p ~/lab && cd ~/lab && LAB_DIR=$PWD /path/to/repo/labs/LNX-305/playbook-handlers/setup
# ...do the task...
LAB_DIR=$PWD /path/to/repo/labs/LNX-305/playbook-handlers/check
```

## Notes

- The grader reruns your playbook with `--check`, twice for real, and once with changed variables.
- The `{% for %}` lines add blank lines unless Ansible's default `trim_blocks` removes them; the grader ignores blank lines anyway.
- The lab needs the package `ansible-core`, a Python 3 with PyYAML and `bash`.
- Reading material: [the lesson](lesson:LNX-305-T02). Afterwards, try [the quiz](quiz:LNX-305-T02).
