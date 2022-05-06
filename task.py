from WOOP_PSS.schedule import Schedule
# Task Class will inherit from schedule
class Task(Schedule):
    # when a task object is created, pass in values for the attributes
    def __init__(self, name, type, startTime, duration, date):
        self.name = name
        self.type = type
        self.startTime = startTime
        self.duration = duration
        self.date = date
    def taskOverlap():
        pass