from hashtable import ChainingHashTable
import csv


class Package:
    def __init__(self, ID, destination, city, state, Zip, deadline, mass, notes, status):
        self.ID = ID
        self.destination = destination
        self.city = city
        self.state = state
        self.Zip = Zip
        self.deadline = deadline
        self.mass = mass
        self.notes = notes
        self.status = status
        # Add delivery time

    def __str__(self):
        return "%s, %s, %s, %s, %s, %s, %s, %s, %s" % (self.ID, self.destination, self.city, self.state, self.Zip, self.deadline, self.mass, self.notes, self.status)


def loadPackageData(file):
    with open(file) as packages:
        packageData = csv.reader(packages, delimiter=',')
        next(packageData)
        for package in packageData:
            packageID = int(package[0])
            packageDestination = package[1]
            packageCity = package[2]
            packageState = package[3]
            packageZip = package[4]
            packageDeadline = package[5]
            packageMass = package[6]
            packageNotes = package[7]
            packageStatus = "Loaded"

            p = Package(packageID, packageDestination, packageCity, packageState,
                        packageZip, packageDeadline, packageMass, packageNotes, packageStatus)

            packageHashTable.insert(packageID, p)


# Creating hash table for packages
packageHashTable = ChainingHashTable()
