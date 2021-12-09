import os
import csv
import sql


# Put the eventlog values ​​obtained through KAPE into the database
def collect_eventlogs(module_dst_path, dbname):
    count = 0
    files = os.listdir(module_dst_path + '\\EventLogs\\')

    for file in files:
        if os.path.isfile(module_dst_path + '\\EventLogs\\' + file):
            with open(module_dst_path + '\\EventLogs\\' + file, 'r', encoding='utf-8') as f:
                reader = csv.reader(f)
                for row in reader:
                    if count == 0:
                        count += 1
                        continue
                    sql.insert_eventlog(dbname, ([row[i] for i in range(len(row))]))
        count = 0
# Eventlog table schema
'''
CREATE TABLE Eventlog(i+d INTEGER PRIMARY KEY AUTOINCREMENT, RecordNumber int, EventRecordID int, TimeCreated datetime, EventID int, Level varchar, Provider varchar, 
Channel varchar, ProcessID int, Threadid int, Computer varchar, ChunkNumber int, UserID varchar, MapDescription varchar, UserName varchar, RemoteHost varchar, PayloadData1 varchar,
 PayloadData2 varchar, PayloadData3 varchar, PayloadData4 varchar, PayloadData5 varchar, PayloadData6 varchar, Executableinfo varchar, HiddenRecord varchar, SourceFile varchar, 
 Keywords varchar, ExtraDataOffset varchar, Payload varchar);
'''