# !/usr/bin/env python
# encoding=utf-8
s1 = 'foofish.net'
s2 = 'vttalk'
s3 = 'welcome to %s and following %s' % (s1, s2)
print s3

# do it pythonic
s3 = 'welcome to {blog} and following {wechat}'.format(blog='foofish.net', wechat='vttalk')
print s3

# -------------------------------------

items = range(10)

odd_items = []
for i in items:
    if i % 2 != 0:
        odd_items.append(i)
copy_item = []
for i in items:
    copy_item.append(i)

print odd_items
print copy_item

print '-------------------'

# do it pythonic
sub_items = items[1:4]
print sub_items
odd_items = items[1::2]
print odd_items

copy_item = items[:]
print copy_item
