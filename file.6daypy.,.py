# s1 = input("enter string:")

# fst = s1[0].upper()
# lst = s1[-1].upper()

# print(fst+s1[1:len(s1)-1]+1st)

n = 128
temp = n
f1 = 0
while n!=0:
     rem = n%10
     check = temp % rem
     if check!= 0:
         f1 = 1
     n = n/10


#if f1 ==0:
#    print("yes")
# else:
#     print("no")


# n = 128
# for i in str(n):
#      print(i)

#11 = [8, 9, 0, 7]
#12 = [7, 6, 5, 4]
#13 = []
#for val in range(len(11)):
#    ans = 11[val]+12[val]
#    13.append(ans)
print(13)    
    


# ! -----> set

# ? charactristics of set
# 1.) set can be created using {}
# 2.) the elements inside set are not indexed
# 3.) does not allow duplicate values
# 4.) it unordered
# 5.) heterogenous
# 6.) mutable or changable

# * Eg:1
# s1 = {9, 9, 89, 7.76, 8+7j, (8, 7, 5), "truck", 'e'}
# print(s1)

# * Eg:2
# s2 = {5, 8, 98, [9, 0]}
#  print(s2) --> error

# * Eg:3
#
# min(), max(), len()

# * Eg:4
# ? to add element inside set

s1 = {8, 78, 67, 'u'}
#add
#s1.add(43)
print(s1)

# ? to delete element inside set
s1 = {8, 78, 67, 'u'}

# pop() # TO delete one element randonly
# s1.pop(0
# print(s1)

# remove()
# s1.remove(978)
# print(s1)

# discard()
# s1.discard(8967)
# print(s1)

# clear()
# 11 = {}
# print(type(11)) --> datatype is dict

# s1 = set() # to create empty set
# print(type(s1))

# s1 = {8, 9, 0}
# s1.clear()
# print(s1)

# * join the sets
s1 = {9, 0, 8}
s2 = {9.90, "card", 't', 56}
# union() --> to combine 2 sets
# s3 = s1.union(s2)
# print(s3)

# * intersection() --> to get common elements inside set
# s1 = {4, 5, 6}
# s2 = {5, 6, 7, 8}
# print(s1.intersection(s2))

# * different()
# s1 = {4, 5, 6}
# s2 = {5, 6, 7,  8}
# print()s1.difference(s2))
# print(s2.difference(s1))
# print(s1.symmetric_difference(s2))


# isdisjoit(), issubset(), issuperset()
# s1 = {8, 9, 0)
# s2 = {6, 7, 5, 8, 9, 0}

# print(s1.issubset(s2))
# print{s2.issuperset(s1))

s1 = {1, 2, 3, 4, 5}
s2 = {3, 2, 7, 8, 9}

# ! ---> problem 1:

# for val in s1:
#     if val in s2:
#          str1 = "Its joint set"
# print(str1)


# ! -----> dictionatry

Eg:1
# d1 = {1:100, 'a':200, 4.5:"hello"}
# print(d1)
# print(len(d1))

# ? char of dictionary
# 1.) have to be surrounded by {}
# 2.) it have to be in the form of key, value pair
# 3.) it is mutable
# 4.) duplicate keys are not allowed, duplicates values are allowed
# 5.) it is unindexed
# 6.) it is ordered
# 7.) key does not allow mutable datatypes, values allow mutable datatype

# d1 = {1:100, 2:200, 3:300, 4:400}
# * to access elements in dictionary
# print(d1)
# or
# to access the values, have to use key
# print(d1[1])# o/p --> 100

# ? some common functions
# len(), min, max()
# print(min(d1))
# print(max(d1))

# ? to find min, max based on values
# print(min(d1.values()))
# print(max(d1.values()))

# ? dictionary based functions
# to add element(key and value pair) in dict
# d1 = {1:100, 2:200, 3:300, 4:400}
# d1[5] = 500
# print(d1)

# ? to replace avalue in dictionary
# d1 = {1:100, 2:200, 3:300, 4:400}
# d1[2]="mango"
# print(d1)

# ? delete element from dictionary
# d1 = {1:100, 2:200, 3:300, 4:400}
# popitem() # --> to delete last key value pair in dict
# d1.popitem()
# print(d1)

# pop()
# d1.pop(2) # 2 is the key in dictionary
# print(d1)

# clear(), del

# join 2 dictionaries
# d1 = {1:100, 2:200, 3:300, 4:400}
# d2 = {"a":"apple", "b":"boy", "g":"game"}
# d1.update(d2)
# print(d1)

# get()
# d1 = {1:100, 2:200, 3:300, 4:400}
# print(d1[3])
# print(d1.get(3))

# to print all the keys()
# print(d1.keys())
# print(type(d1.keys()))

# to print all the values
# print(d1.values())

# * iterating dictionary
# for val in d1: # to iterate keys alone
#     print(val)

# for val in d1.values(): # to iterate values alone
#     print(val)

# to get both key and values
# for key, val in d1.items():
#     print(key, val)

# ! problem:1

n = int(input("enter the value: "))
integer=[]
FLOAT_VALUE=[]
String=[]

for val in range(n):
    value = eval(input("Enter num of times : "))
    if type(value)==int:
        integer.append(value)
    elif type(value)==float:
         float_value.append(value)
    elif type(value) ==str:
         string.append(value)
    else:
       print("Pls provide data in int, float, string")
print(integer)
print(float_value)
print(string)   

# ! -------> problem 3
11 = [1, 2, 3, 4] # key
12 = ["a", "b", "c", "d"] # value
# o/p ---> [1:"a", 2:"b",3:"c", 4:"d"]
# 13 = {}
# print{11[0]}

d1 = {}
d2 = [11[0]] = 12[0]
d1 = [11[1]] = 12[1]
print d1









# mech_name =["name1", "name2", "name3"]
# mech_age  = [23, 22, 24]
# mech_mark = [89, 78, 60]
# mech_email = ["name2@gmail.com", "name3gmail.com]



  
