# Michael Lee - Student ID: 009966260

from Truck import Truck
from Graph import *
import datetime


# Checks the status of a package given a specific time.
def check_package_status(package_id, time_test):
    # Find package in hash table
    package = myHash.search(package_id)

    status_list = package.status
    current_status = 'Unknown'
    # Checks for the address as of time_test
    for i, status in enumerate(status_list):
        if status[1] <= time_test:
            current_status = status[0]
        else:
            break
    return current_status


# Checks the address of a package given a specific time.
def check_address(package_id, time_test):
    # Find package in hash table
    package = myHash.search(package_id)

    address_list = package.address
    current_address = 'Unknown'
    # Check for the address as of time_test
    for i, address in enumerate(address_list):
        if address[1] <= time_test:
            current_address = address[0]
        else:
            break

    city_list = package.city
    current_city = 'Unknown'
    # Check for the city as of time_test
    for i, city in enumerate(city_list):
        if city[1] <= time_test:
            current_city = city[0]
        else:
            break

    zip_code_list = package.zip_code
    current_zip_code = 'Unknown'
    # Check for the zip_code as of time_test
    for i, zip_code in enumerate(zip_code_list):
        if zip_code[1] <= time_test:
            current_zip_code = zip_code[0]
        else:
            break

    state_list = package.state
    current_state = 'Unknown'
    # Check for the state as of time_test
    for i, state in enumerate(state_list):
        if state[1] <= time_test:
            current_state = state[0]
        else:
            break

    return current_address, current_city, current_zip_code, current_state


# Delivers all the packages on a given truck starting from vertex 1.
def deliver_all_packages(start_vertex, Truck, packageList, start_time, g):
    # # PRINTS FOR DEBUGGING PURPOSES
    # print(f'Truck {Truck.number} Delivery Route:\n {Truck.route}')
    # print(f'Mileage: {Truck.mileage}')
    # print(f'Time: {start_time}')
    # print(f'Remaining Packages:\n{view_remaining_vertex(start_vertex, Truck.packageList, g)}')
    # print()

    # Updates the status of each package to 'In Route' once function starts
    for packageID in packageList:
        current_package = myHash.search(packageID)
        current_package.status.append([f'In Route on Truck {Truck.number} - {start_time}', start_time])
        myHash.insert(packageID, current_package)

    # While there are still packages on the truck...
    while (packageList):
        # Finds the closest vertex where there is a package to be delivered
        next_vertex, mileage = find_closest_vertex(start_vertex, packageList, g)

        # Updates the truck route
        Truck.route = Truck.route + ' -> ' + str(next_vertex)
        # # PRINT FOR DEBUGGING PURPOSES
        # print(f'Truck {Truck.number} Delivery Route:\n {Truck.route}')

        # Updates the truck mileage
        Truck.mileage += mileage
        # # PRINT FOR DEBUGGING PURPOSES
        # print(f'Mileage: {Truck.mileage}')

        # Calculates the minutes to drive to next location based on 18 mph average speed
        Truck.time_value += (mileage * 60) / 18
        time_in_seconds = Truck.time_value * 60
        delta = datetime.timedelta(seconds=time_in_seconds)
        # Keeps track of what time the truck arrived to the vertex
        new_time = datetime.datetime.combine(datetime.date.today(), start_time) + delta
        # # PRINT FOR DEBUGGING PURPOSES
        # print(f'Time: {new_time.time()}')

        # Finds any package that needs to be delivered to the next vertex
        current_package = find_package_by_vertex(next_vertex, packageList)
        delivered_package = myHash.search(current_package)  # Finds the package by packageID
        # Delivers that package and updates the status of the package
        delivered_package.status.append([f'Delivered by Truck {Truck.number} - {new_time.time()}', new_time.time()])
        # Updates the hash table
        myHash.insert(current_package, delivered_package)
        Truck.packageList.remove(current_package)  # Removes delivered package from package list
        # # PRINT FOR DEBUGGING PURPOSES
        # print(f'Delivered Package: {myHash.search(current_package)}')

        # Reassigns starting vertex to the next location
        start_vertex = next_vertex

        # # # PRINTS FOR DEBUGGING PURPOSES: Keeps track of what packages are left to deliver
        # print(f'Remaining Packages:\n{view_remaining_vertex(start_vertex, Truck.packageList, g)}')
        # print()

    # Updates truck mileage
    Truck.mileage += g.get_distance(start_vertex, 1)
    mileage = g.get_distance(start_vertex, 1)
    # # PRINT FOR DEBUGGING PURPOSES
    # print(f'Final Mileage: {Truck.mileage}')

    # Updates truck time
    Truck.time_value += (mileage * 60) / 18
    time_in_seconds = Truck.time_value * 60
    delta = datetime.timedelta(seconds=time_in_seconds)
    new_time = datetime.datetime.combine(datetime.date.today(), start_time) + delta
    Truck.current_time = new_time.time()
    # # PRINT FOR DEBUGGING PURPOSES
    # print(f'Final Time: {new_time.time()}')

    # Updates truck route
    Truck.route = Truck.route + ' -> ' + str(1)
    # # PRINT FOR DEBUGGING PURPOSES
    # print(f'Route: {Truck.route}')
    # print('************************************************************************************************************')
    # print()


# Create and load the graph
my_graph = Graph()
my_graph.load_vertices('WGUVertices.csv')
my_graph.load_edges('WGUEdges.csv')


# Create and load the trucks
load_time = datetime.time(7, 00)

truck1 = Truck(1, load_time)
truck1.packageList.extend([1, 7, 8, 13, 14, 15, 16, 19, 20, 21, 29, 30, 34, 37, 39, 40])
# Update the status of each package
for package in truck1.packageList:
    current_package = myHash.search(package)
    current_package.status.append([f'Loaded onto Truck {truck1.number} - {load_time}', load_time])
# The time the truck leaves on delivery
truck1_start_time = datetime.time(8, 00)

truck2 = Truck(2, load_time)
truck2.packageList.extend([3, 4, 5, 9, 10, 11, 12, 17, 18, 22, 24, 36, 38])
# Update the status of each package
for package in truck2.packageList:
    current_package = myHash.search(package)
    current_package.status.append([f'Loaded onto Truck {truck2.number} - {load_time}', load_time])
# The time the truck leaves on delivery
truck2_start_time = datetime.time(12, 00)

truck3 = Truck(3, load_time)
truck3.packageList.extend([2, 6, 23, 25, 26, 27, 28, 31, 32, 33, 35])
# Update the status of each package
for package in truck3.packageList:
    current_package = myHash.search(package)
    current_package.status.append([f'Loaded onto Truck {truck3.number} - {load_time}', load_time])
# The time the truck leaves on delivery
truck3_start_time = datetime.time(9, 15)


# Package 9 Address is being updated as of 10:20 am
# Correct Address (410 S. State St., Salt Lake City, UT 84111)
package = myHash.search(9)
current_time = datetime.time(10, 20)
package.address.append(["410 S State St", current_time])
package.city.append(["Salt Lake City", current_time])
package.zip_code.append(["84111", current_time])


##################################
# Deliver all packages
start_vertex = 1
deliver_all_packages(start_vertex, truck1, truck1.packageList, truck1_start_time, my_graph)

deliver_all_packages(start_vertex, truck3, truck3.packageList, truck3_start_time, my_graph)

deliver_all_packages(start_vertex, truck2, truck2.packageList, truck2_start_time, my_graph)
##################################

# START OF PROGRAM
if __name__ == '__main__':

    print(f'\nWelcome to the WGU Postal Service Delivery System\n')
    # Loop until user exits
    mainMenuLoop = True
    while (mainMenuLoop):
        print('\tMain Menu:')
        print('1. Check Status of Individual Package')
        print('2. Check Status of All Packages')
        print('3. View Truck Details')
        print('4. Exit the program')
        option = input("Please select an option (1, 2, 3, or 4): ")

        # Check Status of Individual Package
        if option == '1':
            # Loop until user enters valid package ID
            packageLoop = True
            while packageLoop:
                packageID = int(input("Please enter a package ID from 1 to 40: "))
                if 0 < int(packageID) <= 40:
                    # Loop until user enters valid time
                    timeLoop = True
                    while (timeLoop):
                        time = input("Please enter the time to check the status (military time - hh:mm): ")
                        hour = None
                        minute = None
                        # Check for valid time
                        if ':' in time:
                            time_parts = time.split(':')
                            # Check for valid time
                            if time_parts[0].isdigit() and time_parts[1].isdigit():
                                hour = time_parts[0]
                                minute = time_parts[1]
                                # Check for valid time
                                if (0 <= int(hour) <= 24) and (0 <= int(minute) <= 59):
                                    status_time = datetime.time(int(hour), int(minute))

                                    print(f'\nStatus for Package {packageID} as of {status_time}:')
                                    headers = ["ID", "Address", "City", "State", "Zip", "Deadline",
                                               "Weight", "Status", "Notes"]
                                    # Format headers to print out in columns
                                    print(f'\t{headers[0]:<4}{headers[1]:^40}{headers[2]:^20}{headers[3]:^8}{headers[4]:^8}'
                                        f'{headers[5]:^10}{headers[6]:^8}{headers[7]:^38}{headers[8]:^20}')
                                    print('*' * 200)

                                    # Find package in hash table
                                    package = myHash.search(packageID)
                                    # Find address of package based on time entered
                                    address, city, zip_code, state = check_address(packageID, status_time)

                                    # Format package data to print out in columns
                                    print(f'\t{package.package_id[-1][0]:<4}{address:^40}{city:^20}{state:^8}'
                                          f'{zip_code:^8}{package.deadline[-1][0]:^10}{package.weight[-1][0]:^8}'
                                          f'{check_package_status(packageID, status_time):^38}{package.notes[-1][0]:^20}')
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

        # Check Status of All Packages
        elif option == '2':
            # Loop until user enters valid time
            timeLoop = True
            while (timeLoop):
                time = input("Please enter the time to check the status of all packages (military time - hh:mm): ")
                hour = None
                minute = None
                # Check for valid time
                if ':' in time:
                    time_parts = time.split(':')
                    # Check for valid time
                    if time_parts[0].isdigit() and time_parts[1].isdigit():
                        hour = time_parts[0]
                        minute = time_parts[1]
                        # Check for valid time
                        if (0 <= int(hour) <= 24) and (0 <= int(minute) <= 59):
                            status_time = datetime.time(int(hour), int(minute))

                            print(f'\nStatus for All Packages as of {status_time}:')
                            headers = ["ID", "Address", "City", "State", "Zip", "Deadline",
                                       "Weight", "Status", "Notes"]
                            # Format headers to print out in columns
                            print(f'\t{headers[0]:<4}{headers[1]:^40}{headers[2]:^20}{headers[3]:^8}{headers[4]:^8}'
                                  f'{headers[5]:^10}{headers[6]:^8}{headers[7]:^38}{headers[8]:^20}')
                            print('*' * 200)

                            # Find package in the hash table and print out data for each package
                            for packageID in range(packageSize("WGUPS Package File.csv")):
                                package = myHash.search(packageID + 1)
                                address, city, zip_code, state = check_address(packageID + 1, status_time)

                                # Format package data to print out in columns
                                print(f'\t{package.package_id[-1][0]:<4}{address:^40}{city:^20}{state:^8}'
                                      f'{zip_code:^8}{package.deadline[-1][0]:^10}{package.weight[-1][0]:^8}'
                                      f'{check_package_status(packageID + 1, status_time):^38}{package.notes[-1][0]:^20}')

                            timeLoop = False
                            print()
                        else:
                            print("Invalid time\n")
                    else:
                        print("Invalid time\n")
                else:
                    print("Invalid time\n")

        # Print truck details (mileage, start/end time, route)
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

        # Exit program
        elif option == '4':
            mainMenuLoop = False
        else:
            print("Invalid option\n")
