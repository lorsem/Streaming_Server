#!/usr/bin/env python3

import os
import sys
import shutil


#unused
def IsIndexed(path):
    for name in os.listdir(path):
        if name == 'indexed.dat':
            return True
        
    return False

currentpath = os.getcwd()
indexfile = open('index.html', 'w')
indexfile.write('''
        <!DOCTYPE html>
        <html>
        <body>
        ''')

for TheDirectory in os.listdir('.'):
    if os.path.isdir(currentpath + '/' + TheDirectory):
        if not os.path.isfile(currentpath + '/' + TheDirectory + '/indexed.dat'):
            if not TheDirectory.startswith('.'):
                formatcartella = TheDirectory.replace(' ', '%20')
                formatcartella = formatcartella.replace('[', '%5B')
                formatcartella = formatcartella.replace(']', '%5D')
                
                #Is it ok <a href="./video/*TheDirectory, etcetera..*
                indexfile.write('''<a href="{0}">{1}</a>
            <br>'''.format('http://192.168.1.150/video/' + TheDirectory+ 'content.html', TheDirectory))


indexfile.write('''
                </body>
                </html>
                ''')
indexfile.close()

## END

#Stub structure:
        
'''
        <!DOCTYPE html>
        <html>
        <body>
        <a href="{0}">{1}</a>
        <br>
        
        </body>
        </html>
'''.format('http://192.168.1.150/video/' + TheDirectory+ 'content.html', TheDirectory)

