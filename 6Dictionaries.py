#Exercise 1 Azamat
#Use the get method to print the value of the "model" key of the car dictionary. Azamat
car =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(car.get("model"))

#Exercise 2 Azamat
#Change the "year" value from 1964 to 2020. Azamat
car =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
car["year"] = 2020

#Exercise 3 Azamat
#Add the key/value pair "color" : "red" to the car dictionary. Azamat
car =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
car["color"] = "red"

#Exercise 4 Azamat
#Use the pop method to remove "model" from the car dictionary. Azamat
car =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
car.pop("model")

#Exercise 5 Azamat
#Use the clear method to empty the car dictionary. Azamat
car =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
car.clear()
