'''
Lesson: Booleans
Author: Jordynne Jade
Date Created: Sept 25, 2024
Date Last Modified: Sept 25, 2024
'''
q1():
  bool1=5<10
  print(bool1)


q2():
  integer = input("Input an integer: ")
  integer = int(integer)
  bool1  = integer > 5
  print(bool1)

q3():
  word = input("Input the letter a: ")
  bool1 = word == "a"
  print(bool1)

q4():
  word = input("Input a word earlier in the dictionary than google: ")
  bool1 = word < "google"
  print(bool1)

q5():
  integer = input("Input an integer: ")
  integer2 = input("Input another integer: ")
  integer = int(integer)
  integer2 = int(integer2)
  num = integer * integer2
  bool1 = num > 40
  print(f"Your numbers multiplied together are greater than 40: {bool1}")

#Do edit the code below
#Comment the lines below when running your tests

#q1()
#q2()
#q3()
#q4()
q5()
