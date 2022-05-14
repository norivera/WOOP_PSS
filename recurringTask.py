from task import task
class recurringTask(task):
    def __init__(self, name, type, startTime, duration, date, sDate, eDate, freq):
        #parent class constructor called (parent = Task class)
        super().__init__(name, type, startTime, duration, date)
        startDate= sDate
        endDate= eDate
        frequency=freq