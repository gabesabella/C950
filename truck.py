import csv
from package import packageHashTable
from package import loadPackageData

# Package data
loadPackageData('./csv/packages.csv')
# Distance data in matrix
distances = list(csv.reader(open('./csv/distances.csv')))
addresses = list(csv.reader(open('./csv/addresses.csv')))

# If row is > col, swap


class Truck:
    def __init__(self):
        # self.departure = departure
        # self.time = date time object
        self.miles = 0
        self.currentLocation = '4001 South 700 East'
        self.previousLocation = ''
        self.packages = []

    def loadPackages(self, packageList):
        packages = []
        for i in range(len(packageList)):
            packages.insert(
                packageList[i], packageHashTable.search(packageList[i]))
        self.packages = packages

    def getAddressID(packages):
        packageID = packages.packages.destination

    def findClosestNeighbor(packages):
        packages = packages.packages
        destinations = []
        addresses = list(csv.reader(open('./csv/addresses.csv')))

        # Get ID and address columns from addresses.csv
        for col in addresses:
            ID = col[0]
            address = col[1]

        for col in distances:
            ID = col[0]
            destinations.append(col[0])
            # print(destinations)
            # print(ID)

    # def getNearestNeighbor(currentAddress):
    #     addresses = list(csv.reader(open('./csv/addresses.csv')))
    #     distances = list(csv.reader(open('./csv/distances.csv')))

    #     for col in addresses:
    #         # ID column from addresses.csv
    #         ID = col[0]

    #         # Address Column from addresses.csv
    #         address = col[1]
    #         # print(ID)
    #         if int(ID) == currentAddress:
    #             # Want to return the corresponding col in distances.csv
    #             distanceList = distances[currentAddress]
    #             # print(distanceList)
    #             for distance in len(distanceList):
    #                 if (distanceList[distance] == ''):
    #                     print('Is it an empty string or comma?')
    #                 else:
    #                     print("Try something else")
    #             return distanceList

    #     print(ID)
    #     print(address)

        # for i in range(len(packages)):
        # print(packages[i].destination)
        # print(destinations[i])
        # if destinations[i] == packages[i].destination:
        #     print('HMMM')
        # else:
        #     print('HMMMMMMMMMMMM!!!!')
        # for i in range(len(destinations)):
        #     print(packages[i].destination)
        #     print(destinations[i])

        # print(destinations)


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

# truck3.findClosestNeighbor()

# truck1.findClosestNeighbor()

# print('Packages in Truck #1')
# for i, sublist in enumerate(truck1.packages):
#     print(truck1.packages[i])

# print('Packages in Truck #2')
# for i, sublist in enumerate(truck2.packages):
#     print(truck2.packages[i])

# print('Destinations of packages on Truck #3')
# for destinations, sublist in enumerate(truck3.packages):
# print(truck3.packages[destinations].destination)
# truck1.findClosestNeighbor()

# for package in range(len(truck3.packages)):
#     getNearestNeighbor(truck3.packages[package].ID)

# Expanded Version


def getDistances(truckPackageIDs, truckDestinations):

    packageDistances = []
    truckPackageDistanceList = []
    allPackageIDs = [[]]

    for col in addresses:
        ID = col[0]
        allPackageIDs.append(ID)

    # print(allPackageIDs)
    # print(len(distances))
    # for allID in range(len(allPackageIDs)):
    #     if allID = truckPackageID[]
    #     for ID in truckPackageIDs:
    #         if ID == truckPackageIDs:
    #             print('this might just work')
    # print(packageDistances)

    print('Row from address data:')
    print(addresses[0])
    print('Row from distance data:')
    print(distances[0])
    for address in range(len(addresses)):
        # print(truckDestination)
        # print(addresses[0][1])
        # print(address)
        print(addresses[address][1])
        # if i == addresses[0][i]:
        #     print("YEEHAH")
        # else:
        #     print('address :' + addresses[0]
        #           [i])
    # print('truck destinations: ' + i)
    # print(allPackageID)
    # for truckPackageID in truckPackageIDs:
    #     if int(allPackageID) == int(truckPackageID):
    #         print('yeeha')
    # for i in range(25):
    #     truckPackageDistanceList.append(distances[truckPackageID])
    # # truckPackageDistanceList.append(
    # # distances[int(truckPackageIDs[truckPackageID])])
    # print('yee')
    print(truckPackageDistanceList)

    # print(distances[26])
    # for truckPackageID in truckPackageIDs:
    #     if allPackageIDs[int(allPackageID)] == truckPackageID:
    #         # print(truckPackageID)
    #         packageDistances.append(distances[truckPackageID])

    # print(packageDistances)

    # for allID in allPackageIDs:
    #     print("Yeeha")

    #     # print(ID)
    #     if int(ID) == currentAddress:
    #         # Want to return the corresponding col in distances.csv
    #         distanceList = distances[currentAddress]
    #         truckPackageDistanceList.append(distanceList)
    # return distanceList
    # else:
    # print('Nah :' + ID)
    # print(ID)
    # print(address)

    # for addyID in range(currentAddress):
    #     for addressAndID in addresses:
    #         ID = addressAndID[0]
    #         if int(ID) == currentAddress:
    #             # Want to return the corresponding col in distances.csv
    #             distanceList = distances[currentAddress]
    #             # print(distanceList)

    # def closestNextDeliver(distanceList):
    #     for distance in range(distanceList)):
    #         distance=distanceList(distance)
    #         print(distance)
    #     # print(row)

    # distances = truck1.packages[0].ID
    # getDistances(distances)

    # closestNextDeliver(distances)

    # print(len(truck1.packages))


# anotherDistanceList = []
# truckPackageDestinations = []
# for package in range(len(truck1.packages)):
#     anotherDistanceList.append(truck1.packages[package].ID)
#     truckPackageDestinations.append(truck1.packages[package].destination)
# print(anotherDistanceList)
# print(truckPackageDestinations)
# getDistances(anotherDistanceList, truckPackageDestinations)

# print(len(addresses))
# for i in range(len(addresses)):
# print(truckDestination)
# print(addresses[0][1])
# print(addresses[0][i])
# print(distances)
# print(distances)
# distanceList = getDistances(distances)
# print(anotherDistanceList)
# getDistances(anotherDistanceList)

# print(distances[26])
# print(anotherDistanceList)
