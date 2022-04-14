def database_sort(database, m, n, k):
    values = []
    index = []
    sorted_database = []

    #in here we are just storing the values of each
    #Kth attribute along with its index so we can sort it later
    for i in range(n):
            values.append(database[i][k])
            index.append(i)

    # This sorts the Kth index for us along with the index which
    # can help us sorting the whole database
    for j in range(len(values)):
        for f in range(j+1,len(values)):
            if (values[j] > values[f]):
                values[j], values[f] = values[f], values[j]
                index[j], index[f] = index[f], index[j]

    #adds the rows to the new databse so that we can fill it in later
    for l in range(n):
        sorted_database.append([])

    #We are getting the values from the old database to the new one
    #But this time we are getting it in order, i did it by order.
    # by iterating through the indices that go first in "index[]"
    for q in range(n):
        for attribute in range(m):
            sorted_database[q].append(database[index[q]][attribute])

    #returning our final value
    return sorted_database

def get_inputs():
    #creating the initial inputs needed
    database = []
    n = int(input("Enter the number of athletes: "))
    m = int(input("Enter the number of attributes: "))
    #As you see in here, python starts countinmg from 0 however
    #for a user friendly way i have done it so they can choose from 1
    #so its less confusing but the program will still work the same way
    k = int(input("What attribute do you want to sort 1 - {0}: ".format(m))) - 1

    #we are now getting the inputs however many times the
    #user has told us to
    for i in range(n):
        attribute_num = 0
        database.append([])
        for f in range(m):
            database[i].append("value")
        for j in range(m):
            print("Enter the values for athlete number ", i+1)
            attribute_add = int(input("Enter the value of attribute {0}: ".format(attribute_num+1)))
            database[i][j] = attribute_add
            attribute_num += 1

    #returning values needed for us to sort.
    return database, m, n, k

def print_database(sorted_database, columns, rows):
    #it can be hard for normal users to understand 2d lists
    #so this is a method to make the databse better looking
    #to make it more user friendly.

    print("Here is the sorted database: \n")

    for i in range(columns):
        print(sorted_database[i])


def main():
    database, m, n, k = get_inputs()

    sorted_database = database_sort(database, m, n, k)

    print_database(sorted_database, n, m)

main()
