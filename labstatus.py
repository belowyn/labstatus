#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys, os, getopt, pickle

usage = "usage: " + str(sys.argv[0]) + " <labmap> <lablist>"

class bcolors:
    green = '\033[92m'
    red = '\033[91m'
    endC = '\033[0m'

    def disable(self):
        self.green = ''
        self.red = ''
        self.endC = ''

def readfile(inmap, inlist):
    map = str(inmap.read())
    iplist = []
    for line in inlist:
        iplist.append(line.replace('\n', ''))
    print map.format(*iplist)


if __name__ == "__main__":
    if len(sys.argv) > 2:
        inmap = open(sys.argv[1], 'r')
        inlist = open(sys.argv[2], 'r')
    else:
        print usage; sys.exit(1)

    readfile(inmap, inlist)
