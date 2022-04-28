"""Microbenchmark for Python's sequence unpacking."""


from argparse import ArgumentParser
from cProfile import Profile
from pstats import Stats, SortKey


def do_unpacking(loops, to_unpack):
    range_it = range(loops)

    for _ in range_it:
        # 400 unpackings
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack

    

def bench_tuple_unpacking(loops):
    x = tuple(range(10))
    return do_unpacking(loops, x)


def bench_list_unpacking(loops):
    x = list(range(10))

    return do_unpacking(loops, x)


def bench_all(loops):
    bench_tuple_unpacking(loops)
    bench_list_unpacking(loops)
    


if __name__ == "__main__":
    benchmarks = {"tuple": bench_tuple_unpacking,
                  "list": bench_list_unpacking}

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
    parser.add_argument("benchmark",
            nargs="?",
            choices=sorted(benchmarks))
    
    options = parser.parse_args()
    name = 'unpack_sequence'
    profiler = Profile(builtins=options.builtins)
    profiler.enable()

    if options.benchmark:
        func = benchmarks[options.benchmark]
        name += "_%s" % options.benchmark
    else:
        func = bench_all

    func(loops=400)
    ps = Stats(profiler).sort_stats(options.sorting)
    
    ps.print_stats(options.amount)
    ps.dump_stats("test.prof")

