"""
SQLite benchmark.

The goal of the benchmark is to test CFFI performance and going back and forth
between SQLite and Python a lot. Therefore the queries themselves are really
simple.
"""

import sqlite3
import math

from argparse import ArgumentParser
from cProfile import Profile
from pstats import Stats, SortKey


class AvgLength(object):

    def __init__(self):
        self.sum = 0
        self.count = 0

    def step(self, x):
        if x is not None:
            self.count += 1
            self.sum += len(x)

    def finalize(self):
        return self.sum / float(self.count)


def bench_sqlite():
    conn = sqlite3.connect(":memory:")
    conn.execute('create table cos (x, y, z);')
    for i in range(1):
        cos_i = math.cos(i)
        conn.execute('insert into cos values (?, ?, ?)',
                     [i, cos_i, str(i)])

    conn.create_function("cos", 1, math.cos)
    for x, cosx1, cosx2 in conn.execute("select x, cos(x), y from cos"):
        assert math.cos(x) == cosx1 == cosx2

    conn.create_aggregate("avglength", 1, AvgLength)
    cursor = conn.execute("select avglength(z) from cos;")
    cursor.fetchone()[0]
    conn.execute("delete from cos;")
    conn.close()
    
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
    bench_sqlite()
    profiler.disable()
    ps = Stats(profiler).sort_stats(SortKey.TIME)
    
    ps.print_stats(args.amount)
    ps.dump_stats("test.prof")

