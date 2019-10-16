#!/usr/bin/python3
from elem import Elem
from pprint import pprint


class Head(Elem):
    def __init__(self, tag='head', attr={}, content=None, tag_type='double'):
        super().__init__(self, tag, attr, content);

if __name__ == '__main__':
    hd = Head();
    pprint(hd)
