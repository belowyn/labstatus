#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys, os, subprocess

usage = "usage: " + str(sys.argv[0]) + " <labmap> <lablist>"

def readfile(inmap, inlist):
    map = str(inmap.read())
    iplist = []
    for line in inlist:
        iplist.append(line.replace('\n', ''))
    leMagic(map, iplist)

def fping(iplist):
    
    up = []
    down = []

    sub = subprocess.Popen('fping', shell=False, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, close_fds=True)

    for ip in iplist:
        sub.stdin.write('%s\n' % ip)
    sub.stdin.close()

    for line in sub.stdout:
        if 'is alive' in line:
            up.append(line.split(' ')[0])
        elif 'is unreachable' in line:
            down.append(line.split(' ')[0])
            
    return up, down

def leMagic(map, iplist):

    up, down = fping(iplist)
    col = []

    for ip in iplist:
        if ip in up:
            col.append('\033[92m' + ip + '\033[0m')
        if ip in down:
            col.append('\033[91m' + ip + '\033[0m')

    print map.format(*col)

if __name__ == "__main__":
    if len(sys.argv) > 2:
        inmap = open(sys.argv[1], 'r')
        inlist = open(sys.argv[2], 'r')
    else:
        print usage; sys.exit(1)

    readfile(inmap, inlist)
