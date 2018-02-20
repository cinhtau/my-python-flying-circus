#!/usr/bin/python
import yaml


def read_inventory(file):
    try:
        stream = open(file, 'r')
        # use yaml library to load
        hosts = yaml.load(stream)
        return hosts
    except IOError:
        print("Can't read from ", file)