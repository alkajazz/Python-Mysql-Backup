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

if not os.path.exists(pathdir): os.makedirs(pathdir)

##################################################
#Check to see if Conf is created if not create it#
##################################################

if not os.path.exists(mkfile):
    file(mkfile, 'w').close()
