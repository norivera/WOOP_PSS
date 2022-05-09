#from module  import  class
from schedule import schedule
import os
import sys
#run in command prompt: pip install console-menu
from consolemenu import *
from consolemenu.items import *
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
    print("|    4. Back                           |")
    print("|______________________________________|")

# def writeMenu():
#     '''
#     tasks for day, week, month
#     '''
#     print(" ______________________________________")
#     print("|                                      |")
#     print("| Please make a selection:             |")
#     print("|    1. Write By Day                   |")
#     print("|    2. Write By Week                  |")
#     print("|    3. Write By Month                 |")
#     print("|    4. Back                           |")
#     print("|______________________________________|")

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
            #dummy hardcoded data for creating a task
            user.createTask("Glowing to school", "Class", 10.25,   0.25,   20220506)
            print("...Task created")
            subMenuLoop = True
            while subMenuLoop:
                subMenu()
                userInput = input(">> ")
                if userInput == "1":
                    editMenuLoop = True
                    while editMenuLoop:
                        editMenu()
                        userInput = input(">> ")
                        if userInput == "1":
                            #dummy hardcoded data for editing a task
                            user.editTask("Doing homework", "Study",     8.25,   0.75,   20220510)
                            print("Task updated")
                        elif userInput == "2":
                            #dummy hardcoded data for adding a task
                            user.createTask("Buying clothes", "Shopping",  9.25,   0.50,   20220520)
                            print("...Task created")
                        elif userInput == "3":
                            #dummy hardcoded data for deleting a task
                            user.deleteTask("Doing homework")
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
                            user.viewSchedule("day", 20220506)
                        elif userInput == "2":
                            print("Schedule by week:")
                            user.viewSchedule("week", 20220506)
                        elif userInput == "3":
                            print("Schedule by month:")
                            user.viewSchedule("month", 20220506)
                        elif userInput == "4":
                            viewMenuLoop = False
                elif userInput == "3":
                    user.writeScheduleToFile
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
