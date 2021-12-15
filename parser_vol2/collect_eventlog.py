import os
import csv
import sql


# Put the eventlog values ​​obtained through KAPE into the database
def collect_eventlogs(module_dst_path, dbname):
    # if not os.path.isdir(module_dst_path + '\\EventLogs\\'):
    #     os.mkdir(module_dst_path + '\\EventLogs\\')

    event_set = {
        # 여기다가 dictionary 형태로 Provider + event ID 추가
        'Application Error' : 1000,
        'Windows Error Reporting' : 1001,
        'Microsoft Windows Security Auditing' : 4720,
        'Microsoft Windows Security Auditing' : 4724,
        'Microsoft Windows Security Auditing' : 4726,
        'Microsoft Windows Security Auditing' : 4731,
        'Microsoft Windows Security Auditing' : 4732,
        'Microsoft Windows Security Auditing' : 4733,
        'Microsoft Windows Security Auditing' : 4734,
        'Microsoft Windows Security Auditing' : 4735,
        'Microsoft Windows Security Auditing' : 4738,
        'Microsoft Windows Security Auditing' : 4756,
        'Microsoft Windows Security Auditing' : 4625,
        'Microsoft Windows Security Auditing' : 4624,
        'Microsoft Windows Security Auditing' : 4625,
        'Microsoft Windows Security Auditing' : 4648,
        'Microsoft Windows Security Auditing' : 4634,
        'Microsoft Windows Security Auditing' : 4616,
        'Microsoft Windows Security Auditing' : 4670,
        'Microsoft Windows Eventlog' : 1100,
        'Microsoft Windows Eventlog' : 1102,
        'Microsoft Windows Terminal Services RemoteConnectionManager' : 1149,
        'Microsoft Windows Security Auditing' : 4624,
        'Microsoft Windows Security Auditing' : 4625,
        'Microsoft Windows Security Auditing' : 4634,
        'Microsoft Windows TerminalServices Licensing' : 21,
        'Microsoft Windows TerminalServices Licensing' : 22,
        'Microsoft Windows TerminalServices Licensing' : 23,
        'Microsoft Windows TerminalServices Licensing' : 24,
        'Microsoft Windows TerminalServices Licensing' : 25,
        'Microsoft Windows TerminalServices Licensing' : 39,
        'Microsoft Windows TerminalServices Licensing' : 40,
        'Microsoft Windows TerminalServices RemoteConnectionManager' : 261,
        'Microsoft Windows TerminalServices Gateway' : 400,
        'Security' : 600,
        'Microsoft Windows PowerShell' : 4104,
        'Microsoft Windows PowerShell' : 4105,
        'Microsoft Windows PowerShell' : 4106,
        'Microsoft Windows Security Auditing' : 4663,
        'Microsoft Windows Security Auditing' : 4670,
        'Microsoft Windows Security Auditing' : 4673,
        'Microsoft Windows Security Auditing' : 4688,
        'Security' : 4703,
        'Microsoft Windows PowerShell' : 8193,
        'Microsoft Windows PowerShell' : 8194,
        'Microsoft Windows PowerShell' : 8195,
        'Microsoft Windows PowerShell' : 8196,
        'Microsoft Windows PowerShell' : 8197,
        'Microsoft Windows PowerShell' : 12039,
        'Microsoft Windows PowerShell' : 40961,
        'Microsoft Windows PowerShell' : 53506,
        'Microsoft Windows PowerShell' : 40962,
        'Microsoft Windows PowerShell' : 53504,
        'Microsoft Office 16 Alerts' : 300,
        'Microsoft Windows Security Auditing' : 4673,
        'Microsoft Windows Security Auditing' : 4720,
        'Microsoft Windows Security Auditing' : 4624,
        'Microsoft Windows Security Auditing' : 4625,
        'Microsoft Windows Security Auditing' : 4648,
        'Microsoft Windows Security Auditing' : 4616,
        'Microsoft Windows Security Auditing' : 4670,
        'Microsoft Windows Eventlog' : 1102,
        'Microsoft Windows Security Auditing' : 4624,
        'Microsoft Windows Security Auditing' : 4625,
        'Microsoft Windows Security Auditing' : 4663,
        'Microsoft-Windows-Windows Defender' : 1000,
        'Microsoft-Windows-Windows Defender' : 1001,
        'Microsoft-Windows-Windows Defender' : 1002
        }
    
    if not os.path.isdir(os.path.join(module_dst_path, 'EvnetLogs')):
        os.mkdir(os.path.join(module_dst_path, 'EvnetLogs'))

    files = os.listdir(os.path.join(module_dst_path, 'EvnetLogs'))


    for file in files:
        if os.path.isfile(os.path.join(module_dst_path, 'EvnetLogs') + file):
            with open(os.path.join(module_dst_path, 'EvnetLogs') + file, 'r', encoding='utf-8') as f:
                reader = csv.reader(f)
                for row in reader:
                    try:
                        for key, val in event_set.items():
                            if row[5].replace('-', ' ')==key.replace('-', ' ') and row[3]==str(val):
                                sql.insert_eventlog(dbname, [row[i] for i in range(len(row))])
                    except:
                        continue


# Eventlog table schema

'''
CREATE TABLE Eventlog(i+d INTEGER PRIMARY KEY AUTOINCREMENT, RecordNumber int, EventRecordID int, TimeCreated datetime, EventID int, Level varchar, Provider varchar, 
Channel varchar, ProcessID int, Threadid int, Computer varchar, ChunkNumber int, UserID varchar, MapDescription varchar, UserName varchar, RemoteHost varchar, PayloadData1 varchar,
 PayloadData2 varchar, PayloadData3 varchar, PayloadData4 varchar, PayloadData5 varchar, PayloadData6 varchar, Executableinfo varchar, HiddenRecord varchar, SourceFile varchar, 
 Keywords varchar, ExtraDataOffset varchar, Payload varchar);
'''