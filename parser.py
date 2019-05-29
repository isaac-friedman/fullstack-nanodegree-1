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
    # The following list comprehension is PEP8 compliant see
    # https://bit.ly/2o9NIZk
    print('\n'.join(["\t{} -- {} views".format(key, value) for (key, value) in results]))


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
    results = c.fetchall()
    db.close()
    print("\n\nOur authors in order of total views:")
    # The following list comprehension is PEP8 compliant see
    # https://bit.ly/2o9NIZk
    print('\n'.join(["\t{} -- {} views".format(key, value) for (key, value) in results]))


def high_error_days():
    db = psycopg2.connect("dbname=news")
    c = db.cursor()
    query = """with t as (select DATE(time) as date, ROUND((count
        (case when
            status != '200 OK' then time
        end) / count(status)::float * 100)::numeric, 3) percent_error
        from log
        group by date)
        select * from t where percent_error > 1
        """
    c.execute(query)
    results = c.fetchall()
    db.close()
    print("\n\nDays where more than 1% of requests resulted in errors:")
    # The following list comprehension is PEP8 compliant see
    # https://bit.ly/2o9NIZk
    print('\n'.join(["\t{} -- {}% errors".format(key, value) for (key, value) in results]))


if __name__ == '__main__':
    top_three_articles()
    top_authors()
    high_error_days()
