import os
import platform
import socket
import psutil
import time
from datetime import datetime
import wmi
import winreg
import sql


# Create a database in dbpath.
def create_db(dbname):
    sql.create_table(dbname)


# if database does not exist, program is terminated.
def check_db(dbpath, dbname):
    # try:
    if os.path.isfile(dbpath):
        os.remove(dbpath)
    create_db(dbname)
    # except Exception as ex:
    #     print('db is open')
    #     print(ex)
    #     exit(0)

# Collects host basic information.
# timezone, os architecture, os build version, os, user etc..
def check_hostinfo(dbname):
    sql.insert_hostinfo(dbname)


def foo(hive, flag):
    aReg = winreg.ConnectRegistry(None, hive)
    aKey = winreg.OpenKey(aReg, r"SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall",
                          0, winreg.KEY_READ | flag)

    count_subkey = winreg.QueryInfoKey(aKey)[0]

    software_list = []

    for i in range(count_subkey):
        software = {}
        try:
            asubkey_name = winreg.EnumKey(aKey, i)
            asubkey = winreg.OpenKey(aKey, asubkey_name)
            software['name'] = winreg.QueryValueEx(asubkey, "DisplayName")[0]

            try:
                software['version'] = winreg.QueryValueEx(asubkey, "DisplayVersion")[0]
            except EnvironmentError:
                software['version'] = 'undefined'
            try:
                software['publisher'] = winreg.QueryValueEx(asubkey, "Publisher")[0]
            except EnvironmentError:
                software['publisher'] = 'undefined'
            try:
                software['installdate'] = winreg.QueryValueEx(asubkey, "InstallDate")[0]
            except EnvironmentError:
                software['installdate'] = 'undefined'
            software_list.append(software)
        except EnvironmentError:
            continue

    return software_list

# Registry collection related to the version of the executable file
def check_swinfo(dbname):
    software_list = foo(winreg.HKEY_LOCAL_MACHINE, winreg.KEY_WOW64_32KEY) + foo(winreg.HKEY_LOCAL_MACHINE, winreg.KEY_WOW64_64KEY) + foo(winreg.HKEY_CURRENT_USER, 0) + foo(winreg.HKEY_LOCAL_MACHINE, winreg.KEY_WOW64_64KEY)
    
    for software in software_list:
        sql.insert_swinfo(dbname, (software['name'], software['version'], software['publisher'], software['installdate']))


# Merge multiple functions into one
def setting(dbpath, dbname):
    try:
        check_db(dbpath, dbname)

        # check_hostinfo(dbname)
        # check_swinfo(dbname)

    except Exception as ex:
        print("[!]Exception occured!! : " + str(ex))
        return