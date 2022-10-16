from hashtable import ChainingHashTable
from package import loadPackageData
from package import packageHashTable


loadPackageData('./csv/packages.csv')

print("Packages from package hash table:")
for i in range(len(packageHashTable.table)):
    print("Package ID: {}".format(packageHashTable.search(i+1)))
