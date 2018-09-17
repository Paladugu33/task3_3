# -*- coding: utf-8 -*-
"""
Created on Mon Sep 17 15:47:36 2018

@author: hmohan
"""

import xlsxwriter
import mysql
import pandas as pd


workbook=xlsxwriter.Workbook("Viotype.xlsx")
worksheet = workbook.add_worksheet("vio type")


import mysql.connector

# CONNECTING TO DATABASE
database = mysql.connector.connect(host='localhost',
                                   user='root',
                                   password='admin',
                                   database='mydb'
                                   )
#connect to cursor                       
cursor = database.cursor()

cursor.execute("select violation_code,violation_description,COUNT(*) as count from VIOLATIONS GROUP BY violation_code,violation_description")

myresult = list(cursor.fetchall())
#print (myresult)
row=1
col=0
worksheet.write(0,0,'code')
worksheet.write(0,1,'description')
worksheet.write(0,2,'count')
for code,desc,count in myresult:
    worksheet.write(row,col,code)
    worksheet.write(row,col+1,desc)
    worksheet.write(row,col+2,count)
    row +=1


df=pd.read_excel('Viotype.xlsx')

tot=(df.sum()['count'])
#row= len(myresult)
worksheet.write(len(myresult)+2,1,'total count:')
worksheet.write(len(myresult)+2,2,tot)

workbook.close()




    



