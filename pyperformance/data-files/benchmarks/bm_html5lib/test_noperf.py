"""Wrapper script for testing the performance of the html5lib HTML 5 parser.

The input data is the spec document for HTML 5, written in HTML 5.
The spec was pulled from http://svn.whatwg.org/webapps/index.
"""
import io
import os.path

import html5lib

from argparse import ArgumentParser
from cProfile import Profile
from pstats import Stats, SortKey


__author__ = "collinwinter@google.com (Collin Winter)"


def bench_html5lib(html_file):
    html_file.seek(0)
    html5lib.parse(html_file)


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

    # Get all our IO over with early.
    filename = os.path.join(os.path.dirname(__file__),
                            "data", "w3_tr_html5.html")
    with open(filename, "rb") as fp:
        html_file = io.BytesIO(fp.read())

    bench_html5lib(html_file)
    
    profiler.disable()
    ps = Stats(profiler).sort_stats(args.sorting)
    
    ps.print_stats(args.amount)
    ps.dump_stats("test.prof")

