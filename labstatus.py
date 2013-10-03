#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys, os, getopt

usage = "usage: " + str(sys.argv[0]) + " <labmap>"

class bcolors:
    green = '\033[92m'
    red = '\033[91m'
    endC = '\033[0m'

    def disable(self):
        self.green = ''
        self.red = ''
        self.endC = ''

def readfile(infile):
    print infile.read()


if __name__ == "__main__":
    if len(sys.argv) > 1:
        infile = open(sys.argv[1], 'r')
    else:
        print usage; sys.exit(1)

    readfile(infile)
