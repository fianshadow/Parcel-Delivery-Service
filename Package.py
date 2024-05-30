# Importing the Package CSV data
import csv
import datetime


class Package:
    # Constructor
    def __init__(self, ID, address, city, state, zip, deadline, weight, notes):
        self.ID = ID
        self.address = address
        self.city = city
        self.state = state
        self.zip = zip
        self.deadline = deadline
        self.weight = weight
        self.notes = notes
        self.status = [['Loaded', datetime.time(7, 00)]]

    # Overwrite print(Package) to print strings instead of object references
    def __str__(self):
        return "%s, %s, %s, %s, %s, %s, %s, %s, %s" % (self.ID, self.address, self.city, self.state,
                                                       self.zip, self.deadline, self.weight,
                                                       self.notes, self.status)


# Read contents of the csv file and load it into the hash table
def loadPackageData(fileName, myHash):
    with open(fileName, 'r') as packageLocations:
        packageData = csv.reader(packageLocations, delimiter=',')
        next(packageData)  # Skip header
        for package in packageData:
            packageID = int(package[0])
            packageAddress = package[1]
            packageCity = package[2]
            packageState = package[3]
            packageZip = package[4]
            packageDeadline = package[5]
            packageWeight = package[6]
            packageNotes = package[7]

            # Create package object
            package = Package(packageID, packageAddress, packageCity, packageState,
                              packageZip, packageDeadline, packageWeight, packageNotes)
            #Insert package into hash table
            myHash.insert(packageID, package)


# Get size of package file
def packageSize(fileName):
    with open(fileName, 'r') as packageLocations:
        packageData = csv.reader(packageLocations, delimiter=',')
        next(packageData)
        packageSize = 0
        # For each row in file, increment package size
        for row in packageData:
            packageSize += 1
        return packageSize
