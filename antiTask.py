from task import task
class antiTask(task):
    def __init__(self, name, type, startTime, duration, date):
        #parent class constructor called (parent = Task class)
        super().__init__(name, type, startTime, duration, date)