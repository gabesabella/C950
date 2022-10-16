from hashtable import ChainingHashTable
from package import packageHashTable

from hashtable import ChainingHashTable
from package import loadPackageData
from package import packageHashTable


loadPackageData('./csv/packages.csv')


class Truck:
    def __init__(self, packages, departure, miles):
        self.packageList = packages
        self.departure = departure
        self.miles = miles


truck1 = ChainingHashTable()


# Truck 1 --> Departs at 8:00
truckOnePackages = [1, 13, 14, 15, 16, 20, 29, 30, 31, 34, 40]
# Package 15 due by 9:00, all others due by 10:30

# Truck 2 --> Departs at 9:05
# Packages 6 and 25 have 10:30 deadline
truckTwoPackages = [3, 6, 18, 25, 27, 28, 32, 33, 35,  36, 38, 39]

# Truck 3 --> All EOD packages
truckThreePackages = [2, 4, 5, 7, 8, 9, 10, 11, 12, 17, 19, 21, 22, 23, 24, 26]

for i in range(len(truckOnePackages)):
    truck1.insert(truckOnePackages[i],
                  packageHashTable.search(truckOnePackages[i]))


print("Packages from package hash table:")
for i in range(len(truck1.table)+1):
    if truck1.search(i) == None:
        continue
    print("Package ID: {}".format(truck1.search(i)))
