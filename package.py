from hashtable import ChainingHashTable
import csv


class Package:
    def __init__(self, ID, address, city, state, Zip, deadline, mass, notes, status):
        self.ID = ID
        self.address = address
        self.city = city
        self.state = state
        self.Zip = Zip
        self.deadline = deadline
        self.mass = mass
        self.notes = notes
        self.status = status

    def __str__(self):
        return "%s, %s, %s, %s, %s, %s, %s, %s, %s" % (self.ID, self.address, self.city, self.state, self.Zip, self.deadline, self.mass, self.notes, self.status)


def loadPackageData(file):
    with open(file) as packages:
        packageData = csv.reader(packages, delimiter=',')
        next(packageData)
        for package in packageData:
            packageID = int(package[0])
            packageAddress = package[1]
            packageCity = package[2]
            packageState = package[3]
            packageZip = package[4]
            packageDeadline = package[5]
            packageMass = package[6]
            packageNotes = package[7]
            packageStatus = "Loaded"

            p = Package(packageID, packageAddress, packageCity, packageState,
                        packageZip, packageDeadline, packageMass, packageNotes, packageStatus)

            packageHashTable.insert(packageID, p)


# Creating hash table for packages
packageHashTable = ChainingHashTable()
