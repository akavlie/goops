# GOOPS
## a Google Product Search data feed generator

Google Product Search allows online retailers to submit a data feed of their
product catalogs. While it's possible to manually create a spreadsheet of
product information and upload to Google, this is not a scalable solution
for large and/or frequently updated product catalogs. Ideally the feeed should
be auto-generated directly from your database, and in turn auto-submitted to Google.

Automatic submission is easy enough -- Google Merchant Center allows you to
point to a data feed URL, which Google will check every 24 hours for updates.
But what about generating the feed? I couldn't find any good tools that take care
of that, so I decided to create one. That is what GOOPS does for you.


## Requirements

Python (2.4+?)
[SQLAlchemy](http://www.sqlalchemy.org/)
[Mako](http://www.makotemplates.org/)


## Usage

1. Dump the source code in a directory on a \*nix server that's accessible
   on the web.
1. Copy `config.py.sample` to `config.py` and fill in your database info.
   The current version assumes a MySQL database, though it could be easily
   modified to work with other DBs (see `connect.py`).
1. Fill in table, field and link names with values appropriate to your database\*.
1. Add a line to your crontab to generate the XML file on a daily basis.
   For example, to generate every day at 2:00 AM:
    00 2    * * *   python /path/to/goops/generate_xml.py
1. Point Google to the resulting XML feed.


\* I assigned variables in an attempt to make the model work across multiple
   database setups, but in hindsight this was a bit naive. SQL database structures
   will be diverse enough that the model will probably need significant modification
   to work for you. If you have some level of comfort working with SQLAlchemy
   (or are willing to learn), it may be of value to you.
   

