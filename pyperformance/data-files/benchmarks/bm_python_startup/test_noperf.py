"""
Benchmark Python startup.
"""
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
    parser.add_argument("-s", "--sorting", 
            type=str,
            choices=["tottime", "cumtime"],
            default="tottime",
            help="profile entries sotring order")
    parser.add_argument("--no-site",
            action="store_true")
    parser.add_argument("--exit",
            action="store_true")

    args = parser.parse_args()
    name = 'python_startup'
    
    profiler = Profile(builtins=args.builtins)
    profiler.enable()

    if args.no_site:
        name += "_no_site"
    if args.exit:
        name += "_exit"

    command = [sys.executable]
    if args.no_site:
        command.append("-S")
    if args.exit:
        command.extend(("-c", "import os; os._exit(0)"))
    else:
        command.extend(("-c", "pass"))

    subprocess.run(command)
    profiler.disable()
    profiler.dump_stats("test.prof")
    ps = Stats(profiler).sort_stats(args.sorting)
    
    ps.print_stats(args.amount)
    ps.dump_stats("test.prof")

