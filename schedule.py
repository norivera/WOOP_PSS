from task import task
class schedule:
    taskList = []
    def __init__(self):
        pass 
    def checkName(name):
        '''
        ensure that each task has a unique name for searching purposes
        loop thru all the task names to find a match
        return true if name does not exist, false if it does
        '''
        pass
    def createTask(self, name, type, sTime, duration, date):
        '''
        date = YYYYMMDD
        sTime, duration = 24HR (increments of .25, rounded to the nearest 15 mins)
        types:
            -Recurring Task:
                "Class" "Study" "Sleep" "Exercise" "Work" "Meal"
            -transitent task:
                "visit" "shopping" "appointment"
            -anti task:
                "cancellation"
        '''
        newTask = task(name, type, sTime,duration,date)
        taskList.append(newTask)
        # if(name not in [x for x.name in taskList]):
        #     newTask = Task(name, type, sTime,duration,date)
        #     taskList.append(newTask)
        # else:
        #     return "task creation failed"

    def viewTask(name):
        pass
    def editTask(name, type, sTime, duration, date):
        pass
    def writeScheduleToFile():
        pass
    def readScheduleToFile(filename):
        pass
    def viewSchedule(period, startDate):
        '''
        printing the schedule for a specified day, week, or month
        '''
        sortedList= taskList.sort(key=lambda x: str(x.date)[4:])
        
        for x in taskList:
            print(x.name)

        for x in sortedList:
            print(x.name)

    def writeSchedule(fileName, period, startDate):
        '''
        updating the schedule for a specified day, week, or month
        '''
        pass