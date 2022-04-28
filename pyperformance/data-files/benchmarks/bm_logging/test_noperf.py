"""
Script for testing the performance of logging simple messages.

Rationale for logging_silent by Antoine Pitrou:

"The performance of silent logging calls is actually important for all
applications which have debug() calls in their critical paths.  This is
quite common in network and/or distributed programming where you want to
allow logging many events for diagnosis of unexpected runtime issues
(because many unexpected conditions can appear), but with those logs
disabled by default for performance and readability reasons."

https://mail.python.org/pipermail/speed/2017-May/000576.html
"""

# Python imports
import io
import logging

# Third party imports
from argparse import ArgumentParser
from cProfile import Profile
from pstats import Stats, SortKey


# A simple format for parametered logging
FORMAT = 'important: %s'
MESSAGE = 'some important information to be logged'


def truncate_stream(stream):
    stream.seek(0)
    stream.truncate()


def bench_silent(loops, logger, stream):
    truncate_stream(stream)

    # micro-optimization: use fast local variables
    m = MESSAGE
    range_it = range(loops)
    t0 = pyperf.perf_counter()

    for _ in range_it:
        # repeat 10 times
        logger.debug(m)
        logger.debug(m)
        logger.debug(m)
        logger.debug(m)
        logger.debug(m)
        logger.debug(m)
        logger.debug(m)
        logger.debug(m)
        logger.debug(m)
        logger.debug(m)

    dt = pyperf.perf_counter() - t0

    if len(stream.getvalue()) != 0:
        raise ValueError("stream is expected to be empty")

    return dt


def bench_simple_output(loops, logger, stream):
    truncate_stream(stream)

    # micro-optimization: use fast local variables
    m = MESSAGE
    range_it = range(loops)
    t0 = pyperf.perf_counter()

    for _ in range_it:
        # repeat 10 times
        logger.warning(m)
        logger.warning(m)
        logger.warning(m)
        logger.warning(m)
        logger.warning(m)
        logger.warning(m)
        logger.warning(m)
        logger.warning(m)
        logger.warning(m)
        logger.warning(m)

    dt = pyperf.perf_counter() - t0

    lines = stream.getvalue().splitlines()
    if len(lines) != loops * 10:
        raise ValueError("wrong number of lines")

    return dt


def bench_formatted_output(logger, stream):
    truncate_stream(stream)

    # micro-optimization: use fast local variables
    fmt = FORMAT
    msg = MESSAGE

    logger.warning(fmt, msg)
    logger.warning(fmt, msg)
    logger.warning(fmt, msg)
    logger.warning(fmt, msg)
    logger.warning(fmt, msg)
    logger.warning(fmt, msg)
    logger.warning(fmt, msg)
    logger.warning(fmt, msg)
    logger.warning(fmt, msg)
    logger.warning(fmt, msg)

    lines = stream.getvalue().splitlines()
   

BENCHMARKS = {
    "silent": bench_silent,
    "simple": bench_simple_output,
    "format": bench_formatted_output,
}


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
    parser.add_argument("benchmark", 
            nargs='?',
            choices=sorted(BENCHMARKS))

    options = parser.parse_args()
    
    profiler = Profile(builtins=options.builtins)
    profiler.enable()

    # NOTE: StringIO performance will impact the results...
    stream = io.StringIO()

    handler = logging.StreamHandler(stream=stream)
    logger = logging.getLogger("benchlogger")
    logger.propagate = False
    logger.addHandler(handler)
    logger.setLevel(logging.WARNING)

    if options.benchmark:
        benchmarks = (options.benchmark)
    else:
        benchmarks = sorted(BENCHMARKS)

    for bench in benchmarks:
        name = 'logging_%s' % bench
        bench_func = BENCHMARKS[bench]
        bench_formatted_output(logger, stream)
    
    profiler.disable()
    ps = Stats(profiler).sort_stats(options.sorting)
    
    ps.print_stats(options.amount)
    ps.dump_stats("test.prof")


