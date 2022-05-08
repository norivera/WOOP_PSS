#from module  import  class
from schedule import schedule
# import recurringTask
# import transientTask


def mainMenu():
    '''
    welcome, import or create from scratch
    '''
    print(" ______________________________________")
    print("|               Welcome                |")
    print("|Please make a selection:              |")
    

    pass
def subMenu():
    '''
    edit, export, view schedule, or return to main menu
    '''
    pass

def main() :
    #driver code here :)
    
    user1 = schedule()
    '''
    creating requires:
        - self, name, type, startTime, duration, 
        types:
            -Recurring Task:
                "Class" "Study" "Sleep" "Exercise" "Work" "Meal"
            -transitent task:
                "visit" "shopping" "appointment"
            -anti task:
                "cancellation"
    '''
                                                #10.25 = 10:15 AM  15 mins     YYYYMMDD 
    user1.createTask("SCHOOL Teim T^T", "Class",    10.25,          0.25,      20220506)
    user1.createTask("SCHOOL Teim T^T", "Class",    10.25,          0.25,      20220510)
    user1.createTask("SCHOOL Teim T^T", "Class",    10.25,          0.25,      20220601)

    user1.viewSchedule("month",20220506) 
    user1.writeSchedule("./data/subFile","month",20220506)

if __name__ == '__main__':
    main()