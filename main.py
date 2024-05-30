from HashTable import *
from Truck import Truck
from CSV import *
from Graph import *
from NearestNeighbor import nearest_neighbor

def getPackageData(myHash):
    for i in range (packageSize('WGUPS Package File.csv')):
        print(f"{myHash.search(i + 1)}")

def deliver_all_packages(start_vertex, Truck, packageList, start_time, g):
    print(f'Truck {Truck.number} Delivery Route:\n {Truck.route}')
    print(f'Mileage: {Truck.mileage}')
    print(f'Time: {start_time}')
    print(f'Remaining Packages:\n{view_remaining_vertex(start_vertex, Truck.packageList, g)}')
    print()

    while (packageList):
        next_vertex, mileage = find_closest_vertex(start_vertex, packageList, g)
        current_package = find_package_by_vertex(next_vertex, packageList)
        Truck.packageList.remove(current_package)

        Truck.route = Truck.route + ' -> ' + str(next_vertex)
        print(f'Truck {Truck.number} Delivery Route:\n {Truck.route}')

        Truck.mileage += mileage
        print(f'Mileage: {Truck.mileage}')

        # Calculates the minutes to drive to next location based on 18 mph average speed
        Truck.time_value += (mileage * 60) / 18
        time_in_seconds = Truck.time_value * 60
        delta = datetime.timedelta(seconds=time_in_seconds)
        new_time = datetime.datetime.combine(datetime.date.today(), start_time) + delta
        print(f'Time: {new_time.time()}')

        start_vertex = next_vertex

        print(f'Remaining Packages:\n{view_remaining_vertex(start_vertex, Truck.packageList, g)}')
        print()

    Truck.mileage += g.get_distance(start_vertex, 1)
    mileage = g.get_distance(start_vertex, 1)
    print(f'Final Mileage: {Truck.mileage}')
    Truck.time_value += (mileage * 60) / 18
    time_in_seconds = Truck.time_value * 60
    delta = datetime.timedelta(seconds=time_in_seconds)
    new_time = datetime.datetime.combine(datetime.date.today(), start_time) + delta
    print(f'Final Time: {new_time.time()}')
    Truck.route = Truck.route + ' -> ' + str(1)
    print(f'Route: {Truck.route}')
    print()

# getPackageData(myHash)
# print()

truck1 = Truck(1)
truck1.packageList.extend([1,7,8,13,14,15,16,19,20,29,30,34,37,39,40])
truck2 = Truck(2)
truck2.packageList.extend([2,3,4,5,10,11,12,17,18,21,22,24,36,38])
truck3 = Truck(3)
truck3.packageList.extend([6,9,23,25,26,27,28,31,32,33,35])

# start_vertex = 1
# print(view_remaining_vertex(start_vertex, truck1.packageList, my_graph))
# print()

# current_package = find_package_by_vertex(10, truck1.packageList)
# print(current_package)
#
# print(truck1.packageList)
# truck1.packageList.remove(current_package)
# print(truck1.packageList)
#
# next_vertex, mileage = find_closest_vertex(start_vertex, truck1.packageList, my_graph)
# print(f'Next Vertex: {next_vertex}, Mileage: {mileage}')

# package = myHash.search(truck1.packageList[0])
# print(package.address)
# print()
#
# print(find_dropoff_vertex(truck1.packageList[0]))
# print()
#
# start_vertex = 1
# print(find_closest_vertex(start_vertex, truck1.packageList, my_graph))
# print()
#
# print(f'Remaining Packages:\n{view_remaining_vertex(start_vertex, truck1.packageList, my_graph)}')
# print()

start_vertex = 1
start_time = datetime.time(8, 00)
deliver_all_packages(start_vertex, truck1, truck1.packageList, start_time, my_graph)

# start_vertex = 1
# start_time = datetime.time(10, 00)
# deliver_all_packages(start_vertex, truck2, truck2.packageList, start_time, my_graph)
#
# start_vertex = 1
# start_time = datetime.time(9, 15)
# deliver_all_packages(start_vertex, truck3, truck3.packageList, start_time, my_graph)

if __name__ == '__main__':
    print('Welcome to the WGU Postal Service Status Application!')

    isExit = True
    while (isExit):
        option = input("Choose an option (1, 2, 3, or 4): ")
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
