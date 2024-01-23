#Exercise 1 Azamat
#Print i as long as i is less than 6. Azamat
i = 1
while i < 6:
  print(i)
  i += 1

#Exercise 2 Azamat
#Stop the loop if i is 3. Azamat
i = 1
while i < 6:
  if i == 3:
    break
  i += 1

#Exercise 3 Azamat
#In the loop, when i is 3, jump directly to the next iteration. Azamat
i = 0
while i < 6:
  i += 1
  if i == 3:
    continue
  print(i)

#Exercise 4 Azamat
#Print a message once the condition is false. Azamat
i = 1
while i < 6:
  print(i)
  i += 1
else:
  print("i is no longer less than 6")
