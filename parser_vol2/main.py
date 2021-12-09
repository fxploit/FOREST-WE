import settings as setting
import live_artifact
import os
import collect_artifact
import sqlite3

def main():
    path = os.getcwd()
    dbname = 'test.db'
    dbpath = path + '/' + dbname
    
    #cur = conn.cursor()

    target_src_path = 'C:\\'
    target_dst_path = r'E:\kape_combined'
    module_dst_path = r'E:\kape_test2'

    setting.setting(dbpath, dbname)
    # live_artifact.get_live_artifact(dbname)
    collect_artifact.collect(target_src_path, target_dst_path, module_dst_path, dbname)

if __name__ == '__main__':
    main()
