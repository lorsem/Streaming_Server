#!/usr/bin/env python3

import os
import sys
import shutil

def CreateIndex(RootDir):#!!!!!!STUB
    indexfile = open('index.html', 'w')
    indexfile.write('''
        <!DOCTYPE html>
        <html>
        <body>
        ''')
    for TheDirectory in os.listdir(RootDir): #for every file in directory
        if os.path.isdir(RootDir + '/' + TheDirectory): #if the 'file' is a directory
            if not TheDirectory.startswith('.'): #and the directory is not hidden
                if not os.path.isdir(spam for spam in os.listdir('')):                        #and there is no directory in the directory:
                    formatDir = TheDirectory.replace(' ', '%20')
                    formatDir = formatDir.replace('[', '%5B')
                    formatDir = formatDir.replace(']', '%5D')
                    #Is it ok <a href=".//*TheDirectory, etcetera..*
                    indexfile.write('''<a href="{0}">{1}</a>
                <br>'''.format('./' + TheDirectory + '/' + 'content.html', TheDirectory))
                else:
                    
                    CreateIndex()

def AddContentHtml():
    pass

def LayDownFiles(RootDir): #Works Recursively
    for name in os.listdir(RootDir):
        if not name.startswith('.') and not name.startswith('__'):
            if os.path.isfile(RootDir + '/' + name) and not os.path.isfile(RootDir + '/.IsLaid.chk'): #If it is a file and has not been laid yet
                #         ./test
                
                vidformat = name.split('.')
                vidformat = vidformat[len(vidformat)-1]
                if vidformat == 'html':
                    print('TheIF')
                    break
                print('\nFORMAT:', vidformat, '\n',  repr(vidformat),  '\n\n')
                newpath = RootDir + "/" + name[:-len(vidformat)-1]
                os.makedirs(newpath)
                open(newpath + '/.IsLaid.chk', 'w').close()
                print ('Working on {0}...'.format(name))
                open(newpath + '/' + 'video' + name[-1*len(vidformat) -1:] , 'a').close()
                try:
                    shutil.move(RootDir + '/' + name, newpath + '/' + 'video' + '.' + vidformat)
                except PermissionError:
                    print("PermissionError: file has been copied?") #If cannot move th file, shutil.move should copy it
                except Exception:
                    print('Unknown error')
            if os.path.isdir(RootDir + '/' + name):
                LayDownFiles(RootDir + '/' + name)



print('Starting to lay out files in current directory...')
LayDownFiles(os.getcwd())
print('DONE')
'''
AddContentHtml()

print('Creating indexes')
'''
    


print('Bye')


'''
  DoNotContinue = False
    for name in os.listdir(RootDir):
        if not name.startswith('.'):
            if not name.startswith('__'):
                if not os.path.isdir(name): #CHECK
                    if not os.path.isfile(RootDir + '/.IsLaid.chk'):
                        open(RootDir + '/.IsLaid.chk', 'w').write('Laid').close()
                        vidformat = name.split('.')
                        vidformat = vidformat[len(vidformat)-1]
                        newpath = RootDir + "/" + name[:-len(vidformat)-1]
                        os.makedirs(newpath)
                        print ('Working on {0}...'.format(name))
                        open(newpath + '/' + 'video' + name[-1*len(vidformat) -1:] , 'a').close()
                        try:
                            shutil.move(name, newpath + '/' + 'video' + '.' + vidformat)
                        except PermissionError:
                            print("PermissionError: file has been copied?") #If cannot move th file, shutil.move should copy it
                    if DoNotContinue: #if it is a directory
                        LayDownFiles(RootDir + '/' + name)
'''