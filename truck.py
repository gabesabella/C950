from package import packageHashTable
from package import loadPackageData

loadPackageData('./csv/packages.csv')

# If row is > col, swap


class Truck:
    def __init__(self):
        # self.departure = departure
        # self.time = date time object
        self.miles = 0
        self.currentLocation = '4001 South 700 East'
        self.previousLocation = ''
        self.newPackageList = [[]]

    # setter method

    def loadPackages(self, packageList):
        newPackageList = [[]]
        for i in range(len(packageList)):
            newPackageList.insert(
                packageList[i], packageHashTable.search(packageList[i]))
        self.newPackageList = newPackageList

    def getPackage(self, packageID):
        newPackageList = self.newPackageList
        for i in self.newPackageList:
            if packageID == newPackageList[0]:
                print("hmm maybe")
            else:
                print("Nope")

            # Truck 1 --> Departs at 8:00
truckOnePackages = [1, 13, 14, 15, 16, 20, 29, 30, 31, 34, 37, 40]
# Package 15 due by 9:00, all others due by 10:30

# Truck 2 --> Departs at 9:05
# Packages 6 and 25 have 10:30 deadline
truckTwoPackages = [3, 6, 18, 25, 27, 28, 32, 33, 35,  36, 38, 39]

# Truck 3 --> All EOD packages
truckThreePackages = [2, 4, 5, 7, 8, 9, 10, 11, 12, 17, 19, 21, 22, 23, 24, 26]

truck1 = Truck()
truck1.loadPackages(truckOnePackages)

truck2 = Truck()
truck2.loadPackages(truckTwoPackages)

truck3 = Truck()
truck3.loadPackages(truckThreePackages)

print(truck3.newPackageList[1])
rows, cols = (5, 5)
arr = [[0]*cols]*rows
print(arr)

# print(truck3.getPackage(4))

# Load in distances and addresses as arrays
# distanceData = [] --> 2d
# addressData = [] --> 1d
# for i in range(len(truckOnePackages)):
#     truck1.insert(truckOnePackages[i],
#                   packageHashTable.search(truckOnePackages[i]))

# From call
# for i in range len(truck1.packageList):
#     print(truck1.packageList[i])

# print("Packages from package hash table:")
# for i in range(len(truck1)+1):
#     # if truck1.search(i) == None:
#     #     continue
#     print(truck1[i])
