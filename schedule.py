from asyncio import create_task
from task import task
from antiTask import antiTask
from recurringTask import recurringTask
from transientTask import transientTask
import json
import collections
from types import SimpleNamespace
from datetime import datetime, timedelta, time

taskList = []
recurringDates=[]
recurringT = ["class", "study", "sleep", "exercise", "work", "meal"]
antiT = ["cancellation"]
transientT = ["visit", "shopping", "appointment"]

class schedule:

    def __init__(self):
        global taskList, recurringDates, recurringT
        pass 

    def createRecurringTask(self, name, type, sTime, duration, sDate, eDate, frequency):
        global taskList, recurringDates

        if  not self.checkInputs(name, type, sTime, duration, 20220516):
            return False


        if type.lower() not in recurringT:
            print("Not a valid task type")
            return False
        duration= round(duration*4)/4
        sTime= round(sTime*4)/4

        try:
            start =datetime.strptime(str(sDate), "%Y%m%d")
            end=datetime.strptime(str(eDate), "%Y%m%d")
        except ValueError: 
            print("This is the incorrect date string format. It should be YYYYMMDD. please try again")
            return False

        
        if not 1<= frequency <= (end-start).days:
            print("Frequency is not between start and end dates, please try again")
            return False

        newTask = recurringTask(name, type, sTime,duration,sDate,eDate,frequency)
        taskList.append(newTask)
        
        day = start
        while day<= end:
            recurringDates.append((day.strftime("%Y%m%d"),sTime,duration))
            day += timedelta(days=frequency)

        return True    

    def createAntiTask(self, name, type, sTime, duration, date):
        global taskList, recurringDates, antiT

        if not self.checkInputs(name, type, sTime, duration, date):
            return False


        if type.lower() not in antiT:
            print("Not a valid task type")
            return False
        duration= round(duration*4)/4
        sTime= round(sTime*4)/4


        if (date, sTime, duration) not in recurringDates:
            print("No recurring task during this date and time, please try again")
            return False
        else:
            recurringDates.remove((date, sTime, duration))
            
        newTask = antiTask(name, type, sTime,duration,date)
        taskList.append(newTask)

        return True

    def createTransientTask(self, name, type, sTime, duration, date):
        global taskList, recurringDates, transientT

        if not self.checkInputs(name, type, sTime, duration, date):
            return False


        if type.lower() not in transientT:
            print("Not a valid task type")
            return False
        duration= round(duration*4)/4
        sTime= round(sTime*4)/4

        if (date, sTime, duration) in recurringDates:
            print("Overlaps with an existing recurring task, please try again")
            return False

        newTask = transientTask(name, type, sTime,duration,date)
        taskList.append(newTask)

        return True

    
    def checkInputs(self, name, type, sTime, duration, date):
        
        if name in [x.name for x in taskList]:
            print("Not a unique task name, please try again")
            return False

        if  not (0.25 <= duration <= 23.75):
            print("Duration not between 0.25 and 23.75, please try again")
            return False 

        if  not (0 <= sTime <= 23.75):
            return False

        try:
            datetime.strptime(str(date), "%Y%m%d")
        except ValueError:
            print("This is the incorrect date string format. It should be YYYYMMDD")
            return False

        return True


    def viewTask(self, name):
        global taskList
        for x in taskList:
                if x.name==name:
                    print(x.name, x.type, x.startTime, x.duration, x.date)

    def deleteTask(self,name):
        global taskList
        taskList = list( filter(lambda x: x.name != name, taskList)) 

    def editTask(self, name, type, sTime, duration, date=0,sDate=0,eDate=0,freq=0):
        global taskList, recurringDates, recurringT, transientT, antiT
        taskList = list( filter(lambda x: x.name != name, taskList))
        for i in taskList:
            if i.name==name:
                s=i.date
                e=i.endDate
                f=i.frequency
                break
        
        if type.lower in recurringT:

            start =datetime.strptime(str(sDate), "%Y%m%d")
            end=datetime.strptime(str(eDate), "%Y%m%d")
            day = start
            while day<= end:
                recurringDates.remove((day.strftime("%Y%m%d"),sTime,duration))
                day += timedelta(days=freq)

            task= self.createRecurringTask(name, type, sTime, duration,sDate,eDate,freq)
            
  
        elif type.lower() in transientT:
            task = self.createTransientTask(name,type, sTime, duration, date)
        else:
            task = self.createAntiTask(name,type, sTime, duration, date)

        
        taskList.append(task)
 
    def writeScheduleToFile(self):
        taskList.sort(key=lambda x: (x.date,x.startTime))

        with open("./data/schedule.txt", "w") as file:
            json.dump([ob.__dict__ for ob in taskList], file)
        file.close()
            

    def readScheduleFromFile(self,filename):
        global taskList, recurringDates, recurringT, transientT, antiT
        
        with open(filename) as file:
            data=json.load(file)

        print(data)
        file.close()
        taskList=[]
        recurringDates=[]

        for x in data: 
            if x.typelower() in recurringT:
                self.createTask(x["name"],x["type"], x["startTime"],x["duration"],x["startDate"],x["endDate"],x["frequency"])
            elif x.typelower() in transientT:
                self.createTask(x["name"],x["type"], x["startTime"],x["duration"],x["date"])
            else:
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
    
    def viewEntireSchedule(self):
        taskList.sort(key=lambda x: (x.date,x.startTime))
        if taskList:
            for x in taskList:
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
        file.close()
