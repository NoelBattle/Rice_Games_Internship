# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '4prac.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!
import os
import sys
import matplotlib.pyplot as plt
import pandas as pd
import csv
import matplotlib.dates as mdates
import numpy as np
import fnmatch
from PyQt5 import QtGui
from pathlib import Path
from PyQt5.QtWidgets import (QComboBox, QApplication, QMainWindow, QPushButton,
                             QToolTip, QMessageBox, QLabel, QWidget, QInputDialog, QLineEdit)

import face_recognition

#image = face_recognition.load_image_file("your_file.jpg")




os.getcwd()

currentDirectory = os.getcwd()
path = "csv_files"
dirs = os.listdir(path)
#list the current directory

print(dirs)

#ask = raw_input("Do you wanna check out Team Members[1] or Enemies[2] Press q to exit")

choice = "love"
listToStr = ', '.join([str(elem) for elem in dirs])


listToStr = listToStr.replace('.', '')
listToStr = listToStr.replace('csv', '')
listToStr = listToStr.replace('-', ' ')
listToStr = listToStr.title()
print(listToStr)

stringtolist = listToStr.split(",")

print (stringtolist)


class Window2(QMainWindow):                           # <===
    def __init__(self):
        global choice
        #choice = choice.title()
        choice = choice.replace(' ', '-')
        choice = choice[1:]
        choice = choice.lower()
      #  mon = 'location'
        print(choice)
       # keyword = 'file'
        for fname in os.listdir(path):
            if choice in fname:
                print(fname, "has the keyword")
                choice = fname;
                print(choice)
        print(choice)
        super().__init__()
        self.setWindowTitle("Window22222")
        
        
        dombo = QComboBox(self)
        self.qlabel = QLabel(self)
        self.qlabel.move(50,16)
        #print(self.qlabel)
        
        
        #print(self.qlabel)
        dombo.activated[str].connect(self.onChanged)
        #dombo.activated[str].connect(self.makeGraph)
        if choice == 'audience-overview.csv':
            df = pd.read_csv("csv_files/audience-overview.csv", error_bad_lines=False)
            print(df.head(10))
            x = df['Day Index']
            y = df['Users']
            plt.bar(x, height = y)
           # plt.scatter(x,y)
           # for col in df.columns: 
            # print(col) 
            
#plt.show()
            dombo.addItem('DayIndex*Users audience overview')
            dombo.addItem("Generate all graphgs in this csv")
            
            
        elif choice == 'acquisition-overview-b.csv' or choice == 'acqusition-overview-a.csv':
            dombo.addItem("Graph")
            dombo.addItem('Direct Traffic* Users acquisition overview')
            dombo.addItem("Generate all graphgs in this csv")
            
        elif choice == 'cohort-analysis.csv':
           dombo.addItem('Time * Users cohort analysis')
           dombo.addItem("Generate all graphgs in this csv")
           
        elif choice == 'freq-rec.csv':
            dombo.addItem('Graph')
            dombo.addItem("Generate all graphgs in this csv")
            
        elif choice == 'location-a.csv':
            dombo.addItem('Country*Users for Location A')
            dombo.addItem("Generate all graphgs in this csv")
            
            
        elif choice == 'location-b.csv':
            dombo.addItem('Country*Users for Location B')
       
       
  
        self.pushButton = QPushButton("Start", self)
        self.pushButton.move(275, 200)
        self.pushButton.setToolTip("<h3>Start the Session</h3>")

        #self.pushButton.clicked.connect(self.makeGraph)    
        
    def onChanged(self, text):
        self.qlabel.setText(text)
        self.qlabel.adjustSize()
        
        nextchoice = text
        print(nextchoice)
        if nextchoice == 'DayIndex*Users audience overview':
            df = pd.read_csv("csv_files/audience-overview.csv", error_bad_lines=False)
            print(df.head(10))
            x = df['Day Index']
            y = df['Users']
            plt.bar(x, height = y)
            plt.savefig('graphs/Time*Users_Cohort.png')
            plt.show()
            
            
        elif nextchoice == 'acquisition-overview-a.csv':
            print('sdfsadffs')
            dombo.addItem("Graph")
            dombo.addItem("Generate all graphs in this csv")
            
        elif nextchoice == 'Direct Traffic* Users acquisition overview':
            df = pd.read_csv("csv_files/acquisition-overview-b.csv", error_bad_lines=False)
            print(df.head(10))
            x = df['Default Channel Grouping']
            y = df['Users']
            plt.bar(x, height = y)
            plt.savefig('graphs/Time*Users_Cohort.png')
            plt.show()
            
        elif nextchoice == 'Time * Users cohort analysis':
           df = pd.read_csv("csv_files/cohort-analysis.csv", error_bad_lines=False)
           print(df.head(10))
           x = df['Time']
           y = df['Total Users']
           plt.bar(x, height = y)
           plt.savefig('graphs/Time*Users_Cohort.png')
           plt.show()
           
        elif nextchoice == 'freq-rec.csv':
            dombo.addItem('Graph')
            dombo.addItem("Generate all graphgs in this csv")
            
        elif nextchoice == 'Country*Users for Location B':
            df = pd.read_csv("csv_files/location-b.csv", error_bad_lines=False)
            print(df.head(10))
            print ("love")
            x = df['Country']
            y = df['Users']
            plt.bar(x, height = y)
            plt.savefig('graphs/Country*UsersLocationA.png')
            plt.show()
            
        elif nextchoice == 'Country*Users for Location A':
            df = pd.read_csv("csv_files/location-a.csv", error_bad_lines=False)
            print(df.head(10))
            print ("love")
            x = df['Country']
            y = df['Users']
            plt.bar(x, height = y)
            
            #path = "graphs"
           # os.mkdir(path)
            plt.savefig('graphs/Country*UsersLocationA.png')
            plt.show()
      #  self.textbox = QLineEdit(self)
       # self.textbox.move(20, 20)
       # self.textbox.resize(280,40)
        
        # Create a button in the window
       # self.button = QPushButton('Show text', self)
        #self.button.move(20,80)
        
        # connect button to function on_click
       # self.button.clicked.connect(self.getText)
       # self.show() 
        
        #self.pushButton = QPushButton("Start", self)
      #  self.pushButton.move(275, 200)
       # self.pushButton.setToolTip("<h3>Start the Session</h3>")
       
    
   




class Window(QMainWindow,QComboBox):
    def __init__(self):
        super().__init__()

        self.title = "First Window"
        self.top = 100
        self.left = 100
        self.width = 680
        self.height = 500


        self.pushButton = QPushButton("Start", self)
        self.pushButton.move(275, 200)
        self.pushButton.setToolTip("<h3>Start the Session</h3>")

        self.pushButton.clicked.connect(self.window2)              # <===
      #  self.comboX = QtWidgets.QComboBox(self.centralwidget)
       # self.comboX.setGeometry(QtCore.QRect(330, 190, 104, 26))
       # self.comboX.setObjectName("comboX")
        self.main_window()
       #  for i in stringtolist:
         #   self.comboX.addItem(i)
    

        
    def onChanged(self, text):
        self.qlabel.setText(text)
        self.qlabel.adjustSize()
        global choice
        choice = text
        print(choice)
        
        #choice = text;
    
  

    def main_window(self):
        
       
        combo = QComboBox(self)
       # combo.addItem("Apple")
        for i in stringtolist:
            combo.addItem(i)

        combo.move(50, 50)
        #money="sdfsdfsdf"
        
        self.qlabel = QLabel(self)
        self.qlabel.move(50,16)
        #print(self.qlabel)
        combo.activated[str].connect(self.onChanged)
        #print(choice)
        
        self.setGeometry(50,50,320,200)
        self.setWindowTitle("QLineEdit Example")
        self.show()
        self.setWindowTitle(self.title)
        self.setGeometry(self.top, self.left, self.width, self.height)
        #self.show()


    def window2(self):                                             # <===
        self.w = Window2()
        self.w.show()
        self.hide()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Window()
    sys.exit(app.exec())