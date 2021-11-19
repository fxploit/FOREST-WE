import sqlite3
import socket
import os, platform, subprocess
import datetime, time
from distutils.dir_util import copy_tree
import hashlib

os.system('chcp 65001')
db = os.path.isfile('test.db')
if db == True:
    os.remove('test.db')
con = sqlite3.connect('test.db')
cur = con.cursor()

def create_db():
    try:
        cur.execute("CREATE TABLE PCinfo (id INTEGER PRIMARY KEY AUTOINCREMENT, Hostname varchar, account varchar, \
        OSversion varchar, OSbootime datetime, Runtime datetime)")
        con.commit()
        cur.execute("CREATE TABLE ArtMD (artid INTEGER PRIMARY KEY AUTOINCREMENT, artname varchar not null, \
        artpath varchar not null, artMtime datetime not null, artAtime datetime not null, \
        artCtime datetime not null, artsize varchar not null, artmd5 varchar not null, artsha1 varchar not null)")
        con.commit()
        cur.execute("CREATE TABLE Usecase (fileid INTEGER PRIMARY KEY AUTOINCREMENT, filename varchar not null, \
        filepath varchar not null, fileMtime datetime not null, fileAtime datetime not null, \
        fileCtime datetime not null, filesize varchar not null, filemd5 varchar not null, filesha1 datetime not null)")
        con.commit()
    except Exception as ex:
        print(ex)


def hostinfo():
    try:
        print("[!] Host PC info")
        Hostname = socket.gethostname()
        account = os.getlogin()
        OSversion = platform.system() + " " + platform.version()
        OSbootime = time.monotonic()/3600
        Runtime = datetime.datetime.now()

        print("[+] Host name >>>",Hostname)
        print("[+] Windows Account >>>",account)
        print("[+] OS version >>>",OSversion)
        print("[+] PC Run Time >>>",OSbootime)
        print("[+] Parser Run Time >>>", Runtime)

        # insert_list = [
        #     (Hostname, account, OSversion, OSbootime, Runtime)
        # ]

    except Exception as ex:
        print(ex)
    return Hostname, account, OSversion, OSbootime, Runtime

def create(path):
    print("\n[!] Create Directory Path:", path+"/Desktop/Art")
    try:
        os.makedirs(path+"/Desktop/Art/IE", exist_ok=True)
    except Exception as ex:
        print(ex)

def ie(path, user):
    try:
        print("\n[!] IE Browser artifact Collecting")
        check = os.path.isdir(path+"/AppData/Local/Microsoft/Windows")
        if check == False:
            print("[!] Not Found IE Path... Default Path is" + check)
        else:
            print("[!] IE Directory Path: " + path + "/AppData/Local/Microsoft/Windows")
        print("[+] IE History, Cache, Cookies, Download List Copying...")

        history = 'C:\\Users\\{}\\AppData\\Local\\Microsoft\\Windows\\WebCache\\WebCacheV*.dat'.format(user)
        cookies = path + "/AppData/Local/Microsoft/Windows/INetCookies/"
        cache = path + "/AppData/Local/Microsoft/Windows/INetCache/IE/"
        downlist = path + "/AppData/Local/Microsoft/Windows/IEDownloadHistory/"

        copy_tree(cookies, path + "/Desktop/Art/IE/Cookies")
        copy_tree(cache, path + "/Desktop/Art/IE/Cache")
        copy_tree(downlist, path + "/Desktop/Art/IE/DownloadList")

        cookies_path = []
        for (root, directories, files) in os.walk(cookies):
            for file in files:

                path = root + '/' + file
                path = path.replace("\\", "/")
                path = path.replace("//", "/")
                cookies_path.append(path)

        cache_path = []
        for (root, directories, files) in os.walk(cache):
            for file in files:
                print('file :' + file)
                path = root + '/' + file
                path = path.replace("\\", "/")
                path = path.replace("//", "/")
                cache_path.append(path)

        downlist_path = []
        for (root, directories, files) in os.walk(downlist):
            for file in files:
                path = root + '/' + file
                path = path.replace("\\", "/")
                path = path.replace("//", "/")
                downlist_path.append(path)


        # WebCacheV*.dat 파일 COPY
        os.system('taskkill /f /im taskhostw.exe')
        os.system('taskkill /f /im dllhost.exe')
        copyPath = 'C:\\Users\\{}\\Desktop\\Art\\IE\\History'.format(user)
        command = 'xcopy /s /h /i /y "{0}" {1}'.format(history, copyPath)
        os.system(command)
    except Exception as ex:
        print(ex)
    return cache_path, cookies_path, downlist_path

def main():

    create_db() #DB,테이블 생성

    #PCinfo 테이블
    host = hostinfo()
    list(host)
    cur.execute("INSERT INTO PCinfo (Hostname, account, OSversion, OSbootime, Runtime) VALUES (?, ?, ?, ?, ?)", (host[0], host[1], host[2], host[3], host[4]))
    con.commit()

    #ArtMD -IE 테이블
    path = 'C:/Users/'+host[1]
    create(path)
    art_ie = ie(path,host[1])

    print('art_ie : ', art_ie)
    ie_name = [] #수집된 아티팩트 이름
    for i in art_ie:
        print('i', i)
        for j in i:
            print('j' + j)
            name = j.split('/')
            ie_name.append(name[-1])

    ie_path = [] #수집된 아티팩트 경로
    for i in art_ie:
        for j in i:
            ie_path.append(j)

    ie_mtime = [] #수집된 아티팩트 수정시간
    for i in art_ie:
        for j in i:
            mtime = os.path.getmtime(j)
            ie_mtime.append(datetime.datetime.fromtimestamp(mtime))

    ie_atime = [] #수집된 아티팩트 마지막 실행시간
    for i in art_ie:
        for j in i:
            atime = os.path.getatime(j)
            ie_atime.append(datetime.datetime.fromtimestamp(atime))

    ie_ctime = [] #수집된 아티팩트 속성변경시간
    for i in art_ie:
        for j in i:
            ctime = os.path.getctime(j)
            ie_ctime.append(datetime.datetime.fromtimestamp(ctime))

    ie_size = [] #수집된 아티팩트 사이즈
    for i in art_ie:
        for j in i:
            size = str(os.path.getsize(j))
            ie_size.append(size+"KB")

    ie_md5 = []
    for i in art_ie:
        for j in i:
            f = open(j, 'rb')
            data = f.read()
            f.close()
            ie_md5.append(hashlib.md5(data).hexdigest())

    ie_sha1 = []
    for i in art_ie:
        for j in i:
            f = open(j, 'rb')
            data = f.read()
            f.close()
            ie_sha1.append(hashlib.sha1(data).hexdigest())

    count = []
    for i in art_ie:
        for j in i:
            count.append(j)
    count = len(count)
    print(count)
    for i in range(1,count):
        print(ie_name[i])
        cur.execute("INSERT INTO ArtMD (artname, artpath, artMtime, artAtime, artCtime, artsize, artmd5, artsha1) VALUES (?, ?, ?, ?, ?, ?, ?, ?)",(ie_name[i], ie_path[i], ie_mtime[i], ie_atime[i], ie_ctime[i], ie_size[i], ie_md5[i], ie_sha1[i]))
        con.commit()


    cur.close()
    con.close()

if __name__ == "__main__":
    main()