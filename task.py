from xml.dom.expatbuilder import parseString
from WOOP_PSS.schedule import Schedule
# Task Class will inherit from schedule
class Task(Schedule):
    # when a task object is created, pass in values for the attributes
    def __init__(self, name, type, startTime, duration, date):
        '''
        initializing the info for each task, and input checking here
        try catch?
        '''
        self.name = name
        self.type = type
        self.startTime = startTime
        self.duration = duration
        self.date = date
    #passing in the taskList from parent or directly accessing in method??
    def taskOverlap(taskList, task):
        '''
        When creating transient tasks, if recurring, check if there is an anti-task to cancel it; if
        so, the transient task is not overlapping 
        '''
        pass