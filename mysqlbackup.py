#!/usr/bin/env python3

import configparser
import os
#import DateTime

path = '/etc/mysqlpybackup/mypy.conf'
pathdir = '/etc/mysqlpybackup'
mkfile = '/etc/fart/test'

#############################################
#Check to see if dir exists if not create it#
#############################################

def checkdir(path):
    if not os.path.exists(pathdir): os.makedirs(pathdir)

##################################################
#Check to see if Conf is created if not create it#
##################################################


def createfile(mkfile):
    if os.path.exists(mkfile) == True:
        print('file exists')
    else:
        if not (os.path.isfile(mkfile)):
            mkuser = input('What is your database user name? ')
            mkpass = input('What is your password? ')
            mkhost = input('what is your host? ')
            f = open(mkfile, 'w')
            f.write('#This is the config file for the script\n \n[Login]\n \nUsername = %s\n \nPassword= %s\n \nHost = %s' % (mkuser, mkpass, mkhost))
            f.close()



checkdir(path)
createfile(mkfile)
