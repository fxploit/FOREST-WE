import pandas as pd
import glob, os
import sql

def collect_ArtMDs(target_dst_path, dbname):
    target = target_dst_path + r'\*CopyLog.csv'
    csvpath = glob.glob(target)[-1]

    csv = pd.read_csv(csvpath,names=['CopiedTimestamp', 'SourceFile', 'DestinationFile', 'FileSize', 'SourceFileSha1', 'DeferredCopy', 'CreatedOnUtc',\
                                         'ModifiedOnUtc', 'LastAccessedOnUtc', 'CopyDuration'], encoding='UTF8')

    artcopytime = csv['CopiedTimestamp']
    artpath = csv['SourceFile']
    artcopypath = csv['DestinationFile']
    artMtime = csv['ModifiedOnUtc']
    artAtime = csv['LastAccessedOnUtc']
    artCtime = csv['CreatedOnUtc']
    artsize = csv['FileSize']
    artsha1 = csv['SourceFileSha1']
    artname = []

    for i in range(len(artpath)):
        name = os.path.basename(artpath[i])
        artname.append(name)


    for i in range(1,len(artpath)):
        sql.insert_ArtMD(dbname, (artname[i], artpath[i], artcopypath[i], artcopytime[i], artMtime[i], artAtime[i], artCtime[i], artsize[i], artsha1[i]))
        