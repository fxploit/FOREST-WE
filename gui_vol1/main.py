import sys
import platform
from PySide2 import QtCore, QtGui, QtWidgets, QtSql
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
from PySide2.QtSql import *

## UI FILE
from ui_splash_screen import Ui_SplashScreen
from ui_main import Ui_MainWindow

## UI FUNCTIONS
from ui_function import *


# GLOBALS
counter = 0
jumper = 0

## APPLICATION WINDOW
class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        ## TOGGLE/BURGUER MENU
        ########################################################################
        self.ui.Btn_Toggle.clicked.connect(lambda: UIFunctions.toggleMenu(self, 250, True))

        ## PAGES
        ########################################################################

        # PAGE 1
        self.ui.btn_page_main.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_1))
        self.ui.pushButton_2.clicked.connect(lambda: UIFunctions.folder_load(self))
        UIFunctions.data_load(self, "SELECT hostname, account, OSversion, OSbit, OSbootime, Runtime, Timezone FROM PCinfo", 1)
        UIFunctions.data_load(self, "SELECT swname, swversion, swinstalldate, swpublisher FROM SWcheck",2)

        # PAGE 2
        self.ui.btn_page_live.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_2))
        UIFunctions.data_load(self, "SELECT netcard, ipv4, macaddr FROM Netinfo", 3)
        UIFunctions.data_load(self, "SELECT Protocol, LocalAddr, ExternalAddr, Status, Pid FROM Live_Netinfo", 4)
        UIFunctions.data_load(self, "SELECT PSname, PSpid, PSppid, PSthds, PShnds, PStime FROM Proinfo", 5)

        # PAGE 3
        self.ui.btn_page_collection.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_3))
        UIFunctions.data_load(self, "SELECT TimeStamp, FileDirectory, Eventinfo FROM UsnJrnl WHERE Eventinfo LIKE '%Deleted%'", 6)

        # PAGE 4
        self.ui.btn_page_analysis.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_4))
        self.ui.pushButton_EventLog.clicked.connect(lambda: UIFunctions.data_load(self,"SELECT * FROM Eventlog", 7))
        self.ui.pushButton_Logfile.clicked.connect(lambda: UIFunctions.data_load(self,"SELECT id, LSN, EventTime, Event, Detail, FileDirectory_Name, Full_Path, Create_Time, Modified_Time, MFT_modified_Time, Access_Time, Redo, Target_VCN, Cluster_Index FROM LogFile", 7))
        self.ui.pushButton_Prefetch.clicked.connect(lambda: UIFunctions.data_load(self,"SELECT PFfilename, PEname, RunCount, LastExec1, LastExec2, LastExec3, LastExec4, LastExec5, LastExec6, LastExec7, LastExec8, VolumeInfo FROM Prefetch", 7))
        self.ui.pushButton_Services.clicked.connect(lambda: UIFunctions.data_load(self,"SELECT * FROM Registry_Services", 7))
        self.ui.pushButton_Scheduler.clicked.connect(lambda: UIFunctions.data_load(self,"SELECT * FROM Registry_Scheduler", 7))
        self.ui.pushButton_UsnJrnl.clicked.connect(lambda: UIFunctions.data_load(self,"SELECT * FROM UsnJrnl", 7))
        self.ui.pushButton_ArtMD.clicked.connect(lambda: UIFunctions.data_load(self,"SELECT * FROM ArtMD", 7))

        # PAGE 5
        self.ui.btn_page_review.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_5))


## SPLASHSCREEN WINDOW
class SplashScreen(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_SplashScreen()
        self.ui.setupUi(self)

        ## SET INITIAL PROGRESS BAR TO (0) ZERO
        self.progressBarValue(0)

        ## REMOVE STANDARD TITLE BAR
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)  # Remove title bar
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)  # Set background to transparent

        ## APPLY DROP SHADOW EFFECT
        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(20)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor(0, 0, 0, 120))
        self.ui.circularBg.setGraphicsEffect(self.shadow)

        ## QTIMER START
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.progress)
        ## TIMER IN MILLISECONDS
        self.timer.start(2)

        ## SHOW SPLASHSCREEN WINDOWS
        #########################################################
        self.show()
        ## END


    ## PROGRESS BAR LOANDING
    #########################################################
    def progress(self):
        global counter
        global jumper
        value = counter

        # HTML TEXT PERCENTAGE
        htmlText = """<p><span style=" font-size:68pt;">{VALUE}</span><span style=" font-size:58pt; vertical-align:super;">%</span></p>"""

        # REPLACE VALUE
        newHtml = htmlText.replace("{VALUE}", str(jumper))

        if (value > jumper):
            # APPLY NEW PERCENTAGE TEXT
            self.ui.labelPercentage.setText(newHtml)
            jumper += 1

        # SET VALUE TO PROGRESS BAR
        # fix max value error if > than 100
        if value >= 100: value = 1.000
        self.progressBarValue(value)

        # CLOSE SPLASH SCREE AND OPEN APP
        if counter > 100:
            # STOP TIMER
            self.timer.stop()

            # # SHOW MAIN WINDOW
            self.main = MainWindow()
            self.main.show()

            # CLOSE SPLASH SCREEN
            self.close()

        # INCREASE COUNTER
        counter += 0.1

    ## PROGRESS BAR VALUE
    #########################################################
    def progressBarValue(self, value):

        ## PROGRESSBAR STYLESHEET BASE
        styleSheet = """
        QFrame{
            border-radius: 150px;
            background-color: qconicalgradient(cx:0.5, cy:0.5, angle:90, stop:{STOP_1} rgba(255, 0, 127, 0), stop:{STOP_2} rgba(85, 170, 255, 255));
        }
        """

        ## GET PROGRESS BAR VALUE, CONVERT TO FLOAT AND INVERT VALUES
        ## stop works of 1.000 to 0.000
        progress = (100 - value) / 100.0

        ## GET NEW VALUES
        stop_1 = str(progress - 0.001)
        stop_2 = str(progress)

        ## SET VALUES TO NEW STYLESHEET
        newStylesheet = styleSheet.replace("{STOP_1}", stop_1).replace("{STOP_2}", stop_2)

        # APPLY STYLESHEET WITH NEW VALUES
        self.ui.circularProgress.setStyleSheet(newStylesheet)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = SplashScreen()
    sys.exit(app.exec_())