# !/usr/bin/env python
# encoding=utf-8
import struct
import hashlib

print struct.pack('>I', 10240099)
print struct.unpack('>IH', '\xf0\xf0\xf0\xf0\x80\x80')

md5 = hashlib.md5()
md5.update('how to use md5 in python hashlib?')
print md5.hexdigest()

sha1 = hashlib.sha1()
sha1.update('how to use sha1 in python hashlib?')
print sha1.hexdigest()
