import sqllite3

class DataBase:
    def __init__(self,dbName):
        self.dbName = dbName
        self.bConnnect = false
    def connect():
        self.conn = sqllite3.connect(self.dbName)
