import sqlite3

from main import *
from ui_main import *
import os

class UIFunctions(MainWindow):

    def toggleMenu(self, maxWidth, enable):
        if enable:

            # GET WIDTH
            width = self.ui.frame_left_menu.width()
            maxExtend = maxWidth
            standard = 70

            # SET MAX WIDTH
            if width == 70:
                widthExtended = maxExtend
            else:
                widthExtended = standard

            # ANIMATION
            self.animation = QPropertyAnimation(self.ui.frame_left_menu, b"minimumWidth")
            self.animation.setDuration(400)
            self.animation.setStartValue(width)
            self.animation.setEndValue(widthExtended)
            self.animation.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
            self.animation.start()


    def folder_load(self):
        FileFolder = QFileDialog.getExistingDirectory(self, "Find Folder")

        buttonReply = QMessageBox.information(
            self, "QMessage Demonstration Menu", FileFolder + " has been selected", QMessageBox.Ok
        )
        self.statusBar().showMessage(FileFolder)

    # def loading(self):
    #     self.ui.

    # def textbox(self):
    #     self.ui.textBrowser.moveCursor(QtGui.QTextCursor.End)

    def report(self, query):
        con = sqlite3.connect("test.db")
        cur = con.cursor()
        sql = cur.execute(query)

        chainnumber = cur.execute("SELECT chain_number FROM Chain_art")
        wer = []
        for i in chainnumber:
            add = cur.execute("select * from Chain_art WHERE chain_number = " +str(i[0])+" and description=1000 or chain_number =" +str(i[0])+ " and description=1001 ORDER by time")
            wer.append(add)
        print(wer)

        new = self.ui.listWidget #유입
        create = self.ui.listWidget_2 #발현
        run = self.ui.listWidget_3 #실행
        share = self.ui.listWidget_4 #연결
        ing = self.ui.listWidget_5 #유지


        cur.close()
        con.close()


    def data_load(self, query, sel):
        con = sqlite3.connect("test.db")
        cur = con.cursor()
        sql = cur.execute(query)

        system = self.ui.Table_System
        soft = self.ui.Table_Software
        net = self.ui.Table_Network
        port = self.ui.Table_Port
        pro = self.ui.Table_Process
        delete = self.ui.Table_Deleted
        parsing = self.ui.Table_Parsing


        if sel == 1:
            table = system
        elif sel == 2:
            table = soft
        elif sel == 3:
            table = net
        elif sel == 4:
            table = port
        elif sel == 5:
            table = pro
        elif sel == 6:
            table = delete
        elif sel == 7:
            table = parsing



        table.setRowCount(0)
        for row, form in enumerate(sql):
            table.insertRow(row)
            for column, data in enumerate(form):
                cell = QtWidgets.QTableWidgetItem(str(data))
                table.setItem(row, column, cell)
        cur.close()
        con.close()
        # table.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        # table.resizeColumnsToContents()




