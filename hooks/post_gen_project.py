#!/usr/bin/env python3
"""Post-generation hook: git init, optional remote, optional Quarto extensions."""
import os
import shutil
import subprocess
import sys

VAULT_DIR = os.getcwd()
GIT_REMOTE = "{{ cookiecutter.git_remote_url }}".strip()
INSTALL_QUARTO = "{{ cookiecutter.install_quarto_extensions }}".lower() == "yes"

QUARTO_EXTENSIONS = [
    "alexander-newton/custom-amsthm-environments",
    "alexander-newton/custom-equation-tags",
    "alexander-newton/econ-paper-template",
]


def run(cmd, check=False):
    return subprocess.run(cmd, cwd=VAULT_DIR, check=check)


def init_git():
    if not shutil.which("git"):
        print("[skip] git not found on PATH")
        return
    run(["git", "init", "-q", "-b", "master"])
    if GIT_REMOTE:
        run(["git", "remote", "add", "origin", GIT_REMOTE])
        print(f"[ok] git initialised with remote {GIT_REMOTE}")
    else:
        print("[ok] git initialised (no remote)")


def install_quarto_extensions():
    if not INSTALL_QUARTO:
        return
    if not shutil.which("quarto"):
        print("[skip] quarto not on PATH; install manually later with:")
        for ext in QUARTO_EXTENSIONS:
            print(f"       quarto add {ext}")
        return
    for ext in QUARTO_EXTENSIONS:
        print(f"[run] quarto add {ext}")
        result = run(["quarto", "add", ext, "--no-prompt"])
        if result.returncode != 0:
            print(f"[warn] failed to add {ext}")


def main():
    init_git()
    install_quarto_extensions()
    print(f"[done] vault ready at {VAULT_DIR}")


if __name__ == "__main__":
    main()
