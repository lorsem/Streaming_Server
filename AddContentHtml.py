#!/usr/bin/env python3


import os

currentpath = os.getcwd()
for name in os.listdir('.'):
    if not name.startswith('.'):
        if not name.startswith('__'):
            if os.path.isdir(name):
                vidfile = os.listdir(currentpath + '/' + name)[0] #ugly but easy
                vidformat = vidfile.split('.')[-1]
               
                htmltipe = 'video/' + vidformat
                contenuto = open(currentpath + '/' + name + '/' + 'content.html' , 'w')
                contenuto.write(
                '''
                <!DOCTYPE html>
                <html>
                <body>
                <center>File: {0}</center>
                <br>
                <video width="1920" height="1080" controls autoplay>
                  <source src="{1}" type="{2}">
                </video>
                
                </body>
                </html>
                '''.format(name, 'video.' + vidformat, htmltipe)                       
                )
                
