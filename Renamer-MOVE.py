#!/usr/bin/env python3

import os
import sys
import shutil

#os.makedirs(newpath)

currentpath = os.getcwd()

for name in os.listdir('.'):
    if not name.startswith('.'):
        if not name.startswith('__'):
            if not os.path.isdir(name): #CHECK
                #          ./test
                formato = name.split('.')
                formato = formato[len(formato)-1]
                newpath = currentpath + "/" + name[:-len(formato)-1]
                os.makedirs(newpath)
                print ('Elaborazione di {0}'.format(name))
                open(newpath + '/' + 'video' + name[-1*len(formato) -1:] , 'a').close()
                try:
                    shutil.move(name, newpath + '/' + 'video' + '.' + formato)
                except PermissionError:
                    print("Errore di permessi - file copiato non spostato(?)")
                    pass
                #os.remove(name)           



#currentpath + name[:-4] + '/' + 'video' + name[-4:] ) #+ name[-4:]


