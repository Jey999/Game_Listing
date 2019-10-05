import pyodbc
import requests
class Game_Listing:
    def __init__(self, server,database,username,password):
        self.server = server
        self.database = database
        self.username = username
        self.password = password
        self.conn_Game = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+password)
        self.cursor = self.conn_Game.cursor()

    def filter_query(self,query):
        return self.cursor.execute(query)