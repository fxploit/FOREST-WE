import sqlite3
import socket
import os
import platform
from datetime import datetime
import psutil
import time

# execute query
def query_execute(dbname, query, args=None):
    conn = sqlite3.connect(dbname)
    if args != None:
        conn.execute(query,args)
    else:
        conn.execute(query)
    conn.commit()
    conn.close()


def query_execute_ret(dbname, query, args=None):
    conn = sqlite3.connect(dbname)
    cur = conn.cursor()

    if args != None:
        cur.execute(query, args)
    else:
        cur.execute(query)

    conn.commit()

    columns = cur.fetchall()


    cur.close()
    conn.close()

    return columns


'''CREATE'''

def create_table(dbname):

    ## PCinfo TABLE CREATE
    query_execute(dbname, 'CREATE TABLE PCinfo (id INTEGER PRIMARY KEY AUTOINCREMENT, hostname varchar, account varchar, OSversion varchar, OSbit varchar, OSbootime datetime, Runtime datetime, Timezone varchar)')

    ## Proinfo TABLE CREATE
    query_execute(dbname, 'CREATE TABLE Proinfo (id INTEGER PRIMARY KEY AUTOINCREMENT, PSname varchar, PSpid int, PSppid int, PSthds int, PShnds int, PStime varchar)')
    
    ## Netinfo TABLE CREATE
    query_execute(dbname, 'CREATE TABLE Netinfo (id INTEGER PRIMARY KEY AUTOINCREMENT, netcard varchar, ipv4 varchar, macaddr varchar)')

    ## SWcheck TABLE CREATE
    query_execute(dbname, 'CREATE TABLE SWcheck (id INTEGER PRIMARY KEY AUTOINCREMENT, swname varchar, swversion varchar, swinstalldate varchar, swpublisher varchar)')

    ## ArtMD TABLE CREATE
    query_execute(dbname, 'CREATE TABLE ArtMD(id INTEGER PRIMARY KEY AUTOINCREMENT, artname varchar, artpath varchar, artcopypath varchar, artcopytime datetime, artMtime datetime,\
         artAtime datetime, artCtime datetime, artsize varchar, artsha1 varchar)')

    ## EventLog TABLE CREATE
    query_execute(dbname, 'CREATE TABLE Eventlog(id INTEGER PRIMARY KEY AUTOINCREMENT, art_key int, RecordNumber int, EventRecordID int, TimeCreated datetime, EventID int, Level varchar,\
         Provider varchar, Channel varchar, ProcessID int, Threadid int, Computer varchar, ChunkNumber int, UserID varchar, MapDescription varchar, UserName varchar, RemoteHost varchar, PayloadData1 varchar, PayloadData2 varchar, PayloadData3 varchar, PayloadData4 varchar, PayloadData5 varchar, PayloadData6 varchar, Executableinfo varchar, HiddenRecord varchar, SourceFile varchar, Keywords varchar, ExtraDataOffset varchar, Payload varchar)')
    
    ## Live_Netinfo TABLE CREATE
    query_execute(dbname, 'CREATE TABLE Live_Netinfo(id INTEGER PRIMARY KEY AUTOINCREMENT, Protocol varchar, LocalAddr varchar, ExternalAddr varchar, Status varchar, Pid int)')

    ## Prefetch TABLE CREATE
    query_execute(dbname, 'CREATE TABLE Prefetch (id INTEGER PRIMARY KEY AUTOINCREMENT, art_key int, PFfilename varchar, PEname varchar, RunCount int , LastExec1 datetime, LastExec2 datetime,\
         LastExec3 datetime, LastExec4 datetime, LastExec5 datetime, LastExec6 datetime, LastExec7 datetime, LastExec8 datetime, VolumeInfo TEXT, Directories TEXT, Resources TEXT)')

    ## $MFT TABLE CREATE
    query_execute(dbname, 'CREATE TABLE MFT (id INTEGER PRIMARY KEY AUTOINCREMENT, EntryNumber int, SequenceNumber int, InUse varchar, ParentEntryNumber int, ParentSequenceNumber int,\
         ParentPath varchar, FileName varchar, Extension varchar, FileSize int, ReferenceCount int, ReparseTarget varchar, IsDirectory Boolean, HasAds Boolean, IsAds Boolean,\
              SI_FN Boolean, uSecZeros Boolean, Copied Boolean, SiFlags varchar, NameType varchar, Created0x10 datetime, Created0x30 datetime, LastModified0x10 datetime,\
                   LastModified0x30 datetime, LastRecordChange0x10 datetime, LastRecordChange0x30 datetime, LastAccess0x10 datetime, LastAccess0x30 datetime, UpdateSequenceNumber int,\
                        LogfileSequenceNumber int, SecurityId int, ObjectIdFileDroid varchar, LoggedUtilStream varchar, ZoneIdContents varchar)')

    query_execute(dbname, 'CREATE TABLE LogFile (id INTEGER PRIMARY KEY AUTOINCREMENT, LSN int, EventTime datetime, Event varchar, Detail varchar, FileDirectory_Name varchar,\
         Full_Path varchar, Create_Time datetime, Modified_Time datetime, MFT_modified_Time datetime, Access_Time datetime, Redo varchar, Target_VCN blob, Cluster_Index int)')


    query_execute(dbname, 'CREATE TABLE UsnJrnl (id INTEGER PRIMARY KEY AUTOINCREMENT, TimeStamp datetime, USN int, FileDirectory varchar, FullPath varchar, EventInfo varchar,\
         SourceInfo varchar, FileAttribute varchar, Carving_Flag varchar, FileReferenceNumber varchar, ParentFileReferenceNumber varchar)')
    

    query_execute(dbname, 'CREATE TABLE Registry_Scheduler (id INTEGER PRIMARY KEY AUTOINCREMENT, art_key int, ExecFile varchar, FilePath varchar, Type int)')


    # UAC Bypass (fodhelper, etc..)
    query_execute(dbname, 'CREATE TABLE Registry_Command (id INTEGER PRIMARY KEY AUTOINCREMENT, art_key int, ExecFile varchar, FilePath varchar, Type int)')

    #Group -> 키워드라 _Group으로 대체
    query_execute(dbname, 'CREATE TABLE Registry_Services (id INTEGER PRIMARY KEY AUTOINCREMENT, art_key int, Name varchar, BatchKeyPath varchar, Description varchar, BatchValueName varchar,\
         DisplayName varchar, StartMode varchar, ServiceType varchar, NameKeyLastWrite datetime, ParametersKeyLastWrite datetime, _Group varchar, ImagePath varchar, ServiceDLL varchar,\
              RequiredPrivileges varchar)')

    
    query_execute(dbname, 'CREATE TABLE Registry_RECmd (id INTEGER PRIMARY KEY AUTOINCREMENT, art_key int, HivePath varchar, HiveType varchar, Description varchar, Category varchar,\
         KeyPath varchar, ValueName varchar, ValueType varchar, ValueData varchar, ValueData2 varchar, ValueData3 varchar, Comment varchar, Recursive varchar, Deleted varchar,\
              LastWriteTimeStamp datetime, PluginDetailFile varchar)')
    
    query_execute(dbname, 'CREATE TABLE Prefetch_list (id INTEGER PRIMARY KEY AUTOINCREMENT, art_key int, FileName varchar, RunCount int, RunTime datetime)')

    query_execute(dbname, 'CREATE TABLE Chain_art (chain_number int, id int, art_key int, description varchar, time datetime)')

'''INSERT'''

# inserting host-related data into db
def insert_hostinfo(dbname):
    query_execute(dbname, 'INSERT INTO PCinfo(hostname, account, OSversion, OSbit, OSbootime, Runtime, Timezone) VALUES(?, ?, ?, ? ,? ,? ,?)', [str(socket.gethostname()), str(os.getlogin()), str(platform.version()), str(platform.architecture()[0]), datetime.fromtimestamp(psutil.boot_time()), datetime.now(), time.tzname[0]])


# inserting swinfo-related data into db
def insert_swinfo(dbname, args):
    query_execute(dbname, 'INSERT INTO SWcheck(swname, swversion, swpublisher, swinstalldate) VALUES (?, ?, ?, ?)', args)

def insert_proinfo(dbname, args):
    query_execute(dbname, 'INSERT INTO Proinfo(PSname, PSpid, PSppid, PSthds, PShnds, PStime) VALUES(?, ?, ?, ?, ?, ?)', args)

def insert_netinfo(dbname, args):
    query_execute(dbname, 'INSERT INTO Netinfo(netcard, ipv4, macaddr) VALUES (?, ?, ?)', args)

def insert_live_netinfo(dbname, args):
    query_execute(dbname, 'INSERT INTO Live_Netinfo(Protocol, LocalAddr, ExternalAddr, Status, Pid) VALUES(?,?,?,?,?)', args)

def insert_eventlog(dbname, args):
    query_execute(dbname, 'INSERT INTO Eventlog(art_key, RecordNumber, EventRecordID, TimeCreated, EventID, Level, Provider, Channel, ProcessID, Threadid, Computer,\
                    ChunkNumber, UserID, MapDescription, UserName, RemoteHost, PayloadData1, PayloadData2, PayloadData3, PayloadData4, PayloadData5, PayloadData6, \
                        Executableinfo, HiddenRecord, SourceFile, Keywords, ExtraDataOffset, Payload) VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)', [1]+args)

def insert_prefetch(dbname, args1, args2, args3):
    query_execute(dbname, 'INSERT INTO Prefetch(art_key, PFfilename, PEname, RunCount, LastExec1, LastExec2, LastExec3, LastExec4, LastExec5, LastExec6, LastExec7, LastExec8, VolumeInfo,\
         Directories, Resources) VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)', [3] + args1 + args2 + args3)
    
    for arg in args2:
        if arg != 0:
            query_execute(dbname, 'INSERT INTO Prefetch_list(art_key, FileName, RunCount, RunTime) VALUES (?,?,?,?)', [3]+[args1[0]]+[args1[2]]+[arg])


def insert_ArtMD(dbname, args):
    query_execute(dbname, 'INSERT INTO ArtMD(artname, artpath, artcopypath, artcopytime, artMtime, artAtime, artCtime, artsize, artsha1) VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?)', args)


#SI<FN 이 오류터져서 <를 _로 변경 SI<FN -> SI_FN
def insert_MFT(dbname, args):
    query_execute(dbname, 'INSERT INTO MFT(EntryNumber, SequenceNumber, InUse, ParentEntryNumber, ParentSequenceNumber, ParentPath, FileName, Extension, FileSize, ReferenceCount,\
         ReparseTarget, IsDirectory, HasAds, IsAds, SI_FN, uSecZeros, Copied, SiFlags, NameType, Created0x10, Created0x30, LastModified0x10, LastModified0x30, LastRecordChange0x10,\
              LastRecordChange0x30, LastAccess0x10, LastAccess0x30, UpdateSequenceNumber, LogfileSequenceNumber, SecurityId, ObjectIdFileDroid, LoggedUtilStream, ZoneIdContents)\
                   VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)', args)


def insert_LogFile(dbname, args):
    query_execute(dbname, 'INSERT INTO LogFile(LSN, EventTime, Event, Detail, FileDirectory_Name, Full_Path, Create_Time, Modified_Time, MFT_modified_Time, Access_Time, Redo,\
         Target_VCN, Cluster_Index) VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?)', args)


def insert_UsnJrnl(dbname, args):
    query_execute(dbname, 'INSERT INTO UsnJrnl (TimeStamp, USN, FileDirectory, FullPath, EventInfo, SourceInfo, FileAttribute, Carving_Flag, FileReferenceNumber,\
         ParentFileReferenceNumber) VALUES(?,?,?,?,?,?,?,?,?,?)', args)

def insert_Registry_Scheduler(dbname, args):
    query_execute(dbname, 'INSERT INTO Registry_Scheduler (art_key, ExecFile, FilePath, Type) VALUES(?,?,?,?)', [2] + args)

def insert_Registry_Command(dbname, args):
    query_execute(dbname, 'INSERT INTO Registry_Command (art_key, ExecFile, FilePath, Type) VALUES(?,?,?,?)', [2] + args)

def insert_Registry_Services(dbname, args):
    query_execute(dbname, 'INSERT INTO Registry_Services (art_key, Name, BatchKeyPath, Description, BatchValueName, DisplayName, StartMode, ServiceType, NameKeyLastWrite, ParametersKeyLastWrite, _Group, ImagePath,\
         ServiceDLL, RequiredPrivileges) VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?)', [2] + args)


def insert_Registry_RECmd(dbname, args):
    query_execute(dbname, 'INSERT INTO Registry_RECmd (art_key, HivePath, HiveType, Description, Category, KeyPath, ValueName, ValueType, ValueData, ValueData2, ValueData3, Comment,\
         Recursive, Deleted, LastWriteTimeStamp, PluginDetailFile) VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)', [2] + args)


def insert_chain_art(dbname, args):
    query_execute(dbname, 'INSERT INTO Chain_art (chain_number, id, art_key, description, time) VALUES(?,?,?,?,?)', args)


'''SELECT'''


def select_chain_start(dbname, basetime=None):
    # 여기다가 chain의 시작이라고 볼 수 있는 행위 event id set 추가 ex) defender, WER, POWERSHELL
    eventid_set = [1000,1001,4104,4105,4106,1000,1001,1002] # WER, POWERSHELL, DEFENDER Event ID
    process_set = [] # 여기다가 우리가 조사할 시작 프로세스들 추가 ex) MS OFFICE, CHROME, EDGE, etc...
    query = ''
    if basetime == None:
        #첫 실행. 즉 겹치는 시간이 존재하지 않음
        #Prefetch 에서 뽑아오기
        
        if process_set:
            query += 'SELECT id, art_key, FileName, RunTime FROM Prefetch_list'
            query += ' WHERE'
            for MalExec in process_set:
                query += ' Prefetch_list.FileName LIKE "%{}%" or'.format(str(MalExec))
            
            query = query[0:-3]
        
        # EventLog에서 뽑아오기
        if process_set:
            query += ' UNION SELECT id, art_key, Provider, TimeCreated FROM EventLog'
        else:
            query += 'SELECT id, art_key, Provider, TimeCreated FROM EventLog'

        if eventid_set:
            query += '  WHERE'
            for eventid in eventid_set:
                query += ' EventLog.EventID='+str(eventid)+' or'
            query = query[0:-3]

    else:
        # 두 번째 이후부터의 실행. 체인을 중복생성하지 않게 하기 위함.
        # prefetch 에서 뽑아오기
        if process_set:
            query += 'SELECT id, art_key, FileName, RunTime FROM Prefetch_list'
            query += ' WHERE'
            for MalExec in process_set:
                query += ' FileName LIKE "%{}%" and RunTime>"{}" or'.format(MalExec, basetime)
            query = query[0:-3]
                


        # EventLog에서 뽑아오기
        if eventid_set:
            if process_set:
                query += ' UNION SELECT id, art_key, Provider, TimeCreated FROM EventLog WHERE'
                for eventid in eventid_set:
                    query += ' EventLog.EventID={} and EventLog.TimeCreated>"{}" or'.format(eventid, basetime)
                query = query[0:-3]
            else:
                query += 'SELECT id, art_key, Provider, TimeCreated FROM EventLog WHERE EventLog.TimeCreated>"{}"'.format(basetime)

    query += ' ORDER BY TimeCreated LIMIT 1'


    return query_execute_ret(dbname, query)
    



def select_chain_end(dbname, start_time, end_time):
    eventid_set = []
    # eventid_set = [4698,4673,5158,4720,4624,4625,4648,4616,4670,1102,4624,4625,4663] # 여기다가 chain의 종료 행위라고 볼 수 있는 event id set 추가 ex) scheduler
    MalExec_set = [] # 여기다가 우리가 생각하는 악성행위에 사용한 프로그램명(프리패치에서 찾아볼 데이터) 추가
    # reg_desc_set = ['schedule', 'run', 'service', 'command']
    reg_desc_set = []

    # select_chain_start 에서 뽑아온 데이터 이후 시점에서의 데이터 조회. 찾는대로 반환
    # Prefetch 에서 뽑아오기
    query = ''
    
    query += 'SELECT id, art_key, FileName, RunTime FROM Prefetch_list WHERE Prefetch_list.RunCount=1 and Prefetch_list.RunTime>"{}" and Prefetch_list.RunTime<"{}"'.format(start_time, end_time)



    if MalExec_set:
        query += ' UNION SELECT id, art_key, FileName, RunTime FROM Prefetch_list WHERE'
        for MalExec in MalExec_set:
            query += ' Prefetch_list.FileName LIKE "%{}%" and Prefetch_list.RunTime>"{}" and Prefetch_list.RunTime<"{}" or'.format(MalExec, start_time, end_time)
            # query += ' Prefetch_list.FileName={} and Prefetch_list.RunTime>={} and Prefetch_list.RunTime<={} or'.format(MalExec, start_time, end_time)
        
        query = query[0:-3] # ' or' 제거


    # EventLog에서 뽑아오기
    if eventid_set:
        if MalExec_set:
            query += ' UNION SELECT id, art_key, EventID, TimeCreated FROM EventLog WHERE'
        else:
            query += 'SELECT id, art_key, EventID, TimeCreated FROM EventLog WHERE'
        for eventid in eventid_set:
            query += ' EventLog.EventID={} and EventLog.TimeCreated>"{}" and EventLog.TimeCreated<"{}" or'.format(eventid, start_time, end_time)

        query = query[0:-3]
    
    # Registry에서 뽑아오기
    if reg_desc_set:
        if MalExec_set or eventid_set:
            query += ' UNION SELECT id, art_key, Description, LastWriteTimeStamp FROM Registry_RECmd WHERE'
        else:
            query += 'SELECT id, art_key, Description, LastWriteTimeStamp FROM Registry_RECmd WHERE'
        for reg_desc in reg_desc_set:
            query += ' Registry_RECmd.Description LIKE "%{}%" and Registry_RECmd.LastWriteTimeStamp>"{}" and Registry_RECmd.LastWriteTimeStamp<"{}" or'.format(reg_desc, start_time, end_time)

        query = query[0:-3]

    query += ' ORDER BY EventLog.TimeCreated LIMIT 1'

    return query_execute_ret(dbname, query)


def select_eventlog(dbname, start_time, end_time, eventid_set=None):
    query = 'SELECT id, art_key, EventID, TimeCreated FROM EventLog'

    if eventid_set:
        query += ' WHERE'
        for eventid in eventid_set:
            query += ' EventID={} and TimeCreated>"{}" and TimeCreated<"{}" or'.format(eventid, start_time, end_time)
        query = query[0:-3]
    else:
        query += ' WHERE TimeCreated>="{}" and TimeCreated<"{}"'.format(start_time, end_time)
    return query_execute_ret(dbname, query)


def select_prefetch(dbname, start_time, end_time, proc_set=None):
    query = 'SELECT id, art_key, FileName, RunTime FROM Prefetch_list'

    if proc_set:
        query += ' WHERE'
        for proc in proc_set:
            query += ' FileName LIKE "%{}%" and RunTime<"{}" and RunTime>"{}" or'.format(proc, start_time, end_time)
        query = query[0:-3]
    else:
        query += ' WHERE RunTime<="{}" and RunTime>"{}"'.format(start_time, end_time)
    return query_execute_ret(dbname, query)


def select_reg_RECmd(dbname, start_time, end_time, reg_set=None):
    query = 'SELECT id, art_key, Description, LastWriteTimeStamp FROM Registry_RECmd'

    if reg_set:
        query += ' WHERE'
        for reg in reg_set:
            query += ' Description LIKE "%{}%" and LastWriteTimeStamp<"{}" and LastWriteTimeStamp>"{}" or'.format(reg, start_time, end_time)
        query = query[0:-3]
    else:
        query += ' WHERE LastWriteTimeStamp<"{}" and LastWriteTimeStamp>"{}"'.format(start_time, end_time)
    
    return query_execute_ret(dbname, query)


def select_reg_services(dbname, start_time, end_time, reg_set=None):
    query = 'SELECT id, art_key, Description, NameKeyLastWrite FROM Registry_Services'

    if reg_set:
        query += ' WHERE'
        for reg in reg_set:
            query += ' Description LIKE "%{}%" and NameKeyLastWrite<"{}" and NameKeyLastWrite>"{}" or'.format(reg, start_time, end_time)
        query = query[0:-3]
    else:
        query += ' WHERE NameKeyLastWrite<"{}" and NameKeyLastWrite>"{}"'.format(start_time, end_time)
    
    return query_execute_ret(dbname, query)


def select_chain_art(dbname, arg):
    query = 'SELECT * FROM chain_art WHERE chain_number={}'.format(arg)
    return query_execute_ret(dbname, query)