#!/usr/bin/env python
"""
Pure-Python Implementation of the AES block-cipher.

Benchmark AES in CTR mode using the pyaes module.
"""

import pyaes

from argparse import ArgumentParser
from cProfile import Profile
from pstats import Stats, SortKey


# 23,000 bytes
CLEARTEXT = b"This is a test. What could possibly go wrong? " * 500

# 128-bit key (16 bytes)
KEY = b'\xa1\xf6%\x8c\x87}_\xcd\x89dHE8\xbf\xc9,'


def bench_pyaes():
    aes = pyaes.AESModeOfOperationCTR(KEY)
    ciphertext = aes.encrypt(CLEARTEXT)

    # need to reset IV for decryption
    aes = pyaes.AESModeOfOperationCTR(KEY)
    plaintext = aes.decrypt(ciphertext)

    # explicitly destroy the pyaes object
    aes = None

    if plaintext != CLEARTEXT:
        raise Exception("decrypt error!")


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
    
    bench_pyaes()

    profiler.disable()
    ps = Stats(profiler).sort_stats(SortKey.TIME)

    ps.print_stats(args.amount)
    ps.dump_stats("test.prof")
