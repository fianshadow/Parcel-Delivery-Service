# Michael Lee - Student ID: 009966260

from HashTable import *
from Truck import Truck
from Package import *
from Graph import *
import datetime

def getPackageData(myHash):
    for i in range (packageSize('WGUPS Package File.csv')):
        package = myHash.search(i + 1)


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
    # print(f'Truck {Truck.number} Delivery Route:\n {Truck.route}')
    # print(f'Mileage: {Truck.mileage}')
    # print(f'Time: {start_time}')
    # print(f'Remaining Packages:\n{view_remaining_vertex(start_vertex, Truck.packageList, g)}')
    # print()

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
        # print(f'Truck {Truck.number} Delivery Route:\n {Truck.route}')

        # Updates the truck mileage
        Truck.mileage += mileage
        # print(f'Mileage: {Truck.mileage}')

        # Calculates the minutes to drive to next location based on 18 mph average speed
        Truck.time_value += (mileage * 60) / 18
        time_in_seconds = Truck.time_value * 60
        delta = datetime.timedelta(seconds=time_in_seconds)
        # Keeps track of what time the truck arrived to the vertex
        new_time = datetime.datetime.combine(datetime.date.today(), start_time) + delta
        # print(f'Time: {new_time.time()}')

        # Finds any package that needs to be delivered to the next vertex
        current_package = find_package_by_vertex(next_vertex, packageList)
        # Delivers the package and updates the status of the package
        delivered_package = myHash.search(current_package) # Finds the package by packageID
        delivered_package.status.append([f'Delivered by Truck {Truck.number} at {new_time.time()}', new_time.time()])
        myHash.insert(current_package, delivered_package)
        Truck.packageList.remove(current_package) # Removes delivered package from package list
        # print(f'Delivered Package: {myHash.search(current_package)}')

        # Keeps track of what packages are left to deliver
        # print(f'Remaining Packages:\n{view_remaining_vertex(start_vertex, Truck.packageList, g)}')
        # print()
        # Reassigns starting vertex to the next location
        start_vertex = next_vertex

    Truck.mileage += g.get_distance(start_vertex, 1)
    mileage = g.get_distance(start_vertex, 1)
    # print(f'Final Mileage: {Truck.mileage}')

    Truck.time_value += (mileage * 60) / 18
    time_in_seconds = Truck.time_value * 60
    delta = datetime.timedelta(seconds=time_in_seconds)
    new_time = datetime.datetime.combine(datetime.date.today(), start_time) + delta
    Truck.current_time = new_time.time()
    # print(f'Final Time: {new_time.time()}')

    Truck.route = Truck.route + ' -> ' + str(1)
    # print(f'Route: {Truck.route}')
    # print('************************************************************************************************************')
    # print()

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

##################################
# Deliver all packages
start_vertex = 1
deliver_all_packages(start_vertex, truck1, truck1.packageList, truck1.start_time, my_graph)
#
deliver_all_packages(start_vertex, truck3, truck3.packageList, truck3.start_time, my_graph)
#
deliver_all_packages(start_vertex, truck2, truck2.packageList, truck2.start_time, my_graph)
##################################

if __name__ == '__main__':
    print(f'\nWelcome to the WGU Postal Service Delivery System!\n')
    # For package 9, address needs to be updated as of 10:20am

    # Loop until user exits
    isExit = True
    while (isExit):
        print('\tMain Menu:')
        print('1. Check Status of Individual Package')
        print('2. Check Status of All Packages')
        print('3. View Truck Details')
        print('4. Exit the program')
        option = input("Please select an option (1, 2, 3, or 4): ")
        if option == '1':
            packageLoop = True
            while packageLoop:
                packageID = int(input("Please enter a package ID from 1 to 40: "))
                if 0 < int(packageID) <= 40:
                    timeLoop = True
                    while (timeLoop):
                        time = input("Please enter the time to check the status (military time - hh:mm): ")
                        hour = None
                        minute = None
                        if ':' in time:
                            time_parts = time.split(':')
                            if time_parts[0].isdigit() and time_parts[1].isdigit():
                                hour = time_parts[0]
                                minute = time_parts[1]
                                if (0 <= int(hour) <= 24) and (0 <= int(minute) <= 59):
                                    status_time = datetime.time(int(hour), int(minute))
                                    print(f'\nStatus for Package {packageID} as of {status_time}:')
                                    headers = ["ID", "Address", "City", "State", "Zip", "Deadline",
                                               "Weight", "Status", "Notes"]
                                    print(f'\t{headers[0]:<4}{headers[1]:^40}{headers[2]:^20}{headers[3]:^7}{headers[4]:^7}'
                                          f'{headers[5]:^10}{headers[6]:^8}{headers[7]:^38}{headers[8]:^20}')
                                    package = myHash.search(packageID)
                                    print(f'\t{package.ID:<4}{package.address:^40}{package.city:^20}{package.state:^7}'
                                            f'{package.zip:^7}{package.deadline:^10}{package.weight:^8}'
                                            f'{check_package_status(packageID, status_time):^38}{package.notes:^20}')
                                    print()
                                    timeLoop = False
                                else:
                                    print("Invalid time\n")
                            else:
                                print("Invalid time\n")
                        else:
                            print("Invalid time\n")
                    packageLoop = False
                else:
                    print("Invalid package ID\n")
        elif option == '2':
            timeLoop = True
            while (timeLoop):
                time = input("Please enter the time to check the status of all packages (military time - hh:mm): ")
                hour = None
                minute = None
                if ':' in time:
                    time_parts = time.split(':')
                    if time_parts[0].isdigit() and time_parts[1].isdigit():
                        hour = time_parts[0]
                        minute = time_parts[1]
                        if (0 <= int(hour) <= 24) and (0 <= int(minute) <= 59):
                            status_time = datetime.time(int(hour), int(minute))
                            print(f'\nStatus for All Packages as of {status_time}:')
                            headers = ["ID", "Address", "City", "State", "Zip", "Deadline",
                                       "Weight", "Status", "Notes"]
                            print(f'\t{headers[0]:<4}{headers[1]:^40}{headers[2]:^20}{headers[3]:^7}{headers[4]:^7}'
                                  f'{headers[5]:^10}{headers[6]:^8}{headers[7]:^38}{headers[8]:^20}')

                            for packageID in range(packageSize("WGUPS Package File.csv")):
                                package = myHash.search(packageID + 1)
                                print(f'\t{package.ID:<4}{package.address:^40}{package.city:^20}{package.state:^7}'
                                      f'{package.zip:^7}{package.deadline:^10}{package.weight:^8}'
                                      f'{check_package_status(packageID + 1, status_time):^38}{package.notes:^20}')
                            timeLoop = False
                            print()
                        else:
                            print("Invalid time\n")
                    else:
                        print("Invalid time\n")
                else:
                    print("Invalid time\n")

        elif option == '3':
            print('\nTruck 1:')
            print(f'\tStart Time:\t{truck1.start_time}\tEnd Time:\t{truck1.current_time}')
            print(f'\tMileage:\t{truck1.mileage:.2f}')
            print(f'\tDelivery Route (by vertex):\t{truck1.route}')
            print(f'\nTruck 2:')
            print(f'\tStart Time:\t{truck2.start_time}\tEnd Time:\t{truck2.current_time}')
            print(f'\tMileage:\t{truck2.mileage:.2f}')
            print(f'\tDelivery Route (by vertex):\t{truck2.route}')
            print(f'\nTruck 3:')
            print(f'\tStart Time:\t{truck3.start_time}\tEnd Time:\t{truck3.current_time}')
            print(f'\tMileage:\t{truck3.mileage:.2f}')
            print(f'\tDelivery Route (by vertex):\t{truck3.route}')
            print(f'\nTotal Mileage for all Trucks:\t{(truck1.mileage + truck2.mileage + truck3.mileage):.2f}')
            print()

        elif option == '4':
            isExit = False
        else:
            print("Invalid option\n")
