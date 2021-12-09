import wmi
import psutil
import subprocess
import sql


# collect information about processes
def Get_Proinfo(dbname):
    WMI_OBJ = wmi.WMI()
    process_list = WMI_OBJ.Win32_Process()

    for process in process_list:
        sql.insert_proinfo(dbname, (process.Name , process.ProcessId, process.ParentProcessId, process.ThreadCount, process.HandleCount, process.CreationDate))


# collect information about network
def Get_Netinfo(dbname):
    addrs = psutil.net_if_addrs()
    for addr in addrs:
        sql.insert_netinfo(dbname, (addr, addrs[addr][1].address, addrs[addr][0].address))


# collect information such as opened ports, protocol, etc.
def Get_Live_Netinfo(dbname):
    out = subprocess.run('netstat -ano | findstr \\[::]\\:',shell=True, capture_output=True)

    buf = out.stdout.decode('euc-kr').replace('\t','').split('\r\n')

    for i in buf:
        if not len(i)>0:
            continue

        j = i.split(' ')

        while '' in j:
            j.remove('')
            if len(j)==5:
                break
        sql.insert_live_netinfo(dbname, (j[0],j[1],j[2],j[3],j[4]))


# Merge multiple functions into one
def get_live_artifact(dbname):
    try:
        Get_Proinfo(dbname)
        Get_Netinfo(dbname)
        Get_Live_Netinfo(dbname)

    except Exception as ex:
        print("[!]Exception occured!! : " + str(ex))