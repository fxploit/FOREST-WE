import collect_MFT
import collect_LogFile
import collect_UsnJrnl

def collect_Filesystems(module_dst_path, dbname):
    # collect_MFT.collect_MFTs(module_dst_path, dbname)
    collect_LogFile.collect_LogFiles(module_dst_path, dbname)
    collect_UsnJrnl.collect_UsnJrnls(module_dst_path, dbname)