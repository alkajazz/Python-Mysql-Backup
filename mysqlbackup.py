#!/usr/bin/env python3

##################################################
#
#    
#
#
#
#
#
##################################################

import configparser
import os
#import DateTime

path = '/etc/mysqlpybackup/mypy.conf'
pathdir = '/etc/mysqlpybackup'
mkfile = '/etc/mysqlpybackup/mypy.conf'

#############################################
#Check to see if dir exists if not create it#
#############################################

def checkdir(path):
    ''' This function checks for the directory '''
    if os.path.exists(pathdir) == True:
        return True
    else:
    ''' And creates it if it doesn't exist'''
        os.makedirs(pathdir)
        return True

##################################################
#Check to see if Conf is created if not create it#
##################################################


def createfile(mkfile):
    '''
    This checks for your conf file
    '''
    if os.path.exists(mkfile) == True:
        return True
    else:
        '''
        If the first function returns false it gives the user prompts to configure the conf file
        '''
        if not (os.path.isfile(mkfile)):
            mkuser = input('What is your database user name? ')
            mkpass = input('What is your password? ')
            mkhost = input('what is your host? ')
            f = open(mkfile, 'w')
            f.write('#This is the config file for the script\n \n[Login]\n \nUsername = %s\n \nPassword= %s\n \nHost = %s' % (mkuser, mkpass, mkhost))
            f.close()
            print('Your conf file has been created')
            return True

###################
#Check Config File#
###################

def checkconfig(path):


def main():
    checkdir(path)
    createfile(mkfile)

if __name__ == '__main__':
    main()
