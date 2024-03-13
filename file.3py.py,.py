# ! Eg:3
# ? Take values of length and breadth of a
# ? from user and check if it is square or not.

#length = int(Input())
#breadth = int(inout())
# if length == breadth:
#    print("its a square")
#else:
#    print("its not square")

# ! Eg:4
# python program to check wheter the
# given integer is a multiple of both 5 and 7

n = int(input("enter the number:"))
if n%5==0 and n%7==0:
     print("yes")
#else:
     print("no")

# ! Eg:5
# Write  a program to accept the cost price  of a bike and display the
# road tax to be paid
# according to the following criteria:

#      Cost price (in Rs)
#      > 100000
#      < 100000

price = int(int("Enter the price:"))
amount = 0
if price>=100000:
    discount = price*(6/100)
    value = price-discount
    tax=value*(15/100)
    total=value+tax
else:
    tax = price*(5/100)
    total = price+tax
#print("The onroad cost of bike is: ",total)


# !-----> if elif
# Eg:1
a = 7
b = 9
c = 30

# if a>b and a>c
# print("A is greater")
# elif b>a and b>c:
#      print("B is greater")
# elif c>a and c>b:
#   print("C is greater")

# A school has following rules for grading system:
# a. Below 25 - F
# b. 25 to 45 - E
# c. 45 to 50 - D
# d. 50 t0 60 - C
# f. above 80 - A
# ask user to enter marks and print the coressponding grades
# mark = int(intput ("enter mark: "))
# if mark>=80 and mark<80:
#       print("A")
# elif mark>=60 and mark<60:
#       print("B")
# elif mark>50 and mark<50:
#       print("C")
#elif mark>40 and mark<50:
#       print print("D")
#else:
#    print("fail")    

 # ! --> short hand if else
 #eg:1
 # a =  9
 # b = 60
 # if a>b:
 #     print("A")
 # else:
 #    print("B")
 #? --> using short hand if else
 # * rules
 # 1.) statement inside the if condition have to be present
 # 2.) elif cannot be used in short hand if else
 # 3.) always it have to end with else

 # print  ("A") if a>b else print ("B")

 # ! code to check the given char is vowel or name
# char = input ("enter the car:")
 # if char=="a" or  char =='e' or char == 'i' or char =='0' or char =='u':
 #     print("is a vowel")
 # else:
 #  print("its consonent")

 # ? or

 # str1 = "aeiouAEIOU"
 # if char in str1:
 #    print("Vowel")
 # else:
 #     print("consonnt")

 # str1 = "aeiouAEIOU"
 # print("vowels") if char in  str1 else print("Consonnent")

 # ! ---> elif ladder using short hand if else
 # Eg:1
 # ? Find greatesr among 3 variables using short hand if else
 # a = 8
 # b = 5
 # c = 9
# print("A is grater") if a>b and a<c else print("B is greater")
 # if b>a and b>c else print("C is greater")

 # ! -------> looping

 # looping can be implimented using
 # for loop
 # while loop

 # ---> for loop
# ? for loop is used for iteartion, if we know the number of times the loop have to run
# ? It is used to iterate the iterables eg(string, list, tuple, etc...)

# todo --> syntax for loop

# for syntax in c
# for(i=0;i<0;i++)
#      primtg("hello"];

# for ufserdgt


# statement
# starement
# statement
# for val in range(10,0,-1):
#    print(val)

# for val in range(10,0,-2):
#     print(val)
# Eg:6
 #for  val in range(10, 0, 1):
#      print(val) # no output

 # Eg:7
  # i pirt the output of 7th multiplicatio table table from 21 to 43
  
#  for  val in range(1,10+1,):
       #print('7','x',val,'=',val*7) --> method:1

# --> Method:2
# ans = "7 X {} = {}"
# print(ans.format(val, val*7))

# --> Method :3
# print(f"7 X {val}={val*7}"}

# ? Eg:5
# break --> used to teerminate the ioop

# for val in rasnge(1,10):
#     if val ==6
#     break
#   print(val)

#Eg:6
for val in range(1,10):
     print(val)
     if val ==6:
#     break
# ? Eg:7
# for val in range(1,10):
#    if val ==6;
#      print(vasl)
#     break

# ! continue
# Eg:1
for val in range(1,10):
     if val ==6: or val ==8 or val ==21:
          continue
     print(val)

# ! practise problems
# ? print the even number between 20 to 40



  
  
  





