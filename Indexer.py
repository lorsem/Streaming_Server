#!/usr/bin/env python3

import os
import sys
import shutil

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

for cartella in os.listdir('.'):
    if os.path.isdir(currentpath + '/' + cartella):
        if not os.path.isfile(currentpath + '/' + cartella + '/indexed.dat'):
            if not cartella.startswith('.'):
                formatcartella = cartella.replace(' ', '%20')
                formatcartella = formatcartella.replace('[', '%5B')
                formatcartella = formatcartella.replace(']', '%5D')
                indexfile.write('''<a href="{0}">{1}</a>
            <br>'''.format('http://192.168.1.150/video/' + cartella + '/' + 'content.html', cartella))


indexfile.write('''
                </body>
                </html>
                ''')
indexfile.close()

        
'''
        <!DOCTYPE html>
        <html>
        <body>
        <a href="{0}">{1}</a>
        <br>
        
        </body>
        </html>
'''.format('http://192.168.1.150/video/' + cartella + '/' + 'content.html', cartella)

