import csv
import datetime


# Creates a package class to capture all package data from 'WGUPS Package File.csv'file
class Package:
    # Constructor creates a tuple for each variable to allow access to previous package information
    # based on the time it was updated.
    def __init__(self, time, package_id, address, city, state, zip_code, deadline, weight, notes):
        self.time = time
        self.package_id = package_id
        self.address = [[address, self.time]]
        self.city = [[city, self.time]]
        self.state = [[state, self.time]]
        self.zip_code = [[zip_code, self.time]]
        self.deadline = [[deadline, self.time]]
        self.weight = [[weight, self.time]]
        self.notes = [[notes, self.time]]
        self.status = [['Heading to Depot', self.time]]

    # Overwrite print(Package) to print strings instead of object references
    def __str__(self):
        return "%s, %s, %s, %s, %s, %s, %s, %s, %s" % (self.package_id, self.address, self.city, self.state,
                                                            self.zip_code, self.deadline, self.weight,
                                                            self.notes, self.status)


# Read contents of the csv file and load it into the hash table
def loadPackageData(fileName, myHash):
    with open(fileName, 'r') as packageLocations:
        packageData = csv.reader(packageLocations, delimiter=',')
        next(packageData)  # Skip header
        for package in packageData:
            package_time = datetime.time(7, 0)
            package_id = int(package[0])
            package_address = package[1]
            package_city = package[2]
            package_state = package[3]
            package_zip = package[4]
            package_deadline = package[5]
            package_weight = package[6]
            package_notes = package[7]

            # Create package object
            package = Package(package_time, package_id, package_address, package_city, package_state,
                              package_zip, package_deadline, package_weight, package_notes)
            # Insert package into hash table
            myHash.insert(package_id, package)


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