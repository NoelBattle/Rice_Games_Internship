
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
from menu import *
#import dependencies



#load directory
os.getcwd()
currentDirectory = os.getcwd()
path = "csv_files"
dirs = os.listdir(path)
#list the current directory

print(dirs)



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
        dombo.addItem("generate all graphs")
        
        #print(self.qlabel)
        dombo.activated[str].connect(self.onChanged)
        #dombo.activated[str].connect(self.makeGraph)
        if choice == 'audience-overview.csv':
            dombo.addItem('DayIndex*Users audience overview')
                
        elif choice == 'acquisition-overview-b.csv' or choice == 'acqusition-overview-a.csv':
            dombo.addItem('Direct Traffic* Users acquisition overview')
            
        elif choice == 'cohort-analysis.csv':
           dombo.addItem('Time * Users cohort analysis')
           
        elif choice == 'freq-rec.csv':
            dombo.addItem("CountryofSessions*Sessions")
            
        elif choice == 'location-a.csv':
            dombo.addItem('Country*Users for Location A')     
            
        elif choice == 'location-b.csv':
            dombo.addItem('Country*Users for Location B')
         
        #self.pushButton = QPushButton("Start", self)
        #self.pushButton.move(275, 200)
        #self.pushButton.setToolTip("<h3>Start the Session</h3>")
        #self.pushButton.clicked.connect(self.makeGraph)    
        
    def onChanged(self, text):
        self.qlabel.setText(text)
        self.qlabel.adjustSize()
        nextchoice = text
        print(nextchoice)
        
        if nextchoice == 'DayIndex*Users audience overview':
            df = pd.read_csv("csv_files/audience-overview.csv", error_bad_lines=False)
            #print(df.head(10))
            x = df['Day Index']
            y = df['Users']
            plt.bar(x, height = y)
            plt.savefig('graphs/Time*Users_Cohort.png')
            plt.show()
            
            
        elif nextchoice == 'generate all graphs':
            df = pd.read_csv("csv_files/audience-overview.csv", error_bad_lines=False)
           # print(df.head(10))
            x = df['Day Index']
            y = df['Users']
            plt.bar(x, height = y)
            plt.savefig('graphs/Time*Users_Cohort.png')
            plt.show()
            
            df = pd.read_csv("csv_files/acquisition-overview-b.csv", error_bad_lines=False)
           # print(df.head(10))
            x = df['Default Channel Grouping']
            y = df['Users']
            plt.bar(x, height = y)
            plt.savefig('graphs/Time*Users_Cohort.png')
            plt.show()
            
            df = pd.read_csv("csv_files/cohort-analysis.csv", error_bad_lines=False)
           # print(df.head(10))
            x = df['Time']
            y = df['Total Users']
            plt.bar(x, height = y)
            plt.savefig('graphs/Time*Users_Cohort.png')
            plt.show()
            
            df = pd.read_csv("csv_files/location-a.csv", error_bad_lines=False)
            #print(df.head(10))
            #print ("love")
            x = df['Country']
            y = df['Users']
            plt.bar(x, height = y)
            plt.savefig('graphs/Country*UsersLocationA.png')
            plt.show()
            
            df = pd.read_csv("csv_files/location-b.csv", error_bad_lines=False)
            #print(df.head(10))
            print ("love")
            x = df['Country']
            y = df['Users']
            plt.bar(x, height = y)
            plt.savefig('graphs/Country*UsersLocationB.png')
            plt.show()
            
            df = pd.read_csv("csv_files/freq-rec.csv", error_bad_lines=False)
            print(df.head(10))
           # print ("love")
            x = df['Count of Sessions']
            y = df['Sessions']
            plt.bar(x, height = y)
            plt.savefig('graphs/CountryofSessions*Sessions feq-rec.png')
            plt.show()
            
            
        elif nextchoice == 'Direct Traffic* Users acquisition overview':
            df = pd.read_csv("csv_files/acquisition-overview-b.csv", error_bad_lines=False)
           # print(df.head(10))
            x = df['Default Channel Grouping']
            y = df['Users']
            plt.bar(x, height = y)
            plt.savefig('graphs/Time*Users_Cohort.png')
            plt.show()
            
        elif nextchoice == 'Time * Users cohort analysis':
           df = pd.read_csv("csv_files/cohort-analysis.csv", error_bad_lines=False)
           #print(df.head(10))
           x = df['Time']
           y = df['Total Users']
           plt.bar(x, height = y)
           plt.savefig('graphs/Time*Users_Cohort.png')
           plt.show()
           
        elif nextchoice == 'CountryofSessions*Sessions': 
            df = pd.read_csv("csv_files/freq-rec.csv", error_bad_lines=False)
           # print(df.head(10))
            print ("love")
            x = df['Count of Sessions']
            y = df['Sessions']
            plt.bar(x, height = y)
            plt.savefig('graphs/CountryofSessions*Sessions feq-rec.png')
            plt.show()
            
        elif nextchoice == 'Country*Users for Location B':
            df = pd.read_csv("csv_files/location-b.csv", error_bad_lines=False)
            #print(df.head(10))
            print ("love")
            x = df['Country']
            y = df['Users']
            plt.bar(x, height = y)
            plt.savefig('graphs/Country*UsersLocationB.png')
            plt.show()
            
        elif nextchoice == 'Country*Users for Location A':
            df = pd.read_csv("csv_files/location-a.csv", error_bad_lines=False)
            #print(df.head(10))
            #print ("love")
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
        self.main_window()
  

        
    def onChanged(self, text):
        self.qlabel.setText(text)
        self.qlabel.adjustSize()
        global choice
        choice = text
        print(choice)
        
    def main_window(self):
        
       
        combo = QComboBox(self)
       
        for i in stringtolist:
            combo.addItem(i)

        combo.move(50, 50)
        self.qlabel = QLabel(self)
        self.qlabel.move(50,16)
        combo.activated[str].connect(self.onChanged)
        
        
        self.setGeometry(100,100,320,200)
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