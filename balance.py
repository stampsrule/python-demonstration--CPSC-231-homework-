#!/usr/bin/python3

# Last Name: Bell
# First Name: Daniel
# Student ID: 282911
# Course: CPSC 231
# Tutorial Section: T02
# Assignment: 4
# Question: bonus
#
#
#A Program that takes a file of numbers and outputs the transaction data for the account
# ------------------------------------------------------------------------------------------

def printinfo(assign, question):
    """generates the header for assignment output"""
    print("Last Name: Bell")
    print ("First Name: Daniel")
    print("Student ID: 282911")
    print("Course: CPSC 231")
    print("Tutorial Section: T02")
    print("Assignment: %d" %assign)
    print("Question: %s" %question)
    print("")

class Account:
    """inputs from a text file a list of numbers and outputs the transaction data for the account"""
    def __init__(self):
        """inits the object, with values of 0 to protect against no value errors in other methods"""
        self.numList=[]
    def getInput(self):
        """opens a file and takes the numbers and generates a list with one integer per list location"""
        numbersFile = open("transactions.txt", "r")
        for line in numbersFile:
            delimLocStart=0
            delimLocEnd=0
            nextInt=0
            while delimLocEnd>-1:
                 delimLocEnd=line.find(' ',delimLocStart)
                 self.numList.append(float(line[delimLocStart:delimLocEnd]))
                 delimLocStart=delimLocEnd+1
    def balance(self):
        """computes the closing balance, reports the invalid transactions and displays the closing balance as well as the account status"""
        #a couple of assumptions not clear in assignment
        #1) there is always an invalid transaction
        #2) there is only 1 invalid transaction
        closeBalance=0
        invalidTrans=0
        withdrawCount=0
        depositCount=0
#        print(self.numList)
        for i in range(len(self.numList)):
            addValue=0
            if self.numList[i]<0:
                if (-1*self.numList[i])>closeBalance:
                    invalidTrans=self.numList[i]
                else:
                    addValue=self.numList[i]
                    withdrawCount+=1
            elif self.numList[i]>0:
                if i!=0:depositCount+=1
                addValue=self.numList[i]
            closeBalance+=addValue
#            print(i,addValue,closeBalance)
        print("Invalid transaction %.2f" %invalidTrans)
        print("Closing balance = %.2f" %closeBalance)
        print("Number of withdrawals = %d" %withdrawCount)
        print("Number of deposits = %d" %depositCount)


# the main body
printinfo(2, "bonus")
myAccount=Account()
myAccount.getInput()
myAccount.balance()
