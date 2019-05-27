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
        from articles a, log l where l.path like '%' || a.slug
        and l.status = '200 OK'
        group by a.title
        order by views desc limit 3"""
    c.execute(query)
    print(c.fetchall())


def top_authors():
    print("Not yet implemented.")


def high_error_days():
    print("Not yet implemented.")


def write_out(filename, content):
    print("Not yet implemented.")


if __name__ == '__main__':
    top_three_articles()
    top_authors()
    high_error_days()
