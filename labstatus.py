#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys, os, subprocess, time

rooms = ["sb-1-1", "sb-1-2", "sb-2-gruppe", "sb-2-sal", "hw", "ikos", "nt-3", "nt-8", "nt-10", "gm", "imk-bachelor", "imk-master", "zeb", "b11"]

labDown = "-"

def loop():
    countLoop = 0

    while 1:
        countLoop += 1
        for lab in rooms:
            readfile(lab, countLoop)
            time.sleep(10)

def readfile(lab, countLoop):
    inmap = open(lab + '-map.txt', 'r')
    inlist = open(lab + '-hosts.txt', 'r')
    map = str(inmap.read())
    iplist = []

    for line in inlist:
        iplist.append(line.replace('\n', ''))

    inmap.close()
    inlist.close()
    leMagic(map, iplist, lab, countLoop)

def fping(iplist):

    iplist.insert(0, 'fping')
    iplist.insert(1, '-u')
    iplist.insert(2, '-t')
    iplist.insert(3, '251')
    iplist.insert(4, '-r')
    iplist.insert(5, '1')

    sub = subprocess.Popen(iplist, shell=False, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, close_fds=True).communicate()[0].split('\n')

    del iplist[0]
    del iplist[0]
    del iplist[0]
    del iplist[0]
    del iplist[0]
    del iplist[0]

    return sub

def leMagic(map, iplist, lab, countLoop):
    global labDown

    startTime = time.time()
    down = fping(iplist)
    col = []

    if down[0] == '':
        if lab == labDown or labDown == "-":
            labDown = "-"
            os.system('clear')
            print ("Keep calm and just relax, everything is working!")
        return

    labDown = lab

    os.system('clear')
    print ("%s:\n") % lab.upper()

    for ip in iplist:
        if ip in down:
            col.append('\033[91m' + ip + '\033[0m')
        else:
            col.append('\033[92m' + ip + '\033[0m')

    print (map.format(*col))

    timeLoop = time.time() - startTime
    print ("Script time: %.4f sec.\nLooped: %d\n") % (timeLoop, countLoop)

if __name__ == "__main__":
    os.system('clear')
    loop()
