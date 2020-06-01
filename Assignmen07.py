# ------------------------------------------------- #
# Title: Assignment07
# Description: A simple example of storing data in a binary file
# ChangeLog: (Who, When, What)
# SHuang, 5.31.2020, Created pickling script
# SHuang, 5.31.2020, Added try-except block
# Shuang, 5.31.2020, Finalized script using both pickling and try-except error handling
# ------------------------------------------------- #

import pickle

#-----------------------Data -------------------------------------------- #

# Declare variables
strFileName = 'teams.dat'
lstTeam = []


#-----------------------Processing -------------------------------------- #

def save_data_to_file(file_name, list_of_data):
    file = open(file_name, "ab") # write data to binary file
    pickle.dump(list_of_data, file)
    file.close()


def read_data_from_file(file_name):
    file = open(file_name, "rb")
    list_of_data = pickle.load(file)  # load() only loads one row of data.
    file.close()
    return list_of_data


#------------------------Presentation ------------------------------------ #

# Get sport and team name from user
# Try-except block prevents user from entering sport as integer or number
try:
    strSport = input("Enter a Sport: ")
    if strSport.isnumeric():
            raise Exception ("Do not use numbers for sports")

except Exception as e:
        print("You made a mistake!")
        print(e)
        exit()

#strSport = str(input("Enter a Sport: "))
strTeam = str(input("Enter a Team: "))
lstTeam = [strSport, strTeam]


print(lstTeam[0], lstTeam[1], sep= " | ")

# Store data in binary file
save_data_to_file(strFileName, lstTeam)


#print(read_data_from_file(strFileName))