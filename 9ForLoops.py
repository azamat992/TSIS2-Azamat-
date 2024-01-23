#Exercise 1 Azamat
#Loop through the items in the fruits list. Azamat
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)

#Exercise 2 Azamat
#In the loop, when the item value is "banana", jump directly to the next item. Azamat
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    continue
  print(x)

#Exercise 3 Azamat
#Use the range function to loop through a code set 6 times. Azamat
for x in range(6):
  print(x)

#Exercise 4 Azamat
#Exit the loop when x is "banana". Azamat
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    break
  print(x)
