def read_file():
    """
    this function reads a file
    parameters:
    filename: the name of the file we want to read
    """
try:
    file = input("Enter Catalog File Name:")
    file_object =  open(file,'r')
except FileNotFoundError:
    msg = "ERROR: " + file + " does not exist"
    print(msg)
    exit()

contents = file_object.read()
print(contents)
file_object.close()
"""
this part reads the file to a list/dictionary
"""
full_dict = []
with open(file,'r') as file_object:
    for line in file_object:
        line_list = line.split()
        temp_dict = {}
        temp_dict['partno'] = int(line_list[0])
        temp_dict['description'] = line_list[1]
        temp_dict['price'] = float(line_list[2])
        temp_dict['supplier'] = line_list[3]
        temp_dict['maufactureno'] = int(line_list[4])
        full_dict.append(temp_dict)
        
for dict in full_dict:
     print(dict)


