import csv
import enum
from truck import Truck

addresses = list(csv.reader(open('./csv/addresses.csv')))
distances = list(csv.reader(open('./csv/distances.csv')))





# def compareAddresses():
#     addresses = list(csv.reader(open('./csv/addresses.csv')))
#     for addressAndID in addresses:
#         ID = addressAndID[0]
#         address = addressAndID[1]

#         print(ID)
#         print(address)

# def getNearestNeighbor(currentAddress):
#     addresses = list(csv.reader(open('./csv/addresses.csv')))
#     distances = list(csv.reader(open('./csv/distances.csv')))

#     for addressAndID in addresses:
#         ID = addressAndID[0]
#         if int(ID) == currentAddress:
#             # Want to return the corresponding col in distances.csv
#             distanceList = distances[currentAddress]
#             print(distanceList)
#             return distanceList
#         # else:
#             # print('Nah :' + ID)
#         address = addressAndID[1]

#         # print(ID)
#         # print(address)


# getNearestNeighbor(7)


# IDs = addresses[col][0]
# addressList = addresses[int(col)][1]
# IDs = addresses[1][1]
# print(IDs)

# print(len(addresses))

# print(addresses[1][1])
