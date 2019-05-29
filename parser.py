#!/usr/bin/env python3
#
# A script that queries the news.sql database to answer very specific
# questions.# This project will be submitted in partial fulfillment of the
# requirements for Udacity's Fullstack Web Developer Nanodegree program.
# Following that, it can be extended int a more general purpose log parser to
# be adapted to other databases.


import psycopg2


def top_three_articles():
    db = psycopg2.connect("dbname=news")
    c = db.cursor()
    query = """select a.title, count(l.path) as views
        from articles a, log l where l.path = '/article/' || a.slug
        and l.status = '200 OK'
        group by a.title
        order by views desc limit 3"""
    c.execute(query)
    results = c.fetchall()
    db.close()
    print("The Three Most Viewed Articles:")
    print('\n'.join(["{} -- {} views".format(key,value) for (key, value) in results]))

def top_authors():
    db = psycopg2.connect("dbname=news")
    c = db.cursor()
    query = """select auth.name, count(l.path) as views
        from articles art, log l, authors auth
        where l.path = '/article/' || art.slug
        and art.author = auth.id
        and l.status = '200 OK'
        group by auth.name
        order by views desc"""
    c.execute(query)
    print(c.fetchall())
    db.close()


def high_error_days():
    db = psycopg2.connect("dbname=news")
    c = db.cursor()
    # We can get a performance boost by searching for "404 NOT FOUND" string
    # literal instead of doing string matching because it happens that our
    # database only contains 404 and 200 statuses.
    # TODO: Create a list of errors to put in the query so it will work in a
    # real world scenario.

    query = """with t as (select DATE(time) as date, ROUND((count
        (case when
            status != '200 OK' then time
        end) / count(status)::float * 100)::numeric, 3) percent_error
        from log
        group by date)
        select * from t where percent_error > 1
        """
    c.execute(query)
    print(c.fetchall())
    db.close()


def write_out(filename, content):
    print("Not yet implemented.")


if __name__ == '__main__':
    top_three_articles()
    top_authors()
    high_error_days()
