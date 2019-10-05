from db_class import *
server = 'localhost,1433'
database = 'Game'
username = 'SA'
password = 'Passw0rd2018'

Game = Game_Listing(server,database,username,password)

##As a user i can create one game

#Game.create("'Wretch32'", "'Mario Kart'", "'40.00'","'07984632101'","'Oxford'","''","''")
#Game.read(2)
Game.read_all()
#Game.delete(4)