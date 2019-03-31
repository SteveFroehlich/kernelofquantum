#!/usr/bin/python

import os
import subprocess


def hidden(file):
    return file.startswith(".")


def to_uri(path):
    uri = ""
    for i in range(1, len(path)):
        uri += path[i] + "/"
    return uri


def install(package):
    cmd = ["pip", "install"]
    cmd.extend(package)
    subprocess.run(cmd)


def find_packages():
    # traverse root directory, and list directories as dirs and files as files
    packages = []
    for root, dirs, files in os.walk("."):
        path = root.split(os.sep)
        # search for the setup.py file that defines packages
        for file in files:
            if file == "setup.py":
                setup_path = to_uri(path)
                print(setup_path)
                packages.append(setup_path)
    return packages


def enforce_reqs(packages):
    # assume requirements is in the working dir
    num_packages = len(packages)
    num_packs_in_requirments = get_num_lines("requirements.txt")
    assert num_packages == num_packs_in_requirments


def get_num_lines(file):
    non_blank_count = 0
    with open(file) as infp:
        for line in infp:
           if line.strip():
              non_blank_count += 1
    return non_blank_count


ORIGIN_PATH = "."  # working dir


def main():
    packages = find_packages()
    # install(packages)
    enforce_reqs(packages)
    print("\nSUCCESS:\ncount of setup.py files matches count of non blank lines in requirements.txt\n")


if __name__== "__main__":
    main()
