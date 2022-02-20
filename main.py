           #Statement
           #if / else
#Syntex:-
#if condition:
#do this
#else:
#do this

#Example

#print("Welcome to the RollerCoaster!\n")
#height = int(input("what is your height?(in Cms)\n"))


#if height < 120:
#   print("You can't enter!!!")
#else:
#   print("here is your ticket ^^")


#one (=)sign means we are assigning a value to something. and if there are (==)signs then it means we are equating a particular value to something.
#== equal to
#!= not equal to

          #EVEN or ODD:-
#To check whether the number is odd or even we can write a code like this:-

#number = int(input("Which number do you want to check? "))

#if number % 2 == 0:
#     print("This is an even number.")
#else:
#     print("This is an odd number")    

#to check where a number will give a reminder or not after division we can use Modulo(%) sign, Example:-
#10 % 2 = 0 as it will divide completly.
#whether,
#5 % 2 = 1 as it will not divide completly.

      #Nested if/ else statement:-
#Syntax:-
#if conditon:
#  if another conditon:
#   do this
#  else:
#   do this 
#    .
#    .
#    .
#    .
#else:
#   do this 

              #elif:-
#Syntax
#if condition:
#  do this 
# elif condition:
#   do This
# elif condition:
#   do This
#.
#.
#.
#.
#.
#else:
#  do this     
#better use this instead of nested if/else for easy code. 

          #if/ else/ elif
#Syntax:-
#if condition:
#  do this
#elif condition:
#  do this
#else:
#  do this    

            #Multiple if
#if condition1:
#  do this
#if conditon2:
#  do this
#if condititon3:
#  do this
#.
#.
#.
#.                  
            #example:-

# print("Welcome to the RollerCoaster!\n")
# height = int(input("what is your height?(in Cms)\n"))
# bill = 0

# if height >= 120:
#   print("You can enter in the RollerCoaster :)")
#   age = int(input("what is your age?\n"))
#   if age < 12:
#    bill = 5
#    print("children tickets are $5")
#   elif age <= 18:
#    bill = 7 
#    print("Youth tickets are $7")
#   else:
#    bill = 12 
#    print("Adult tickets are $12")
#   Photo= input("Do you also wanna take photos?\nY or N\n")
#   if Photo == "Y":
#     print("Pay Extra $3")
#     bill = bill + 3
#     print(f"So in total pay ${bill}, And ENJOY ^^")
#   else:
#     print("Enjoy the ride. ^^")  
# else:
#   print("You can't enter!!!")    

          #Logical Operators
#and, or, not.  
#use "and" when A and B both conditon is true for entire line of code.

# FOR "and"
# A and B 
# T     T = T
# T     F = F
# F     T = F
# F     F = F 

# FOR "or"
# A or B
# T    T = T
# T    F = T
# F    T = T
# F    F = F

# FOR "not", it basically converts 
# T = F
# and F = T

# To combine two digits together we can use this code:-
#input 
# K = 45
# P = 56
# score = int(str(K) + str(P))
# print(score)
#output
#4556