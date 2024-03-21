# ! Method riding
# * Polymorphism in classes

# class bank:
#     def ratio(self):
#         print("All banks has repo rate")

# class SBI(bank):
#     def ratio(self):
#         print("SBI rate is 9%")

# class IOB(bank):
#     def ratio(self):
#         print("IOB rate is 7.5%")

# i = IOB()
# i.ratio()

# s = SBI()
# s.ratio()

# ? Eg:2
# class USA:
#    def language(self):
#        print("English")

#     def capital(self):
#         print("Washington DC")

# class India(USA):
#     def language(self):
#         print("New delhi")

# I = India()
# I.language()
# I.capital()

# Eg:3
# Polymorphism using objects

# c1, c2 --> c1 = print(c1), print(c2)
# f1, f2


# class c1:
#     def f1(self):
#         print("class 1")

# class c2(c1):
#     def f1(self):
#         super().f1()
#         print("class 2")

# obj1 = c2()
# obj1.f1()

# * Eg:4

# class c1:
#     def f1(self):
#         print("class 1")

# class c2(c1):
#     def f1(self):
#         print("class 2")

# obj1 = c2()
# obj2 = c1()

# def display(a):
#     a.f1()
# display(obj1)
# display(obj2)

#* changing the functionality of builtin functions
# a = 9
# b = 6
# print(a+b)
# print(a.__add__(b)) #? dunder method
# print(a.__sub__(b))
# print(a.__mul__(b))

# class shooping:
#     def __init__(self, l1):
#         self.items = l1

#     def __len__(self):
#         length = len(self.items)
#         return length
# s = shooping([1,2,3,4,5])
# print(len(s))
        
# ! ---> Method overloading
# ! Eg:1
class suming:
    def add(self, a,b):
        print(a+b)

    def add(self, a, b, c):
        print(a+b+c)

s = suming()
# s.add(4, 3) # ! -----> error
s.add(4, 5, 1)
    

    
