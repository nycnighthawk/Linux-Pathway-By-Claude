---
{"title": "Borg backup", "url": "https://wiki.archlinux.org/title/Borg_backup", "retrieved": "2026-11-01", "license": "GFDL-1.3-or-later"}
---

# Borg backup

Related articles

-   [System backup](../en/System_backup.html "System backup")
-   [Synchronization and backup programs](../en/Synchronization_and_backup_programs.html "Synchronization and backup programs")

[BorgBackup](https://www.borgbackup.org/) (short: Borg) is a deduplicating backup program. Optionally, it supports compression and authenticated encryption.

The main goal of Borg is to provide an efficient and secure way to backup data. The data deduplication technique used makes Borg suitable for daily backups since only changes are stored. The authenticated encryption technique makes it suitable for backups to not fully trusted targets.

## Installation {#Installation}

[Install](../en/Help:Reading.html#Installation_of_packages "Install") the [borg](https://archlinux.org/packages/?name=borg) package. The next major release, version 2, is available as beta with [borg2](https://aur.archlinux.org/packages/borg2/)^AUR^.

For additional features, install the following packages:

[python-pyfuse3](https://archlinux.org/packages/?name=python-pyfuse3)
:   for mounting archives

[openssh](https://archlinux.org/packages/?name=openssh)
:   for connecting to remote hosts

[borgmatic](https://archlinux.org/packages/?name=borgmatic)
:   a set of wrapper scripts to control Borg via YAML files instead of terminal commands ([borgmatic](../en/Borgmatic.html "Borgmatic"), ([Website](https://torsion.org/borgmatic/))

[borgctl](https://aur.archlinux.org/packages/borgctl/)^AUR^
:   borgbackup without bash scripts - similar to borgmatic with a slightly different feature set ([borgctl](https://github.com/kmille/borgctl))

[pika-backup](https://archlinux.org/packages/?name=pika-backup)
:   a libadwaita/GTK4 based GUI for Borg

[vorta](https://archlinux.org/packages/?name=vorta)
:   a Qt-based GUI for Borg

[borgtui-git](https://aur.archlinux.org/packages/borgtui-git/)^AUR^
:   A TUI and CLI for regularly scheduled backups

If you wish to backup to a different machine than the one where data is sourced, this other machine (the \"server\") also requires borg to be installed. In order to facilitate creation and management of backups, server administrators can take advantage of:

[borgwarehouse](https://aur.archlinux.org/packages/borgwarehouse/)^AUR^
:   a WebUI for a Borg\'s central repository server, comparable to the paid-service offered by [https://www.borgbase.com/](https://www.borgbase.com/).

[borgreport](https://aur.archlinux.org/packages/borgreport/)^AUR^
:   Get a report on repositories with statistics, warnings and error messages (optionally per email) and export OpenMetrics.

## Documentation {#Documentation}

The official [documentation](https://borgbackup.readthedocs.io/en/stable/index.html) includes a [quickstart guide](https://borgbackup.readthedocs.io/en/stable/quickstart.html#a-step-by-step-example). Local documentation can be found in [borg(1)](https://man.archlinux.org/man/borg.1) and `apropos borg`.

Additionally, guidance can be found through the command, either generally:

    $ borg help

or for specific commands:

    $ borg help command

## Usage {#Usage}

The main concept behind Borg is **de-duplication**: rather than accumulating files as in traditional TAR archiving, de-duplication verifies the identity of files, regardless of their names, by hashing them so that they are only copied once. This means that even without compression, it takes up minimal space for repeated incremental backups.

File compression is optional and supports multiple algorithms (zstd is recommended) and intensities.

Archives created with Borg can be mounted as FUSE filesystems for browsing and restoring individual files.

Archives can be created locally, or on remote systems using [SSHFS](../en/SSHFS.html "SSHFS"), [NFS](../en/NFS.html "NFS"), [Samba](../en/Samba.html "Samba"), or similar mounting solutions. Transfer over [SSH](../en/OpenSSH.html "OpenSSH") is supported, but the remote host must have Borg available.

### Creating repositories {#Creating_repositories}

Borg repositories can be encrypted or made tamper-evident. For more information on modes and options, consult the [official documentation on setting up a repository](https://borgbackup.readthedocs.io/en/stable/usage/init.html?highlight=repokey).

To create a Borg repository without encryption or authentication:

    $ borg init --encryption=none /path/to/repo

### Creating archives {#Creating_archives}

Individual archive instances can be created within the repository with the `borg create` command. Each archive must be given a unique name. Borg includes [a list of placeholders](https://borgbackup.readthedocs.io/en/stable/usage/help.html#borg-placeholders) to make adding strings such at dates, times, usernames, and hostnames easier.

To create an archive of the `archivable-dir` directory with the hostname of the source machine and the current date:

    $ borg create /path/to/repo::{hostname}-{now:%Y-%m-%d} archivable-dir

Borg supports extensive inclusion and exclusion options. To exclude `.pyc` files from the archive:

    $ borg create ... --exclude '*.pyc' /path/to/repo::archive-name

More information can be found on the `borg create` [documentation page](https://borgbackup.readthedocs.io/en/stable/usage/create.html).

### Pruning archives {#Pruning_archives}

The removal of old archives is not performed automatically, but can be performed manually with the `borg prune` command. The number of archives to keep must be specified, and can be limited by the time the archive was created.

To keep only the last 7 daily archives, the last four weekly archives, and the last three monthly archives:

    $ borg prune --keep-daily=7 --keep-weekly=4 --keep-monthly=3 /path/to/repo

To keep only the last 10 archives, regardless of when they were created:

    $ borg prune --keep-last=10 /path/to/repo

To keep all archives from the past 30 days, regardless of how many archives that includes:

    $ borg prune --keep-within=30d /path/to/repo

**Note** Pruning will delete the archives but will not actually free space in the repository. To free space, use the `borg compact` command on the repository.

**Warning** Pruning is performed on **all** archives in the repository unless restricted by the `--prefix` or `--glob-archives` flags.

More information can be found on the `borg prune` [documentation page](https://borgbackup.readthedocs.io/en/stable/usage/prune.html).

### Restoring from an archive {#Restoring_from_an_archive}

To restore from an archive:

    $ borg extract /path/to/repo::archive-name path/to/restore

**Note** Borg will extract the *full path* relative to the current working directory. This means that restoring the path `/home/archuser/path/to/restore` from an archive while in the archuser\'s home directory will result in the full restored path being `/home/archuser/home/archuser/path/to/restore`.

Alternatively, a repository can be mounted for interactive restoration:

    $ borg mount /path/to/repo::archive-name

## Tips and tricks {#Tips_and_tricks}

### Cache exclusion {#Cache_exclusion}

Archives\' size can be reduced by excluding cache directories. Directories that adhere to the [Cache Directory Archiving Standard](http://fileformats.archiveteam.org/wiki/Cache_Directory_Tagging_Standard) can be automatically excluded by appending `--exclude-caches` to the archive creation command:

    $ borg create ... --exclude-caches /path/to/repo::archive-name

### Listing affected files {#Listing_affected_files}

Many operations in Borg support the `--list` flag to list affected files or archives. If paired with `--dry-run`, the user can verify the effects of a given command.

## See also {#See_also}

-   [Official documentation](https://borgbackup.readthedocs.io/en/stable/)
