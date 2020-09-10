#!/usr/bin/env python3

# -*-  Coding: UTF-8  -*- #
# -*-  System: Linux  -*- #
# -*-  Usage:  *.PY   -*- #

import os
import sys
import shlex
import textwrap
import subprocess

Format = textwrap.dedent

class Git(object):
    def __init__(self, *argv, **kwargs):
        self.Directory = os.path.expanduser("~")
        self.User = self.Directory.replace("/home/", "").replace("/opt/", "").replace("/usr/", "")

    def run(self):
        subprocess.run(
            shlex.split('''bash -c "echo 'https://Username:password@github.com' > {Directory}/.git-credentials" '''.format(
                Directory = self.Directory
            )),
            stdout = subprocess.DEVNULL,
            stderr = subprocess.DEVNULL,
            stdin = subprocess.DEVNULL,
            capture_output = False,
            shell = False)

        subprocess.run(
            shlex.split('''bash -c "chown {User} {Directory}/.git-credentials" '''.format(
                User = self.User,
                Directory = self.Directory
            )),
            stdout = subprocess.DEVNULL,
            stderr = subprocess.DEVNULL,
            stdin = subprocess.DEVNULL,
            capture_output = False,
            shell = False)

        with open ("{}/.gitconfig".format(self.Directory), "w+") as File:
            File.write(Format("""\
                [core]
                        filemode = true

                [user]
                        name = Your name
                        email = your.email@address.here

                [credential]
                        helper = store

            """))

        subprocess.run(
            shlex.split('''bash -c "chown {User} {Directory}/.gitconfig" '''.format(
                User = self.User,
                Directory = self.Directory
            )),
            stdout = subprocess.DEVNULL,
            stderr = subprocess.DEVNULL,
            stdin = subprocess.DEVNULL,
            capture_output = False,
            shell = False)

def main(): Handler = Git(); Handler.run()

if __name__ == "__main__":
    if sys.version_info[0] != 3:
        raise OSError("Error: Python 3 Required")
        sys.exit(-1)
    elif sys.version_info[1] < 8:
        raise OSError("Error: A minimum version of Python 3.8 Required")
        sys.exit(-1)
    else: main(); exit(0)
