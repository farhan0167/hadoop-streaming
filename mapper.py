#!/usr/bin/python2

import sys

# input comes from STDIN (stream data that goes to the program)
for line in sys.stdin:
    
    l = line.strip().split()
    
    for i in range(len(l)-1):
        if i==0:
            print "..., %s\t%d" %(l[i], 1)
        print "%s, %s\t%d" %(l[i],l[i+1],1)
    print "%s, ...\t%d" %(l[-1], 1)
