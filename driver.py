#from module  import  class
from schedule import schedule
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

    '''
    userInput = input(mainMenu())
    if user == 1:
         subMenu()
    elif user == 2:
        filename = input("Please enter the complete filepath to file: ")
        readScheduleFromFile(filename)
    '''
                                               
    user.createTask("1", "Class",    10.25,          0.25,      20220506)
    user.createTask("2", "Class",    8.25,          0.25,      20220510)
    user.createTask("3", "Class",    9.25,          0.25,      20220601)

    #user.viewSchedule("month",20220506) 
    user.writeScheduleToFile()

if __name__ == '__main__':
    main()