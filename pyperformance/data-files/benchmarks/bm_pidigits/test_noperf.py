# coding: utf-8
"""
Calculating some of the digits of π.

This benchmark stresses big integer arithmetic.

Adapted from code on:
http://benchmarksgame.alioth.debian.org/
"""

import itertools

from argparse import ArgumentParser
from cProfile import Profile
from pstats import Stats, SortKey


DEFAULT_DIGITS = 2000
icount = itertools.count
islice = itertools.islice


def gen_x():
    return map(lambda k: (k, 4 * k + 2, 0, 2 * k + 1), icount(1))


def compose(a, b):
    aq, ar, as_, at = a
    bq, br, bs, bt = b
    return (aq * bq,
            aq * br + ar * bt,
            as_ * bq + at * bs,
            as_ * br + at * bt)


def extract(z, j):
    q, r, s, t = z
    return (q * j + r) // (s * j + t)


def gen_pi_digits():
    z = (1, 0, 0, 1)
    x = gen_x()
    while 1:
        y = extract(z, 3)
        while y != extract(z, 4):
            z = compose(z, next(x))
            y = extract(z, 3)
        z = compose((10, -10 * y, 0, 1), z)
        yield y


def calc_ndigits(n):
    return list(islice(gen_pi_digits(), n))


def add_cmdline_args(cmd, args):
    cmd.extend(("--digits", str(args.digits)))


if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument("-b", "--builtins",
            action="store_false",
            help="option for cProfile.Profile() class")
    parser.add_argument("-a", "--amount",
            type=int,
            default=20,
            help="number of cumbersome functions")
    parser.add_argument("--digits", 
            type=int,
            default=DEFAULT_DIGITS,
            help="Number of computed pi digits (default: %s)"
                          % DEFAULT_DIGITS)
    args = parser.parse_args()

    profiler = Profile(builtins=args.builtins)
    profiler.enable()

    calc_ndigits(args.digits)
    profiler.disable()
    ps = Stats(profiler).sort_stats(SortKey.TIME)

    ps.print_stats(args.amount)
    ps.dump_stats("test.prof")


