
class task:
    # when a task object is created, pass in values for the attributes
    def __init__(self, name, type, startTime, duration, date):
        '''
        initializing the info for each task
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

    #### SETTER AND GETTER METHODS ####
    def getName(self):
        return self.name
    def getType(self):
        return self.type
    def getStartTime(self):
        return self.startTime
    def getDuration(self):
        return self.duration
    def getDate(self):
        return self.date
    
    def setName(self, name):
        self.name = name
    def setType(self, type):
        self.type = type
    def setStartTime(self, startTime):
        self.startTime = startTime
    def setDuration(self, duration):
        self.duration = duration
    def setDate(self, date):
        self.date = date