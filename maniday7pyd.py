#assignment--->
#1.)
##d1 = {'Ten': 10, 'Twenty': 20, 'Thirty': 30}
##d2 = {'Thirty': 30, 'Fourty': 40, 'Fifty': 50}
#Merge two python dictionary
# o/p --> {'Ten': 10, 'Twenty': 20, 'Thirty': 30, 'Fourty': 40, 'Fifty': 50}

#code:1,
##d1.update(d2)
##print(d1)

# 2.)Python Program to determine if 
# the given Sets Are Disjoint 
# or Not without Using Inbuilt-in Functions
#set1 = {'Python', 'Java', 'Data Science'}
#set2 = {'ML', 'AI', 'R Language', 'Python'}
#set3 = {'Data Analytics', 'Robotics', 'Deep Learning', 'ML'}

#code:2,
##c = 0
##flag =0
##for val in range(3):
##    c=c+1
##    if c==1:
##       for val in set1:
##        for val in set2 or val in set3:
##           flag=1
##           break
##            
##    if c==2:       
##       for val in set2:
##        if val in set1 or val in set3:
##             flag=1
##             break
##            
##    if c==3:
##       for val in set3:
##        if val in set2 or val in set1:
##            flag=1
##            break
##if flag==0:
##    print("Disjiont")
##else:
##    print("joint")
##    

        


        


# 3.)
##l1 = ["M", "na", "i", "Ke"]
##l2 = ["y", "me", "s", "lly"]
#O/P --> ['My', 'name', 'is', 'Kelly']

 #code:3,
#l3 = []
##for val in range(len(l1)):
##    ans = l1[val]+l2[val]
##    l3.append(ans)
##print(l3)
##      (or)

##l3 = []
##i=0
##while i<len(l1):
##    l3.append(l1[i]+l2[i])
##    i+=1
##print(l3)

# !------>Functions
# ? DEF
# Function is a block of code which is used to perform a specific funtionality
#Function can be created using def keywords

# ? function has 3 parts
# Function declaration
# Function defanction
# Function call

# Eg:1,
##def grteet(): # function defanition
##    print("Greetig User!!")

##greet()
##greet()
##greet()
##greet()
##greet()
##greet()
##greet() #function calling

# Eg:2,
def greeting(name):
      print("Welcome", name)

for val in range (3):
    username = input("Enter the name: ")
    greeting(username)






          
