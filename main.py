import functions



file = input("Enter Catalog File Name:")
functions.read_file(file)
cars = []
cars = functions.add_to_list(file)


sortedcars = []
str = input("Do you want to sort the catalog by supplier, price, or part number?:")

while functions.sorting(str, cars) == 0:
    str = input("Do you want to sort the catalog by supplier, price, or part number?:")

sortedcars = functions.sorting(str, cars)

functions.printlog(sortedcars,str)



