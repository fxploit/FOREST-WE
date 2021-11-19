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

class MyApp(QWidget):
        
    def __init__(self):
        super().__init__()
        self.initUI()
        self.initParser()

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
        
        self.SelectFile_btn = QPushButton('Select file', self)
        self.SelectFile_btn.clicked.connect(self.fileopen)
        
        
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
        self.MainTab_layout.addWidget(self.log_textbox, 7, 0, 1, 2)
        
        
        
        self.setWindowTitle('parser')
        self.setGeometry(300, 300, 500, 500)
        self.show()
        
        
        
    def fileopen(self):
        folder = QFileDialog.getExistingDirectory(self, "Select Directory")
        self.FilePath_textbox.setText(folder)
        self.Parsing(folder)
    
    
    def initParser(self):
        self.HostInfo_textbox.setText(str(socket.gethostname()))
        self.Account_textbox.setText(str(os.getlogin()))
        if(str(os.getlogin()) != 'administrator'):
            QMessageBox.question(self, 'Message', 'Administrator privileges are recommended',
                                 QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        
        self.OSInfo_textbox.setText(str(platform.system()+platform.version()))
        self.OSBootTime_textbox.setText(str(int(time.monotonic()/3600)))
        self.ParserExecTime_textbox.setText(str(datetime.datetime.now()))
        
    def Parsing(self, folder):
        users = os.listdir(r'C:\Users')

        for user in users:
            try:
                if os.path.isdir('C:\\Users\\'+user):
                    self.log_textbox.append('Collect ' + user + ' artifact')
                    self.Browser(user,folder)
                    self.FileSystem('C:', folder)
                    
                    self.log_textbox.append('')
            except Exception as ex:
                self.log_textbox.append(str(ex))
        
        
    def Browser(self, user, folder):
        self.log_textbox.append('[*] Collect browser artifact')
        self.Chrome(user, folder)
        
        
    def Chrome(self, user, folder):
        path = 'C:/Users/'+user
        self.log_textbox.append("[*] Chrome Browser artifact Collecting...")
        check = os.path.isdir(path+"/AppData/Local/Google")
    
        if check == False:
            self.log_textbox.append("[!] Not Found Chrome Path... Default Path is not valid")
            self.log_textbox.append("[!] Default path is " + path + "/AppData/Local/Google")
            
        else:
            self.log_textbox.append("[!] Chrome Directory Path: "+path+"/AppData/Local/Google")
            self.log_textbox.append("[+] Chrome History, Cache, Cookies, Download List Copying...")

            history = path+"/AppData/Local/Google/Chrome/User Data/Default/History"
            cookies = path+"/AppData/Local/Google/Chrome/User Data/Default/Cookies"
            cache = path+"/AppData/Local/Google/Chrome/User Data/Default/Cache/"
            
            CopyFile(history, folder + '/' +user + "/History")
            CopyFile(cookies, folder + '/' +user + "/Cookies")
            CopyDirectory(cache, folder + '/' +user + "/Cache")
            
            
    def Registry(self, path, folder):  #레지스트리 내용 수집(SAM, SECURITY, SOFTWARE, SYSTEM, DEFAULT, NTUSER.DAT)
        try:
            self.log_textbox.append("[*] Registry artifact Collecting...")
            registry_path = "C:\Windows\System32\config"
            check = os.path.isdir(registry_path)
            if check == False :
                self.log_textbox.append("[!] Not Found registry Path.... Default Path is not valid")
            else :
                self.log_textbox.append("[!] Registry Directory Path : " + registry_path)
            self.log_textbox.append("[+] Registry Copying...")
    
            CopyFile(registry_path+"\SAM", folder + '/Registry')
            CopyFile(registry_path+"\SECURITY", folder + '/Registry')
            CopyFile(registry_path+"\SOFTWARE", folder + '/Registry')
            CopyFile(registry_path+"\SYSTEM", folder + '/Registry')
            CopyFile(registry_path+"\DEFAULT", folder + '/Registry')
            CopyFile(path+"\\NTUSER.DAT", folder + '/Registry')
                     
        except Exception as ex:
            self.log_textbox.append(str(ex))
            
            
    def File_create_open(self, path, folder): # 파일 열기 및 생성 관련 아티팩트 
        try:
            self.log_textbox.append("[*] Collecting artifacts related to file creation and opening...")
            
            RecentDocs_path = path+"\AppData\Roaming\Microsoft\Windows\Recent"
            HWPRecentFiles_path = path+"\AppData\Roaming\HNC\Office\Recent"
            OfficeRecentFiles_path = path+"\AppData\Roaming\Microsoft\Office\Recent"
            LNKFiles_path = path+"\AppData\Roaming\Microsoft\Windows\Recent"
            Jumplist_path = path+"\AppData\Roaming\Microsoft\Windows\Recent\AutomaticDestinations"
    
    
            self.log_textbox.append("[+] Start copying artifacts related to file creation and opening...")
            
            self.log_textbox.append("[+] Start copying RecentDocs...")
            CopyDirectory(RecentDocs_path, folder + "/File_create_open/RecentDocs")
            self.log_textbox.append("[+] Start copying OfficeRecentFiles...")
            CopyDirectory(OfficeRecentFiles_path, folder + "/File_create_open/OfficeRecentFiles") 
            self.log_textbox.append("[+] Start copying HWPRecentFiles...")
            CopyDirectory(HWPRecentFiles_path, folder + "/File_create_open/HWPRecentFiles") 
            self.log_textbox.append("[+] Start copying LNKFiles...")
            CopyDirectory(LNKFiles_path, folder + "/File_create_open/LNKFiles") 
            self.log_textbox.append("[+] Start copying Jumplist...")
            CopyDirectory(Jumplist_path, folder + "/File_create_open/Jumplist") 
             
        except Exception as ex:
            self.log_textbox.append(ex)
            
        
    def program_start(self, path, folder) : # 프로그램 실행
        try:
            self.log_textbox.append("[*] Collecting artifacts related to program execution...")
            
            prefetch_path = "C:/Windows/Prefetch"
            psevent_ptah = "C:/Windows/System32/winevt/Logs"
            Amcache_path = "C:/Windows/appcompat/Programs"
    
            self.log_textbox.append("[+] Copying artifacts related to program execution...")
            
            CopyDirectory(prefetch_path, folder + "/program_start/prefetch")
            CopyFile(psevent_ptah+"\Microsoft-Windows-PowerShell%4Operational.evtx", folder + "/program_start/PowerShell Event") 
            CopyFile(Amcache_path+"\Amcache.hve", folder + "/program_start/Amcache")
            
        except Exception as ex:
            self.log_textbox.append(ex)

    def user_account(self, path, folder) : # 계정 사용 
        try:
            self.log_textbox.append("[*] Collecting artifacts related to user account...")
            
            SuccesEvt_path = "C:/Windows/System32/winevt/Logs"
            RDPEvt_path = "C:/Windows/System32/winevt/Logs"  # System.evtx 찾기 위한 경로
            RDPEvtcache_path = path+"/AppData/Local/Microsoft/Terminal Server Client/Cache" #Microsoft\Terminal Server Client\Cache 경로
                            
            self.log_textbox.append("[+] Copying artifacts related to user account...")
            
            CopyFile(SuccesEvt_path+"/Security.evtx", folder + "/user_account/Succes Fail Logons")
            CopyFile(RDPEvt_path+"/System.evtx", folder + "/user_account/RDP Usage")
            CopyDirectory(RDPEvtcache_path, folder + "/user_account/RDP Usage/Cache")
            
        except Exception as ex:
            self.log_textbox.append(ex)
    

    def continuous_execution(self, path, folder) : # 지속실행 등록
        try:
            self.log_textbox.append("[*] Collecting artifacts related to continuous execution...")
            
            Startup_path = path+"\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup"  # 시작 프로그램 경로
            Scheduler_path = "C:\Windows\System32\Tasks"  # 스케줄러 폴더 경로(Tasks)
            SystemTime_path = "C:\Windows\System32\winevt\Logs"  # System.evtx 찾기 위한 경로
    
            self.log_textbox.append("[+] Copying artifacts related to continuous execution...")
            
            CopyDirectory(Startup_path, folder + "/continuous execution/Startup") 
            CopyDirectory(Scheduler_path, folder + "/continuous execution/Scheduler") 
            CopyFile(SystemTime_path+"\Security.evtx", folder + "/continuous execution/System Time") 
            CopyFile(SystemTime_path+"\System.evtx", folder + "/continuous execution/System Time")
     
        except Exception as ex:
            self.log_textbox.append(ex)
            
            
    def TimeLine(self, path, folder) :
        try:
            self.log_textbox.append("[*] TimeLine artifact Collecting...")
            timeline_path = path+"/AppData/Local/ConnectedDevicesPlatform/388c4b714cf9ab22"

            self.log_textbox.append("[+] TimeLine Copying...")
                  
            CopyDirectory(timeline_path, folder + "/TimeLine") # 폴더 통채로 복사 , shutil.copy2()는 파일 한개 복사
                    
        except Exception as ex:
            self.log_textbox.append(ex)

    def  WindowsDefender(self, path, folder) : # Windows Defender 수집
        try:
            self.log_textbox.append("[*] Windows Defender artifact Collecting...")
    
            WinDefender_path = "C:/ProgramData/Microsoft/Windows Defender/Scans/History/Service/DetectionHistory"  # Windows Defender 관련 폴더 경로

            self.log_textbox.append("[+] Windows Defender Copying...")
                  
            CopyDirectory(WinDefender_path, folder + "/Windows Defender") # 폴더 통채로 복사 , shutil.copy2()는 파일 한개 복사
                    
        except Exception as ex:
            self.log_textbox.append(ex)      

  
    
    def WER(self, path, folder) : #WER(Windows Error Reporting) 수집
        try:
            self.log_textbox.append("[*] WER artifact Collecting...")
    
            WER_path = "C:/ProgramData/Microsoft/Windows/WER"  # System.evtx 찾기 위한 경로
    
            self.log_textbox.append("[+] WER Copying...")
                  
            CopyDirectory(WER_path, folder + "/WER") 
                    
        except Exception as ex:
            self.log_textbox.append(ex)      
    
    
    def Recycle(self, path, folder) : #Recycle 수집
        try:
            self.log_textbox.append("[*] Recycle artifact Collecting...")
    
            Recycle_path = "C:/$Recycle.Bin"  

            self.log_textbox.append("[+] Recycle Copying...")
                  
            CopyDirectory(Recycle_path, folder + "/RecycleBin") 
                    
        except Exception as ex:
            self.log_textbox.append(ex)     


    def FileSystem(self, drive, folder):
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
        except Exception as ex:
            self.log_textbox.append('[!] File copy failed')
            self.log_textbox.append(str(ex))
            
    
    def CopyDirectory(self, src, dst):
        try:
            if not os.path.isdir(src):
                self.log_textbox.append('[!] ' + src + ' doen not exist')
            else:
                self.Create(dst)
                self.log_textbox.append('[+] Start copying directory from ' + src + ' to ' + dst)
                copy_tree(src, dst)
        except Exception as ex:
            self.log_textbox.append('[!] Directory copy failed')
            self.log_textbox.append(str(ex))
        
    def Create(self, folder):
        if not os.path.isdir(folder):
            self.log_textbox.append('[!] ' + folder + ' does not exist, create folder')
            os.mkdir(folder)
        
        
        
        
        
        
        

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())
