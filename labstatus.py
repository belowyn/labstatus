#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys, os, subprocess, time

rooms = ["sb-1-1", "sb-1-2", "sb-2-gruppe", "sb-2-sal", "hw", "nt-10", "gm"]

def loop():
    countLoop = 0

    while 1:
        countLoop += 1
        for lab in rooms:
            os.system('clear')
            print "%s:\n" % lab.upper()
            startTime = time.time()
            readfile(lab)
            timeLoop = time.time() - startTime
            print "Script time: %.4f sec.\nLooped: %d\n" % (timeLoop, countLoop)
            time.sleep(10)

def readfile(lab):
    inmap = open(lab + '-map.txt', 'r')
    inlist = open(lab + '-hosts.txt', 'r')
    map = str(inmap.read())
    iplist = []

    for line in inlist:
        iplist.append(line.replace('\n', ''))
    
    inmap.close()
    inlist.close()
    leMagic(map, iplist)

def fping(iplist):
    
    up = []
    down = []

    iplist.insert(0, 'fping')

    sub = subprocess.Popen(iplist, shell=False, stdout=subprocess.PIPE, stderr=subprocess.PIPE, close_fds=True).communicate()[0]
    
    sub = sub.split('\n')

    for line in sub:
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
    loop()
