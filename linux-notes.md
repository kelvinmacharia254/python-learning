# Linux Command-Line Revision Guide

*Enhanced and corrected from three pages of handwritten notes — 17 October 2026*

## 1. Navigation and filesystem layout

The shell starts in a working directory. Absolute paths start at `/`; relative paths are resolved from the working directory. `~` expands to your home directory.

| Command | Purpose | Example |
|---|---|---|
| `pwd` | Print working directory | `pwd` |
| `ls` | List entries | `ls -lah` |
| `cd` | Change directory | `cd ~/projects` |
| `cd ..` | Go to parent directory | `cd ..` |
| `cd -` | Return to previous directory | `cd -` |
| `ls -a` | Include hidden entries | `ls -a` |

Useful locations: `/home` user directories; `/etc` system configuration; `/var/log` logs; `/tmp` temporary files; `/usr/bin` many executable programs; `/proc` process and kernel information.

**Try it:** `pwd; ls -lah; cd /tmp; pwd; cd -`.

## 2. File and directory manipulation

| Command | Purpose | Example |
|---|---|---|
| `mkdir` | Create directory | `mkdir -p practice/reports` |
| `touch` | Create empty file or update timestamps | `touch practice/notes.txt` |
| `cp` | Copy files | `cp notes.txt notes.bak` |
| `cp -r` | Copy directories recursively | `cp -r source destination` |
| `mv` | Move or rename | `mv old.txt new.txt` |
| `rm` | Remove file | `rm old.txt` |
| `rm -r` | Remove directory tree | `rm -r old_directory` |
| `rmdir` | Remove empty directory | `rmdir empty_directory` |

**Caution:** `rm` generally does not move files to a recycle bin. Inspect the target before deleting; be especially careful with `rm -r` and never use `sudo rm -rf` casually.

## 3. Ownership, groups and permissions

Every Linux file has an owning user, an owning group, and permissions for **user**, **group**, and **others**. Inspect with `ls -l filename`, identify your account with `whoami`, and list your groups with `id` or `groups`.

Example: `-rwxr-x---` means a regular file (`-`), user `rwx`, group `r-x`, others `---`.

| Permission | Value | On files | On directories |
|---|---:|---|---|
| `r` | 4 | Read contents | List directory entries (subject to traversal) |
| `w` | 2 | Modify contents | Create, delete, rename entries when combined with `x` |
| `x` | 1 | Execute program/script | Traverse/search directory |

Numeric mode adds values separately for each class: `chmod 755 script.sh` = `rwxr-xr-x`; `chmod 644 notes.txt` = `rw-r--r--`; `chmod 700 private` = `rwx------`. `chmod 640 file` = `rw-r-----`.

Symbolic mode: `chmod u+x script.sh` adds execute for owner; `chmod g-w file` removes group write; `chmod o= file` removes all permissions for others. Ownership is changed with `chown user:group file` (typically requires privilege), and group ownership with `chgrp group file`.

**Important nuance:** Deleting a file depends mainly on write and execute permissions on its parent directory, not the file's own write bit. Root privileges and ACLs can modify normal access expectations. Use `getfacl file` if ACLs are relevant.

**Practice:** `touch demo.sh; chmod 640 demo.sh; ls -l demo.sh; chmod u+x demo.sh; ls -l demo.sh`.

## 4. Finding files and filtering text

`find` searches directory trees; `grep` searches text within input.

```bash
find ~/projects -type f -name '*.py'
find . -type d -name 'tests'
grep -n 'TODO' app.py
grep -Rni --include='*.py' 'import os' .
```

`find` can filter by name, type, size, modification time and more. `grep -i` ignores case; `-n` prints line numbers; `-R` searches recursively. Quote patterns so the shell does not expand them before `find` or `grep` sees them.

Other useful commands: `which python3` (executable location), `type python3` (how the shell resolves a command), `command -v python3` (portable command lookup).

## 5. Wildcards, globbing, pipes and redirection

The shell expands glob patterns **before** running most commands:

| Pattern | Meaning | Example |
|---|---|---|
| `*` | Zero or more characters | `ls *.py` |
| `?` | Exactly one character | `ls file?.txt` |
| `[abc]` | One of the listed characters | `ls file[12].txt` |
| `[0-9]` | One digit | `ls report[0-9].txt` |

Glob matching and hidden files depend on shell settings; in Bash, `*` does not match leading-dot names by default. `?` is a glob wildcard in filenames, but in a regular expression it has a different meaning.

Pipes send one command's standard output into another command's standard input:

```bash
ps aux | grep '[p]ython'
find . -type f -name '*.py' | wc -l
```

Redirection is different from piping:

| Operator | Meaning |
|---|---|
| `>` | Write stdout to file, replacing existing contents |
| `>>` | Append stdout |
| `<` | Read stdin from file |
| `2>` | Redirect stderr |
| `2>&1` | Redirect stderr to current stdout destination |
| `|` | Pipe stdout into next command |

```bash
printf 'first\n' > log.txt
printf 'second\n' >> log.txt
cat log.txt
python3 app.py > output.log 2>&1
```

## 6. Text processing

| Command | Main use | Example |
|---|---|---|
| `head` | First lines | `head -n 10 data.csv` |
| `tail` | Last lines | `tail -n 20 app.log` |
| `tail -f` | Follow appended log lines | `tail -f app.log` |
| `wc` | Count lines, words, bytes | `wc -l data.csv` |
| `sort` | Sort lines | `sort names.txt` |
| `uniq` | Remove/count adjacent duplicates | `sort names.txt \| uniq -c` |
| `cut` | Extract delimited fields | `cut -d, -f2 data.csv` |
| `tr` | Translate/delete characters | `tr 'a-z' 'A-Z'` |
| `sed` | Stream edits | `sed 's/old/new/g' file.txt` |
| `cat` | Display/concatenate | `cat file.txt` |
| `less` | Page through output | `less app.log` |

**Corrections:** `uniq` only groups *adjacent* duplicate lines; usually sort first. `cut` does not parse complex quoted CSV reliably; use Python's `csv` module for real CSV files. `sed` can perform substitutions, not just character transformations.

## 7. Processes, foreground/background jobs and exit status

A process is a running instance of a program. Each process has a PID; its parent is identified by a PPID.

```bash
ps                  # Processes associated with this terminal
ps aux              # Snapshot of processes (BSD-style options)
ps -ef              # Snapshot with PID and PPID (POSIX-style options)
pgrep -af python    # Find matching processes
jobs                # Jobs managed by current shell
sleep 120 &         # Start a job in background
fg %1               # Bring shell job 1 to foreground
```

`Ctrl+C` sends SIGINT to the foreground job; `Ctrl+Z` normally sends SIGTSTP, suspending it. `bg %1` resumes a suspended job in the background; `fg %1` resumes it in the foreground. A background process is not automatically protected from shell logout.

`kill PID` sends SIGTERM (15) by default, allowing the process to handle cleanup. `kill -9 PID` sends SIGKILL (9), which cannot be caught or handled and should be a last resort. `kill -STOP PID` suspends a process and `kill -CONT PID` resumes it. `pkill -f pattern` targets matching processes; use carefully.

`$?` is the exit status of the **most recently completed foreground command or pipeline**. By convention `0` indicates success; nonzero indicates failure or another condition. It is not a universal truth that every nonzero value means a program malfunction (e.g. `grep` returns 1 for no matches).

```bash
ls /tmp
printf 'Exit status: %s\n' "$?"
```

**Important:** Check `$?` immediately: any subsequent command replaces it. In Bash, pipeline status defaults to that of the last command; `set -o pipefail` changes this behavior.

## 8. Shell variables versus environment variables

A shell variable belongs to the current shell. An environment variable is exported and inherited by child processes. Child processes cannot ordinarily change their parent's environment.

```bash
project=bridge_design       # Shell variable; no spaces around =
printf '%s\n' "$project"
export PROJECT=bridge_design
printenv PROJECT
printenv | grep '^HOME='
echo "$HOME"
```

`env` lists environment variables (and can run commands with modified environments). `printenv` displays environment variables. `export NAME=value` exports a variable. `unset NAME` removes it from the current shell. `PATH` is the executable search path, `HOME` is the home directory, `PWD` is the current working directory, and `VIRTUAL_ENV` is commonly set by an activated Python virtual environment.

**Security:** Never put secrets in publicly shared terminal screenshots or commit `.env` files containing secrets to Git. Avoid printing secret-bearing environment variables into logs.

## 9. Guided practical lab: a Python project

Run the following in a safe practice directory:

```bash
mkdir -p ~/linux-lab/src ~/linux-lab/logs
cd ~/linux-lab
printf 'print("Hello Linux")\n' > src/main.py
pwd
find . -type f
ls -l src/main.py
chmod 640 src/main.py
python3 src/main.py > logs/run.log 2>&1
cat logs/run.log
wc -l logs/run.log
printf 'Exit code: %s\n' "$?"
```

**Think:** Why does `python3 src/main.py` work without execute permission on `main.py`? Because the Python interpreter is the executable; it opens the script as data. Direct execution (`./src/main.py`) needs executable permission, an appropriate shebang such as `#!/usr/bin/env python3`, and a usable interpreter.

## 10. Self-test questions

1. How do absolute and relative paths differ?
2. What is the difference between `chmod 755` and `chmod 644`?
3. Why is directory `x` permission important?
4. How do `find` and `grep` differ?
5. Why should `find -name '*.py'` quote its pattern?
6. What is the difference between `>` and `>>`?
7. Why might `sort names.txt | uniq -c` be more useful than `uniq -c names.txt`?
8. How do `Ctrl+C` and `Ctrl+Z` differ?
9. When is `kill -9` inappropriate?
10. What is the difference between a shell variable and an exported environment variable?
11. What happens to `$?` after another command runs?
12. Why can Python execute a non-executable `.py` file when invoked as `python3 file.py`?

## 11. Revision schedule and learning references

**First revision (20 minutes):** Navigation, file operations, ownership and permissions. **Second revision (20 minutes):** Find, grep, globbing, pipes, redirection and text processing. **Third revision (20 minutes):** Processes, job control, environment and exit codes. Finish each session by completing at least three commands without looking at the table.

**Recommended references:**

- Linux Journey — https://linuxjourney.com/
- The Linux Command Line by William Shotts — https://linuxcommand.org/tlcl.php
- GNU Coreutils manual — https://www.gnu.org/software/coreutils/manual/
- Bash Reference Manual — https://www.gnu.org/software/bash/manual/bash.html
- Linux man pages — https://man7.org/linux/man-pages/
- Explain Shell (community command explanation tool) — https://explainshell.com/

**Next topics:** SSH and key management; package managers; services with `systemctl` and logs with `journalctl`; Bash scripting; file descriptors; Python virtual environments; Git and Linux permissions; cron and systemd timers.
