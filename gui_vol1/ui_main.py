# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainddjoid.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1121, 691)
        MainWindow.setStyleSheet(u"background-color: rgb(45, 45, 45);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setMinimumSize(QSize(1000, 500))
        self.centralwidget.setStyleSheet(u"")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.Top_Bar = QFrame(self.centralwidget)
        self.Top_Bar.setObjectName(u"Top_Bar")
        self.Top_Bar.setMaximumSize(QSize(16777215, 40))
        self.Top_Bar.setStyleSheet(u"background-color: rgb(35, 35, 35);")
        self.Top_Bar.setFrameShape(QFrame.NoFrame)
        self.Top_Bar.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.Top_Bar)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_toggle = QFrame(self.Top_Bar)
        self.frame_toggle.setObjectName(u"frame_toggle")
        self.frame_toggle.setMinimumSize(QSize(70, 0))
        self.frame_toggle.setMaximumSize(QSize(70, 40))
        self.frame_toggle.setStyleSheet(u"background-color: rgb(85, 170, 255);")
        self.frame_toggle.setFrameShape(QFrame.StyledPanel)
        self.frame_toggle.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_toggle)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.Btn_Toggle = QPushButton(self.frame_toggle)
        self.Btn_Toggle.setObjectName(u"Btn_Toggle")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Btn_Toggle.sizePolicy().hasHeightForWidth())
        self.Btn_Toggle.setSizePolicy(sizePolicy)
        self.Btn_Toggle.setMinimumSize(QSize(0, 0))
        self.Btn_Toggle.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"border: 0px solid;")
        icon = QIcon()
        icon.addFile(u"../whale-removebg-preview.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Btn_Toggle.setIcon(icon)
        self.Btn_Toggle.setIconSize(QSize(55, 55))

        self.verticalLayout_2.addWidget(self.Btn_Toggle)


        self.horizontalLayout.addWidget(self.frame_toggle)

        self.frame_top = QFrame(self.Top_Bar)
        self.frame_top.setObjectName(u"frame_top")
        self.frame_top.setFrameShape(QFrame.StyledPanel)
        self.frame_top.setFrameShadow(QFrame.Raised)

        self.horizontalLayout.addWidget(self.frame_top)


        self.verticalLayout.addWidget(self.Top_Bar)

        self.Content = QFrame(self.centralwidget)
        self.Content.setObjectName(u"Content")
        self.Content.setFrameShape(QFrame.NoFrame)
        self.Content.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.Content)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame_left_menu = QFrame(self.Content)
        self.frame_left_menu.setObjectName(u"frame_left_menu")
        self.frame_left_menu.setMinimumSize(QSize(70, 0))
        self.frame_left_menu.setMaximumSize(QSize(70, 16777215))
        self.frame_left_menu.setStyleSheet(u"background-color: rgb(35, 35, 35);")
        self.frame_left_menu.setFrameShape(QFrame.StyledPanel)
        self.frame_left_menu.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_left_menu)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.frame_top_menus = QFrame(self.frame_left_menu)
        self.frame_top_menus.setObjectName(u"frame_top_menus")
        self.frame_top_menus.setMinimumSize(QSize(0, 0))
        self.frame_top_menus.setFrameShape(QFrame.NoFrame)
        self.frame_top_menus.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_top_menus)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.btn_page_main = QPushButton(self.frame_top_menus)
        self.btn_page_main.setObjectName(u"btn_page_main")
        self.btn_page_main.setMinimumSize(QSize(0, 40))
        font = QFont()
        font.setBold(True)
        font.setWeight(75)
        self.btn_page_main.setFont(font)
        self.btn_page_main.setStyleSheet(u"QPushButton{	\n"
"	background-color: rgb(35, 35, 35);\n"
"	color: rgb(255, 255, 255);\n"
"	border: 0px solid;\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgb(85, 170, 255);\n"
"}")

        self.verticalLayout_4.addWidget(self.btn_page_main)

        self.btn_page_live = QPushButton(self.frame_top_menus)
        self.btn_page_live.setObjectName(u"btn_page_live")
        self.btn_page_live.setMinimumSize(QSize(0, 40))
        self.btn_page_live.setFont(font)
        self.btn_page_live.setStyleSheet(u"QPushButton{	\n"
"	background-color: rgb(35, 35, 35);\n"
"	color: rgb(255, 255, 255);\n"
"	border: 0px solid;\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgb(85, 170, 255);\n"
"}")

        self.verticalLayout_4.addWidget(self.btn_page_live)

        self.btn_page_collection = QPushButton(self.frame_top_menus)
        self.btn_page_collection.setObjectName(u"btn_page_collection")
        self.btn_page_collection.setMinimumSize(QSize(0, 40))
        self.btn_page_collection.setFont(font)
        self.btn_page_collection.setStyleSheet(u"QPushButton{	\n"
"	background-color: rgb(35, 35, 35);\n"
"	color: rgb(255, 255, 255);\n"
"	border: 0px solid;\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgb(85, 170, 255);\n"
"}")

        self.verticalLayout_4.addWidget(self.btn_page_collection)

        self.btn_page_analysis = QPushButton(self.frame_top_menus)
        self.btn_page_analysis.setObjectName(u"btn_page_analysis")
        self.btn_page_analysis.setMinimumSize(QSize(0, 40))
        self.btn_page_analysis.setFont(font)
        self.btn_page_analysis.setStyleSheet(u"QPushButton{	\n"
"	background-color: rgb(35, 35, 35);\n"
"	color: rgb(255, 255, 255);\n"
"	border: 0px solid;\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgb(85, 170, 255);\n"
"}")

        self.verticalLayout_4.addWidget(self.btn_page_analysis)

        self.btn_page_review = QPushButton(self.frame_top_menus)
        self.btn_page_review.setObjectName(u"btn_page_review")
        self.btn_page_review.setMinimumSize(QSize(0, 40))
        self.btn_page_review.setFont(font)
        self.btn_page_review.setStyleSheet(u"QPushButton{	\n"
"	background-color: rgb(35, 35, 35);\n"
"	color: rgb(255, 255, 255);\n"
"	border: 0px solid;\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgb(85, 170, 255);\n"
"}")

        self.verticalLayout_4.addWidget(self.btn_page_review)


        self.verticalLayout_3.addWidget(self.frame_top_menus, 0, Qt.AlignTop)


        self.horizontalLayout_2.addWidget(self.frame_left_menu)

        self.frame_pages = QFrame(self.Content)
        self.frame_pages.setObjectName(u"frame_pages")
        self.frame_pages.setFrameShape(QFrame.StyledPanel)
        self.frame_pages.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_pages)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.stackedWidget = QStackedWidget(self.frame_pages)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.page_1 = QWidget()
        self.page_1.setObjectName(u"page_1")
        self.verticalLayout_6 = QVBoxLayout(self.page_1)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.frame = QFrame(self.page_1)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_11 = QVBoxLayout(self.frame)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.frame_2 = QFrame(self.frame)
        self.frame_2.setObjectName(u"frame_2")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy1)
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.frame_12 = QFrame(self.frame_2)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setFrameShape(QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QFrame.Raised)
        self.verticalLayout_18 = QVBoxLayout(self.frame_12)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.label_7 = QLabel(self.frame_12)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setFont(font)
        self.label_7.setStyleSheet(u"color: #FFFFFF")

        self.verticalLayout_18.addWidget(self.label_7)

        self.Table_System = QTableWidget(self.frame_12)
        if (self.Table_System.columnCount() < 7):
            self.Table_System.setColumnCount(7)
        __qtablewidgetitem = QTableWidgetItem()
        self.Table_System.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.Table_System.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.Table_System.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.Table_System.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.Table_System.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.Table_System.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.Table_System.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        self.Table_System.setObjectName(u"Table_System")
        self.Table_System.setStyleSheet(u"background-color: rgb(150, 150, 150);\n"
"color: rgb(0, 0, 0);")
        self.Table_System.setSortingEnabled(True)

        self.verticalLayout_18.addWidget(self.Table_System)


        self.horizontalLayout_5.addWidget(self.frame_12)

        self.frame_13 = QFrame(self.frame_2)
        self.frame_13.setObjectName(u"frame_13")
        self.frame_13.setFrameShape(QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QFrame.Raised)
        self.verticalLayout_20 = QVBoxLayout(self.frame_13)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.label_8 = QLabel(self.frame_13)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setFont(font)
        self.label_8.setStyleSheet(u"color: #FFFFFF")

        self.verticalLayout_20.addWidget(self.label_8)

        self.Table_Software = QTableWidget(self.frame_13)
        if (self.Table_Software.columnCount() < 4):
            self.Table_Software.setColumnCount(4)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.Table_Software.setHorizontalHeaderItem(0, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.Table_Software.setHorizontalHeaderItem(1, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.Table_Software.setHorizontalHeaderItem(2, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.Table_Software.setHorizontalHeaderItem(3, __qtablewidgetitem10)
        self.Table_Software.setObjectName(u"Table_Software")
        font1 = QFont()
        font1.setBold(False)
        font1.setWeight(50)
        self.Table_Software.setFont(font1)
        self.Table_Software.setStyleSheet(u"background-color: rgb(150, 150, 150);\n"
"color: rgb(0, 0, 0);")
        self.Table_Software.setShowGrid(True)
        self.Table_Software.setGridStyle(Qt.SolidLine)
        self.Table_Software.setSortingEnabled(True)
        self.Table_Software.setRowCount(0)

        self.verticalLayout_20.addWidget(self.Table_Software)


        self.horizontalLayout_5.addWidget(self.frame_13)


        self.verticalLayout_11.addWidget(self.frame_2)

        self.frame_3 = QFrame(self.frame)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.frame_10 = QFrame(self.frame_3)
        self.frame_10.setObjectName(u"frame_10")
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.frame_10.sizePolicy().hasHeightForWidth())
        self.frame_10.setSizePolicy(sizePolicy2)
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_10)
        self.horizontalLayout_4.setSpacing(12)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.label_6 = QLabel(self.frame_10)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setFont(font)
        self.label_6.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_6.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_4.addWidget(self.label_6)

        self.lineEdit = QLineEdit(self.frame_10)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setStyleSheet(u"color: #FFFFFF")

        self.horizontalLayout_4.addWidget(self.lineEdit)

        self.pushButton_2 = QPushButton(self.frame_10)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"background-color: rgb(153, 153, 153);")

        self.horizontalLayout_4.addWidget(self.pushButton_2)


        self.horizontalLayout_3.addWidget(self.frame_10, 0, Qt.AlignBottom)

        self.frame_11 = QFrame(self.frame_3)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setFrameShape(QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Raised)
        self.verticalLayout_19 = QVBoxLayout(self.frame_11)
        self.verticalLayout_19.setSpacing(0)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.verticalLayout_19.setContentsMargins(0, 0, 0, 0)
        self.pushButton = QPushButton(self.frame_11)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 255, 255);")

        self.verticalLayout_19.addWidget(self.pushButton)


        self.horizontalLayout_3.addWidget(self.frame_11, 0, Qt.AlignRight|Qt.AlignBottom)


        self.verticalLayout_11.addWidget(self.frame_3, 0, Qt.AlignBottom)

        self.frame_4 = QFrame(self.frame)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setMaximumSize(QSize(16777215, 16777215))
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.verticalLayout_12 = QVBoxLayout(self.frame_4)
        self.verticalLayout_12.setSpacing(0)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.textBrowser = QTextBrowser(self.frame_4)
        self.textBrowser.setObjectName(u"textBrowser")
        self.textBrowser.setMinimumSize(QSize(800, 100))
        self.textBrowser.setMaximumSize(QSize(16777215, 16777215))

        self.verticalLayout_12.addWidget(self.textBrowser)


        self.verticalLayout_11.addWidget(self.frame_4)


        self.verticalLayout_6.addWidget(self.frame)

        self.stackedWidget.addWidget(self.page_1)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.verticalLayout_7 = QVBoxLayout(self.page_2)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.frame_5 = QFrame(self.page_2)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.verticalLayout_13 = QVBoxLayout(self.frame_5)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.frame_6 = QFrame(self.frame_5)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.frame_6)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.frame_23 = QFrame(self.frame_6)
        self.frame_23.setObjectName(u"frame_23")
        self.frame_23.setFrameShape(QFrame.StyledPanel)
        self.frame_23.setFrameShadow(QFrame.Raised)
        self.verticalLayout_30 = QVBoxLayout(self.frame_23)
        self.verticalLayout_30.setObjectName(u"verticalLayout_30")
        self.label_13 = QLabel(self.frame_23)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setFont(font)
        self.label_13.setStyleSheet(u"color: #FFFFFF")

        self.verticalLayout_30.addWidget(self.label_13)

        self.Table_Network = QTableWidget(self.frame_23)
        if (self.Table_Network.columnCount() < 3):
            self.Table_Network.setColumnCount(3)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.Table_Network.setHorizontalHeaderItem(0, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.Table_Network.setHorizontalHeaderItem(1, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.Table_Network.setHorizontalHeaderItem(2, __qtablewidgetitem13)
        self.Table_Network.setObjectName(u"Table_Network")
        self.Table_Network.setStyleSheet(u"background-color: rgb(150, 150, 150);\n"
"color: rgb(0, 0, 0);")
        self.Table_Network.setSortingEnabled(True)

        self.verticalLayout_30.addWidget(self.Table_Network)


        self.horizontalLayout_7.addWidget(self.frame_23)

        self.frame_22 = QFrame(self.frame_6)
        self.frame_22.setObjectName(u"frame_22")
        self.frame_22.setFrameShape(QFrame.StyledPanel)
        self.frame_22.setFrameShadow(QFrame.Raised)
        self.verticalLayout_29 = QVBoxLayout(self.frame_22)
        self.verticalLayout_29.setObjectName(u"verticalLayout_29")
        self.label_12 = QLabel(self.frame_22)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setFont(font)
        self.label_12.setStyleSheet(u"color: #FFFFFF")

        self.verticalLayout_29.addWidget(self.label_12)

        self.Table_Port = QTableWidget(self.frame_22)
        if (self.Table_Port.columnCount() < 5):
            self.Table_Port.setColumnCount(5)
        __qtablewidgetitem14 = QTableWidgetItem()
        self.Table_Port.setHorizontalHeaderItem(0, __qtablewidgetitem14)
        __qtablewidgetitem15 = QTableWidgetItem()
        self.Table_Port.setHorizontalHeaderItem(1, __qtablewidgetitem15)
        __qtablewidgetitem16 = QTableWidgetItem()
        self.Table_Port.setHorizontalHeaderItem(2, __qtablewidgetitem16)
        __qtablewidgetitem17 = QTableWidgetItem()
        self.Table_Port.setHorizontalHeaderItem(3, __qtablewidgetitem17)
        __qtablewidgetitem18 = QTableWidgetItem()
        self.Table_Port.setHorizontalHeaderItem(4, __qtablewidgetitem18)
        self.Table_Port.setObjectName(u"Table_Port")
        self.Table_Port.setFont(font1)
        self.Table_Port.setStyleSheet(u"background-color: rgb(150, 150, 150);\n"
"color: rgb(0, 0, 0);")
        self.Table_Port.setShowGrid(True)
        self.Table_Port.setGridStyle(Qt.SolidLine)
        self.Table_Port.setSortingEnabled(True)
        self.Table_Port.setRowCount(0)

        self.verticalLayout_29.addWidget(self.Table_Port)


        self.horizontalLayout_7.addWidget(self.frame_22)


        self.verticalLayout_13.addWidget(self.frame_6)

        self.frame_7 = QFrame(self.frame_5)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setFont(font1)
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.verticalLayout_14 = QVBoxLayout(self.frame_7)
        self.verticalLayout_14.setSpacing(0)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.verticalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.frame_8 = QFrame(self.frame_7)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.verticalLayout_15 = QVBoxLayout(self.frame_8)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.label_14 = QLabel(self.frame_8)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setFont(font)
        self.label_14.setStyleSheet(u"color: #FFFFFF")

        self.verticalLayout_15.addWidget(self.label_14)

        self.Table_Process = QTableWidget(self.frame_8)
        if (self.Table_Process.columnCount() < 6):
            self.Table_Process.setColumnCount(6)
        __qtablewidgetitem19 = QTableWidgetItem()
        self.Table_Process.setHorizontalHeaderItem(0, __qtablewidgetitem19)
        __qtablewidgetitem20 = QTableWidgetItem()
        self.Table_Process.setHorizontalHeaderItem(1, __qtablewidgetitem20)
        __qtablewidgetitem21 = QTableWidgetItem()
        self.Table_Process.setHorizontalHeaderItem(2, __qtablewidgetitem21)
        __qtablewidgetitem22 = QTableWidgetItem()
        self.Table_Process.setHorizontalHeaderItem(3, __qtablewidgetitem22)
        __qtablewidgetitem23 = QTableWidgetItem()
        self.Table_Process.setHorizontalHeaderItem(4, __qtablewidgetitem23)
        __qtablewidgetitem24 = QTableWidgetItem()
        self.Table_Process.setHorizontalHeaderItem(5, __qtablewidgetitem24)
        self.Table_Process.setObjectName(u"Table_Process")
        self.Table_Process.setMinimumSize(QSize(750, 0))
        self.Table_Process.setMaximumSize(QSize(16777215, 16777215))
        self.Table_Process.setSizeIncrement(QSize(0, 0))
        self.Table_Process.setFont(font1)
        self.Table_Process.setLayoutDirection(Qt.LeftToRight)
        self.Table_Process.setStyleSheet(u"background-color: rgb(150, 150, 150);\n"
"color: rgb(0, 0, 0);")
        self.Table_Process.setSortingEnabled(True)
        self.Table_Process.setRowCount(0)
        self.Table_Process.setColumnCount(6)
        self.Table_Process.horizontalHeader().setHighlightSections(False)

        self.verticalLayout_15.addWidget(self.Table_Process)


        self.verticalLayout_14.addWidget(self.frame_8)


        self.verticalLayout_13.addWidget(self.frame_7)


        self.verticalLayout_7.addWidget(self.frame_5)

        self.stackedWidget.addWidget(self.page_2)
        self.page_3 = QWidget()
        self.page_3.setObjectName(u"page_3")
        self.verticalLayout_8 = QVBoxLayout(self.page_3)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.frame_14 = QFrame(self.page_3)
        self.frame_14.setObjectName(u"frame_14")
        self.frame_14.setFrameShape(QFrame.StyledPanel)
        self.frame_14.setFrameShadow(QFrame.Raised)
        self.verticalLayout_21 = QVBoxLayout(self.frame_14)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.frame_15 = QFrame(self.frame_14)
        self.frame_15.setObjectName(u"frame_15")
        sizePolicy3 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.frame_15.sizePolicy().hasHeightForWidth())
        self.frame_15.setSizePolicy(sizePolicy3)
        self.frame_15.setFrameShape(QFrame.StyledPanel)
        self.frame_15.setFrameShadow(QFrame.Raised)
        self.verticalLayout_16 = QVBoxLayout(self.frame_15)
        self.verticalLayout_16.setSpacing(0)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.verticalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.label_15 = QLabel(self.frame_15)
        self.label_15.setObjectName(u"label_15")
        font2 = QFont()
        font2.setPointSize(14)
        font2.setBold(True)
        font2.setWeight(75)
        self.label_15.setFont(font2)
        self.label_15.setStyleSheet(u"color: #FFFFFF")

        self.verticalLayout_16.addWidget(self.label_15, 0, Qt.AlignTop)

        self.frame_9 = QFrame(self.frame_15)
        self.frame_9.setObjectName(u"frame_9")
        sizePolicy1.setHeightForWidth(self.frame_9.sizePolicy().hasHeightForWidth())
        self.frame_9.setSizePolicy(sizePolicy1)
        self.frame_9.setStyleSheet(u"background-color: rgb(65, 65, 65);")
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.frame_9)
        self.horizontalLayout_8.setSpacing(0)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.frame_24 = QFrame(self.frame_9)
        self.frame_24.setObjectName(u"frame_24")
        sizePolicy2.setHeightForWidth(self.frame_24.sizePolicy().hasHeightForWidth())
        self.frame_24.setSizePolicy(sizePolicy2)
        self.frame_24.setFrameShape(QFrame.StyledPanel)
        self.frame_24.setFrameShadow(QFrame.Raised)
        self.verticalLayout_17 = QVBoxLayout(self.frame_24)
        self.verticalLayout_17.setSpacing(0)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.verticalLayout_17.setContentsMargins(0, 0, 0, 0)
        self.checkBox = QCheckBox(self.frame_24)
        self.checkBox.setObjectName(u"checkBox")
        font3 = QFont()
        font3.setPointSize(10)
        font3.setBold(True)
        font3.setWeight(75)
        self.checkBox.setFont(font3)
        self.checkBox.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.verticalLayout_17.addWidget(self.checkBox)

        self.checkBox_2 = QCheckBox(self.frame_24)
        self.checkBox_2.setObjectName(u"checkBox_2")
        self.checkBox_2.setFont(font3)
        self.checkBox_2.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.verticalLayout_17.addWidget(self.checkBox_2)

        self.checkBox_3 = QCheckBox(self.frame_24)
        self.checkBox_3.setObjectName(u"checkBox_3")
        self.checkBox_3.setFont(font3)
        self.checkBox_3.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.verticalLayout_17.addWidget(self.checkBox_3)

        self.checkBox_4 = QCheckBox(self.frame_24)
        self.checkBox_4.setObjectName(u"checkBox_4")
        self.checkBox_4.setFont(font3)
        self.checkBox_4.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.verticalLayout_17.addWidget(self.checkBox_4)

        self.checkBox_5 = QCheckBox(self.frame_24)
        self.checkBox_5.setObjectName(u"checkBox_5")
        self.checkBox_5.setFont(font3)
        self.checkBox_5.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.verticalLayout_17.addWidget(self.checkBox_5)


        self.horizontalLayout_8.addWidget(self.frame_24, 0, Qt.AlignHCenter)

        self.frame_25 = QFrame(self.frame_9)
        self.frame_25.setObjectName(u"frame_25")
        sizePolicy2.setHeightForWidth(self.frame_25.sizePolicy().hasHeightForWidth())
        self.frame_25.setSizePolicy(sizePolicy2)
        self.frame_25.setFrameShape(QFrame.StyledPanel)
        self.frame_25.setFrameShadow(QFrame.Raised)
        self.verticalLayout_31 = QVBoxLayout(self.frame_25)
        self.verticalLayout_31.setSpacing(0)
        self.verticalLayout_31.setObjectName(u"verticalLayout_31")
        self.verticalLayout_31.setContentsMargins(0, 0, 0, 0)
        self.checkBox_7 = QCheckBox(self.frame_25)
        self.checkBox_7.setObjectName(u"checkBox_7")
        self.checkBox_7.setFont(font3)
        self.checkBox_7.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.verticalLayout_31.addWidget(self.checkBox_7)

        self.checkBox_6 = QCheckBox(self.frame_25)
        self.checkBox_6.setObjectName(u"checkBox_6")
        self.checkBox_6.setFont(font3)
        self.checkBox_6.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.verticalLayout_31.addWidget(self.checkBox_6)

        self.checkBox_8 = QCheckBox(self.frame_25)
        self.checkBox_8.setObjectName(u"checkBox_8")
        self.checkBox_8.setFont(font3)
        self.checkBox_8.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.verticalLayout_31.addWidget(self.checkBox_8)

        self.checkBox_9 = QCheckBox(self.frame_25)
        self.checkBox_9.setObjectName(u"checkBox_9")
        self.checkBox_9.setFont(font3)
        self.checkBox_9.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.verticalLayout_31.addWidget(self.checkBox_9)

        self.checkBox_10 = QCheckBox(self.frame_25)
        self.checkBox_10.setObjectName(u"checkBox_10")
        self.checkBox_10.setFont(font3)
        self.checkBox_10.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.verticalLayout_31.addWidget(self.checkBox_10)


        self.horizontalLayout_8.addWidget(self.frame_25, 0, Qt.AlignHCenter)

        self.frame_26 = QFrame(self.frame_9)
        self.frame_26.setObjectName(u"frame_26")
        sizePolicy2.setHeightForWidth(self.frame_26.sizePolicy().hasHeightForWidth())
        self.frame_26.setSizePolicy(sizePolicy2)
        self.frame_26.setFrameShape(QFrame.StyledPanel)
        self.frame_26.setFrameShadow(QFrame.Raised)
        self.verticalLayout_32 = QVBoxLayout(self.frame_26)
        self.verticalLayout_32.setSpacing(0)
        self.verticalLayout_32.setObjectName(u"verticalLayout_32")
        self.verticalLayout_32.setContentsMargins(0, 0, 0, 0)
        self.checkBox_12 = QCheckBox(self.frame_26)
        self.checkBox_12.setObjectName(u"checkBox_12")
        self.checkBox_12.setFont(font3)
        self.checkBox_12.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.verticalLayout_32.addWidget(self.checkBox_12)

        self.checkBox_11 = QCheckBox(self.frame_26)
        self.checkBox_11.setObjectName(u"checkBox_11")
        self.checkBox_11.setFont(font3)
        self.checkBox_11.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.verticalLayout_32.addWidget(self.checkBox_11)

        self.checkBox_13 = QCheckBox(self.frame_26)
        self.checkBox_13.setObjectName(u"checkBox_13")
        self.checkBox_13.setFont(font3)
        self.checkBox_13.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.verticalLayout_32.addWidget(self.checkBox_13)

        self.checkBox_14 = QCheckBox(self.frame_26)
        self.checkBox_14.setObjectName(u"checkBox_14")
        self.checkBox_14.setFont(font3)
        self.checkBox_14.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.verticalLayout_32.addWidget(self.checkBox_14)

        self.checkBox_15 = QCheckBox(self.frame_26)
        self.checkBox_15.setObjectName(u"checkBox_15")
        self.checkBox_15.setFont(font3)
        self.checkBox_15.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.verticalLayout_32.addWidget(self.checkBox_15)


        self.horizontalLayout_8.addWidget(self.frame_26, 0, Qt.AlignHCenter)


        self.verticalLayout_16.addWidget(self.frame_9)


        self.verticalLayout_21.addWidget(self.frame_15)

        self.frame_16 = QFrame(self.frame_14)
        self.frame_16.setObjectName(u"frame_16")
        self.frame_16.setFrameShape(QFrame.StyledPanel)
        self.frame_16.setFrameShadow(QFrame.Raised)
        self.verticalLayout_22 = QVBoxLayout(self.frame_16)
        self.verticalLayout_22.setSpacing(0)
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.verticalLayout_22.setContentsMargins(0, 0, 0, 0)
        self.pushButton_3 = QPushButton(self.frame_16)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setFont(font)
        self.pushButton_3.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 255, 255);")

        self.verticalLayout_22.addWidget(self.pushButton_3)


        self.verticalLayout_21.addWidget(self.frame_16, 0, Qt.AlignRight|Qt.AlignVCenter)

        self.frame_17 = QFrame(self.frame_14)
        self.frame_17.setObjectName(u"frame_17")
        sizePolicy1.setHeightForWidth(self.frame_17.sizePolicy().hasHeightForWidth())
        self.frame_17.setSizePolicy(sizePolicy1)
        self.frame_17.setFrameShape(QFrame.StyledPanel)
        self.frame_17.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_17)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.frame_18 = QFrame(self.frame_17)
        self.frame_18.setObjectName(u"frame_18")
        sizePolicy1.setHeightForWidth(self.frame_18.sizePolicy().hasHeightForWidth())
        self.frame_18.setSizePolicy(sizePolicy1)
        self.frame_18.setFrameShape(QFrame.StyledPanel)
        self.frame_18.setFrameShadow(QFrame.Raised)
        self.verticalLayout_25 = QVBoxLayout(self.frame_18)
        self.verticalLayout_25.setObjectName(u"verticalLayout_25")
        self.frame_20 = QFrame(self.frame_18)
        self.frame_20.setObjectName(u"frame_20")
        self.frame_20.setFrameShape(QFrame.StyledPanel)
        self.frame_20.setFrameShadow(QFrame.Raised)
        self.verticalLayout_26 = QVBoxLayout(self.frame_20)
        self.verticalLayout_26.setSpacing(0)
        self.verticalLayout_26.setObjectName(u"verticalLayout_26")
        self.verticalLayout_26.setContentsMargins(0, 0, 0, 0)
        self.label_3 = QLabel(self.frame_20)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font2)
        self.label_3.setStyleSheet(u"color: #FFFFFF")

        self.verticalLayout_26.addWidget(self.label_3)

        self.textBrowser_2 = QTextBrowser(self.frame_20)
        self.textBrowser_2.setObjectName(u"textBrowser_2")

        self.verticalLayout_26.addWidget(self.textBrowser_2)


        self.verticalLayout_25.addWidget(self.frame_20)


        self.horizontalLayout_6.addWidget(self.frame_18, 0, Qt.AlignLeft)

        self.frame_19 = QFrame(self.frame_17)
        self.frame_19.setObjectName(u"frame_19")
        self.frame_19.setFrameShape(QFrame.StyledPanel)
        self.frame_19.setFrameShadow(QFrame.Raised)
        self.verticalLayout_23 = QVBoxLayout(self.frame_19)
        self.verticalLayout_23.setSpacing(0)
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.verticalLayout_23.setContentsMargins(0, 0, 0, 0)
        self.frame_21 = QFrame(self.frame_19)
        self.frame_21.setObjectName(u"frame_21")
        sizePolicy1.setHeightForWidth(self.frame_21.sizePolicy().hasHeightForWidth())
        self.frame_21.setSizePolicy(sizePolicy1)
        self.frame_21.setFrameShape(QFrame.StyledPanel)
        self.frame_21.setFrameShadow(QFrame.Raised)
        self.verticalLayout_24 = QVBoxLayout(self.frame_21)
        self.verticalLayout_24.setObjectName(u"verticalLayout_24")
        self.label_9 = QLabel(self.frame_21)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setFont(font2)
        self.label_9.setStyleSheet(u"color: #FFFFFF")

        self.verticalLayout_24.addWidget(self.label_9)

        self.Table_Deleted = QTableWidget(self.frame_21)
        if (self.Table_Deleted.columnCount() < 3):
            self.Table_Deleted.setColumnCount(3)
        __qtablewidgetitem25 = QTableWidgetItem()
        self.Table_Deleted.setHorizontalHeaderItem(0, __qtablewidgetitem25)
        __qtablewidgetitem26 = QTableWidgetItem()
        self.Table_Deleted.setHorizontalHeaderItem(1, __qtablewidgetitem26)
        __qtablewidgetitem27 = QTableWidgetItem()
        self.Table_Deleted.setHorizontalHeaderItem(2, __qtablewidgetitem27)
        self.Table_Deleted.setObjectName(u"Table_Deleted")
        self.Table_Deleted.setStyleSheet(u"background-color: rgb(150, 150, 150);\n"
"color: rgb(0, 0, 0);")
        self.Table_Deleted.setSortingEnabled(True)
        self.Table_Deleted.horizontalHeader().setCascadingSectionResizes(False)
        self.Table_Deleted.verticalHeader().setCascadingSectionResizes(False)

        self.verticalLayout_24.addWidget(self.Table_Deleted)


        self.verticalLayout_23.addWidget(self.frame_21)


        self.horizontalLayout_6.addWidget(self.frame_19)


        self.verticalLayout_21.addWidget(self.frame_17)


        self.verticalLayout_8.addWidget(self.frame_14)

        self.stackedWidget.addWidget(self.page_3)
        self.page_4 = QWidget()
        self.page_4.setObjectName(u"page_4")
        self.verticalLayout_9 = QVBoxLayout(self.page_4)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.frame_27 = QFrame(self.page_4)
        self.frame_27.setObjectName(u"frame_27")
        self.frame_27.setFrameShape(QFrame.StyledPanel)
        self.frame_27.setFrameShadow(QFrame.Raised)
        self.verticalLayout_33 = QVBoxLayout(self.frame_27)
        self.verticalLayout_33.setSpacing(0)
        self.verticalLayout_33.setObjectName(u"verticalLayout_33")
        self.verticalLayout_33.setContentsMargins(0, 0, 0, 0)
        self.frame_28 = QFrame(self.frame_27)
        self.frame_28.setObjectName(u"frame_28")
        self.frame_28.setFrameShape(QFrame.StyledPanel)
        self.frame_28.setFrameShadow(QFrame.Raised)
        self.verticalLayout_34 = QVBoxLayout(self.frame_28)
        self.verticalLayout_34.setObjectName(u"verticalLayout_34")
        self.frame_30 = QFrame(self.frame_28)
        self.frame_30.setObjectName(u"frame_30")
        self.frame_30.setFrameShape(QFrame.StyledPanel)
        self.frame_30.setFrameShadow(QFrame.Raised)
        self.verticalLayout_37 = QVBoxLayout(self.frame_30)
        self.verticalLayout_37.setObjectName(u"verticalLayout_37")
        self.label_17 = QLabel(self.frame_30)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setFont(font2)
        self.label_17.setStyleSheet(u"color: #FFFFFF")

        self.verticalLayout_37.addWidget(self.label_17)

        self.frame_33 = QFrame(self.frame_30)
        self.frame_33.setObjectName(u"frame_33")
        self.frame_33.setFrameShape(QFrame.StyledPanel)
        self.frame_33.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.frame_33)
        self.gridLayout.setObjectName(u"gridLayout")
        self.pushButton_EventLog = QPushButton(self.frame_33)
        self.pushButton_EventLog.setObjectName(u"pushButton_EventLog")
        self.pushButton_EventLog.setFont(font)
        self.pushButton_EventLog.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.gridLayout.addWidget(self.pushButton_EventLog, 0, 0, 1, 1)

        self.pushButton_Prefetch = QPushButton(self.frame_33)
        self.pushButton_Prefetch.setObjectName(u"pushButton_Prefetch")
        self.pushButton_Prefetch.setFont(font)
        self.pushButton_Prefetch.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.gridLayout.addWidget(self.pushButton_Prefetch, 0, 1, 1, 1)

        self.pushButton_Services = QPushButton(self.frame_33)
        self.pushButton_Services.setObjectName(u"pushButton_Services")
        self.pushButton_Services.setFont(font)
        self.pushButton_Services.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.gridLayout.addWidget(self.pushButton_Services, 0, 2, 1, 1)

        self.pushButton_Browser = QPushButton(self.frame_33)
        self.pushButton_Browser.setObjectName(u"pushButton_Browser")
        self.pushButton_Browser.setFont(font)
        self.pushButton_Browser.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.gridLayout.addWidget(self.pushButton_Browser, 0, 3, 1, 1)

        self.pushButton_Scheduler = QPushButton(self.frame_33)
        self.pushButton_Scheduler.setObjectName(u"pushButton_Scheduler")
        self.pushButton_Scheduler.setFont(font)
        self.pushButton_Scheduler.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.gridLayout.addWidget(self.pushButton_Scheduler, 1, 0, 1, 1)

        self.pushButton_Logfile = QPushButton(self.frame_33)
        self.pushButton_Logfile.setObjectName(u"pushButton_Logfile")
        self.pushButton_Logfile.setFont(font)
        self.pushButton_Logfile.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.gridLayout.addWidget(self.pushButton_Logfile, 1, 1, 1, 1)

        self.pushButton_UsnJrnl = QPushButton(self.frame_33)
        self.pushButton_UsnJrnl.setObjectName(u"pushButton_UsnJrnl")
        self.pushButton_UsnJrnl.setFont(font)
        self.pushButton_UsnJrnl.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.gridLayout.addWidget(self.pushButton_UsnJrnl, 1, 2, 1, 1)

        self.pushButton_11 = QPushButton(self.frame_33)
        self.pushButton_11.setObjectName(u"pushButton_11")
        self.pushButton_11.setFont(font)
        self.pushButton_11.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.gridLayout.addWidget(self.pushButton_11, 1, 3, 1, 1)

        self.pushButton_13 = QPushButton(self.frame_33)
        self.pushButton_13.setObjectName(u"pushButton_13")
        self.pushButton_13.setFont(font)
        self.pushButton_13.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.gridLayout.addWidget(self.pushButton_13, 0, 4, 1, 1)

        self.pushButton_12 = QPushButton(self.frame_33)
        self.pushButton_12.setObjectName(u"pushButton_12")
        self.pushButton_12.setFont(font)
        self.pushButton_12.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.gridLayout.addWidget(self.pushButton_12, 1, 4, 1, 1)


        self.verticalLayout_37.addWidget(self.frame_33)


        self.verticalLayout_34.addWidget(self.frame_30)


        self.verticalLayout_33.addWidget(self.frame_28)

        self.frame_29 = QFrame(self.frame_27)
        self.frame_29.setObjectName(u"frame_29")
        self.frame_29.setFrameShape(QFrame.StyledPanel)
        self.frame_29.setFrameShadow(QFrame.Raised)
        self.verticalLayout_35 = QVBoxLayout(self.frame_29)
        self.verticalLayout_35.setObjectName(u"verticalLayout_35")
        self.frame_32 = QFrame(self.frame_29)
        self.frame_32.setObjectName(u"frame_32")
        self.frame_32.setFrameShape(QFrame.StyledPanel)
        self.frame_32.setFrameShadow(QFrame.Raised)
        self.verticalLayout_36 = QVBoxLayout(self.frame_32)
        self.verticalLayout_36.setObjectName(u"verticalLayout_36")
        self.label_16 = QLabel(self.frame_32)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setFont(font2)
        self.label_16.setStyleSheet(u"color: #FFFFFF")

        self.verticalLayout_36.addWidget(self.label_16)

        self.Table_Parsing = QTableWidget(self.frame_32)
        if (self.Table_Parsing.columnCount() < 3):
            self.Table_Parsing.setColumnCount(3)
        __qtablewidgetitem28 = QTableWidgetItem()
        self.Table_Parsing.setHorizontalHeaderItem(0, __qtablewidgetitem28)
        __qtablewidgetitem29 = QTableWidgetItem()
        self.Table_Parsing.setHorizontalHeaderItem(1, __qtablewidgetitem29)
        __qtablewidgetitem30 = QTableWidgetItem()
        self.Table_Parsing.setHorizontalHeaderItem(2, __qtablewidgetitem30)
        self.Table_Parsing.setObjectName(u"Table_Parsing")
        self.Table_Parsing.setMinimumSize(QSize(750, 0))
        self.Table_Parsing.setMaximumSize(QSize(16777215, 16777215))
        self.Table_Parsing.setSizeIncrement(QSize(0, 0))
        self.Table_Parsing.setFont(font1)
        self.Table_Parsing.setLayoutDirection(Qt.LeftToRight)
        self.Table_Parsing.setStyleSheet(u"background-color: rgb(150, 150, 150);\n"
"color: rgb(0, 0, 0);")
        self.Table_Parsing.setSortingEnabled(True)
        self.Table_Parsing.setRowCount(0)
        self.Table_Parsing.setColumnCount(3)
        self.Table_Parsing.horizontalHeader().setHighlightSections(False)

        self.verticalLayout_36.addWidget(self.Table_Parsing)


        self.verticalLayout_35.addWidget(self.frame_32)


        self.verticalLayout_33.addWidget(self.frame_29)


        self.verticalLayout_9.addWidget(self.frame_27)

        self.stackedWidget.addWidget(self.page_4)
        self.page_5 = QWidget()
        self.page_5.setObjectName(u"page_5")
        self.verticalLayout_10 = QVBoxLayout(self.page_5)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.label_5 = QLabel(self.page_5)
        self.label_5.setObjectName(u"label_5")
        font4 = QFont()
        font4.setPointSize(40)
        self.label_5.setFont(font4)
        self.label_5.setStyleSheet(u"color: #FFFFFF")
        self.label_5.setAlignment(Qt.AlignCenter)

        self.verticalLayout_10.addWidget(self.label_5)

        self.stackedWidget.addWidget(self.page_5)

        self.verticalLayout_5.addWidget(self.stackedWidget)


        self.horizontalLayout_2.addWidget(self.frame_pages)


        self.verticalLayout.addWidget(self.Content)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        MainWindow.setWindowFilePath(QCoreApplication.translate("MainWindow", u"color: #FFFFFF", None))
        self.Btn_Toggle.setText("")
        self.btn_page_main.setText(QCoreApplication.translate("MainWindow", u"Main", None))
        self.btn_page_live.setText(QCoreApplication.translate("MainWindow", u"Live", None))
        self.btn_page_collection.setText(QCoreApplication.translate("MainWindow", u"Collection", None))
        self.btn_page_analysis.setText(QCoreApplication.translate("MainWindow", u"Analysis", None))
        self.btn_page_review.setText(QCoreApplication.translate("MainWindow", u"Review", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"SYSTEM INFORMATION", None))
        ___qtablewidgetitem = self.Table_System.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"HOSTNAME", None));
        ___qtablewidgetitem1 = self.Table_System.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"ACCOUNT", None));
        ___qtablewidgetitem2 = self.Table_System.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"OSVERSION", None));
        ___qtablewidgetitem3 = self.Table_System.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"OSBIT", None));
        ___qtablewidgetitem4 = self.Table_System.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"OSBOOTIME", None));
        ___qtablewidgetitem5 = self.Table_System.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"RUNTIME", None));
        ___qtablewidgetitem6 = self.Table_System.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"TIMEZONE", None));
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"INSTALLED SOFTWARE VERSION", None))
        ___qtablewidgetitem7 = self.Table_Software.horizontalHeaderItem(0)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"SWNAME", None));
        ___qtablewidgetitem8 = self.Table_Software.horizontalHeaderItem(1)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"SWVERSION", None));
        ___qtablewidgetitem9 = self.Table_Software.horizontalHeaderItem(2)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"SWINSTALLDATE", None));
        ___qtablewidgetitem10 = self.Table_Software.horizontalHeaderItem(3)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("MainWindow", u"SWPUBLISHER", None));
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"SAVE PATH", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"Browser", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"START", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"NETWORK INFO", None))
        ___qtablewidgetitem11 = self.Table_Network.horizontalHeaderItem(0)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("MainWindow", u"NETCARD", None));
        ___qtablewidgetitem12 = self.Table_Network.horizontalHeaderItem(1)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("MainWindow", u"IPv4", None));
        ___qtablewidgetitem13 = self.Table_Network.horizontalHeaderItem(2)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("MainWindow", u"MACADDR", None));
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"PORT INFO", None))
        ___qtablewidgetitem14 = self.Table_Port.horizontalHeaderItem(0)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("MainWindow", u"PROTOCOL", None));
        ___qtablewidgetitem15 = self.Table_Port.horizontalHeaderItem(1)
        ___qtablewidgetitem15.setText(QCoreApplication.translate("MainWindow", u"LOCALADDR", None));
        ___qtablewidgetitem16 = self.Table_Port.horizontalHeaderItem(2)
        ___qtablewidgetitem16.setText(QCoreApplication.translate("MainWindow", u"EXTERNALADDR", None));
        ___qtablewidgetitem17 = self.Table_Port.horizontalHeaderItem(3)
        ___qtablewidgetitem17.setText(QCoreApplication.translate("MainWindow", u"STATUS", None));
        ___qtablewidgetitem18 = self.Table_Port.horizontalHeaderItem(4)
        ___qtablewidgetitem18.setText(QCoreApplication.translate("MainWindow", u"PID", None));
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"PROCESS INFO", None))
        ___qtablewidgetitem19 = self.Table_Process.horizontalHeaderItem(0)
        ___qtablewidgetitem19.setText(QCoreApplication.translate("MainWindow", u"PSNAME", None));
        ___qtablewidgetitem20 = self.Table_Process.horizontalHeaderItem(1)
        ___qtablewidgetitem20.setText(QCoreApplication.translate("MainWindow", u"PPSID", None));
        ___qtablewidgetitem21 = self.Table_Process.horizontalHeaderItem(2)
        ___qtablewidgetitem21.setText(QCoreApplication.translate("MainWindow", u"PSPPID", None));
        ___qtablewidgetitem22 = self.Table_Process.horizontalHeaderItem(3)
        ___qtablewidgetitem22.setText(QCoreApplication.translate("MainWindow", u"PSTHDS", None));
        ___qtablewidgetitem23 = self.Table_Process.horizontalHeaderItem(4)
        ___qtablewidgetitem23.setText(QCoreApplication.translate("MainWindow", u"PSHNDS", None));
        ___qtablewidgetitem24 = self.Table_Process.horizontalHeaderItem(5)
        ___qtablewidgetitem24.setText(QCoreApplication.translate("MainWindow", u"PSTIME", None));
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"Collected Artifact", None))
        self.checkBox.setText(QCoreApplication.translate("MainWindow", u"RDP", None))
        self.checkBox_2.setText(QCoreApplication.translate("MainWindow", u"WER", None))
        self.checkBox_3.setText(QCoreApplication.translate("MainWindow", u"Scheduler", None))
        self.checkBox_4.setText(QCoreApplication.translate("MainWindow", u"Scheduler", None))
        self.checkBox_5.setText(QCoreApplication.translate("MainWindow", u"Scheduler", None))
        self.checkBox_7.setText(QCoreApplication.translate("MainWindow", u"Scheduler", None))
        self.checkBox_6.setText(QCoreApplication.translate("MainWindow", u"Scheduler", None))
        self.checkBox_8.setText(QCoreApplication.translate("MainWindow", u"Scheduler", None))
        self.checkBox_9.setText(QCoreApplication.translate("MainWindow", u"Scheduler", None))
        self.checkBox_10.setText(QCoreApplication.translate("MainWindow", u"Scheduler", None))
        self.checkBox_12.setText(QCoreApplication.translate("MainWindow", u"Scheduler", None))
        self.checkBox_11.setText(QCoreApplication.translate("MainWindow", u"Scheduler", None))
        self.checkBox_13.setText(QCoreApplication.translate("MainWindow", u"Scheduler", None))
        self.checkBox_14.setText(QCoreApplication.translate("MainWindow", u"Scheduler", None))
        self.checkBox_15.setText(QCoreApplication.translate("MainWindow", u"Scheduler", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"Analysis", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Collected Chain", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Deleted List", None))
        ___qtablewidgetitem25 = self.Table_Deleted.horizontalHeaderItem(0)
        ___qtablewidgetitem25.setText(QCoreApplication.translate("MainWindow", u"Timestamp", None));
        ___qtablewidgetitem26 = self.Table_Deleted.horizontalHeaderItem(1)
        ___qtablewidgetitem26.setText(QCoreApplication.translate("MainWindow", u"FileName", None));
        ___qtablewidgetitem27 = self.Table_Deleted.horizontalHeaderItem(2)
        ___qtablewidgetitem27.setText(QCoreApplication.translate("MainWindow", u"EventInfo", None));
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"Collected Artifact", None))
        self.pushButton_EventLog.setText(QCoreApplication.translate("MainWindow", u"EVENT LOG", None))
        self.pushButton_Prefetch.setText(QCoreApplication.translate("MainWindow", u"PREFETCH", None))
        self.pushButton_Services.setText(QCoreApplication.translate("MainWindow", u"SERVICES", None))
        self.pushButton_Browser.setText(QCoreApplication.translate("MainWindow", u"BROWSER", None))
        self.pushButton_Scheduler.setText(QCoreApplication.translate("MainWindow", u"SCHEDULER", None))
        self.pushButton_Logfile.setText(QCoreApplication.translate("MainWindow", u"LOGFILE", None))
        self.pushButton_UsnJrnl.setText(QCoreApplication.translate("MainWindow", u"USNJRNL", None))
        self.pushButton_11.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_13.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_12.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"Artifact Detail", None))
        ___qtablewidgetitem28 = self.Table_Parsing.horizontalHeaderItem(0)
        ___qtablewidgetitem28.setText(QCoreApplication.translate("MainWindow", u"1", None));
        ___qtablewidgetitem29 = self.Table_Parsing.horizontalHeaderItem(1)
        ___qtablewidgetitem29.setText(QCoreApplication.translate("MainWindow", u"2", None));
        ___qtablewidgetitem30 = self.Table_Parsing.horizontalHeaderItem(2)
        ___qtablewidgetitem30.setText(QCoreApplication.translate("MainWindow", u"3", None));
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"PAGE 5", None))
    # retranslateUi

