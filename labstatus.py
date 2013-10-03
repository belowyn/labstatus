#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys, os, subprocess

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
    #fping(iplist)
    leMagic(map, iplist)
    #print map.format(*iplist)

def fping(iplist):
    
    up = []
    down = []

    sub = subprocess.Popen('fping', shell=False, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, close_fds=True)

    for ip in iplist:
        sub.stdin.write('%s\n' % ip)
    sub.stdin.close()

        #for ip, res in sub.stdout:
        #    if 'is alive' in res:
        #        print bcolors.green + ip + bcolors.endC
        #    elif 'is unreachable' in res:
        #        print bcolors.red + ip + bcolors.endC
    for line in sub.stdout:
        if 'is alive' in line:
            #print bcolors.green + line + bcolors.endC
            up.append(line.split(' ')[0])
        elif 'is unreachable' in line:
            #print bcolors.red + line + bcolors.endC
            down.append(line.split(' ')[0])
            
    return up, down

def leMagic(map, iplist):

    up, down = fping(iplist)


    #print up
    #print down
    col = []

    for ip in iplist:
        if ip in up:
            col.append('\033[92m' + ip + '\033[0m')
        if ip in down:
            col.append('\033[91m' + ip + '\033[0m')

    #for bajs in col:
    #    print bajs
    #print iplist
    print map.format(*col)

if __name__ == "__main__":
    if len(sys.argv) > 2:
        inmap = open(sys.argv[1], 'r')
        inlist = open(sys.argv[2], 'r')
    else:
        print usage; sys.exit(1)

    readfile(inmap, inlist)
