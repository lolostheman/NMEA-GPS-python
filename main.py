import functions

file = input("Enter Catalog File Name:")
functions.read_file(file)
cars = []
cars = functions.add_to_list(file)



str = input("Do you want to sort the catalog by part number, price or supplier?")

sortedcars = []
sortedcars = functions.sorting(str, cars)
functions.printlog(sortedcars)


