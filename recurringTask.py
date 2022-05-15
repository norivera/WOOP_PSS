from task import task
class recurringTask(task):
    def __init__(self, name, type, startTime, duration, sDate, eDate, freq):
        #parent class constructor called (parent = Task class)
        super().__init__(name, type, startTime, duration, sDate)
        self.endDate= eDate
        self.frequency=freq