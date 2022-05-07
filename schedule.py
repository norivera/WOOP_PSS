from asyncio import create_task
from task import task
import json
import collections
from types import SimpleNamespace

taskList = []
class schedule:
    
    def __init__(self):
        global taskList
        pass 
    #def checkName(name):
    #    '''
    #    ensure that each task has a unique name for searching purposes
    #    loop thru all the task names to find a match
    #    return true if name does not exist, false if it does
    #    '''
    #    pass
    def createTask(self, name, type, sTime, duration, date):
        global taskList

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

    def viewTask(self, name):
        for x in taskList:
                if x.name==name:
                    print(x.name, x.type, x.startTime, x.duration, x.date)

    def deleteTask(self,name):
        global taskList
        taskList = list( filter(lambda x: x.name != name, taskList) ) 

    def editTask(self, name, type, sTime, duration, date):
        taskList = list( filter(lambda x: x.name != name, taskList))
        self.createTask(name,type,sTime,duration,date)

    def writeScheduleToFile(self):
        with open("./data/schedule.txt", "w") as file:
            json.dump([ob.__dict__ for ob in taskList], file)

    def readScheduleFromFile(self,filename):
        with open(filename) as file:
            data=json.load(file)

        print(data)
        taskList=[]

        for x in data: 
            self.createTask(x["name"],x["type"], x["startTime"],x["duration"],x["date"])


    def viewSchedule(self, period, startDate):
        '''
        printing the schedule for a specified day, week, or month
        '''
        
        # need to handle overflow of days for month and year or figure our a better format
        endDate=startDate
        if period=="day":
            endDate+=1
        elif period=="week":
            endDate+=7

        # sorts the list based on date, need to add functionality also for time
        taskList.sort(key=lambda x: (str(x.date)[4:]), reverse=True)
        
        if taskList:    
            for x in taskList:
                print(x.name, x.startTime)



    def writeSchedule(fileName, period, startDate):
        '''
        updating the schedule for a specified day, week, or month
        '''
        pass