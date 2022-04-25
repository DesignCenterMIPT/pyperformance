import functools


from chameleon import PageTemplate
from argparse import ArgumentParser
from cProfile import Profile
from pstats import Stats, SortKey


BIGTABLE_ZPT = """\
<table xmlns="http://www.w3.org/1999/xhtml"
xmlns:tal="http://xml.zope.org/namespaces/tal">
<tr tal:repeat="row python: options['table']">
<td tal:repeat="c python: row.values()">
<span tal:define="d python: c + 1"
tal:attributes="class python: 'column-' + str(d)"
tal:content="python: d" />
</td>
</tr>
</table>"""


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
    
    tmpl = PageTemplate(BIGTABLE_ZPT)
    table = [dict(a=1, b=2, c=3, d=4, e=5, f=6, g=7, h=8, i=9, j=10)
        for x in range(500)]
    options = {'table': table}

    func = functools.partial(tmpl, options=options)
    func()

    profiler.disable()
    ps = Stats(profiler).sort_stats(SortKey.TIME)

    ps.print_stats(args.amount)
    ps.dump_stats("test.prof")
