#!/usr/bin/env python3

import os
import sys
import shutil


currentpath = os.getcwd()

for name in os.listdir('.'):
    if not name.startswith('.'):
        if not name.startswith('__'):
            if not os.path.isdir(name): #CHECK
                #         ./test
                vidformat = name.split('.')
                vidformat = vidformat[len(vidformat)-1]
                newpath = currentpath + "/" + name[:-len(vidformat)-1]
                os.makedirs(newpath)
                print ('Working on {0}...'.format(name))
                open(newpath + '/' + 'video' + name[-1*len(vidformat) -1:] , 'a').close()
                try:
                    shutil.move(name, newpath + '/' + 'video' + '.' + vidformat)
                except PermissionError:
                    print("PermissionError: file has been copied?") #If cannot move th file, shutil.move should copy it



