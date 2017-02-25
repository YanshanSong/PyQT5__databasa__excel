# -*- coding: utf-8 -*-

"""
Module implementing MainWindow.
"""

from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui, QtWidgets
from Ui_main import Ui_MainWindow
from Ui_main2 import Ui_Main2Window 
import pymssql
import _mssql
import uuid
import decimal

import xlwt

host = ""
username = ""
password = ""
my_directory_path = ""

#----------------------Main2Window---------------------------
class Main2Window(QMainWindow, Ui_Main2Window):
    """
    Class documentation goes here.
    """
    def __init__(self, parent=None):
        """
        Constructor
        
        @param parent reference to the parent widget
        @type QWidget
        """
        super(Main2Window, self).__init__(parent)
        self.setupUi(self)
        
    @pyqtSlot()
    def on_toolButton_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        global my_directory_path
        my_directory_path = QtWidgets.QFileDialog.getExistingDirectory( self, u'选择文件夹', '/')
        #print(my_directory_path)
        self.lineEdit.setText(my_directory_path)
        
    
    @pyqtSlot()
    def on_pushButton_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        if not my_directory_path:    
            my_button_3 = QMessageBox.warning(self, 'warning', '请选择文件保存路径')
        else:
            try:
                connection = pymssql.connect(host=host,user=username,password=password,charset="UTF8")
                cursor = connection.cursor()
        
	            # 获取数据库中所有表名
                sql = "SELECT Name FROM hospital_test..SysObjects Where XType='U' ORDER BY Name "    
                cursor.execute(sql)
                table_info = cursor.fetchall()
                table = []
                for each in table_info:
                    table.append(each[0])
		            
                #使用指定数据库 
                sql = "use hospital_test"
                cursor.execute(sql)
		        
		        #取出第一张表的数据
                sql = "select * from %s order by '个人剂量计编号'"% table[0]
                cursor.execute(sql)
                result = cursor.fetchall()
                print(result)
                namefields = cursor.description
                namelist = []

                for i in range(len(result)):
                    app = { }
                    for j in range(len(result[i])):
                        app[namefields[j][0]] =  result[i][j]
                    namelist.append(app)
		       
		        #取出第二张表的数据
                sql = "select * from %s order by '个人剂量计编号'" % table[1]
                cursor.execute(sql)
                result = cursor.fetchall()
                datafields = cursor.description
                datalist = []

                for i in range(len(result)):
                    app = { }
                    for j in range(len(result[i])):
                        app[datafields[j][0]] =  result[i][j]
                    datalist.append(app)
		        
		        #根据关键字归类
                cs_first_name = []
                cs_second_name= []
                xc_third_name = []
                for i in range(len(namelist)):
                    if(namelist[i]["个人剂量计编号"][:12] == "JS-SZ-CS-033"):
                        cs_first_name.append(namelist[i])
                    elif(namelist[i]["个人剂量计编号"][:12] == "JS-SZ-CS-034"):
                        cs_second_name.append(namelist[i])
                    else:
                        xc_third_name.append(namelist[i])

		        #print(len(cs_first_name),len(cs_second_name),len(xc_third_name))

                cs_first_data = []
                cs_second_data = []
                xc_third_data = []
                for i in range(len(datalist)):
                    if(datalist[i]["个人剂量计编号"][:12] == "JS-SZ-CS-033"):
                        cs_first_data.append(datalist[i])
                    elif(datalist[i]["个人剂量计编号"][:12] == "JS-SZ-CS-034"):
                        cs_second_data.append(datalist[i])
                    else:
                        xc_third_data.append(datalist[i]) 
		        #print(len(cs_first_data),len(cs_second_data),len(xc_third_data))  

		        #向excel写入数据
		        #名单
                workbook_cs_first_name = xlwt.Workbook()
                sheet = workbook_cs_first_name.add_sheet('sheet1')
                for i in range(len(namefields)):
                    sheet.write(0,i,namefields[i][0])

                for row in range(len(cs_first_name)):
                    for col in range(len(namefields)):
                        sheet.write(row+1,col,cs_first_name[row][namefields[col][0]])

                workbook_cs_first_name.save(my_directory_path + "/常熟市第一人民医院名单.xls")

                workbook_cs_second_name = xlwt.Workbook()
                sheet = workbook_cs_second_name.add_sheet('sheet1')
                for i in range(len(namefields)):
                    sheet.write(0,i,namefields[i][0])

                for row in range(len(cs_second_name)):
                    for col in range(len(namefields)):
                        sheet.write(row+1,col,cs_second_name[row][namefields[col][0]])
                workbook_cs_second_name.save(my_directory_path + "/常熟市第二人民医院名单.xls")

                workbook_xc_third_name = xlwt.Workbook()
                sheet = workbook_xc_third_name.add_sheet('sheet1')
                for i in range(len(namefields)):
                    sheet.write(0,i,namefields[i][0])

                for row in range(len(xc_third_name)):
                    for col in range(len(namefields)):
                        sheet.write(row+1,col,xc_third_name[row][namefields[col][0]])
                workbook_xc_third_name.save(my_directory_path + "/苏州市相城区人民医院名单.xls")

		        #数据
                workbook_cs_first_data = xlwt.Workbook()
                sheet = workbook_cs_first_data.add_sheet('sheet1')
                for i in range(len(datafields)):
                    sheet.write(0,i,datafields[i][0])
 
                for row in range(len(cs_first_data)):
                    for col in range(len(datafields)):
                        sheet.write(row+1,col,cs_first_data[row][datafields[col][0]])

                workbook_cs_first_data.save(my_directory_path + "/常熟市第一人民医院数据.xls")

                workbook_cs_second_data = xlwt.Workbook()
                sheet = workbook_cs_second_data.add_sheet('sheet1')
                for i in range(len(datafields)):
                    sheet.write(0,i,datafields[i][0])

                for row in range(len(cs_second_data)):
                    for col in range(len(datafields)):
                        sheet.write(row+1,col,cs_second_data[row][datafields[col][0]])
                workbook_cs_second_data.save(my_directory_path + "/常熟市第二人民医院数据.xls")

                workbook_xc_third_data = xlwt.Workbook()
                sheet = workbook_xc_third_data.add_sheet('sheet1')
                for i in range(len(datafields)):
                    sheet.write(0,i,datafields[i][0])

                for row in range(len(xc_third_data)):
                    for col in range(len(datafields)):
                        sheet.write(row+1,col,xc_third_data[row][datafields[col][0]])
                workbook_xc_third_data.save(my_directory_path + "/苏州市相城区人民医院数据.xls") 	
                
                my_button_4= QMessageBox.information(self, 'success', '导出成功')
                
            except Exception:
                my_button_5 = QMessageBox.warning(self, 'warning', '导出失败')        
        
        

#----------------------MainWindow---------------------------
class MainWindow(QMainWindow, Ui_MainWindow):
    """
    Class documentation goes here.
    """
    def __init__(self, parent=None):
        """
        Constructor
        
        @param parent reference to the parent widget
        @type QWidget
        """
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        self.lineEdit.returnPressed.connect(self.on_pushButton_clicked)
        self.lineEdit_2.returnPressed.connect(self.on_pushButton_clicked)
        self.lineEdit_3.returnPressed.connect(self.on_pushButton_clicked)
    
    @pyqtSlot()
    def on_pushButton_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        global host
        host = self.lineEdit.text().strip()
        global username 
        username = self.lineEdit_2.text().strip()
        global password 
        password = self.lineEdit_3.text().strip()
        print(host,username,password)
        
        if (not host) or (not username) or (not password):
            my_button_1 = QMessageBox.warning(self, 'warning', '请填写完整连接信息')                
        else:    
            try:
                connection = pymssql.connect(host=host,user=username,password=password,charset="UTF8")
            except Exception:
                my_button_2 = QMessageBox.warning(self, 'warning', '连接失败，请检查连接信息')
            else:
                self.hide()
                self.main2window = Main2Window()
                self.main2window.show()

                cursor = connection.cursor()

                sql = "SELECT Name FROM hospital_test..SysObjects Where XType='U' ORDER BY Name "
                cursor.execute(sql)
                table_info = cursor.fetchall()

                for each in table_info:
                	self.main2window.textBrowser.append(each[0])
                    
                excel_list = ["常熟市第一人民医院名单.xls", "常熟市第一人民医院数据.xls", "常熟市第二人民医院名单.xls","常熟市第二人民医院数据.xls", "苏州市相城区第三人民医院名单.xls", "苏州市相城区第三人民医院数据.xls"]
                for each in excel_list:
                    self.main2window.textBrowser_2.append(each)
    
    @pyqtSlot()
    def on_pushButton_2_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        self.close()
        
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ui = MainWindow()
    ui.show()
    sys.exit(app.exec_())
