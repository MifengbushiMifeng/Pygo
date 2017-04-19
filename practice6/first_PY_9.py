# !/usr/bin/env python
# encoding=utf-8
"""practice metaclass in python"""
___author___ = 'Jonathan Zhou'


# store the column name and column type of the database
class Field(object):
    def __init__(self, name, column_type):
        self.name = name
        self.column_type = column_type

    def __str__(self):
        return '<%s:%s>' % (self.__class__.__name__, self.name)


class StringField(Field):
    def __int__(self, name):
        super(StringField, self).__init__(name, 'varchar(100)')


class IntergerField(Field):
    def __init__(self, name):
        super(IntergerField, self).__init__(name, 'bigint')


# design the meta-class
class ModelMetaclass(type):
    def __new__(cls, name, bases, attrs):
        if name == 'Model':
            return type.__new__(cls, name, bases, attrs)
        mappings = dict()
        for k, v in attrs.iteritems():
            if isinstance(v, Field):
                print 'Found mapping: %s==>%s' % (k, v)
                mappings[k] = v
        for k in mappings.iterkeys():
            attrs.pop(k)
        attrs['__table__'] = name
        attrs['__mappings__'] = mappings
        return type.__new__(cls, name, bases, attrs)


class Model(dict):
    pass


class User(Model):
    pass
