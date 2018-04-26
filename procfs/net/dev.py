#!/usr/bin/env python
# -*- encoding=utf8 -*-

'''
FileName:   dev.py
Author:     Fasion Chan
@contact:   fasionchan@gmail.com
@version:   $Id$

Description:

Changelog:

'''

import os

from collections import (
    OrderedDict,
)


def fetch():
    path = '/proc/net/dev'

    if not os.path.exists(path):
        return

    lines = open(path).readlines()

    categories = [
        c.strip()
        for c in lines[0].split('|')[-2:]
    ]

    field_groups = [
        fns.split()
        for fns in lines[1].split('|')[-2:]
    ]

    devices = OrderedDict()
    for line in lines[2:]:
        iface, values = line.split(':')

        iface = iface.strip()
        values = [
            int(value)
            for value in values.split()
        ]

        device = OrderedDict()
        for category, fields in zip(categories, field_groups):
            device[category] = OrderedDict(zip(fields, values))
            values = values[len(fields):]

        devices[iface] = device

    return devices
