"""
Iterate on commits of the asyncio Git repository using the Dulwich module.
"""

import os

import dulwich.repo

from argparse import ArgumentParser
from cProfile import Profile
from pstats import Stats, SortKey


def iter_all_commits(repo):
    # iterate on all changes on the Git repository
    for entry in repo.get_walker():
        pass


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
    
    repo_path = os.path.join(os.path.dirname(__file__), 'data', 'asyncio.git')
    repo = dulwich.repo.Repo(repo_path)
    head = repo.head()
    iter_all_commits(repo)
    repo.close()

    profiler.disable()
    profiler.dump_stats("test.prof")
    ps = Stats(profiler).sort_stats(SortKey.TIME)
    
    ps.print_stats(args.amount)
    ps.dump_stats("test.prof")
