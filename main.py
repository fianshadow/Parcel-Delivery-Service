# Michael Lee - Student ID: 009966260

from HashTable import *
from Truck import Truck
from Package import *
from Graph import *
import datetime

def getPackageData(myHash):
    for i in range (packageSize('WGUPS Package File.csv')):
        print(f"{myHash.search(i + 1)}")

def check_package_status(packageID, current_time):
    package = myHash.search(packageID)
    statuses = package.status
    current_status = 'Unknown'
    for i, status in enumerate(statuses):
        if status[-1] <= current_time:
            current_status = status[-2]
        else:
            break
    return current_status

def deliver_all_packages(start_vertex, Truck, packageList, start_time, g):
    print(f'Truck {Truck.number} Delivery Route:\n {Truck.route}')
    print(f'Mileage: {Truck.mileage}')
    print(f'Time: {start_time}')
    print(f'Remaining Packages:\n{view_remaining_vertex(start_vertex, Truck.packageList, g)}')
    print()

    # Updates the status of each package to 'In Route' once function gets ran
    for packageID in packageList:
        current_package = myHash.search(packageID)
        current_package.status.append([f'In Route on Truck {Truck.number} as of {start_time}', start_time])
        myHash.insert(packageID, current_package)

    # While there are still packages on the truck...
    while (packageList):
        # Finds the closest vertex where there is a package to be delivered
        next_vertex, mileage = find_closest_vertex(start_vertex, packageList, g)

        # Updates the truck route
        Truck.route = Truck.route + ' -> ' + str(next_vertex)
        print(f'Truck {Truck.number} Delivery Route:\n {Truck.route}')

        # Updates the truck mileage
        Truck.mileage += mileage
        print(f'Mileage: {Truck.mileage}')

        # Calculates the minutes to drive to next location based on 18 mph average speed
        Truck.time_value += (mileage * 60) / 18
        time_in_seconds = Truck.time_value * 60
        delta = datetime.timedelta(seconds=time_in_seconds)
        # Keeps track of what time the truck arrived to the vertex
        new_time = datetime.datetime.combine(datetime.date.today(), start_time) + delta
        print(f'Time: {new_time.time()}')

        # Finds any package that needs to be delivered to the next vertex
        current_package = find_package_by_vertex(next_vertex, packageList)
        # Delivers the package and updates the status of the package
        delivered_package = myHash.search(current_package) # Finds the package by packageID
        delivered_package.status.append([f'Delivered by Truck {Truck.number} at {new_time.time()}', new_time.time()])
        myHash.insert(current_package, delivered_package)
        Truck.packageList.remove(current_package) # Removes delivered package from package list
        print(f'Delivered Package: {myHash.search(current_package)}')

        # Keeps track of what packages are left to deliver
        print(f'Remaining Packages:\n{view_remaining_vertex(start_vertex, Truck.packageList, g)}')
        print()
        # Reassigns starting vertex to the next location
        start_vertex = next_vertex

    Truck.mileage += g.get_distance(start_vertex, 1)
    mileage = g.get_distance(start_vertex, 1)
    print(f'Final Mileage: {Truck.mileage}')

    Truck.time_value += (mileage * 60) / 18
    time_in_seconds = Truck.time_value * 60
    delta = datetime.timedelta(seconds=time_in_seconds)
    new_time = datetime.datetime.combine(datetime.date.today(), start_time) + delta
    Truck.start_time = new_time.time()
    print(f'Final Time: {new_time.time()}')

    Truck.route = Truck.route + ' -> ' + str(1)
    print(f'Route: {Truck.route}')
    print('************************************************************************************************************')
    print()

# Create and load the graph
my_graph = Graph()
my_graph.load_vertices('WGUVertices.csv')
my_graph.load_edges('WGUEdges.csv')

# Create and load the trucks
start_time = datetime.time(8, 00)
truck1 = Truck(1, start_time)
truck1.packageList.extend([1,7,8,13,14,15,16,19,20,21,29,30,34,37,39,40])

start_time = datetime.time(12, 00)
truck2 = Truck(2, start_time)
truck2.packageList.extend([3,4,5,9,10,11,12,17,18,22,24,36,38])

start_time = datetime.time(9, 15)
truck3 = Truck(3, start_time)
truck3.packageList.extend([2,6,23,25,26,27,28,31,32,33,35])

start_time = datetime.time(7, 00)



current_time = datetime.time(8,3)
print('Checking Package Status:')
print(check_package_status(1, current_time))
print()

##################################
# Deliver all packages
start_vertex = 1
deliver_all_packages(start_vertex, truck1, truck1.packageList, truck1.start_time, my_graph)
#
deliver_all_packages(start_vertex, truck3, truck3.packageList, truck3.start_time, my_graph)
#
deliver_all_packages(start_vertex, truck2, truck2.packageList, truck2.start_time, my_graph)

print(f'Total Combined Truck Mileage: {truck1.mileage + truck2.mileage + truck3.mileage}')
print(f'Time Finished: {max(truck1.start_time, truck2.start_time, truck3.start_time)}')
print()
##################################

current_time = datetime.time(12, 30)
print('Checking Package Status:')
print(check_package_status(11, current_time))
print()

if __name__ == '__main__':
    print('Welcome to the WGU Postal Service Delivery System!')
    # 1. print all package status by truck as of a time
    # 2. print total mileage as of a time

    # 2. get a single package status with a time
    # 3. get all package status with a specific time
    # 4. exit the program

    # For package 9, address needs to be updated as of 10:20am

    # Loop until user exits
    isExit = True
    while (isExit):
        print('\n\tOptions:')
        print('1. Package Status')
        print()
        option = input("Please select an option (ex. 1, 2, 3, or 4): ")
        if option == '1':
            isExit = False
        elif option == '2':
            isExit = False
        elif option == '3':
            isExit = False
        elif option == '4':
            isExit = False
        else:
            print("Invalid option")
