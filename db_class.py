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

    def create (self,username, game,price,phone,location,longitude,latitude):
        create_listing = f"INSERT INTO Game_Listing (Username,Game,Price,Phone,Location,Longitude,Latitude) VALUES({username},{game},{price},{phone},{location},{longitude},{latitude})"
        self.cursor.execute(create_listing)
        self.conn_Game.commit()



    def read (self,ID):
        find_specific_listing = self.cursor.execute(f"SELECT * FROM Game_Listing WHERE GameID = {ID}").fetchone()
        print(find_specific_listing)

    def read_all(self):
        read_all_listing = self.cursor.execute(f"SELECT * FROM Game_listing").fetchall()
        for data in read_all_listing:
            print(f" {data[0]}, {data[1]},{data[2]},{data[3]},{data[4]},{data[5]},{data[6]},{data[7]}")

    def delete(self,ID):
        delete_listing = f"DELETE Game_Listing WHERE GameID = {ID}"
        self.cursor.execute(delete_listing)
        self.conn_Game.commit()

    def location(self, ID):
        query = self.cursor.execute(f"SELECT Location FROM Game_listing WHERE GameID = {ID}")
        postcode = query.fetchone()
        argument = ' '.join(row for row in postcode)
        path = 'http://api.postcodes.io/postcodes/'
        request_postcode = requests.get(path + argument)
        post_code_dict = request_postcode.json()   #decode json strings into python objects
        longitude = post_code_dict ['result']['longitude'] #result is the key the values that i want are for long and lat
        latitude = post_code_dict['result']['latitude']
        update_listing = f"UPDATE Game_Listing SET Longitude = {longitude}, Latitude = {latitude} WHERE GameID = {ID}"
        self.cursor.execute(update_listing)
        self.conn_Game.commit()

        # print(f' longitude :'),print(details)
        # print(f' latitude :'), print(details2)

