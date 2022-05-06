import task
class Schedule:
    taskList #List of task object
    def __init__(self):
        pass
    def checkName(name):
        '''
        ensure that each task has a unique name for searching purposes
        loop thru all the task names to find a match
        return true if name does not exist, false if it does
        '''
        pass
    def createTask(name, type, sTime, duration, date):
        if(checkName(name)):
            newTask = Task(name, type, sTime,duration,date)
        else:
            return "task creation failed"

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
        printing the schedul efor a specified day, week, or month
        '''
        pass
    def writeSchedule(fileName, period, startDate):
        '''
        updating the schedule for a specified day, week, or month
        '''
        pass