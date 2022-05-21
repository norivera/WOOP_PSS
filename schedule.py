from asyncio import create_task
from antiTask import antiTask
from recurringTask import recurringTask
from transientTask import transientTask
import json
from datetime import datetime, timedelta, time

# David Johannsen
# CS 3560.03
# Cyrena Burke, Irfan Iqbal, Noe Rivera, Dany Flores, Alexa Tang
# May 20, 2022

taskList = [] # List of task objects
recurringDates=[] # List of all dates that contain a recurring task

# List of the task subtypes to determine which type
recurringT = ["class", "study", "sleep", "exercise", "work", "meal"]
transientT = ["visit", "shopping", "appointment"]
antiT = ["cancellation"]

class schedule:

    def __init__(self):
        global taskList, recurringDates, recurringT, transientT, antiT
        pass 

    # Method for creating a reucrring task including the extra sDate, eDate, frequency
    def createRecurringTask(self, name, type, sTime, duration, sDate, eDate, frequency):
        global taskList, recurringDates

        # Check inputs for name, type sTime, duration
        if  not self.checkInputs(name, type, sTime, duration, 20220516):
            return False

        # Check if the type is valid
        if type.lower() not in recurringT:
            print("Not a valid task type")
            return False
        
        # Round the start time and duration for the user
        duration= round(duration*4)/4
        sTime= round(sTime*4)/4

        # Check if the start and end dates are in the right format
        try:
            start =datetime.strptime(str(sDate), "%Y%m%d")
            end=datetime.strptime(str(eDate), "%Y%m%d")
        except ValueError: 
            print("This is the incorrect date string format. It should be YYYYMMDD. please try again")
            return False

        # Check if the frequency is between the start and end dates
        if not 1<= frequency <= (end-start).days:
            print("Frequency is not between start and end dates, please try again")
            return False

        # Calculate and create list of all the recurring Dates based on teh frequencry
        rDates = []
        day = start
        while day<= end:
            rDate=(int(day.strftime("%Y%m%d")),float(sTime),float(duration))
            rDates.append(rDate) #templist
            day += timedelta(days=frequency)

        # Compare the list of current Recurring Dates to the new one being created to check for overlap
        overlap=False
        for x in recurringDates: 
            for y in rDates:
                if x[0] == y[0]:
                    xStartTime = x[1]
                    xEndTime = x[1] + x[2] # end time for existing recurring task
                    sTime=int(sTime)
                    newTaskEnd = sTime + duration #ending time for the task being created

                    # Check 3 cases, if new task is between a task, starts before and ends between, or starts between and ends after
                    if ((sTime >= xStartTime) and (newTaskEnd <= xEndTime))\
                    or ((xStartTime <= sTime < xEndTime) and (newTaskEnd >= xEndTime))\
                    or ((sTime <= xStartTime) and (xStartTime < newTaskEnd <= xEndTime))\
                    or ((sTime <= xStartTime) and (newTaskEnd >= xEndTime)):
                        print("There is an overlapping Recurring Task, please try again")
                        return False
        # Compare the new reucrring dates to the current dates in taskList which includes transient and anti tasks
        for x in taskList: 
            for y in rDates:
                if x.date == y[0]:
                    xStartTime = x.startTime
                    xEndTime = x.startTime + x.duration # end time for existing recurring task
                    sTime=int(sTime)
                    newTaskEnd = sTime + duration #ending time for the task being created

                    # Check 3 cases, if new task is between a task, starts before and ends between, or starts between and ends after
                    if ((sTime >= xStartTime) and (newTaskEnd <= xEndTime))\
                    or ((xStartTime <= sTime < xEndTime) and (newTaskEnd >= xEndTime))\
                    or ((sTime <= xStartTime) and (xStartTime < newTaskEnd <= xEndTime))\
                    or ((sTime <= xStartTime) and (newTaskEnd >= xEndTime)):
                        print("There is an overlapping Transient task, please try again")
                        return False                

        # If no overlap, add recurring dates
        for r in rDates:
            recurringDates.append(r)
         
        # Create recurring task and append to the list
        newTask = recurringTask(name, type, sTime,duration,int(sDate),int(eDate),int(frequency))
        taskList.append(newTask)
        return True    

    # Create anti task
    def createAntiTask(self, name, type, sTime, duration, date):
        global taskList, recurringDates, antiT

        # Check inputs
        if not self.checkInputs(name, type, sTime, duration, date):
            return False

        # Check if anti task type is Cancellation
        if type.lower() not in antiT:
            print("Not a valid task type")
            return False

        # Round duration and StartTime to .25 increments
        duration= round(duration*4)/4
        sTime= round(sTime*4)/4
        
        # Check if anti task exactly overlaps a recurring task
        if (int(date), float(sTime), float(duration)) not in recurringDates:
            print("No recurring task during this date and time, please try again")
            return False
        else:
            recurringDates.remove((int(date), float(sTime), float(duration)))
            
        # Create anti task and append to the list
        newTask = antiTask(name, type, float(sTime),float(duration),int(date))
        taskList.append(newTask)

        return True

    # Create a transient task
    def createTransientTask(self, name, type, sTime, duration, date):
        global taskList, recurringDates, transientT

        # Check inputs
        if not self.checkInputs(name, type, sTime, duration, date):
            return False

        # Check if task type is in list and valid
        if type.lower() not in transientT:
            print("Not a valid task type")
            return False
        
        # Round duration and start time to .25 increments
        duration= round(duration*4)/4
        sTime= round(sTime*4)/4
        
        overlap=False
        # Check for overlap in taskList and recurring Dates for the 3 cases mentioned above
        for x in taskList: 
            if x.date == int(date) and x.type.lower() in transientT:
                xStartTime = x.startTime
                xEndTime = x.startTime + x.duration # end time for existing recurring task
                newTaskEnd = sTime + duration #ending time for the task being created

                if ((sTime >= xStartTime) and (newTaskEnd <= xEndTime))\
                or ((xStartTime <= sTime < xEndTime) and (newTaskEnd >= xEndTime))\
                or ((sTime <= xStartTime) and (xStartTime < newTaskEnd <= xEndTime))\
                or ((sTime <= xStartTime) and (newTaskEnd >= xEndTime)):
                    overlap=True
                    #print("There is an overlapping Transient task, please try again")
                    #return False    

        for x in recurringDates: 

            if x[0] == int(date):
                xStartTime = x[1] 
                xEndTime = x[1] + x[2] # end time for existing recurring task
                stime=int(sTime)
                newTaskEnd = sTime + duration #ending time for the task being created 

                if ((sTime >= xStartTime) and (newTaskEnd <= xEndTime))\
                or ((xStartTime <= sTime < xEndTime) and (newTaskEnd >= xEndTime))\
                or ((sTime <= xStartTime) and (xStartTime < newTaskEnd <= xEndTime))\
                or ((sTime <= xStartTime) and (newTaskEnd >= xEndTime)):
                    overlap = True

                if overlap:
                    for i in taskList:
                        if i.date== x[0] and i.type.lower()== "cancellation" and i.startTime==x[1] and i.duration==x[2]:
                            overlap=False
                       
                if overlap:
                    print("There is an overlapping task, please try again")
                    return False
                
        # Create transient task and append to the list
        newTask = transientTask(name, type, sTime,duration,int(date))
        taskList.append(newTask)

        return True

    
    def checkInputs(self, name, type, sTime, duration, date):
        '''
            Checking the task data inputs, ensuring that the name is unique,
            that the duration and sTime are between the correct ranges, and 
            that the date is in the correct format
        '''
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


   # Find and view task attributs based on the name in taskList
    def viewTask(self, name):
        global taskList
        for x in taskList:
                if x.name==name:
                    print(x.name, x.type, x.startTime, x.duration, x.date)

    
    # Method to find and delete task and any recurring dates based on the name
    def deleteTask(self,name):
        global taskList, recurringDates, recurringT
        
        t=""
        # Once task is found, get the rest of the attributes
        for i in taskList:
            if i.name==name:
                t=i.type
                s=i.date
                # If recurring task, get end date, frequency, and duration
                if t.lower() in recurringT:
                    e=i.endDate
                    f=i.frequency
                    d=i.duration
                sT=i.startTime
                break
        taskList = list( filter(lambda x: x.name != name, taskList)) # Creates new list without given name task
        
        # Re-calculate the recurring dates if recurring task and delete from the recurringDates list
        if t.lower() in recurringT:
            start =datetime.strptime(str(s), "%Y%m%d")
            end=datetime.strptime(str(e), "%Y%m%d")
            day = start
            while day<= end:
                if (int(day.strftime("%Y%m%d")),sT,d) in recurringDates:
                    recurringDates.remove((int(day.strftime("%Y%m%d")),sT,d))
                day += timedelta(days=f)

    # Edit a task by deleting by name and recreating it using the createTask method based on the type
    def editTask(self, name, type, sTime, duration, date=0,sDate=0,eDate=0,freq=0):
        '''
            This method searches for the task that the user would like to edit by its
            unique name, and reassigns the values to the new task data
        '''
        global taskList, recurringDates, recurringT, transientT, antiT
    
        for i in taskList:
            if i.name==name:
                t=i.type
                s=i.date
                # If recurring task, get end date, frequency, and duration
                if t.lower() in recurringT:
                    e=i.endDate
                    f=i.frequency
                    d=i.duration
                sT=i.startTime
                break
        taskList = list( filter(lambda x: x.name != name, taskList)) # Creates new list without given name task
        
        # Re-calculate the recurring dates if recurring task and delete from the recurringDates list
        if t.lower() in recurringT:

            start =datetime.strptime(str(s), "%Y%m%d")
            end=datetime.strptime(str(e), "%Y%m%d")

            day = start
            while day<= end:
                if (day.strftime("%Y%m%d"),sT,d) in recurringDates:
                    recurringDates.remove((day.strftime("%Y%m%d"),sT,d))
                day += timedelta(days=f)

            
        # Re-create the task based on the type
    # Method writes schedule to Json file       if t.lower() in recurringT:    
            self.createRecurringTask(name, type, sTime, duration,sDate,eDate,freq)
        elif t.lower() in transientT:
            self.createTransientTask(name,type, sTime, duration, date)
        else:
            self.createAntiTask(name,type, sTime, duration, date)


    # Dumps the contents of taskList into a file in json format sorted by date and then time
    def writeScheduleToFile(self):
    # Method reads schedule from Json file        global taskList

        taskList.sort(key=lambda x: (x.date,x.startTime))

        with open("./data/schedule.json", "w") as file:
            json.dump([ob.__dict__ for ob in taskList], file)
        file.close()
            

    # Read Schedule from given file 
    def readScheduleFromFile(self,filename):
        global taskList, recurringDates, recurringT, transientT, antiT
        
        with open(filename) as file:
            data=json.load(file)
            
        file.close()
        # creprints schedule for a specific time period: day, week, or monthating task objects based on the type, to make the appriopriate function calls
        for x in data: 
            if x["Type"].lower() in recurringT:
                self.createRecurringTask(x["Name"],x["Type"], float(x["StartTime"]),float(x["Duration"]),int(x["StartDate"]),int(x["EndDate"]),int(x["Frequency"]))
            elif x["Type"].lower() in transientT:
                self.createTransientTask(x["Name"],x["Type"], float(x["StartTime"]),float(x["Duration"]),int(x["Date"]))
            else:
                self.createAntiTask(x["Name"],x["Type"], float(x["StartTime"]),float(x["Duration"]),int(x["Date"]))


    def viewSchedule(self, period, startDate):
        '''
        printing the schedule for a specified day, week, or month
        '''
        
        # Calculate the endDate based on the period of time given(1 for day, 7 for week, and 30 for month)
        endDate= startDate
        if period=="day":
            endDate = (datetime.strptime(str(startDate), '%Y%m%d') + timedelta(days=1)).strftime('%Y%m%d')
        elif period=="week":
            endDate = (datetime.strptime(str(startDate), '%Y%m%d') + timedelta(weeks=1)).strftime('%Y%m%d')
        elif period=="month":
            endDate = (datetime.strptime(str(startDate), '%Y%m%d') + timedelta(days=30)).strftime('%Y%m%d')
        
        # Sort and print out the tasks
        taskList.sort(key=lambda x: (x.date,x.startTime))
        if taskList:    
            for x in taskList:
                if str(startDate) <= str(x.date) <= endDate:
                            print(x.date, x.name, ", ", x.type,": " ,x.startTime, ", ", x.duration)
    
    # Prints out all the tasks in the scheudle
    def viewEntireSchedule(self):
        global taskList, recurringDates


       # Sort by date and then time and print out all tasks
        taskList.sort(key=lambda x: (x.date,x.startTime))
        if taskList:
                for x in taskList:
                    print(x.date, x.name, ", ", x.type,": " ,x.startTime, ", ", x.duration)
    
    # Write Schedule to file based on given time period in json format
    def writeSchedule(self, fileName, period, startDate):
        
        # Calculate end date based on given time period
        endDate= startDate
        if period=="day":
            endDate = (datetime.strptime(str(startDate), '%Y%m%d') + timedelta(days=1)).strftime('%Y%m%d')
        elif period=="week":
            endDate = (datetime.strptime(str(startDate), '%Y%m%d') + timedelta(weeks=1)).strftime('%Y%m%d')
        elif period=="month":
            endDate = (datetime.strptime(str(startDate), '%Y%m%d') + timedelta(days=30)).strftime('%Y%m%d')

        # Create sublist based on tasks within the given time frame
        subList = list( filter(lambda x: str(startDate) <= str(x.date) <= endDate, taskList))
    
        # Sort tasks in sublist and print them out
        subList.sort(key=lambda x: (x.date,x.startTime))
        with open(fileName, "w") as file:
            json.dump([ob.__dict__ for ob in subList], file)
        file.close()
