from HashTable import *
from Truck import Truck
from CSV import *
from Graph import *
from NearestNeighbor import nearest_neighbor

def getPackageData(myHash):
    for i in range (packageSize('WGUPS Package File.csv')):
        print(f"{myHash.search(i + 1)}")


getPackageData(myHash)
print()

truck1 = Truck(1)
truck1.packageList.extend([1,2,3,4,5])
truck2 = Truck(2)

package = myHash.search(truck1.packageList[0])
print(package.address)



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
