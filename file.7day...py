# code:
# d1 = {'ten':10, 'twenty':20 'thirty':30}
# d2 = {'thirty': 30, 'fourty':40, 'fifty':50}
# d1.update(d2)
# print(d1)

# set1 = {'Python', 'Java', 'Data Science'}
# set2 = {'ML', 'AI', 'R Language', 'Python'}
# set3 = {'Data Analytics', 'Robotics', 'Deep Learning'}
# c = 0
# for val in  range(3):
#        c=c+1
#        if c==1:
#               if val in set2 or val in set3:
#                  flag = 1
#                  break
#        if c==2:
#             for val in set2:
#                if val in set2 or val in set3:
#                    flag=2
#                    break
#        if c==3:
#            for val in set3:
#                if val in set1 or val in set1:
#                    flag = 3
#                    break
                
# if flag==0:
#     print("Disjoint")
# else:
#    print("Joint")
    
# Eg:3
list1 = ["M", "na", "i", "ke"]
list2 = ["y", "me", "s", "11y"]

l3 = []
# for val in range(len(list1)):
#    ans = list1[val]+list2[val]
#     l3.append(ans)
#print(13)

i=0
while i<len(list1):
     l3.append(list1[i]+list2[i])
     i+=1
print(l3)

# ! functions
#? Def
# Function is a block of code  which is used to perform a specfic functionality
# Function can be created using def keyword

# ? Function has 3 parts
# Function declaration
# Function  defanition
# Function call

# Eg:1

# def great(): function defanition
#           print("Greetings User !")

# greet()
# greet()
# greet()
# greet()
# greet()
# greet()
# greet() # function calling


# ! Eg:2
# ? Function with parameter
def greeting (name):
    print("Welcome", name)

for val in range(3):
    username = input("Enter the name: ")
    greeting(username) # username is argument



