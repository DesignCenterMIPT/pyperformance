import glob
import os.path
import sys
import subprocess

from argparse import ArgumentParser
from cProfile import Profile
from pstats import Stats, SortKey


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

    datadir = os.path.join(os.path.dirname(__file__), 'data', '2to3')
    pyfiles = glob.glob(os.path.join(datadir, '*.py.txt'))

    command = [sys.executable, "-m", "lib2to3", "-f", "all"] + pyfiles
    subprocess.run(command, capture_output=True)  
        
    profiler.disable()
    ps = Stats(profiler).sort_stats(SortKey.TIME)
    
    ps.print_stats(args.amount)
    ps.dump_stats("test.prof")
