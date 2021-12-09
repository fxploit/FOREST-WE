import sys
from PyQt5.QtWidgets import *
from PyQt5 import QtWidgets
import socket
import os
import platform
import datetime
import shutil
from distutils.dir_util import copy_tree
import time
import pytsk3
import sqlite3
from pathlib import Path
import hashlib
import subprocess


os.system('chcp 65001')
        
    
    

class MyApp(QWidget):
        
    def __init__(self):
        super().__init__()
        
        
        
        if os.path.isfile('test8.db'): os.remove('test8.db')
        self.con = sqlite3.connect('test8.db')
        self.cur = self.con.cursor()
        
        self.create_db()
        self.initUI()
        
        host = self.initParser()
        list(host)
        self.cur.execute("INSERT INTO PCinfo (Hostname, account, OSversion, OSbootime, Runtime) VALUES (?, ?, ?, ?, ?)", (host[0], host[1], host[2], host[3], host[4]))
        self.con.commit()
        
        
    def initUI(self):
        #layout settings : Grid Layout
        self.grid = QGridLayout()
        self.setLayout(self.grid)
        
        # tab1 = QWidget()
        # tabs = QTabWidget()
        # tabs.addTab(tab1, 'Tab1')
        
        self.main_tab = QWidget()
        self.collect_tab = QWidget()
        self.analysis_tab = QWidget()
        self.report_tab = QWidget()
        
        self.tabs = QTabWidget()
        self.tabs.addTab(self.main_tab, 'MAIN')
        self.tabs.addTab(self.collect_tab, 'COLLECT')
        self.tabs.addTab(self.analysis_tab, 'ANALYSIS')
        self.tabs.addTab(self.report_tab, 'REPORT')
        
        
        
        
        # btn1 = QPushButton('&Button1', self)
        # btn1.clicked.connect(self.func1)
        # button example
        
        # main_btn = QPushButton('MAIN', self)
        # collect_btn = QPushButton('COLLECT', self)
        # analysis_btn = QPushButton('ANALYSIS', self)
        # report_btn = QPushButton('REPORT', self)
        
        self.SelectFile_btn = QPushButton('Select folder', self)
        self.SelectFile_btn.clicked.connect(self.fileopen)
        self.Collect_btn = QPushButton('Start collecting', self)
        self.Collect_btn.clicked.connect(self.Start_collect)
        
        # label1 = QLabel('Label1', self)
        # label1.move(20, 20)
        # label example
        
        self.HostInfo_label = QLabel('Host Name', self)
        self.Account_label = QLabel('Account list', self)
        self.OSInfo_label = QLabel('OS(Build Version)', self)
        self.OSBootTime_label = QLabel('OS boot time(hour)', self)
        self.ParserExecTime_label = QLabel('Parser execution time', self)
        self.Filepath_label = QLabel('', self)
        
        
        
        self.HostInfo_textbox = QLineEdit()
        self.HostInfo_textbox.setReadOnly(True)
        self.Account_textbox = QLineEdit()
        self.Account_textbox.setReadOnly(True)
        self.OSInfo_textbox = QLineEdit()
        self.OSInfo_textbox.setReadOnly(True)
        self.OSBootTime_textbox = QLineEdit()
        self.OSBootTime_textbox.setReadOnly(True)
        self.ParserExecTime_textbox = QLineEdit()
        self.ParserExecTime_textbox.setReadOnly(True)
        self.ParserExecTime_textbox = QLineEdit()
        self.ParserExecTime_textbox.setReadOnly(True)
        
        self.FilePath_textbox = QLineEdit()
        self.FilePath_textbox.setReadOnly(True)
        
        
        
        self.log_textbox = QTextEdit()
        self.log_textbox.setAcceptRichText(False)
        self.log_textbox.setReadOnly(True)
        
        # grid.addWidget(QLabel('Title:'), 0, 0)
        # grid layout example
        
        # grid.addWidget(main_btn, 0, 0)
        # grid.addWidget(collect_btn, 0, 1)
        # grid.addWidget(analysis_btn, 0, 2)
        # grid.addWidget(report_btn, 0, 3)
        # layout example
        
        self.grid.addWidget(self.tabs, 0, 0)
        
        self.MainTab_layout = QGridLayout()
        self.main_tab.setLayout(self.MainTab_layout)
        
        self.MainTab_layout.addWidget(self.HostInfo_label, 1, 0)
        self.MainTab_layout.addWidget(self.HostInfo_textbox, 1, 1)
        self.MainTab_layout.addWidget(self.Account_label, 2, 0)
        self.MainTab_layout.addWidget(self.Account_textbox, 2, 1)
        self.MainTab_layout.addWidget(self.OSInfo_label, 3, 0)
        self.MainTab_layout.addWidget(self.OSInfo_textbox, 3, 1)
        self.MainTab_layout.addWidget(self.OSBootTime_label, 4, 0)
        self.MainTab_layout.addWidget(self.OSBootTime_textbox, 4, 1)
        self.MainTab_layout.addWidget(self.ParserExecTime_label, 5, 0)
        self.MainTab_layout.addWidget(self.ParserExecTime_textbox, 5, 1)
        self.MainTab_layout.addWidget(self.FilePath_textbox, 6, 0)
        self.MainTab_layout.addWidget(self.SelectFile_btn, 6, 1)
        self.MainTab_layout.addWidget(self.Collect_btn, 7, 0, 1, 2)
        self.MainTab_layout.addWidget(self.log_textbox, 8, 0, 1, 2)
        
        
        
        self.setWindowTitle('parser')
        self.setGeometry(300, 300, 500, 500)
        self.show()
        
    def fileopen(self):
        global folder
        folder = QFileDialog.getExistingDirectory(self, "Select Directory")
        self.FilePath_textbox.setText(folder)
        
    def Start_collect(self):
        self.Parsing(folder)
    
    def initParser(self):
        try:
            Hostname = socket.gethostname()
            account = os.getlogin()
            OSversion = platform.system() + " " + platform.version()
            OSbootime = time.monotonic()/3600
            Runtime = datetime.datetime.now()
            
            
            self.HostInfo_textbox.setText(str(Hostname))
            self.Account_textbox.setText(str(account))
            
            #이 부분이 로그인한 계정으로 되기 떄문에 관리자 권한으로 실행시켜도 알람이 뜸. 이 부분 해결을 어떻게 해야 할지 찾아야 함.
            if(str(account) != 'administrator'):
                QMessageBox.question(self, 'Message', 'Administrator privileges are recommended',
                                     QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
            
            self.OSInfo_textbox.setText(str(OSversion))
            self.OSBootTime_textbox.setText(str(OSbootime))
            self.ParserExecTime_textbox.setText(str(Runtime))
        except Exception as ex:
            self.log_textbox.append(str(ex))
            
        return Hostname, account, OSversion, OSbootime, Runtime
        
    def Parsing(self, folder):
        users = os.listdir(r'C:\Users')
        
        for user in users:
            if not os.path.isdir('C:/Users/' + user):
                users.remove(user)
        
        try:
            # self.FileSystem('C:', folder)
            self.Browser(folder, users)
            # self.Registry(folder) -> 미완성 
            self.File_create_open(folder, users)
            self.program_start(folder)
            self.user_account(folder, users)
            self.continuous_execution(folder, users)
            # # self.TimeLine(folder, users) -> 미완성
            
            self.WindowsDefender(folder)
            self.WER(folder)
            self.Recycle(folder)
            
            self.cur.close()
            self.con.close()
            
            self.log_textbox.append('Done')
        except Exception as ex:
            self.log_textbox.append(str(ex))
    
        
    def Browser(self, folder, users): # 계정별
        try:
            self.log_textbox.append('[*] Collect browser artifact')
            self.Chrome(folder, users)
            self.Edge(folder, users)
            self.Ie(folder, users)
        except Exception as ex:
            self.log_textbox.append(str(ex))
        
    def Chrome(self, folder, users): # 계정별
        try:
            for user in users:
                path = 'C:/Users/'+user
                self.log_textbox.append("[*] Chrome Browser artifact Collecting...")
                
                self.log_textbox.append("[+] Chrome History, Cache, Cookies, Download List Copying...")
                
                check = os.path.isdir(path+"/AppData/Local/Google")
                if check == False:
                    self.log_textbox.append("[!] Not Found Chrome Path... Default Path is "+ path + "/AppData/Local/Google")
                else:
                    self.log_textbox.append("[!] Chrome Directory Path: "+path+"/AppData/Local/Google")
                
                    history = path+"/AppData/Local/Google/Chrome/User Data/Default/History"
                    cookies = path+"/AppData/Local/Google/Chrome/User Data/Default/Cookies"
                    cache = path+"/AppData/Local/Google/Chrome/User Data/Default/Cache/"
                    
                    self.CopyFile(history, folder + '/' +user + "/History")
                    self.CopyFile(cookies, folder + '/' +user + "/Cookies")
                    self.CopyDirectory(cache, folder + '/' +user + "/Cache")
        except Exception as ex:
            self.log_textbox.append(str(ex))
            
    def Edge(self, folder, users): # 계정별
        try:
            for user in users:
                path = 'C:/Users/'+user
                self.log_textbox.append("[*] Edge Browser artifact Collecting...")
                
                check = os.path.isdir(path+"/AppData/Local/Microsoft/Edge")
                if check == False:
                    self.log_textbox.append("[!] Not Found Edge Path... Default Path is"+ path + "/AppData/Local/Microsoft/Edge")
                else:
                    self.log_textbox.append("[!] Edge Directory Path: " + path + "/AppData/Local/Microsoft/Edge")
                    self.log_textbox.append("[+] Edge History, Cache, Cookies, Download List Copying...")
            
                    history = path+"/AppData/Local/Microsoft/Edge/User Data/Default/History"
                    cookies = path+"/AppData/Local/Microsoft/Edge/User Data/Default/Cookies"
                    cache = path+"/AppData/Local/Microsoft/Edge/User Data/Default/Cache/"
            
                    self.CopyFile(history, folder + '/' + user + "/Edge/History")
                    self.CopyFile(cookies, folder + '/' + user + "/Edge/Cookies")
                    self.CopyDirectory(cache, folder +  '/' + user + "/Edge/Cache")
        except Exception as ex:
            self.log_textbox.append(str(ex))
    
    def Ie(self, folder,  users): # 계정별 
        try:
            for user in users:
                path = 'C:/Users/'+user
                self.log_textbox.append("[*] IE Browser artifact Collecting...")
                
                self.log_textbox.append("[+] IE History, Cache, Cookies, Download List Copying...")
                
                history = 'C:\\Users\\{}\\AppData\\Local\\Microsoft\\Windows\\WebCache\\WebCacheV*.dat'.format(user)
                cookies = path+"/AppData/Local/Microsoft/Windows/INetCookies/"
                cache = path+"/AppData/Local/Microsoft/Windows/INetCache/IE/"
                downlist = path+"/AppData/Local/Microsoft/Windows/IEDownloadHistory/"
        
                self.CopyDirectory(cookies, folder +  '/' + user + "/IE/Cookies")
                self.CopyDirectory(cache, folder +  '/' + user + "/IE/Cache")    
                self.CopyDirectory(downlist, folder +  '/' + user + "/IE/DownloadList")
        
                # WebCacheV*.dat 파일 COPY
                # os.system('taskkill /f /im taskhostw.exe')
                # os.system('taskkill /f /im dllhost.exe')   
                # copyPath = folder +  '/' + user + '/IE/History'
                # command = 'xcopy /s /h /i /y "{0}" {1}'.format(history,copyPath) 
                # os.system(command)
        except Exception as ex:
            self.log_textbox.append(str(ex))
    
    def Registry(self, folder):  #레지스트리 내용 수집(SAM, SECURITY, SOFTWARE, SYSTEM, DEFAULT, NTUSER.DAT) 계정별 X, 실패하셨다고 함.
        try:
            self.log_textbox.append("[*] Registry artifact Collecting...")
            registry_path = "C:\Windows\System32\config"
            
            self.log_textbox.append("[+] Registry Copying...")
    
            self.CopyFile(registry_path+"\SAM", folder + '/Registry/SAM')
            self.CopyFile(registry_path+"\SECURITY", folder + '/Registry/SECURITY')
            self.CopyFile(registry_path+"\SOFTWARE", folder + '/Registry/SOFTWARE')
            self.CopyFile(registry_path+"\SYSTEM", folder + '/Registry/SYSTEM')
            self.CopyFile(registry_path+"\DEFAULT", folder + '/Registry/DEFAULT')
            self.CopyFile(self.path+"\\NTUSER.DAT", folder + '/Registry/NTUSER.DAT')
            
        except Exception as ex:
            self.log_textbox.append(str(ex))
            
    def File_create_open(self, folder, users): # 파일 열기 및 생성 관련 아티팩트 싹다 계정별
        try:
            for user in users:
                path = 'C:/Users/'+user
                
                self.log_textbox.append("[*] Collecting artifacts related to file creation and opening...")
                
                RecentDocs_path = path+"\AppData\Roaming\Microsoft\Windows\Recent"
                HWPRecentFiles_path = path+"\AppData\Roaming\HNC\Office\Recent"
                OfficeRecentFiles_path = path+"\AppData\Roaming\Microsoft\Office\Recent"
                LNKFiles_path = path+"\AppData\Roaming\Microsoft\Windows\Recent"
                Jumplist_path = path+"\AppData\Roaming\Microsoft\Windows\Recent\AutomaticDestinations"
        
        
                self.log_textbox.append("[+] Start copying artifacts related to file creation and opening...")
                
                self.log_textbox.append("[+] Start copying RecentDocs...")
                self.CopyDirectory(RecentDocs_path, folder + '/' + user + "/File_create_open/RecentDocs")
                self.log_textbox.append("[+] Start copying OfficeRecentFiles...")
                self.CopyDirectory(OfficeRecentFiles_path, folder + '/' + user + "/File_create_open/OfficeRecentFiles") 
                self.log_textbox.append("[+] Start copying HWPRecentFiles...")
                self.CopyDirectory(HWPRecentFiles_path, folder + '/' + user + "/File_create_open/HWPRecentFiles") 
                self.log_textbox.append("[+] Start copying LNKFiles...")
                self.CopyDirectory(LNKFiles_path, folder + '/' + user + "/File_create_open/LNKFiles") 
                self.log_textbox.append("[+] Start copying Jumplist...")
                self.CopyDirectory(Jumplist_path, folder + '/' + user + "/File_create_open/Jumplist") 
             
        except Exception as ex:
            self.log_textbox.append(ex)
        
    def program_start(self, folder) : # 프로그램 실행 관련, 계정별 아티팩트 X
        try:
            self.log_textbox.append("[*] Collecting artifacts related to program execution...")
            
            prefetch_path = "C:/Windows/Prefetch"
            psevent_ptah = "C:/Windows/System32/winevt/Logs"
            Amcache_path = "C:/Windows/appcompat/Programs"
    
            self.log_textbox.append("[+] Copying artifacts related to program execution...")
            
            self.CopyDirectory(prefetch_path, folder + "/program_start/prefetch")
            self.CopyFile(psevent_ptah+"\Microsoft-Windows-PowerShell%4Operational.evtx", folder + "/program_start/PowerShell Event") 
            # self.CopyFile(Amcache_path+"\Amcache.hve", folder + "/program_start/Amcache") -> 미완성
            
        except Exception as ex:
            self.log_textbox.append(ex)

    def user_account(self, folder, users): # RDP evt -> 계정별로 남음
        try:
            self.log_textbox.append("[*] Collecting artifacts related to user account...")
            
            SuccesEvt_path = "C:/Windows/System32/winevt/Logs"
            RDPEvt_path = "C:/Windows/System32/winevt/Logs"  # System.evtx 찾기 위한 경로
            
            self.log_textbox.append("[+] Copying artifacts related to user account...")
            
            self.CopyFile(SuccesEvt_path+"/Security.evtx", folder + "/user_account/Succes Fail Logons")
            self.CopyFile(RDPEvt_path+"/System.evtx", folder + "/user_account/RDP Usage")
            for user in users:
                path = 'C:/Users/' + user
                
                RDPEvtcache_path = path+"/AppData/Local/Microsoft/Terminal Server Client/Cache" #Microsoft\Terminal Server Client\Cache 경로
                
                self.CopyDirectory(RDPEvtcache_path, folder + '/' + user + "/user_account/RDP Usage/Cache")
            
        except Exception as ex:
            self.log_textbox.append(ex)

    def continuous_execution(self, folder, users) : # 지속실행 등록 계정 사용 X
        try:
            self.log_textbox.append("[*] Collecting artifacts related to continuous execution...")
            
            Scheduler_path = "C:\Windows\System32\Tasks"  # 스케줄러 폴더 경로(Tasks)
            SystemTime_path = "C:\Windows\System32\winevt\Logs"  # System.evtx 찾기 위한 경로
            
            self.log_textbox.append("[+] Copying artifacts related to continuous execution...")
            
            self.CopyDirectory(Scheduler_path, folder + "/continuous execution/Scheduler") 
            self.CopyFile(SystemTime_path+"\Security.evtx", folder + "/continuous execution/System Time") 
            self.CopyFile(SystemTime_path+"\System.evtx", folder + "/continuous execution/System Time")
            
            for user in users:
                path = 'C:/Users/' + user
                
                Startup_path = path+"\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup"  # 시작 프로그램 경로
                self.CopyDirectory(Startup_path, folder + "/continuous execution/Startup") 
                
            
        except Exception as ex:
            self.log_textbox.append(str(ex))
            
    def TimeLine(self, folder, users) : # 계정별로 남음, 아직 성공 못하셨다고 함.
        try:
            self.log_textbox.append("[*] TimeLine artifact Collecting...")
            
            for user in users:
                path = 'C:/Users/' + user
                
                timeline_path = path+"/AppData/Local/ConnectedDevicesPlatform/388c4b714cf9ab22"
                
                self.log_textbox.append("[+] TimeLine Copying...")
                          
                self.CopyDirectory(timeline_path, folder + '/' + user + "/TimeLine") # 폴더 통채로 복사 , shutil.copy2()는 파일 한개 복사
                
        except Exception as ex:
            self.log_textbox.append(ex)

    def  WindowsDefender(self, folder) : # Windows Defender 수집 계정별 X
        try:
            self.log_textbox.append("[*] Windows Defender artifact Collecting...")
    
            WinDefender_path = "C:/ProgramData/Microsoft/Windows Defender/Scans/History/Service/DetectionHistory"  # Windows Defender 관련 폴더 경로

            self.log_textbox.append("[+] Windows Defender Copying...")
                  
            self.CopyDirectory(WinDefender_path, folder + "/Windows Defender") # 폴더 통채로 복사 , shutil.copy2()는 파일 한개 복사
                    
        except Exception as ex:
            self.log_textbox.append(ex)      

    def WER(self, folder) : #WER(Windows Error Reporting) 수집 계정별 X
        try:
            self.log_textbox.append("[*] WER artifact Collecting...")
            
            WER_path = "C:/ProgramData/Microsoft/Windows/WER"  # System.evtx 찾기 위한 경로
            
            self.log_textbox.append("[+] WER Copying...")
                  
            self.CopyDirectory(WER_path, folder + "/WER") 
                    
        except Exception as ex:
            self.log_textbox.append(ex)      
    
    def Recycle(self, folder) : #Recycle 수집, 계정별 X
        try:
            self.log_textbox.append("[*] Recycle artifact Collecting...")
            
            Recycle_path = "C:/$Recycle.Bin"
            
            self.log_textbox.append("[+] Recycle Copying...")
                  
            self.CopyDirectory(Recycle_path, folder + "/RecycleBin") 
                    
        except Exception as ex:
            self.log_textbox.append(ex)     

    def FileSystem(self, drive, folder): # 계정별 X
        self.log_textbox.append('[*] Collect filesystem artifact of '+ drive + ' drive')
        
        volume='\\\\.\\' + drive #드라이브
        img=pytsk3.Img_Info(volume) #드라이브 파일 핸들 생성
        fs=pytsk3.FS_Info(img) #파일 핸들 이용해서 드라이브 내부 정보
        
        
        self.MFT(folder, fs)
        self.LogFile(folder, fs)
        self.Extract_UsnJrnl(folder, fs)
    
    def MFT(self, folder, fs):
        self.log_textbox.append('[+] Collect $MFT')
        self.Extract('/$MFT', folder, fs)
        
    def LogFile(self, folder, fs):
        self.log_textbox.append('[+] Collect $LogFile')
        self.Extract('/$LogFile', folder, fs)
        
    def Extract_UsnJrnl(self, folder, fs):
        self.log_textbox.append('[+] Collect $UsnJrnl')
        try:
            f=fs.open('/$Extend/$UsnJrnl')
            found=False
            
            for attr in f:
                if attr.info.name == b'$J':
                    found=True
                    break
            if not found:
                self.log_textbox.append('[!] $UsnJrnl not found')
            else:
                self.log_textbox.append('[+] $UsnJrnl exists, start copying')
                with open(folder + '/$UsnJrnl','wb') as o:
                    offset=0
                    size=attr.info.size
                    while offset < size:
                        available_to_read = min(1024*1024,size-offset)
                        buf = f.read_random(offset, available_to_read, attr.info.type, attr.info.id) #attr.info.type,attr.info.id
                        if not buf:
                            break
                        o.write(buf)
                        offset += len(buf)
        except Exception as ex:
            self.log_textbox.append('[!] Error occured while collecting $UsnJrnl')
        
    def Extract(self, filename, folder, fs):
        try:
            f=fs.open(filename)
            with open(folder + filename,'wb') as o:
                self.log_textbox.append('[+] ' + filename + ' exists, start copying')
                offset = 0
                size = f.info.meta.size
                while offset<size:
                    available_to_read = min(1024*1024,size-offset)
                    buf = f.read_random(0,available_to_read)
                    if not buf: break
                    o.write(buf)
                    offset += len(buf)
        except Exception as ex:
            self.log_textbox.append('[!] Error occured while collecting '+ filename)
            self.log_textbox.append(str(ex))
        
    def CopyFile(self, src, dst):
        try:
            if not os.path.isfile(src):
                self.log_textbox.append('[!] ' + src + ' doen not exist')
            else:
                self.Create(dst)
                self.log_textbox.append('[+] Start copying file from ' + src + ' to ' + dst)
                shutil.copy2(src, dst)
                self.insert_db(src)
        except Exception as ex:
            self.log_textbox.append('[!] File copy failed')
            self.log_textbox.append(str(ex))
    
    def insert_db(self, file):
        try:
            # # artname, artpath, artMtime, artAtime, artCtime, artsize, artmd5, artsha1
            # # INSERT INTO stocks VALUES ('2006-01-05','BUY','RHAT',100,35.14)
            
            artname = file.split('/')[-1]
            artpath = file
            artMtime = datetime.datetime.fromtimestamp(os.path.getmtime(file))
            artAtime = datetime.datetime.fromtimestamp(os.path.getatime(file))
            artCtime = datetime.datetime.fromtimestamp(os.path.getctime(file))
            
            artsize = str(os.path.getsize(file)) + 'KB'
            
            with open(file,'rb') as f:
                buf = f.read()    
                artmd5 = hashlib.md5(buf).hexdigest()
                artsha1 = hashlib.sha1(buf).hexdigest()
            
            
            self.cur.execute("INSERT INTO ArtMD (artname, artpath, artMtime, artAtime, artCtime, artsize, artmd5, artsha1) VALUES (?, ?, ?, ?, ?, ?, ?, ?)",(artname, artpath, artMtime, artAtime, artCtime, artsize, artmd5, artsha1))
            self.con.commit()
            
        except Exception as ex:
            self.log_textbox.append(str(ex))    
            
    
    def CopyDirectory(self, src, dst):
        try:
            if not os.path.isdir(src):
                self.log_textbox.append('[!] ' + src + ' doen not exist')
            else:
                self.Create(dst)
                self.log_textbox.append('[+] Start copying directory from ' + src + ' to ' + dst)
                
                for root, dirs, files in os.walk(src):
                    for file in files:
                        self.insert_db((root+file).replace('\\', '/'))
                copy_tree(src, dst)
        except Exception as ex:
            self.log_textbox.append('[!] Directory copy failed')
            self.log_textbox.append(str(ex))
        
    def Create(self, folder):
        if folder.find('\\') != -1:
            url = folder.split('\\')
        else:
            url = folder.split('/')
        target = ''
        try:
            for i in range(len(url)):
                target = ""
                for j in range(i+1):
                    target += str(url[j])
                    target += '/'
                
                if not os.path.isdir(target):
                    os.mkdir(target)
            
        except Exception as ex:
            self.log_textbox.append(str(ex))

    
    def create_db(self):
        try:
            self.cur.execute("CREATE TABLE PCinfo (id INTEGER PRIMARY KEY AUTOINCREMENT, Hostname varchar, account varchar, \
            OSversion varchar, OSbootime datetime, Runtime datetime)")
            self.con.commit()
            self.cur.execute("CREATE TABLE ArtMD (artid INTEGER PRIMARY KEY AUTOINCREMENT, artname varchar not null, \
            artpath varchar not null, artMtime datetime not null, artAtime datetime not null, \
            artCtime datetime not null, artsize varchar not null, artmd5 varchar not null, artsha1 varchar not null)")
            self.con.commit()
            self.cur.execute("CREATE TABLE Usecase (fileid INTEGER PRIMARY KEY AUTOINCREMENT, filename varchar not null, \
            filepath varchar not null, fileMtime datetime not null, fileAtime datetime not null, \
            fileCtime datetime not null, filesize varchar not null, filemd5 varchar not null, filesha1 datetime not null)")
            self.con.commit()
        except Exception as ex:
            self.log_textbox.append(str(ex))
            

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())