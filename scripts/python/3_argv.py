#!/usr/bin/python

import sys,getopt

print "Argument Count:", len(sys.argv)
print "Arguments:", sys.argv
print "\n"

opts, args = getopt.getopt(sys.argv[1:],"hi:o:",["ifile=","ofile="])
#hi:o:
#h for help, i for inputfile but requires a filename because of :, o for outputfile requiring a filename

for opt,arg in opts:
    if opt=='-h':
        print "usage:",sys.argv[0],"-i <inputfile> -o <outputfile>"
    elif opt=='-i':
        print "input file",arg
    elif opt=='-o':
        print "output file",arg
    else:
        print "wrong option"
