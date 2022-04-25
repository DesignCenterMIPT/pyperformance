import sys
import subprocess

from argparse import ArgumentParser
from cProfile import Profile
from pstats import Stats, SortKey
from pyperformance.venv import get_venv_program


def get_hg_version(hg_bin):
    # Fast-path: use directly the Python module
    try:
        from mercurial.__version__ import version
        if isinstance(version, bytes):
            return version.decode('utf8')
        else:
            return version
    except ImportError:
        pass

    # Slow-path: run the "hg --version" command
    proc = subprocess.Popen([sys.executable, hg_bin, "--version"],
                            stdout=subprocess.PIPE,
                            universal_newlines=True)
    stdout = proc.communicate()[0]
    if proc.returncode:
        print("ERROR: Mercurial command failed!")
        sys.exit(proc.returncode)
    return stdout.splitlines()[0]


if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument("-b", "--builtins",
            action="store_false",
            help="option for cProfile.Profile() class")
    parser.add_argument("-a", "--amount", 
            type=int,
            default=20,
            help="number of cumbersome functions")
    args = parser.parse_args()
    
    profiler = Profile(builtins=args.builtins)
    profiler.enable()
    
    hg_bin = get_venv_program('hg')
    get_hg_version(hg_bin)

    command = [sys.executable, hg_bin, "help"]
    subprocces.run(command)

    profiler.disable()
    s = Stats(profiler).sort_stats(SortKey.TIME)
    
    ps.print_stats(args.amount)
    ps.dump_stats("test.prof")
