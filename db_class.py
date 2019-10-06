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

    def location_details(self, ID):
        query = self.cursor.execute(f"SELECT Location FROM Game_listing WHERE GameID = {ID}")
        postcode = query.fetchone()
        pc = ' '.join([row for row in postcode])
        url = 'http://api.postcodes.io/postcodes/'
        request_postcode = requests.get(url + pc)
        post_code_dict = request_postcode.json()
        details = post_code_dict
        print(details)

    # name = input("Tell me your name: ")
    # print('Hello', name, 'and Welcome to Via where you can list your old games and cash out', )
    # listings = input('would you like to view all our listings for today?')
    # if input != 'no':
    #     print('These are all our current listings:')
    # for listings in Game.read_all():
    #
    #
    # while user_input != 'no':
    #     add_pet = input(name + ' would you like to add a pet ?')
    #     if add_pet == 'no':
    #         print('ffs what do u want to do?')
    #     elif add_pet == 'yes':
    #         pet_owner = input('can i get the name of the owner please?')
    #         pet_name = input('can i get the name of your pet please?')
    #         pet_specie = input('what specie is your pet?')
    #         pet_breed = input('what breed is that?')
    #         new_pet = Pet(pet_owner, pet_name, pet_specie, pet_breed)
    #         pet_list.append(new_pet)
    #         for pets in pet_list:
    #             print('Pet owner:', pets.owner, ',  ', 'Pet name:', pets.name)
    #         print('your pet has now been added to Vet Delight :)')
    #         break
    #     else:
    #         print('Not valid try again')