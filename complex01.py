#!/usr/bin/env python3

# create a list called list1
list1 = ["cisco_nxos", "arista_eos", "cisco_ios"]
# display list1
print(list1)

print (list1[1])

list2 = ["This is fun"]

list1.extend(list2)

print (list1)

list3 = ["10.0.0", "2020"]

list1.extend(list3)

print (list1)

print (list1[4])

print (list1[4][0])

