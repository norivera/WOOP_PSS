from ast import arg
from asyncio.windows_events import NULL
#from module  import  class
from schedule import schedule 
import sys

# David Johannsen
# CS 3560.03
# Cyrena Burke, Irfan Iqbal, Noe Rivera dawg, Dany Flores, Alexa Tang
# May 20, 2022

#Lists with specific task names to determine which type of task
recurringT = ["class", "study", "sleep", "exercise", "work", "meal"]
transientT = ["visit", "shopping", "appointment"]

#### COMMAND LINE UI #######
def mainMenu():
    '''
    welcome, import or create from scratch 
    '''
    print(" ______________________________________")
    print("|          Welcome to PSS              |")
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
    print("|           SubMenu                    |")
    print("| Please make a selection:             |")
    print("|    1. Edit Schedule                  |")
    print("|    2. View Schedule                  |")
    print("|    3. Export Schedule                |")
    print("|    4. Back                           |")
    print("|______________________________________|")

def editMenu():
    print(" ______________________________________")
    print("|           EditMenu                   |")
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
    print("|           ViewMenu                   |")
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
    '''
        This method collects the data necessary for the creation
        of each task type
    '''
    taskInfoMenuLoop = True
    while taskInfoMenuLoop:
        print(" ______________________________________")
        print("|                                      |")
        print("| Select a task type:                  |")
        print("|    1. Recurring                      |")
        print("|    2. Transient                      |")
        print("|    3. Anti-Task                      |")
        print("|    4. Back                           |")
        print("|______________________________________|")
        tType = input(">> ")
        if tType == "1":    # recurring task
            name = input("Please enter the name of the task (case sensitive): ")
            tType = input("Select a recurring task type:\n Class, Study, Sleep, Exercise, Work, Meal\n")
            startTime = input("Please enter the start time (a value from 0.25 - 23.75): ")
            duration = input("Please enter the duration of the task (a value from 0.25 - 23.75): ")
            startDate = input("Please enter the start date in the form YYYYMMDD: ")
            endDate = input("Please enter the end date in the form YYYYMMDD: ")
            frequency = input("Please enter the frequency number: ")
            taskInfoMenuLoop = False
            return name, tType, float(startTime), float(duration), startDate, endDate, int(frequency)
        elif tType == "2": # transient task
            name = input("Please enter the name of the task (case sensitive): ")
            tType = input("Select a transient task type:\nVisit, Shopping, Appointment\n ")
            startTime = input("Please enter the start time (a value from 0.25 - 23.75): ")
            duration = input("Please enter the duration of the task (a value from 0.25 - 23.75): ")
            date = input("Please enter the date in the form YYYYMMDD: ")
            taskInfoMenuLoop = False
            return name, tType, float(startTime), float(duration), date
        elif tType == "3": # anti-task
            name = input("Please enter the name of the task (case sensitive): ")
            tType = "Cancellation"
            startTime = input("Please enter the start time (a value from 0.25 - 23.75): ")
            duration = input("Please enter the duration of the task (a value from 0.25 - 23.75): ")
            date = input("Please enter the date in the form YYYYMMDD: ")
            taskInfoMenuLoop = False
            return name, tType, float(startTime), float(duration), date
        elif tType == "4":
            taskInfoMenuLoop = False

def subMenLoop(user, subMenuLoop):
    '''
        This is the menu logic to get from the SubMenu to the menus
        of its respective options
    '''
    while subMenuLoop:
        subMenu()
        userInput = input(">> ")
        if userInput == "1":  # edit schedule
            editMenuLoop = True
            while editMenuLoop:
                editMenu()
                userInput = input(">> ")
                if userInput == "1":    # edit task
                    args = list(taskInfoPrompt())
                    user.editTask(*args) # passing the elements of the tuple as a list of args 
                    print("Task updated")
                elif userInput == "2":  # add task
                    args = list(taskInfoPrompt())
                    args[1] = args[1].lower()
                    #figuring out the task type:
                    if args[1] in recurringT:# recurring task # the '*' means the elements in args will be the arguments of createTask func
                        if user.createRecurringTask(*args):
                            print("...Task created")
                        else:
                            print("problem creating task")
                    elif args[1] in transientT: #transient task
                        if user.createTransientTask(*args):
                            print("...Task created")
                        else:
                            print("problem creating task")
                    elif args[1] == "cancellation": #anti task
                        if user.createAntiTask(*args):
                            print("...Task created")
                        else:
                            print("problem creating task")
                    else:
                        print("Bad type input, please try again")
                        continue
                elif userInput == "3":  # delete task
                    taskName = input("Please enter the name of the task (case sensitive): ")
                    user.deleteTask(taskName)
                    print("Task deleted")
                elif userInput == "4":  # back to previous menu, submenu
                    editMenuLoop = False
        elif userInput == "2":  # view schedule
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
                    print("Viewing entire Schedule:")
                    user.viewEntireSchedule()
                elif userInput == "5":
                    viewMenuLoop = False
        elif userInput == "3":  # export schedule
            user.writeScheduleToFile()
            print("Schedule exported to '/data/schedule.json'")
        elif userInput == "4":
            subMenuLoop = False

def main() :
    global recurringT, transientT
    user = schedule() #one user obeject per execution of the program
    subMenuLoop = False
    while True:
        ########## START MAIN MENU ##########
        mainMenu()
        userInput = input(">> ")
        if userInput == "1": #creating a new schedule from scratch
            args = list(taskInfoPrompt())
            try:
            #runs if no error, trying to account for bad num inputs, since casting in infoPrompt function
                # finding the task type:
                args[1] = args[1].lower()
                if args[1] in recurringT:# recurring task # the '*' means the elements in args will be the arguments of createTask func
                    if user.createRecurringTask(*args):
                        subMenuLoop = True
                        print("...Task created")
                    else:
                        print("problem creating task")
                elif args[1] in transientT: #transient task
                    if user.createTransientTask(*args):
                        subMenuLoop = True
                        print("...Task created")
                    else:
                        print("problem creating task")
                elif args[1] == "cancellation": #anti task
                    if user.createAntiTask(*args):
                        subMenuLoop = True
                        print("...Task created")
                    else:
                        print("problem creating task")
                else:
                    print("Bad type input, please try again")
                    continue
            except Exception as e:
                print(repr(e)) #should take care of errors that a thrown when casting bad strings from taskInfoPrompt method
                print("Bad input, please try again")
                continue
            ###### SUB MENU FUNCTION CALL ####
            subMenLoop(user, subMenuLoop)
            #################################
        elif userInput == "2":  # import schedule
            filename = input("Please enter the complete filepath to file: ")
            user.readScheduleFromFile(filename)
            print("File imported!")
            subMenuLoop = True
            subMenLoop(user, subMenuLoop)
        elif userInput == "3": #exit program
            sys.exit("Thank you for using the PSS. WOOP WOOP :)")
        else:
            print("Invalid option, please try again :)")
        ########## END MAIN MENU ##########

 
if __name__ == '__main__':
    main()
