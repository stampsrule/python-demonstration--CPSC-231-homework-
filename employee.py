#!/usr/bin/python3

# Last Name: Bell
# First Name: Daniel
# Student ID: 282911
# Course: CPSC 231
# Tutorial Section: T02
# Assignment: 4
# Question: 2
#
# 
#A Program that takes a file of employee pay data  and outputs a table of the payment  numbers in assending order
# ------------------------------------------------------------------------------------------
import csv
from operator import itemgetter, attrgetter

def printinfo(assign, question):
    """generates the header for assignment output"""
    print("Last Name: Bell")
    print ("First Name: Daniel")
    print("Student ID: 282911")
    print("Course: CPSC 231")
    print("Tutorial Section: T02")
    print("Assignment: %d" %assign)
    print("Question: %d" %question)
    print("")

class Payroll:
    """inputs from a text file a csv of employee data  and outputs the pay  numbers in assending  order"""
    def __init__(self):
        """inits the object, with values of 0 to protect against no value errors in other methods"""
        self.payData={}
    def getInput(self):
        """opens a file and takes the numbers and generates a dictionary with one employee per key, the key is the employee ID"""
        payData = open("records.txt", "r")
        for line in payData:
            delimLocStart=0
            delimLocEnd=0
            nextInt=0
            key="0000"
            while delimLocEnd>-1:
                 delimLocEnd=line.find(',',delimLocStart)
                 if delimLocStart==0:
                     key=line[delimLocStart:delimLocEnd]
                     self.payData[key]=[]
                 else:
                     self.payData[key].append(line[delimLocStart:delimLocEnd])
                 delimLocStart=delimLocEnd+1
    def payroll(self): 
        """takes the pay info dictionary and calculates the pay info and prints out the pay info for each employee
        sortedKeys=sorted(self.payData, key=itemgetter(0))
        for key in sortedKeys:
            if int(self.payData[key][1])<40:
                regPay=float(self.payData[key][0])*int(self.payData[key][1])
            else:
                regPay=float(self.payData[key][0])*40
            if int(self.payData[key][1])<40:
                otPay=0
            else:
                otPay=float(self.payData[key][0])*1.5*(int(self.payData[key][1])-40)
            totalSalary=regPay+otPay
            self.payData[key].append(regPay)
            self.payData[key].append(otPay)
            self.payData[key].append(totalSalary)
        print("%10s%10s%10s%10s"%("Employee", "Regular", "Overtime", "Total"))
        print("-"*40)
        sortedKeys.sort()
        for key in sortedKeys:
            print("%10d%10.2f%10.2f%10.2f"%(int(key), float(self.payData[key][2]), float(self.payData[key][3]), float(self.payData[key][4])))
#            print("{0:>{width}}".format(key, width=20))





#the main method of the program
printinfo(4, 2)
myPayroll=Payroll()
myPayroll.getInput()
myPayroll.payroll()







