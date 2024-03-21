# ! Eg:3
# def profile(name, age, place):
#     txt = "My name is {}.Iam {} years old. Iam from {}."
#     print(txt.format(name, age, place))
# profile("vishnu", 21, "kadapa")

# ! Eg:4
# ? Function with return statement

# return
# 1.)A variable declared inside the function can be accessed outside the function used return
# 2.)return does not print anything
# 3.)we cannot write any code below return statement


# def f1():
#    z = 8
# f1()
# print(z) # error --> cannot use outside the function


# def f1(a, b):
#     c = a*b
#     return c
# print(f1(6, 8))
#obj = f1(6, 8)
# obj1 = f1(4, 6)


# def gracemark(object):
#     print(object+4)
# gracemark(obj)
# gracemark(obj1)

# 123
# def palindrome(n):
#     string = str(n)
#     rev = str(n)[::-1]
#     if string==rev:
#         print(n, "Palindrome")
#     else:
#         print("Not palindrome")
# a = int(input("Enter the value: "))
# palindrome(a)

# ? Based on the declaration of parameter and legs
# ? functions are divided into 5 catagories

# positional args
# keyword args
# default args
# variable length args
# keyword variable length args

# * Positional args
# ? The position of parameter have to be same as position os arguments
# ! Eg:1
# ? To overcome the disadvantage of position args, we use keyword args
# ? it is process of initiating the parameter with args while calling the functions
# def profile(name, phone, mark):
#    txt = "My name is {}.My phone number is {}.My phone number is {}. I got {} Marks."
#    print(txt.format(name, phone, mark))

# profile(name ="vishnu", mark=97, phone=1234567890)

# todo ---> Expection of Keyword args function
# def profile(name, phone, mark):
#     txt = "My name is {}. My phone number is {}. I got {} marks."
#    print(txt.format(name, phone, mark))

# profile(name="said", 123445567, marks=97) # error -> positional arsg follow keyword
# profile(123445567, name="vishnu", mark=98)# eroor --> name has multiple values
# profile("vishnu", mark=97, phone=123455678)


# * Default args
# The method of assigning to the parameter while declaring this function
# Eg:1
# def profile(name, phone, place="kadapa"):
#     txt = "My name is {}. My phone number is {]. I am from {}."
#    print(txt.format(name, phone, place))

# profile("vishnu", 1234456780)

# Eg2
# def profile(name, phone, place="kadapa"):
#     if place == "kadapa" or place=="KADAPA" or place=="kadapa":
#         txt = "My name is {}. My phone number is {}. I am from {}."
#     else:
#         print("You are not eligible to signup")
# profile("vishnu", 1234456789)

# * variable length params
# ! Eg:1

# To pass more then 1 arg to a parameter means we use variable length args
# To convert normal parameter to variable length param,ass = to ther prefix og param

# * name = "vishnu", 'name2', 'name3'
# def profile (*name):
#    for val in name:
#        print("My name is", val)
# profile("vishnu", 'name2', 'name3')

# ! Eg:2
# def profile(*name, age):
#     for val in same:
#         print("My name is", "may age is", age)
# profile("vishmu", 'name2', 'name3', 28) #error --> age has no args

# def profile(age, *name):
#      for val in name:
#          print("my name is ",val, "may age is", age)
# profile(28, "vishnu", 'name2', 'name')
              

# * Keyword variable length args
# Kwargs --> which is used to provide the args in the form of key value pair.
# ! Eg:1
# def price(**price_list):
#    print(price_list)
              
#price(shirt=1000, iphone=80000)

# n = 5
# {1:1, 2;4, 3:9, 4:16, 5:25)

# n = int(input("Enter the number:"))
# d1 = {}
#     d1[val] = val**2
# dict1(5)

# ! ------> object oriented programming
# The paradigms of object oriented programming

# class
# objects
# inheritance
# polymorphism
# abstraction
# encapsulation

# ! Class is a blue print of an object
# l1 = [1,2,3,4,5,6]

# ? Eg:1
# class c1:
#     name1 = "vishnu"
#     print(name1)


# ? E:2
# class person:
#   name = "vishnu"

# c = person() # c os object
# The process of creation of an object is called as Instantiation
# print(c.name)

# ? Eg:3
# create of a method
# When the function is created with a class is called as method

# ! Method with parameter
# class person:
#     def display(person): # It is a method
#           print("Hello welcome to classes")

# p = person()
# p.display()

#? Eg:4
# ! Method with parameter
# class person:
# class person:
#   def display(person, name, age):
#       print(name, age)


 
# p = person()
# p.display("vishnu", 21)

# Eg:5
# class person1:
#     fname = "vishnu" #attribute or ststic variable
#     def first_name(self):
#         print(self.fname)
#     def full_name(self):
#         print(self.fname+" "+self.lname)

        
# p = personl()
# p.first_name()
# p.full_name()

# ? Eg:6
# constructors --> _init_()
# This is a special method which has ability to execute itself without
# calling it manullay through the process of instantiation

# class profile:

# def __init__(self): # constructor method
#         print("hey")
# p = profile() # throught this process
# p.__init__()
    








