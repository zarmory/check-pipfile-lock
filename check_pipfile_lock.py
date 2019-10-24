#!/usr/bin/env python

import os
from pathlib import Path
from typing import List, Optional

import click
import clickclick as cc
from pipenv.project import Project


@click.command("check-pipfile-lock")
@click.argument("pipfile_locks", metavar="PATH-TO-PIPFILE-LOCK", type=click.Path(exists=True), nargs=-1, required=False)
def main(pipfile_locks: List[str]):
    """
    Check whether specified Pipfile.lock file(s) are up to date with their Pipfile(s).
    If no Pipfile.lock paths are provided, the current directory is assumed.
    """
    if not pipfile_locks:
        pipfile_locks = [Path(os.getcwd()) / "Pipfile.lock"]

    for pipfile_lock in pipfile_locks:
        pipfile_dir: Path = Path(pipfile_lock).parent
        if not check_dir(pipfile_dir):
            cc.fatal_error(f"{pipfile_lock} is out of date. Consider running 'pipenv lock' or 'pipenv install'")


def check_dir(dir_path: Optional[Path] = None) -> bool:
    """
    Check whether specified directory container a valid and
    up-to-date Pipfile.lock. Lack of Pipfile.lock is considered
    as success.
    """
    cur_path: Path = os.getcwd()

    try:
        if dir_path:
            os.chdir(dir_path)

        project = Project()
        if not project.lockfile_exists:
            return

        old_hash = project.get_lockfile_hash()
        new_hash = project.calculate_pipfile_hash()
        return old_hash == new_hash
    finally:
        os.chdir(cur_path)


if __name__ == "__main__":
    main()
