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
        # table.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        # table.resizeColumnsToContents()




