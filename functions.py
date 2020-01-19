from operator import itemgetter

def read_file(file):
    """
    this function reads a file. and prints it how it is read in the .txt.
    this function also adds the file into a dictionary.
    parameters:
    filename: the name of the file we want to read
    """
    try:
        file_object =  open(file,'r')
    except FileNotFoundError:
        msg = "ERROR: " + file + " does not exist"
        print(msg)
        exit()

    contents = file_object.read()
    return contents
    file_object.close()



def add_to_list(file):
    full_dict = []
    with open(file,'r') as file_object:
        for line in file_object:
            line_list = line.split()
            temp_dict = {}
            temp_dict['part number'] = int(line_list[0])
            temp_dict['description'] = line_list[1]
            temp_dict['price'] = float(line_list[2])
            temp_dict['supplier'] = line_list[3]
            temp_dict['maufactureno'] = int(line_list[4])
            full_dict.append(temp_dict)
    cars = []

    for dict in full_dict:
        cars.append(dict)
    for dict in cars:
        print(dict['part number'])
    return cars
    

def sorting(msg, cars):
    if msg  == "part number":
        newlist = sorted(cars, key=lambda k: k['part number'])
        return newlist
    elif msg == "price":
        newlist = sorted(cars, key=lambda k: k['price'])
        return newlist
    elif msg == "supplier":
        newlist = sorted(cars, key=lambda k: k['price'])
        return newlist
    else:
        print("ERROR: Category unknown")


def printlog(list):
    print("                 Full Catalog      \r")
    print("Part no.    Description      Price     Supplier    Manu. Part No.\r")
    print("----------------------------------------------------------------------------------\r")
    for dict in list:
        print(dict['part number'],"     ",dict['description'],"     ",dict['price'],"      ", dict['supplier'],"      ", dict['maufactureno'])

       




