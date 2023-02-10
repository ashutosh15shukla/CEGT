# ########################################################################### #
# Coaching Exam Generation Tool
# Module: Framework
# License: None (Closed)
# Ver: 0.03
# Release: Pre-Alpha
# Author: Ashutosh K. Shukla
# Functionalities: Picking definitions and questions for print on letterhead
# ########################################################################### #

# Libs
from tkinter import *

# Global variables
global class_selection, title, version, font, file

# Info
version = "0.03 Alpha"
heading = "Exam and Definition Generation Tool"
font = ("Times", "20")
filename = "StudentData.txt"

# Field Lists
acc11 = [
    "Introduction to Accounting",
    "Basic Accounting Terms",
    "Accounting, Accounting Standards, IND-AS and GST",
    "Basis of Accounting",
    "Accounting Equation",
    "Accounting Procedures",
    "Origin of Transactions",
    "Journals",
    "Ledgers",
    "Cash Books",
    "Other Books",
    "Bank Reconciliation Statement",
    "Trial Balance",
    "Depreciations",
    "Provision and Reverse",
    "Accounting for Bills of Exchange",
    "Rectification of Errors",
    "Financial Statements of Sole Proprietorship",
    "Adjustment in Preperation of Financial Statements"    ]

stat11 = [
    "stat 1", "stat 2", "stat 3", "stat 4", "stat 5", "stat 6", "stat 7", "stat 8", "stat 9", "stat 10", "stat 11", "stat 12" 
]

me11 = [
    "micro 1", "micro 2", "micro 3", "micro 4", "micro 5", "micro 6", "micro 7", "micro 8", "micro 9", "micro 10", "micro 11", "micro 12" 
]

bu11 = [
    "busi 1", "busi 2", "busi 3", "busi 4", "busi 5", "busi 6", "busi 7", "busi 8", "busi 9", "busi 10", "busi 11", "busi 12"
]

acc12 = [1,2,3,4,5,6,7,8,9]

stat12 = [
    "stat 21", "stat 22", "stat 23", "stat 24", "stat 25", "stat 26", "stat 7", "stat 8", "stat 9", "stat 10", "stat 11", "stat 12"
]

in12 = [21,22,23,24,25,26,27,28,29]

ma12 = [31,32,33,34,35,36,37,38,39]

# Functions
def expo():
    pass

def gridclear():
    list = mainwin.grid_slaves()
    for l in list:
        l.grid_forget()

def listhandler():
    gridclear()
    pass

def subhandler(e):
    gridclear()
    global acc11,stat11, bu11, me11, acc12, stat12, in12, ma12 # Sub Names
    acc11b,stat11b, bu11b, me11b, acc12b, stat12b, in12b, ma12b = [],[],[],[],[],[],[],[] # Sub Button Lists
    alpha = []   # to set sub
    beta = [] # to set buttons
    # To load sublist and buttonlists
    if e == 1:  
        alpha = acc11
        beta = acc11b
    elif e == 2:
        alpha = stat11
        beta = stat11b
    elif e == 3:
        alpha = bu11
        beta = bu11b
    elif e == 4:
        alpha = me11
        beta = me11b
    elif e == 5:
        alpha = acc12
        beta = acc12b
    elif e == 6:
        alpha = stat12
        beta = stat12b
    elif e == 7:
        alpha = in12
        beta = in12b
    elif e == 8:
        alpha = ma12
        beta = ma12b
    
    y=0
    x=0
    for i in alpha:
        i = Button(mainwin, text=i, width=44, font=font, command=listhandler)
        i.grid(row=x//2, column=y)
        x+=1
        if y==0:
            y=1
        else:
            y=0
        beta.append(i)
    # To unload sublist and buttonlists
    if e == 1:  
        acc11 = alpha
        acc11b = beta
    elif e == 2:
        stat11 = alpha
        stat11b = beta
    elif e == 3:
        bu11 = alpha
        bu11b = beta
    elif e == 4:
        me11 = alpha
        me11b = beta
    elif e == 5:
        acc12 = alpha
        acc12b = beta
    elif e == 6:
        stat12 = alpha
        stat12b = beta
    elif e == 7:
        in12 = alpha
        in12b = beta
    elif e == 8:
        ma12 = alpha
        ma12b = beta
    
    if class_selection == 11:
        back = Button(mainwin, text="Back", command=eleventh, font=font).grid(row=11, column=0, sticky="news", rowspan=1)
    elif class_selection ==12:
        back = Button(mainwin, text="Back", command=twelfth, font=font).grid(row=11, column=0, sticky="news", rowspan=1)
        
def eleventh():
    global class_selection
    class_selection=11
    gridclear()
    acco = Button(mainwin, text="Accountancy", font=font, command=lambda:subhandler(1), height=7).grid(row=0, column=0, sticky="news")
    stat = Button(mainwin, text="Statistics", font=font, command=lambda:subhandler(2), height=7).grid(row=0, column=1, sticky="news")
    busi = Button(mainwin, text="Business Studies", font=font, command=lambda:subhandler(3), height=7).grid(row=1, column=0, sticky="news")
    micr = Button(mainwin, text="Microeconomics", font=font, command=lambda:subhandler(4), height=7).grid(row=1, column=1, sticky="news")
    back = Button(mainwin, text="Back", command=main, font=font).grid(row=2, column=0, sticky="news", rowspan=8)

def twelfth():
    global class_selection
    class_selection=12
    gridclear()
    accu = Button(mainwin, text="Accountancy", font=font, command=lambda:subhandler(5), height=7).grid(row=0, column=0, sticky="news")
    stai = Button(mainwin, text="Statistics", font=font, command=lambda:subhandler(6), height=7).grid(row=0, column=1, sticky="news")
    inec = Button(mainwin, text="Indian Economics", font=font, command=lambda:subhandler(7), height=7).grid(row=1, column=0, sticky="news")
    macr = Button(mainwin, text="Macroeconomics", font=font, command=lambda:subhandler(8), height=7).grid(row=1, column=1, sticky="news")
    back = Button(mainwin, text="Back", command=main, font=font).grid(row=2, column=0, sticky="news", rowspan=8)

def classhandler(e):
    if e==11:
        eleventh()
    elif e==12:
        twelfth()

# Window inits
mainwin = Tk()
mainwin.title(f"{heading} - Version: {version}")
mainwin.minsize(1200,600)
for i in range(10):
    mainwin.rowconfigure(i, weight=1)
for i in range(2):    
    mainwin.columnconfigure(i, weight=1)

# Buttons init
def main():
    gridclear()
    btn_11 = Button(mainwin, text="Class 11th", font=font, command=lambda: classhandler(11), height=7).grid(row=0, sticky="news", columnspan=3)
    btn_12 = Button(mainwin, text="Class 12th", font=font, command=lambda: classhandler(12), height=7).grid(row=1, sticky="news", columnspan=3)
    exp = Button(mainwin, text="Export PDF", font=font, command=expo).grid(row=2, column=1, sticky="news", rowspan=8)
    exit = Button(mainwin, text="Exit", font=font, command=lambda:mainwin.destroy()).grid(row=2, column=0, sticky="news", rowspan=8)

main()

# Window loop
mainwin.mainloop()