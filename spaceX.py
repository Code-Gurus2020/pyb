#!/usr/bin/python3
''' Use PaceX data to make presentable data '''

import urlib.request

SURI = "https://api.spacexdata.com/v3/cores"

def main():
   coreData = urllib.request.urlopen(SURI)

   xString = coreData.read().decode()

   print(type(xString))

   # convert STRING data into Python Lists and Dictionaries
    listOfCores = json.loads(xString)
    print(type(listOfCores))

    for core in listOfCores:
        print(core, end="\n\n")

if __name__ == "__main__":
    main()

