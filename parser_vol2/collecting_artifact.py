import subprocess
import sqlite3
import csv
import collect_eventlog
import collect_prefetch

# collect artifacts by using KAPE tool
def collect_artifacts(target_src_path, target_dst_path, module_dst_path):

    command = '.\kape.exe --tsource ' + target_src_path + ' --tdest ' + target_dst_path + ' --tflush --target WindowsDefender,Chrome,RecycleBin,RegistryHives,WebBrowsers,\
    PowerShellConsole,$J,$LogFile,$MFT,Amcache,ApplicationEvents,EventLogs,EventLogs-RDP,LNKFilesAndJumpLists,Prefetch,RDPLogs,RecentFileCache,WER,WindowsFirewall,\
        WindowsTimeline --mdest ' + module_dst_path + ' --mflush --module BrowsingHistoryView,EvtxECmd_RDP,FullEventLogView_ScheduledTasks,JLECmd,LECmd,SBECmd,MFTECmd_$MFT,\
            NTFS_Log_Tracker_$J,NTFS_Log_Tracker_$LogFile,autoruns,RBCmd,AmcacheParser,AppCompatCacheParser,PECmd,RecentFileCacheParser,RECmd_AllRegExecutablesFoundOrRun,\
                RECmd_RegistryASEPs,RECmd_SoftwareASEPs,RECmd_SystemASEPs,RECmd_UserActivity,EvtxECmd_to_TLN --mef csv'

    output = subprocess.run(command, shell=True, capture_output=True)


# Merge multiple functions into one
def collect(target_src_path, target_dst_path, module_dst_path, dbname):
    try:
        collect_artifacts(target_src_path, target_dst_path, module_dst_path)
        collect_eventlog.collect_eventlogs(module_dst_path, dbname)
        collect_prefetch.collect_prefetchs(target_dst_path, dbname)

    except Exception as ex:
        print("[!]Exception occured!! : " + str(ex))