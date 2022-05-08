from asyncio import create_task
from task import task
import json
import collections
from types import SimpleNamespace
from datetime import datetime, timedelta, time

taskList = []
class schedule:

    def __init__(self):
        global taskList
        pass 

    def createTask(self, name, type, sTime, duration, date):
        global taskList

        '''
        date = YYYYMMDD
        sTime, duration = 24HR (increments of .25, rounded to the nearest 15 mins)
        types:
            -Recurring Task:
                "Class" "Study" "Sleep" "Exercise" "Work" "Meal" 
            -transitent task:
                "Visit" "Shopping" "Appointment" "Fishing"
            -anti task:
                "cancellation"
        '''
        recurringT = ["Class", "Study", "Sleep", "Exercise", "Work", "Meal"]
        transitentT = ["Visit", "Shopping", "Appointment", "Fishing"]
        antiT = ["Cancellation"]
        #INPUT CHECKING
        if(not self.checkName(name)):
            print("Not a unique task name, please try again")
            return False

        if (type not in recurringT) and (type not in transitentT) and (type not in antiT):
            print("Invalid task type, please try again")
            return False
        if  not (0.25 <= duration <= 23.75):
            return False
        else: 
            duration= round(duration*4)/4
        if  not (0 <= sTime <= 23.75):
            return False
        else: 
            duration= round(sTime*4)/4

        try:
            datetime.strptime(str(date), "%Y%m%d")
        except ValueError:
            print("This is the incorrect date string format. It should be YYYYMMDD")
            return False
       
            
        newTask = task(name, type, sTime,duration,date)
        taskList.append(newTask)

    def checkName(self, name):
        '''
        ensure that each task has a unique name for searching purposes
        loop thru all the task names to find a match
        return true if name does not exist, false if it does
        '''
        if name not in [x.name for x in taskList]:
            return True
        else:
            return False

    def viewTask(self, name):
        global taskList
        for x in taskList:
                if x.name==name:
                    print(x.name, x.type, x.startTime, x.duration, x.date)

    def deleteTask(self,name):
        global taskList
        taskList = list( filter(lambda x: x.name != name, taskList)) 

    def editTask(self, name, type, sTime, duration, date):
        global taskList
        taskList = list( filter(lambda x: x.name != name, taskList))
        self.createTask(name,type,sTime,duration,date)

    def writeScheduleToFile(self):
        taskList.sort(key=lambda x: (x.date,x.startTime))

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
        endDate= startDate
        if period=="day":
            endDate = (datetime.strptime(str(startDate), '%Y%m%d') + timedelta(days=1)).strftime('%Y%m%d')
        elif period=="week":
            endDate = (datetime.strptime(str(startDate), '%Y%m%d') + timedelta(weeks=1)).strftime('%Y%m%d')
        elif period=="month":
            endDate = (datetime.strptime(str(startDate), '%Y%m%d') + timedelta(days=30)).strftime('%Y%m%d')

        # sorts the list based on date, need to add functionality also for time
        
        taskList.sort(key=lambda x: (x.date,x.startTime))
        if taskList:    
            for x in taskList:
                if str(startDate) <= str(x.date) <= endDate:
                    print(x.name, x.startTime)


    def writeSchedule(self, fileName, period, startDate):
        '''
        updating the schedule for a specified day, week, or month
        '''
        # need to handle overflow of days for month and year or figure our a better format
        endDate= startDate
        if period=="day":
            endDate = (datetime.strptime(str(startDate), '%Y%m%d') + timedelta(days=1)).strftime('%Y%m%d')
        elif period=="week":
            endDate = (datetime.strptime(str(startDate), '%Y%m%d') + timedelta(weeks=1)).strftime('%Y%m%d')
        elif period=="month":
            endDate = (datetime.strptime(str(startDate), '%Y%m%d') + timedelta(days=30)).strftime('%Y%m%d')

        # sorts the list based on date, need to add functionality also for time
        subList = list( filter(lambda x: str(startDate) <= str(x.date) <= endDate, taskList))
    
        subList.sort(key=lambda x: (x.date,x.startTime))
        with open(fileName, "w") as file:
            json.dump([ob.__dict__ for ob in subList], file)