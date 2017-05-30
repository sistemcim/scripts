#!/usr/bin/python

import sys,getopt
import os

def newFile(filename):
#    print "\nNew file"
    file=open(filename,"w")
    file.close()
    print "Done.\n"
    
def writeToFile(filename,fileContent):
#    print "\nWrite to file"
    file=open(filename,"a+")
#    file.seek(0,0)
    for line in fileContent:
        file.write(line)
    file.close()
    print "Done.\n"

def readFromFile(filename):
#    print "\nRead from file"
    i=0
    with open(filename,"r") as file:
        for line in file:
            i +=1
            print "Line ",i,"=> ",line.rstrip('\n')
    print "Done.\n"

def deleteFile(filename):
    os.remove(filename)
    print "Done.\n"
    
defaultFileContent=["This file content will be written to test file.\n",
    "The procedure is automatic and functions are used.\n",
    "Further, command line parameters can be used.\n"]

def printHelpMenu():
    print "File Operations Test Program"
    print "-n/--new-file for new file"
    print "-w/--write-file to write to file"
    print "-r/--read-file to read file"
    print "-d/--delete-file to delete file"
    print "\n",sys.argv[0],"-n test1"

if len(sys.argv) > 1:
    opts,args = getopt.getopt(sys.argv[1:],"hn:w:r:d:",["help","new-file=","write-file=","read-file=","delete-file="])
    for opt,arg in opts:
        if opt in ("-h","--help"):
            printHelpMenu()
        elif opt in("-n","--new-file"):
            newFile(arg)
        elif opt in("-w","--write-file"):
            
            print "Insert file content and press q.\nor\nsimple press q. for default content."
            newFileContent = []
            while True:
                line = sys.stdin.readline().rstrip('\n')
                if line == 'q.':
                    break
                newFileContent.append(line+"\n")     

            if len(newFileContent)!=0:
                defaultFileContent=newFileContent
            writeToFile(arg,defaultFileContent)

        elif opt in("-r","--read-file"):
            readFromFile(arg)
            
        elif opt in("-d","--delete-file"):
            deleteFile(arg)
else:
#    command="python " + sys.argv[0] + " -h"
#    os.system(command)
    printHelpMenu()
    
