"""
Test the performance of pathlib operations.

This benchmark stresses the creation of small objects, globbing, and system
calls.
"""

# Python imports
import os
import pathlib
import shutil
import tempfile

from argparse import ArgumentParser
from cProfile import Profile
from pstats import Stats, SortKey


NUM_FILES = 2000


def generate_filenames(tmp_path, num_files):
    i = 0
    while num_files:
        for ext in [".py", ".txt", ".tar.gz", ""]:
            i += 1
            yield os.path.join(tmp_path, str(i) + ext)
            num_files -= 1


def setup(num_files):
    tmp_path = tempfile.mkdtemp()
    for fn in generate_filenames(tmp_path, num_files):
        with open(fn, "wb") as f:
            f.write(b'benchmark')

    return tmp_path


def bench_pathlib(tmp_path):
    base_path = pathlib.Path(tmp_path)

    # Warm up the filesystem cache and keep some objects in memory.
    path_objects = list(base_path.iterdir())
    # FIXME: does this code really cache anything?
    for p in path_objects:
        p.stat()
    assert len(path_objects) == NUM_FILES, len(path_objects)

    
    # Do something simple with each path.
    for p in base_path.iterdir():
        p.stat()
    for p in base_path.glob("*.py"):
        p.stat()
    for p in base_path.iterdir():
        p.stat()
    for p in base_path.glob("*.py"):
        p.stat()

    
if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument("-b", "--builtins",
            action="store_false",
            help="option for cProfile.Profile() class")
    parser.add_argument("-a", "--amount",
            type=int,
            default=20,
            help="number of cumbersome functions")
    parser.add_argument("-s", "--sorting", 
            type=str,
            choices=["tottime", "cumtime"],
            default="tottime",
            help="profile entries sotring order")
    args = parser.parse_args()

    profiler = Profile(builtins=args.builtins)
    profiler.enable()
    
    tmp_path = setup(NUM_FILES)
    try:
        bench_pathlib(tmp_path)
    finally:
        shutil.rmtree(tmp_path)
    
    ps = Stats(profiler).sort_stats(args.sorting)

    ps.print_stats(args.amount)
    ps.dump_stats("test.prof")

