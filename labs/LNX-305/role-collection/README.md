# Lab: write a role, package it as a collection, install it and use it

You will write a small role with a documented variable interface, wrap it in a collection, build and install the
collection into a project-local directory and call the role by its fully qualified name. The grader also feeds the role a
bad value to prove that the argument spec is enforced.

## Starting state

`setup` writes `ansible.cfg` (which finds collections in `./collections`), an inventory for `localhost`, `site.yml` (it
calls `acme.tools.banner`, which does not exist yet), an empty `src/acme_tools/` directory and a blank `answers.txt`.

## Your task

1. Create `src/acme_tools/galaxy.yml` for namespace `acme`, name `tools`, version `1.0.0` (the file also needs `authors`,
   `readme`, `description` and a licence; add a short `README.md` next to it).
2. Create the role `banner` under `src/acme_tools/roles/banner/` with `tasks/main.yml`, `defaults/main.yml`, a template and
   `meta/argument_specs.yml`. Variables, all prefixed with `banner_`: `banner_dest` (required string, no default),
   `banner_text` (string, default `Authorised use only`) and `banner_repeat` (integer, default 1).
3. The role creates the destination directory and renders the template to `banner_dest`. The file holds the text line
   `banner_repeat` times and then the line `# end of banner`.
4. Build the collection into `dist/`, install the tarball into `collections/`, and run `ansible-playbook site.yml`.
5. Fill in `answers.txt`.

## Grade it

```bash
mkdir -p ~/lab && cd ~/lab && LAB_DIR=$PWD /path/to/repo/labs/LNX-305/role-collection/setup
# ...do the task...
LAB_DIR=$PWD /path/to/repo/labs/LNX-305/role-collection/check
```

## Notes

- The grader rebuilds and reinstalls the collection itself, so the installed copy always matches your source.
- Validation of `meta/argument_specs.yml` runs automatically before the role's tasks.
- The lab needs the package `ansible-core` and PyYAML.
- Reading material: [the lesson](lesson:LNX-305-T03). Afterwards, try [the quiz](quiz:LNX-305-T03).
