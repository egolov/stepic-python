import time

class Loggable:
    def log(self, msg):
        print(str(time.ctime()) + ": " + str(msg))

class LoggableList(list, Loggable):
    def append(self, item):
        super().append(item)
        self.log(item)

l = LoggableList()
l.append(1)
