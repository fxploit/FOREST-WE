import sql
from winreg import *
import os
import glob
import csv
from tqdm import tqdm

def collect_registry(key, hive, dbname):
    varReg = ConnectRegistry(None, hive)
    varKey = OpenKey(varReg, key, 0, KEY_ALL_ACCESS)
    count_subkey = QueryInfoKey(varKey)[1]

    buf=[]

    for i in range(count_subkey):
        n, v, t = EnumValue(varKey, i) # 지정한 레지스트리의 하위 키값 조회
        buf.append([n,v,t])

    CloseKey(varKey) # 핸들 객체 반환
    CloseKey(varReg)
    return buf

def collect_schedulers(dbname):
    try:
        for i in collect_registry(r"SOFTWARE\Microsoft\Windows\CurrentVersion\Run", HKEY_CURRENT_USER, dbname):
            sql.insert_Registry_Scheduler(dbname, i)
    except:
        pass
    try: 
        for i in collect_registry(r'SOFTWARE\Microsoft\Windows\CurrentVersion\Run', HKEY_LOCAL_MACHINE, dbname):
            sql.insert_Registry_Scheduler(dbname, i)
    except:
        pass
    try:
        for i in collect_registry(r'Software\Microsoft\Windows\CurrentVersion\RunOnce', HKEY_LOCAL_MACHINE, dbname):
            sql.insert_Registry_Scheduler(dbname, i)
    except:
        pass
    try:
        for i in collect_registry(r'Software\Microsoft\Windows\CurrentVersion\RunOnce', HKEY_CURRENT_USER, dbname):
            sql.insert_Registry_Scheduler(dbname, i)
    except:
        pass
    try:
        for i in collect_registry(r'Software\Microsoft\Windows\CurrentVersion\Explorer\StartupApproved\Run', HKEY_CURRENT_USER, dbname):
            sql.insert_Registry_Scheduler(dbname, i)
    except:
        pass
    try:
        for i in collect_registry(r'SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\StartupApproved\Run', HKEY_LOCAL_MACHINE, dbname):
            sql.insert_Registry_Scheduler(dbname, i)
    except:
        pass
    try:
        for i in collect_registry(r'SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\StartupApproved\Run32', HKEY_LOCAL_MACHINE, dbname):
            sql.insert_Registry_Scheduler(dbname, i)
    except:
        pass
    try:
        for i in collect_registry(r'SOFTWARE\WOW6432Node\Microsoft\Windows\CurrentVersion\Run', HKEY_LOCAL_MACHINE, dbname):
            sql.insert_Registry_Scheduler(dbname, i)
    except:
        pass
    try:
        for i in collect_registry(r'SOFTWARE\WOW6432Node\Microsoft\Windows\CurrentVersion\RunOnce', HKEY_LOCAL_MACHINE, dbname):
            sql.insert_Registry_Scheduler(dbname, i)
    except:
        pass

def collect_command(dbname):
    try:
        for i in collect_registry(r'Software\Classes\ms-settings\shell\open\command', HKEY_CURRENT_USER, dbname):
            print(i)
            sql.insert_Registry_Command(dbname, i)
    except:
        pass

    try:
        for i in collect_registry(r'Software\Classes\mscfile\shell\open\command', HKEY_CURRENT_USER, dbname):
            sql.insert_Registry_Command(dbname, i)
    except:
        pass

    try:
        for i in collect_registry(r'Software\Classes\AppX82a6gwre4fdg3bt635tn5ctqjf8msdd2\Shell\open\command', HKEY_CURRENT_USER, dbname):
            sql.insert_Registry_Command(dbname, i)
    except:
        pass


def collect_services(module_dst_path, dbname):
    paths=[]
    files=[]
    for root, dirs, files1 in os.walk(module_dst_path+'\\Registry'):
        paths.append(root)
        for path in paths:
            files += glob.glob(root+'\\*_Services*')
    
    files=set(files)

    for file in tqdm(files):
        with open(file, 'r', encoding='utf-8') as f:
            reader = csv.reader(f)
            for row in tqdm(reader):
                try:
                    sql.insert_Registry_Services(dbname, [row[i] for i in range(len(row))])
                except:
                    continue



def collect_Registry_RECmd(module_dst_path, dbname):
    paths=[]
    files=[]
    encoding_set = ['latin-1', 'utf-8', 'euc-kr']

    for root, dirs, files1 in os.walk(module_dst_path+'\\Registry'):
        paths.append(root)
        for path in paths:
            files += glob.glob(root+'\\*RECmd_Batch*')
    
    files = set(files)
    count = 0

    for file in files:
        for encode in encoding_set:
            try:
                with open(file, 'r', encoding=encode) as f:
                    reader = csv.reader(f)
                    for row in tqdm(reader):
                        try:
                            sql.insert_Registry_RECmd(dbname, [row[i] for i in range(len(row))])
                        except Exception as ex:
                            print(ex)
                            continue
            except:
                continue


def collect_registries(module_dst_path, dbname):
    collect_schedulers(dbname)
    collect_command(dbname)
    collect_services(module_dst_path, dbname)
    collect_Registry_RECmd(module_dst_path, dbname)
