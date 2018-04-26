#!/usr/bin/env python
# -*- encoding=utf8 -*-

'''
FileName:   partitions.py
Author:     Fasion Chan
@contact:   fasionchan@gmail.com
@version:   $Id$

Description:

Changelog:

'''

from collections import (
    OrderedDict,
)


def fetch():
    path = '/proc/partitions'

    lines = open(path).readlines()

    fields = lines[0].split()

    partitions = OrderedDict()

    for line in lines[1:]:
        values = line.split()
        if not values:
            continue

        name = values[-1]
        values = map(int, values[:-1]) + [name]

        partitions[name] = OrderedDict(zip(fields, values))

    return partitions
