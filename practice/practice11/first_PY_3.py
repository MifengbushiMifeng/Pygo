# !/usr/bin/env python
# encoding=utf-8
import urllib
import functools

result = []
for i in range(10):
    s = i * 2
    result.append(s)

print result

# do it pythonic
print [i * 2 for i in xrange(10)]


# using a decorator in your code
def web_lookup(url, saved={}):
    if url in saved:
        return saved[url]
    page = urllib.urlopen(url).read()
    saved[url] = page
    return page


# do it pythonic by using decorator
def cache(func):
    saved = {}

    @functools.wraps(func)
    def wrapper(url):
        if url in saved:
            return saved[url]
        else:
            page = func(url)
            saved[url] = page
            return page

    return wrapper


@cache
def web_lookup_with_decorator(url):
    return urllib.urlopen(url).read()
