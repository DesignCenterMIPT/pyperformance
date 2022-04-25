"""Test the performance of the Django template system.

This will have Django generate a 150x150-cell HTML table.
"""

import pyperf

import django.conf
from django.template import Context, Template
from argparse import ArgumentParser
from cProfile import Profile
from pstats import Stats, SortKey


# 2016-10-10: Python 3.6 takes 380 ms
DEFAULT_SIZE = 100


def bench_django_template(size):
    template = Template("""<table>
{% for row in table %}
<tr>{% for col in row %}<td>{{ col|escape }}</td>{% endfor %}</tr>
{% endfor %}
</table>
    """)
    table = [range(size) for _ in range(size)]
    context = Context({"table": table})

    template.render(context)


def prepare_cmd(runner, cmd):
    cmd.append("--table-size=%s" % runner.args.table_size)


if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument("-b", "--builtins",
            action="store_false",
            help="option for cProfile.Profile() class")
    parser.add_argument("-a", "--amount", 
            type=int,
            default=20,
            help="number of cumbersome functions")
    parser.add_argument("--table-size",
                     type=int, default=DEFAULT_SIZE,
                     help="Size of the HTML table, height and width "
                          "(default: %s)" % DEFAULT_SIZE)
    args = parser.parse_args()
    profiler = Profile(builtins=args.builtins)
    profiler.enable()
    
    django.conf.settings.configure(TEMPLATES=[{
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
    }])
    django.setup()

    bench_django_template(args.table_size)
        
    profiler.disable()
    ps = Stats(profiler).sort_stats(SortKey.TIME)
    
    ps.print_stats(args.amount)
    ps.dump_stats("test.prof")

