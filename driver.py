#from module  import  class
from schedule import schedule
import os
import sys
#run in command prompt: pip install console-menu
# from consolemenu import *
# from consolemenu.items import *
# sample code for the menu: https://pypi.org/project/console-menu/ 
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
    print("|    1. View By Day                    |")
    print("|    2. View By Week                   |")
    print("|    3. View By Month                  |")
    print("|    4. View Entire Schedule           |")
    print("|    5. Back                           |")
    print("|______________________________________|")

def writeMenu():
    '''
    tasks for day, week, month
    '''
    print(" ______________________________________")
    print("|                                      |")
    print("| Please make a selection:             |")
    print("|    1. Write By Day                   |")
    print("|    2. Write By Week                  |")
    print("|    3. Write By Month                 |")
    print("|    4. Write Entire Schedule          |")
    print("|    5. Back                           |")
    print("|______________________________________|")

def taskInfoPrompt():
    name = input("Please enter the name of the task: ")
    tType = input(\
    "There are 3 types of tasks:\n \
        - Recurring: Class, Study, Sleep, Exercise, Work, Meal\n \
        - Transient: Visit, Shopping, Appointment\n \
        - Anti-Task: Cancellation\nPlease enter the type of task: ")
    startTime = input("Please enter the start time (a value from 0.25 - 23.75): ")
    duration = input("Please enter the duration of the task (a value from 0.25 - 23.75): ")
    date = input("Please enter the date in the form YYYYMMDD: ")
    return name, tType, float(startTime), float(duration), date;


def main() :
    #driver code here :)
    '''
    creating requires:
        - self, name, type, startTime, duration, 
    '''
    user = schedule()

    while True:
        mainMenu()
        userInput = input(">> ")
        if userInput == "1":
            print("New schedule created. Add a task!")
            try:
            #runs if no error, trying to account for bad num inputs, since casting in infoPrompt function
                args = taskInfoPrompt()
                if user.createTask(*args): # the '*' means the elements in args will be the arguments of createTask func
                    print("...Task created")
                    subMenuLoop = True
                else:
                    print("Bad input, please try again")
                    continue
            except:
                print("Bad input, please try again")
                continue
            while subMenuLoop:
                subMenu()
                userInput = input(">> ")
                if userInput == "1":
                    editMenuLoop = True
                    while editMenuLoop:
                        editMenu()
                        userInput = input(">> ")
                        if userInput == "1":
                            args = taskInfoPrompt()
                            user.createTask(*list(args)) # passing the elements of the tuple as a list of args 
                            print("Task updated")
                        elif userInput == "2":
                            args = taskInfoPrompt()
                            user.createTask(*args)
                            print("...Task created")
                        elif userInput == "3":
                            taskName = input("Please enter the name of the task (case sensitive): ")
                            user.deleteTask(taskName)
                            print("Task deleted")
                        elif userInput == "4":
                            editMenuLoop = False
                elif userInput == "2":
                    viewMenuLoop = True
                    while viewMenuLoop:
                        viewMenu()
                        userInput = input(">> ")
                        if userInput == "1":
                            print("Schedule by day:")
                            date = input("Please enter the date in form YYYYMMDD: ")
                            user.viewSchedule("day", date)
                        elif userInput == "2":
                            print("Schedule by week:")
                            date = input("Please enter the date in form YYYYMMDD: ")
                            user.viewSchedule("week", date)
                        elif userInput == "3":
                            print("Schedule by month:")
                            date = input("Please enter the date in form YYYYMMDD: ")
                            user.viewSchedule("month", date)
                        elif userInput == "4":
                            print("Viewing entire Schedule")
                        elif userInput == "5":
                            viewMenuLoop = False
                elif userInput == "3":
                    user.writeScheduleToFile()
                    print("Schedule exported")
                elif userInput == "4":
                    subMenuLoop = False
        elif userInput == "2":
            filename = input("Please enter the complete filepath to file: ")
            user.readScheduleFromFile(filename)
            print("File imported!")
        elif userInput == "3":
            sys.exit("Thank you for using the PSS. WOOP WOOP :)")
        else:
            print("Invalid option, please try again :)")



    # menu = ConsoleMenu("Welcome to PSS")
    # selection_menu = SelectionMenu(["Edit", "Add", "View", "Delete"])
    # submenu_item1 = SubmenuItem("Create schedule", selection_menu, menu)
    # submenu_item2 = SubmenuItem("Import schedule", selection_menu, menu)
    # menu.append_item(submenu_item1)
    # menu.append_item(submenu_item2)
    # menu.show()
    # menu_item2 = MenuItem("Export Schedule")
    #submenu_item = SubmenuItem("Edit Schedule Menu", selection_menu, mainMenu)

                                               
    # user.createTask("1", "Class",    10.25,          0.25,      20220506)
    # user.createTask("2", "Class",    8.25,          0.25,      20220510)
    # user.createTask("3", "Class",    9.25,          0.25,      20220601)

    #user.viewSchedule("month",20220506) 
    # user.writeScheduleToFile()

if __name__ == '__main__':
    main()
