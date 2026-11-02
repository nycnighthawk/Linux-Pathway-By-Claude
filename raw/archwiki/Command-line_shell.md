---
{"title": "Command-line shell", "url": "https://wiki.archlinux.org/title/Command-line_shell", "retrieved": "2026-11-02", "license": "GFDL-1.3-or-later"}
---

# Command-line shell

Related articles

-   [Core utilities](../en/Core_utilities.html "Core utilities")
-   [dotfiles](../en/Dotfiles.html "Dotfiles")

From [Wikipedia](https://en.wikipedia.org/wiki/Unix_shell "wikipedia:Unix shell"):

A Unix shell is a command-line interpreter or shell that provides a traditional user interface for the Unix operating system and for Unix-like systems. Users direct the operation of the computer by entering commands as text for a command line interpreter to execute or by creating text scripts of one or more such commands.

## List of shells {#List_of_shells}

Shells that are more or less [POSIX compliant](https://pubs.opengroup.org/onlinepubs/9799919799/utilities/V3_chap02.html) are listed under [#POSIX compliant](#POSIX_compliant), while shells that have a different syntax are under [#Alternative shells](#Alternative_shells).

### POSIX compliant {#POSIX_compliant}

These shells can all be linked from `/usr/bin/sh`. When [Bash](../en/Bash.html "Bash"), [mksh](https://aur.archlinux.org/packages/mksh/)^AUR^ and [zsh](../en/Zsh.html "Zsh") are invoked with the `sh` name, they automatically become more POSIX compliant.

-   **[Bash](../en/Bash.html "Bash")** --- Bash extends the Bourne shell with command-line history and completion, indexed and associative arrays, integer arithmetic, process substitution, here strings, regular expression matching and brace expansion.

[https://www.gnu.org/software/bash/](https://www.gnu.org/software/bash/) \|\| [bash](https://archlinux.org/packages/?name=bash)

-   **[Dash](../en/Dash.html "Dash")** --- Descendant of the NetBSD version of the Almquist Shell (ash). A fast POSIX-compliant shell that aims to be as small as possible.

[http://gondor.apana.org.au/\~herbert/dash/](http://gondor.apana.org.au/~herbert/dash/) \|\| [dash](https://archlinux.org/packages/?name=dash)

-   **KornShell (ksh)** --- The KornShell language is a complete, powerful, high-level programming language for writing applications, often more easily and quickly than with other high-level languages. This makes it especially suitable for prototyping. ksh has the best features of the Bourne shell and the C shell, plus many new features of its own. Thus ksh can do much to enhance your productivity and the quality of your work, both in interacting with the system, and in programming. ksh programs are easier to write, and are more concise and readable than programs written in a lower-level language such as C.

[http://www.kornshell.com](http://www.kornshell.com) \|\| [ksh](https://archlinux.org/packages/?name=ksh)

-   **nsh** --- A command-line shell like fish, but POSIX compatible.

[https://github.com/nuta/nsh](https://github.com/nuta/nsh) \|\| [nsh-git](https://aur.archlinux.org/packages/nsh-git/)^AUR^

-   **[Oil Shell](../en/Oil_Shell.html "Oil Shell") (OSH)** --- Oil Shell is a Bash-compatible UNIX command-line shell. OSH can be run on most UNIX-like operating systems, including GNU/Linux. It is written in Python (v2.7), but ships with a native executable. The dialect of Bash recognized by OSH is called the OSH language.

[https://oils.pub/](https://oils.pub/) \|\| [oils-for-unix](https://archlinux.org/packages/?name=oils-for-unix)

-   **shed** --- A modern POSIX shell written in Rust, focusing on smooth line editing and rich interactive features.

[https://github.com/km-clay/shed](https://github.com/km-clay/shed) \|\| [shed-sh](https://aur.archlinux.org/packages/shed-sh/)^AUR^

-   **Yash** --- Yet another shell is a POSIX-compliant command-line shell written in C99 (ISO/IEC 9899:1999). Yash is intended to be the most POSIX-compliant shell in the world while supporting features for daily interactive and scripting use.

[https://magicant.github.io/yash/](https://magicant.github.io/yash/) \|\| [yash](https://aur.archlinux.org/packages/yash/)^AUR^

-   **[Zsh](../en/Zsh.html "Zsh")** --- Shell designed for interactive use, although it is also a powerful scripting language. Many of the useful features of Bash, ksh, and tcsh were incorporated into Zsh; many original features were added. The [introductory document](https://zsh.sourceforge.net/Intro/intro_toc.html) details some of the unique features of Zsh.

[https://www.zsh.org/](https://www.zsh.org/) \|\| [zsh](https://archlinux.org/packages/?name=zsh)

**Tip** POSIX and Bash scripts can be linted with [shellcheck](https://archlinux.org/packages/?name=shellcheck).

### Alternative shells {#Alternative_shells}

-   **[C shell](https://en.wikipedia.org/wiki/C_shell "wikipedia:C shell") (tcsh)** --- Command language interpreter usable both as an interactive login shell and a shell script command processor. It includes a command-line editor, programmable word completion, spelling correction, a history mechanism, job control and a C-like syntax.

[https://www.tcsh.org](https://www.tcsh.org) \|\| [tcsh](https://archlinux.org/packages/?name=tcsh)

-   **Closh** --- Bash-like shell based on Clojure.

[https://github.com/dundalek/closh](https://github.com/dundalek/closh) \|\| [closh](https://aur.archlinux.org/packages/closh/)^AUR^

-   **Elvish** --- Elvish is a modern and expressive shell that can carry internally structured values through pipelines. This feature makes it possible to avoid a lot of complex text processing code. It features an expressive programming language, with features like exceptions, namespacing and anonymous functions. It also has a powerful readline which checks the syntax while typing, and syntax highlighting by default.

[https://elv.sh](https://elv.sh) \|\| [elvish](https://archlinux.org/packages/?name=elvish)

-   **[fish](../en/Fish.html "Fish")** --- Smart and user-friendly command line shell. Fish performs full-color command-line syntax highlighting, as well as highlighting and completion for commands and their arguments, file existence, and history. It supports complete-as-you-type for history and commands. Fish is able to parse the system\'s man pages in order to determine valid arguments for commands, allowing it to highlight and complete commands. Easy last-command revision can be done using `Alt+Up`. Additionally, fish features significantly simplified programming syntax and control flow (similar to ruby). For more information, see the [tutorial](https://fishshell.com/docs/current/tutorial).

[https://fishshell.com/](https://fishshell.com/) \|\| [fish](https://archlinux.org/packages/?name=fish)

-   **ion** --- Ion is a modern system shell that features a simple, yet powerful, syntax. It is written entirely in Rust, which greatly increases the overall quality and security of the shell, eliminating the possibilities of a ShellShock-like vulnerability, and making development easier. It also offers a level of performance that exceeds that of Dash, when taking advantage of Ion\'s features. While it is developed alongside, and primarily for, RedoxOS, it is fully capable on other \*nix platforms. For more details, look it up at [manual](https://doc.redox-os.org/ion-manual/).

[https://gitlab.redox-os.org/redox-os/ion/](https://gitlab.redox-os.org/redox-os/ion/) \|\| [ion-git](https://aur.archlinux.org/packages/ion-git/)^AUR^

-   **Murex** --- A command line shell with improved features and an enhanced UX.

[https://murex.rocks/](https://murex.rocks/) \|\| [murex](https://aur.archlinux.org/packages/murex/)^AUR^

-   **[nushell](../en/Nushell.html "Nushell")** --- Nu draws inspiration from functional programming languages, and modern CLI tools. Rather than thinking of files and services as raw streams of text, Nu looks at each input as something with structure.

[https://www.nushell.sh](https://www.nushell.sh) \|\| [nushell](https://archlinux.org/packages/?name=nushell)

-   **Oh** --- Unix shell written in Go. It is similar in spirit but different in detail from other Unix shells. Oh extends the shell\'s programming language features without sacrificing the shell\'s interactive features.

[https://github.com/michaelmacinnis/oh](https://github.com/michaelmacinnis/oh) \|\| [oh-git](https://aur.archlinux.org/packages/oh-git/)^AUR^

-   **[PowerShell](https://en.wikipedia.org/wiki/PowerShell "wikipedia:PowerShell")** --- PowerShell is an object-oriented programming language and interactive command line shell, originally written for and exclusive to Windows. Later on, it was open sourced and ported to macOS and Linux.

[https://github.com/PowerShell/PowerShell](https://github.com/PowerShell/PowerShell) \|\| [powershell](https://aur.archlinux.org/packages/powershell/)^AUR^

-   **[rc](https://en.wikipedia.org/wiki/rc "wikipedia:rc")** --- Command interpreter for Plan 9 that provides similar facilities to UNIX's Bourne shell, with some small additions and less idiosyncratic syntax.

[https://doc.cat-v.org/plan_9/4th_edition/papers/rc](https://doc.cat-v.org/plan_9/4th_edition/papers/rc) \|\| [9base](https://archlinux.org/packages/?name=9base)

-   **xonsh** --- Python-powered shell with additional shell primitives that you are used to from Bash and IPython.

[https://xon.sh/](https://xon.sh/) \|\| [xonsh](https://archlinux.org/packages/?name=xonsh)

## Changing your default shell {#Changing_your_default_shell}

After installing one of the above shells, you can execute that shell inside of your current shell, by just running its executable. If you want to be served that shell when you login however, you will need to change your default shell.

To list all installed shells, run:

    $ chsh -l

And to set one as default for your user do:

    $ chsh -s /full/path/to/shell

If you are using [systemd-homed](../en/Systemd-homed.html "Systemd-homed"), run:

    $ homectl update --shell=/full/path/to/shell user

where *`/full/path/to/shell`* is the full path as given by `chsh -l`.

**Note** The default shell for new users is [Bash](../en/Bash.html "Bash"). To switch back to it, use `/usr/bin/bash` as the shell path in the above commands.

If you now log out and log in again, you will be greeted by the other shell.

**Tip** *chsh* uses `/etc/shells` as reference. If a recently installed shell is not present on the list, it can be manually added to this file.

## Uninstalling shell {#Uninstalling_shell}

**Warning** Failure to follow the below procedure may result in users no longer having access to a working shell.

[Change the default shell](#Changing_your_default_shell) before removing the package of the shell.

Alternatively, modify the [user database](../en/User_database.html "User database").

Use it for every user with a shell other than *bash* set as their login shell (including root if needed). When completed, the package can be removed.

## Login shell {#Login_shell}

A *login shell* is an invocation mode in which the shell reads files intended for one-time initialization, such as system-wide `/etc/profile` or the user\'s `~/.profile` or other shell-specific file(s). These files set up the initial environment, which is inherited by all other processes started from the shell (including other non-login shells or graphical programs). Hence, they are read-only once at the beginning of a session, which is, for example, when the user logs in to the console or via [SSH](../en/Secure_Shell.html "SSH"), changes the user with [sudo](../en/Sudo.html "Sudo") or [su](../en/Su.html "Su") using the `--login` parameter, or when the user manually invokes a login shell (e.g., by `bash --login`).

See [#Configuration files](#Configuration_files) and the links therein for an overview of the various initialization files. For more information about login shells, see also [Difference between Login Shell and Non-Login Shell?](https://unix.stackexchange.com/q/38175) and [Why a \"login\" shell over a \"non-login\" shell?](https://unix.stackexchange.com/q/324359) on Stack Exchange.

## Configuration files {#Configuration_files}

To autostart programs in console or upon login, you can use shell startup files/directories. Read the documentation for your shell, or its ArchWiki article, e.g., [Bash#Configuration files](../en/Bash.html#Configuration_files "Bash") or [Zsh#Startup/Shutdown files](../en/Zsh.html#Startup/Shutdown_files "Zsh").

See also [Wikipedia:Unix shell#Configuration files](https://en.wikipedia.org/wiki/Unix_shell#Configuration_files "wikipedia:Unix shell") for a comparison of various configuration files of various shells.

### /etc/profile {#/etc/profile}

Upon login, all Bourne-compatible shells source `/etc/profile`, which in turn sources any readable `*.sh` files in `/etc/profile.d/`: these scripts do not require an interpreter directive, nor do they need to be executable. They are used to set up an environment and define application-specific settings.

### Standardisation {#Standardisation}

It is possible to make (some) shell configuration files follow the same naming convention, as well as support some common configuration between the shells.

See [the article about this](https://blog.flowblok.id.au/2013-02/shell-startup-scripts.html) and the [related repository](https://heptapod.host/flowblok/shell-startup). See also [xsh](https://github.com/sgleizes/xsh).

## Input and output {#Input_and_output}

See also [GregsWiki](https://mywiki.wooledge.org/BashGuide/InputAndOutput "gregswiki:BashGuide/InputAndOutput") and [I/O Redirection](https://www.tldp.org/LDP/abs/html/io-redirection.html).

-   Redirections truncate files before commands are executed:

        $ command file > file

    will therefore not work as expected. While some commands ([sed](../en/Core_utilities.html#Essentials "Sed") for example) provide an option to edit files in place, many do not. In such cases you can use the [sponge(1)](https://man.archlinux.org/man/sponge.1) command from the [moreutils](https://archlinux.org/packages/?name=moreutils) package.

-   Because *cat* is not built into the shell, on many occasions you may find it more convenient to use a [redirection](https://en.wikipedia.org/wiki/Redirection_(computing) "wikipedia:Redirection (computing)"), for example, in scripts, or if you care a lot about performance. In fact `< `*`file`* does the same as `cat `*`file`*.

-   POSIX-compliant shells support [Here Documents](https://tldp.org/LDP/abs/html/here-docs.html):

        $ cat << EOF
        one
        two
        three
        EOF

-   Shell [pipelines](https://en.wikipedia.org/wiki/Pipeline_(Unix) "wikipedia:Pipeline (Unix)") operate on stdout by default. To operate on [stderr(3)](https://man.archlinux.org/man/stderr.3) you can redirect *stderr* to *stdout* with *`command`*` 2>&1 | `*`othercommand`* or, for Bash 4, *`command`*` |& `*`othercommand`*.

-   Remember that many GNU [core utilities](../en/Core_utilities.html "Core utilities") accept files as arguments, so for example, `grep `*`pattern`*` < `*`file`* is replaceable with `grep `*`pattern`*` `*`file`*.

## See also {#See_also}

-   [Evolution of shells in Linux](https://developer.ibm.com/tutorials/l-linux-shells/) on the IBM DeveloperWorks
-   [terminal.sexy](https://terminal.sexy/) --- Terminal Color Scheme Designer
-   [Hyperpolyglot](https://hyperpolyglot.org/unix-shells) --- Side-by-side comparison of shell syntaxes
-   [UNIX Power Tools](https://docstore.mik.ua/orelly/unix/upt/index.htm) --- General command-line tool usage
-   [commandlinefu.com](https://www.commandlinefu.com/commands/browse) --- Command-line snippets sharing
-   [List of applications/Utilities#Terminal emulators](../en/List_of_applications/Utilities.html#Terminal_emulators "List of applications/Utilities")
