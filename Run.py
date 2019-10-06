from db_class import *
server = 'localhost,1433'
database = 'Game'
username = 'SA'
password = 'Passw0rd2018'

Game = Game_Listing(server,database,username,password)

##As a user i can create one game

#Game.create("'Wretch32'", "'Mario Kart'", "'40.00'","'07984632101'","'Oxford'","''","''")
#Game.read(2)
#Game.read_all()
#Game.delete(4)
Game.location(2)



















#
# name = input("Tell me your name: ")
# print('Hello', name, 'and Welcome to Via where you can list your old games and cash out', )
# listings = input('would you like to view all our listings for today?')
# if input != 'no':
#     print('These are all our current listings:')
# Game.read_all()
#
# user_input = ''
# while user_input!='no' :
#     user_input= input( name + ' would you like to create a listing ?')
#     if user_input=='no':
#         print('ffs what do u want to do?' )
#     elif user_input== 'yes':
#         username = input('create a username')
#         game = input('Enter the name of the game you would like to list ')
#         price = input('how much would you like to list it for')
#         phone = input('Please enter your telephone number')
#         location = input('Please enter your city')
#         newgame= Game_Listing(username,game,price,phone,location)
#         print(newgame)
#         Game.read_all()
#
#     else:
#         print('Not valid try again')
#
#
#     def write(self):
#         Game_Listing = Game()
#         Username = input("create a username: ")
#         game = input("Enter the name of the game you would like to list: ")
#         price = input("how much would you like to list it for: ")
#         phone = input("Please enter your telephone number: ")
#         location = input("Please enter your city: ")
#
#         try:
#             Game_Listing.cursor.execute(f"INSERT INTO Game_Listing (Username,Game,Price,Phone,Location) VALUES({username},{game},{price},{phone},{location}");
#         except:
#             print("Something has gone wrong. Please check the code!")