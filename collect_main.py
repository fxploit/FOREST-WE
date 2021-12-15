import subprocess
import collect_eventlog
import collect_prefetch
import collect_ArtMD
import collect_Filesystem
import time
import collect_registry
import os



# collect artifacts by using KAPE tool
def collect_artifacts(target_src_path, target_dst_path, module_dst_path):
    command = '.\kape\\kape.exe --tsource '+ target_src_path + ' --tdest '+ target_dst_path + ' --tflush --target WindowsDefender,Chrome,RecycleBin,RegistryHives,WebBrowsers,PowerShellConsole,$J,$LogFile,$MFT,Amcache,ApplicationEvents,EventLogs,EventLogs-RDP,LNKFilesAndJumpLists,Prefetch,RDPLogs,RecentFileCache,WER,WindowsFirewall,WindowsTimeline --mdest ' + module_dst_path + '\
            --mflush --module BrowsingHistoryView,EvtxECmd_RDP,FullEventLogView_ScheduledTasks,JLECmd,LECmd,SBECmd,MFTECmd_$MFT,NTFS_Log_Tracker_$J,NTFS_Log_Tracker_$LogFile,autoruns,RBCmd,AmcacheParser,AppCompatCacheParser,PECmd,RecentFileCacheParser,RECmd_AllRegExecutablesFoundOrRun,RECmd_RegistryASEPs,RECmd_SoftwareASEPs,RECmd_SystemASEPs,RECmd_RECmd_Batch_MC,RECmd_UserActivity,EvtxECmd_to_TLN --mef csv'
    
    # output = subprocess.check_call(['kape\\kape.exe', '--tsource', target_src_path, '--tdest', target_dst_path, '--tflush', '--target', 'WindowsDefender,Chrome,RecycleBin,RegistryHives,WebBrowsers,PowerShellConsole,$J,$LogFile,$MFT,Amcache,ApplicationEvents,EventLogs,EventLogs-RDP,LNKFilesAndJumpLists,Prefetch,RDPLogs,RecentFileCache,WER,WindowsFirewall,WindowsTimeline',
    #  '--mdest', module_dst_path, '--mflush', '--module', 'BrowsingHistoryView,EvtxECmd_RDP,FullEventLogView_ScheduledTasks,JLECmd,LECmd,SBECmd,MFTECmd_$MFT,NTFS_Log_Tracker_$J,NTFS_Log_Tracker_$LogFile,autoruns,RBCmd,AmcacheParser,AppCompatCacheParser,PECmd,RecentFileCacheParser,RECmd_AllRegExecutablesFoundOrRun,RECmd_RegistryASEPs,RECmd_SoftwareASEPs,RECmd_SystemASEPs,RECmd_UserActivity,EvtxECmd_to_TLN'
    #  , '--mef', 'csv'], shell=True)
    
    # command = 'kape\\kape.exe --msource E:\kape_combined --mdest E:\kape_test2 --mflush --module RECmd_AllRegExecutablesFoundOrRun,RECmd_RECmd_Batch_MC,RECmd_RegistryASEPs,RECmd_SystemASEPs,RECmd_UserActivity --mef csv'

    proc = subprocess.call(command, shell=True)
    print(proc)


# Merge multiple functions into one
def collect(target_src_path, target_dst_path, module_dst_path, dbname):
    start = time.time()
    # try:

    collect_artifacts(target_src_path, target_dst_path, module_dst_path)
    print('collect artifacts : '+str(time.time()-start))
    collect_eventlog.collect_eventlogs(module_dst_path, dbname)
    print('parsing eventlog : '+str(time.time()-start))
    collect_prefetch.collect_prefetchs(target_dst_path, dbname)
    print('parsing prefetch : '+str(time.time()-start))
    collect_ArtMD.collect_ArtMDs(target_dst_path, dbname)
    print('parsing ArtMD : '+str(time.time()-start))
    collect_Filesystem.collect_Filesystems(module_dst_path, dbname)
    print('parsing FileSystem : '+str(time.time()-start))
    collect_registry.collect_registries(module_dst_path, dbname)
    print('parsing registry : '+str(time.time()-start))


    # except Exception as ex:
    #     print("[!]Exception occured!! : " + str(ex))
