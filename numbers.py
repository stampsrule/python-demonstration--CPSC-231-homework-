#!/usr/bin/python3

# Last Name: Bell
# First Name: Daniel
# Student ID: 282911
# Course: CPSC 231
# Tutorial Section: T02
# Assignment: 4
# Question: 1
#
# 
#A Program that takes a file of numbers and outputs a table of the numbers in reverse order
# ------------------------------------------------------------------------------------------

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

class NumberReverse:
    """inputs from a text file a list of numbers and outputs the numbers in reverse order"""
    def __init__(self):
        """inits the object, with values of 0 to protect against no value errors in other methods"""
        self.numList=[]
    def getInput(self):
        """opens a file and takes the numbers and generates a list with one integer per list location"""
        numbersFile = open("numbers.txt", "r")
        for line in numbersFile:
            delimLocStart=0
            delimLocEnd=0
            nextInt=0
            while delimLocEnd>-1:
                 delimLocEnd=line.find(' ',delimLocStart)
                 self.numList.append(line[delimLocStart:delimLocEnd])
                 delimLocStart=delimLocEnd+1
    def output(self):
        """takes the list of integers, reverses it, prints it out in 5 columns left aligned"""
        self.numList.reverse()
        def lengthFinder(columnNumber):
            currentLength=0
            longestLength=0
            for i in range(columnNumber, len(self.numList),5):
                currentLength=len(self.numList[i])
                if currentLength>longestLength:
                    longestLength=currentLength
            return longestLength+1
        columnWidth=[]
        for i in range(5):
            columnWidth.append(lengthFinder(i))
        for i in range(len(self.numList)):
            print('{0:>{width}}'.format(self.numList[i], width=columnWidth[i%5]), end=' ')
            if i%5==4:
                print()
        print()



#the main method of the program
printinfo(4, 1)
myNumberList=NumberReverse()
myNumberList.getInput()
myNumberList.output()
