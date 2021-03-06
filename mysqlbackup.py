#!/usr/bin/env python3

####################################################################
#  Simple python script that you can queue up in cron to mysqldump #
#  requires python config parser module                            #
#  i didn't do a dir check for /backups/mysql/ oops                #
####################################################################

import configparser
import os
import time
import getpass

path = '/etc/mysqlpybackup/mypy.conf'
pathdir = '/etc/mysqlpybackup'
mkfile = '/etc/mysqlpybackup/mypy.conf'
filestamp = time.strftime('%y-%m-%d')

###############################################
# Check to see if dir exists if not create it #
###############################################

def checkdir(path):
    if os.path.exists(pathdir) == True:
        return True
    else:
        os.makedirs(pathdir)
        return True

####################################################
# Check to see if Conf is created if not create it #
####################################################


def createfile(mkfile):
    if os.path.exists(mkfile) == True:
        return True
    else:
        if not (os.path.isfile(mkfile)):
            mkuser = input('What is your database user name? ')
            mkpass = getpass.getpass('What is your password? ')
            mkhost = input('what is your host? ')
            f = open(mkfile, 'w')
            f.write('#This is the config file for the script\n \n[Login]\n \nUsername = %s\n \nPassword = %s\n \nHost = %s' % (mkuser, mkpass, mkhost))
            f.close()
            print('Your conf file has been created')
            return True

#####################################
# Check Config and back up database # 
#####################################

def backupsql(path):
    config = configparser.ConfigParser()
    config.read(path)
    username = config.get('Login', 'Username')
    password = config.get('Login', 'Password')
    host = config.get('Login', 'Host')
    database_list_command = "mysql -u %s -p%s -h %s --silent -N -e 'show databases'" % (username, password, host)
    for database in os.popen(database_list_command).readlines():
        database = database.strip()
        if database == 'information_schema':
            continue
        if database == 'performance_schema':
            continue
        filename = "/backups/mysql/%s-%s.sql" % (database, filestamp)
        os.popen("mysqldump -u %s -p%s -h %s -e --opt -c %s | gzip -c > %s.gz" % (username, password, host, database, filename))

####################
# main function yo #
####################


def main():
    if checkdir(path) == True and createfile(mkfile) == True:
        backupsql(path)

if __name__ == '__main__':
    main()
