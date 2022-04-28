from argparse import ArgumentParser
from cProfile import Profile
from pstats import Stats, SortKey

from sympy import expand, symbols, integrate, tan, summation
from sympy.core.cache import clear_cache


def bench_expand():
    x, y, z = symbols('x y z')
    expand((1 + x + y + z) ** 20)


def bench_integrate():
    x, y = symbols('x y')
    f = (1 / tan(x)) ** 10
    return integrate(f, x)


def bench_sum():
    x, i = symbols('x i')
    summation(x ** i / i, (i, 1, 400))


def bench_str():
    x, y, z = symbols('x y z')
    str(expand((x + 2 * y + 3 * z) ** 30))


def bench_sympy(funnc):
    for _ in range(1):
        # Don't benchmark clear_cache(), exclude it of the benchmark
        clear_cache()
        func()
        


BENCHMARKS = ("expand", "integrate", "sum", "str")


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
    parser.add_argument("benchmark", nargs='?',
                                  choices=BENCHMARKS)
    args = parser.parse_args()

    profiler = Profile(builtins=args.builtins)
    profiler.enable()
    
    import gc
    gc.disable()

    if args.benchmark:
        benchmarks = (args.benchmark,)
    else:
        benchmarks = BENCHMARKS

    for bench in benchmarks:
        name = 'sympy_%s' % bench
        func = globals()['bench_' + bench]
        bench_sympy(func)


    profiler.disable()
    ps = Stats(profiler).sort_stats(args.sorting)

    ps.print_stats(args.amount)
    ps.dump_stats("test.prof")

