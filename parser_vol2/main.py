import settings as setting
import live_artifact
import os
import collect_main
import analyze_main
import time

def main():
    path = os.getcwd()
    dbname = 'test.db'
    dbpath = path + '/' + dbname
    
    #cur = conn.cursor()

    target_src_path = 'C:\\'
    target_dst_path = r'C:\kape_combined'
    module_dst_path = r'C:\kape_test2'


    # print('start : ', time.ctime(time.time()))
    # setting.setting(dbpath, dbname)
    # print('setting : ', time.ctime(time.time()))
    # live_artifact.get_live_artifact(dbname)
    # print('live artifact : ', time.ctime(time.time()))
    # collect_main.collect(target_src_path, target_dst_path, module_dst_path, dbname)
    # print('collect : ', time.ctime(time.time()))
    chain_buf = analyze_main.analyze(dbname)
    print('analyze : ', time.ctime(time.time()))



    print(chain_buf)

if __name__ == '__main__':
    main()
