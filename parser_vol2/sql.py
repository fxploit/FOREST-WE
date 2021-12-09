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
    query_execute(dbname, 'CREATE TABLE ArtMD(id INTEGER PRIMARY KEY AUTOINCREMENT, artname varchar, artpath varchar, artcopypath varchar, artcopytime datetime, artMtime datetime, artAtime datetime, artCtime datetime, artsize varchar, artsha1 varchar)')

    ## EventLog TABLE CREATE
    query_execute(dbname, 'CREATE TABLE Eventlog(id INTEGER PRIMARY KEY AUTOINCREMENT, RecordNumber int, EventRecordID int, TimeCreated datetime, EventID int, Level varchar, Provider varchar, Channel varchar, ProcessID int, Threadid int, Computer varchar, ChunkNumber int, UserID varchar, MapDescription varchar, UserName varchar, RemoteHost varchar, PayloadData1 varchar, PayloadData2 varchar, PayloadData3 varchar, PayloadData4 varchar, PayloadData5 varchar, PayloadData6 varchar, Executableinfo varchar, HiddenRecord varchar, SourceFile varchar, Keywords varchar, ExtraDataOffset varchar, Payload varchar)')
    
    ## Live_Netinfo TABLE CREATE
    query_execute(dbname, 'CREATE TABLE Live_Netinfo(id INTEGER PRIMARY KEY AUTOINCREMENT, Protocol varchar, LocalAddr varchar, ExternalAddr varchar, Status varchar, Pid int)')

    ## Prefetch TABLE CREATE
    query_execute(dbname, 'CREATE TABLE Prefetch ( id INTEGER PRIMARY KEY AUTOINCREMENT, PFfilename varchar, PEname varchar, RunCount int , LastExec1 datetime, LastExec2 datetime, LastExec3 datetime, LastExec4 datetime, LastExec5 datetime, LastExec6 datetime, LastExec7 datetime, LastExec8 datetime, VolumeInfo TEXT, Directories TEXT, Resources TEXT)')


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
    query_execute(dbname, 'INSERT INTO Eventlog(RecordNumber, EventRecordID, TimeCreated, EventID, Level, Provider, Channel, ProcessID, Threadid, Computer,\
                    ChunkNumber, UserID, MapDescription, UserName, RemoteHost, PayloadData1, PayloadData2, PayloadData3, PayloadData4, PayloadData5, PayloadData6, \
                        Executableinfo, HiddenRecord, SourceFile, Keywords, ExtraDataOffset, Payload) VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)', args)

def insert_prefetch(dbname, args):
    query_execute(dbname, 'INSERT INTO Prefetch(PFfilename, PEname, RunCount, LastExec1, LastExec2, LastExec3, LastExec4, LastExec5, LastExec6, LastExec7, LastExec8, VolumeInfo, Directories, Resources) VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?)', args)

'''
CREATE TABLE Prefetch ( id INTEGER PRIMARY KEY AUTOINCREMENT, PFfilename varchar, PEname varchar, RunCount int , LastExec1 datetime, LastExec2 datetime, 
LastExec3 datetime, LastExec4 datetime, LastExec5 datetime, LastExec6 datetime, LastExec7 datetime, LastExec8 datetime, VolumeInfo TEXT, Directories TEXT, Resources TEXT);
'''


'''SELECT'''

