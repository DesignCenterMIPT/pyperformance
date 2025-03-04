
"""Test the performance of simple HTTP serving and client using the Tornado
framework.

A trivial "application" is generated which generates a number of chunks of
data as a HTTP response's body.
"""

import sys
import socket

from tornado.httpclient import AsyncHTTPClient
from tornado.httpserver import HTTPServer
from tornado.gen import coroutine
from tornado.ioloop import IOLoop
from tornado.netutil import bind_sockets
from tornado.web import RequestHandler, Application

from argparse import ArgumentParser
from cProfile import Profile
from pstats import Stats, SortKey


HOST = "127.0.0.1"
FAMILY = socket.AF_INET

CHUNK = b"Hello world\n" * 1000
NCHUNKS = 5

CONCURRENCY = 150


class MainHandler(RequestHandler):

    @coroutine
    def get(self):
        for i in range(NCHUNKS):
            self.write(CHUNK)
            yield self.flush()

    def compute_etag(self):
        # Overriden to avoid stressing hashlib in this benchmark
        return None


def make_application():
    return Application([
        (r"/", MainHandler),
    ])


def make_http_server(request_handler):
    server = HTTPServer(request_handler)
    sockets = bind_sockets(0, HOST, family=FAMILY)
    assert len(sockets) == 1
    server.add_sockets(sockets)
    sock = sockets[0]
    return server, sock


def bench_tornado():
    server, sock = make_http_server(make_application())
    host, port = sock.getsockname()
    url = "http://%s:%s/" % (host, port)
    namespace = {}

    @coroutine
    def run_client():
        client = AsyncHTTPClient()
        
        futures = [client.fetch(url) for j in range(CONCURRENCY)]
        for fut in futures:
            resp = yield fut
            buf = resp.buffer
            buf.seek(0, 2)
            assert buf.tell() == len(CHUNK) * NCHUNKS

        client.close()

    IOLoop.current().run_sync(run_client)
    server.stop()



if __name__ == "__main__":
    # 3.8 changed the default event loop to ProactorEventLoop which doesn't
    # implement everything required by tornado and breaks this benchmark.
    # Restore the old WindowsSelectorEventLoop default for now.
    # https://bugs.python.org/issue37373
    # https://github.com/python/pyperformance/issues/61
    # https://github.com/tornadoweb/tornado/pull/2686

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

    if sys.platform == 'win32' and sys.version_info[:2] >= (3, 8):
        import asyncio
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

    bench_tornado()
    profiler.disable()
    ps = Stats(profiler).sort_stats(args.sorting)
    
    ps.print_stats(args.amount)
    ps.dump_stats("test.prof")

