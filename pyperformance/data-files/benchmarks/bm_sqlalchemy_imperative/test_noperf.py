
from sqlalchemy import Column, ForeignKey, Integer, String, Table, MetaData
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

from argparse import ArgumentParser
from cProfile import Profile
from pstats import Stats, SortKey


metadata = MetaData()

Person = Table('person', metadata,
               Column('id', Integer, primary_key=True),
               Column('name', String(250), nullable=False))

Address = Table('address', metadata,
                Column('id', Integer, primary_key=True),
                Column('street_name', String(250)),
                Column('street_number', String(250)),
                Column('post_code', String(250), nullable=False),
                Column('person_id', Integer, ForeignKey('person.id')))

# Create an engine that stores data in the local directory's
# sqlalchemy_example.db file.
engine = create_engine('sqlite://')

# Create all tables in the engine. This is equivalent to "Create Table"
# statements in raw SQL.
metadata.create_all(engine)


# Bind the engine to the metadata of the Base class so that the
# declaratives can be accessed through a DBSession instance
metadata.bind = engine

DBSession = sessionmaker(bind=engine)
# A DBSession() instance establishes all conversations with the database
# and represents a "staging zone" for all the objects loaded into the
# database session object. Any change made against the objects in the
# session won't be persisted into the database until you call
# session.commit(). If you're not happy about the changes, you can
# revert all of them back to the last commit by calling
# session.rollback()
session = DBSession()


# add 'npeople' people to the database
def bench_sqlalchemy(npeople):
    # drop rows created by the previous benchmark
    cur = Person.delete()
    cur.execute()
    cur = Address.delete()
    cur.execute()

    # Run the benchmark once
    for i in range(npeople):
        # Insert a Person in the person table
        new_person = Person.insert()
        new_person.execute(name="name %i" % i)

        # Insert an Address in the address table
        new_address = Address.insert()
        new_address.execute(post_code='%05i' % i)

    # do 'npeople' queries per insert
    for i in range(npeople):
        cur = Person.select()
        cur.execute()


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
    parser.add_argument("--rows", 
            type=int,
            default=100,
            help="Number of rows (default: 100)")

    args = parser.parse_args()

    profiler = Profile(builtins=args.builtins)
    profiler.enable()

    bench_sqlalchemy(args.rows)
    profiler.disable()
    ps = Stats(profiler).sort_stats(args.sorting)
    
    ps.print_stats(args.amount)
    ps.dump_stats("test.prof")


