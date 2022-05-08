#from module  import  class
from schedule import schedule
import os
import sys
#run in command prompt: pip install console-menu
from consolemenu import *
from consolemenu.items import *
# import recurringTask
# import transientTask


def mainMenu():
    '''
    welcome, import or create from scratch
    '''
    print(" ______________________________________")
    print("|           Welcome to PSS             |")
    print("| Please make a selection:             |")
    print("|    1. Create schedule                |")
    print("|    2. Import schedule                |")
    print("|    3. Exit                           |")
    print("|______________________________________|")
    
def subMenu():
    '''
    edit, export, view schedule, or return to main menu
    '''
    print(" ______________________________________")
    print("|                                      |")
    print("| Please make a selection:             |")
    print("|    1. Edit Schedule                  |")
    print("|    2. View Schedule                  |")
    print("|    3. Export Schedule                |")
    print("|    4. Back                           |")
    print("|______________________________________|")

def editMenu():
    print(" ______________________________________")
    print("|            Edit Schedule             |")
    print("| Please make a selection:             |")
    print("|    1. Edit Task                      |")
    print("|    2. Add Task                       |")
    print("|    3. Delete Task                    |")
    print("|    4. Back                           |")
    print("|______________________________________|")

def viewMenu():
    '''
    tasks for day, week, month
    '''
    print(" ______________________________________")
    print("|                                      |")
    print("| Please make a selection:             |")
    print("|    1. View Entire Schedule           |")
    print("|    2. View By Day                    |")
    print("|    3. View By Week                   |")
    print("|    3. View By Month                  |")
    print("|    4. Back                           |")
    print("|______________________________________|")

def writeMenu():
    '''
    tasks for day, week, month
    '''
    print(" ______________________________________")
    print("|                                      |")
    print("| Please make a selection:             |")
    print("|    1. Write Entire Schedule          |")
    print("|    2. Write By Day                   |")
    print("|    3. Write By Week                  |")
    print("|    3. Write By Month                 |")
    print("|    4. Back                           |")
    print("|______________________________________|")

def main() :
    #driver code here :)
    user = schedule()
    '''
    creating requires:
        - self, name, type, startTime, duration, 
    '''
    # ### MAIN MENU ###
    # userInput = input(mainMenu())
    # if userInput == 1:
    #     userInput = input(subMenu())
    #     if userInput == 1:
    #         userInput = input(editMenu())
    #     elif userInput == 2:
    #         userInput = input(viewMenu())
    #     elif userInput == 3:
    #         userInput = input(exportMenu())
    #     else:
    #         userInput == input(mainMenu())
    # elif userInput == 2:
    #     filename = input("Please enter the complete filepath to file: ")
    #     readScheduleFromFile(filename)
    #     userInput = input(subMenu())
            
    # elif userInput == 3:
    #     sys.exit("Thank you for using the PSS :)")
    
    # loop = True
    # while loop:
    #     userInput = input(mainMenu())
    #     if userInput == 1:
    #         userInput == input(subMenu())
    #     elif userInput == 2:
    #         filename = input("Please enter the complete filepath to file: ")
    #         readScheduleFromFile(filename)
    #         userInput = input(subMenu())
    #     elif userInput == 3:
    #         sys.exit("Thank you for using the PSS :)")



    mainMenu = ConsoleMenu("Title", "Subtitle")

        
    

                                               
    user.createTask("1", "Class",    10.25,          0.25,      20220506)
    user.createTask("2", "Class",    8.25,          0.25,      20220510)
    user.createTask("3", "Class",    9.25,          0.25,      20220601)

    #user.viewSchedule("month",20220506) 
    user.writeScheduleToFile()

if __name__ == '__main__':
    main()
