#Print the second item of the list:
thislist1 = ["apple", "banana", "cherry"]
print(thislist1[1])

#Print the last item of the list:
thislist2 = ["apple", "banana", "cherry"]
print(thislist2[-1])

#Return the third, fourth, and fifth item:
thislist3 = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist3[2:5])

#This example returns the items from the beginning to, but NOT including, "kiwi":
thislist4 = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist4[:4])

#This example returns the items from "cherry" to the end:
thislist5 = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist5[2:])

#This example returns the items from "orange" (-4) to, but NOT including "mango" (-1):
thislist6 = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist6[-4:-1])

#Check if "apple" is present in the list:
thislist7 = ["apple", "banana", "cherry"]
if "apple" in thislist7:
  print("Yes, 'apple' is in the fruits list")
  