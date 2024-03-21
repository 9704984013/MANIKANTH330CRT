# ---> while loop
# ----> break using while loop


# eg:1
#i = 20
#while i<31:
 #   if i ==27:
#        continue
#    print(i)
#    i+=1

 #Eg:2,
#i = 20
#while i<31:
#    print(i)
#    if i ==27:
 #       break
 #   i+=1

 #eg:3
#i = 20
#while i <31:
 # if i ==27: 
 #        print(i)
 #        break
#  i+=1

#eg:4
#i = 20
#while i <31:
 # if i ==27:
#      continue
#      print(i)
 # i=i+1

#eg:
#i = 20
#while i<31:
#    i=i+1
#    if i ==27:
#         continue
#    print(i)


# eg:5
# while to iterate from 12 to 22
# find the sum of all numbers

#i =12
#sum=0
#while i<22:
 #  sum=sum+i
 #  i+=1
   #print(sum)

# eg:6
# Find the average of value from 20 to 25

#i =20
#sum=0
#count = 0
#while i<=25:
#  sum=sum+i
#  count+=1
#  i+=1
#  print(sum/count)

# ! ---------> Nested for loop

# Eg:1

#for row in range(1, 3+1):
#   for col in range(1, 4+1):
#        print(row, col)

# Eg:2
#* * * *
#* * * *
#* * * *
#* * * *

# Eg:3
#for row in range(2):
 #   for col in range(2):
 #     print("****")
 #rows = int(input("enter the rows"))
#col  = int(input("enter the col"))

# Eg:4
#  for row in range(row):
#  for in range(col):
 #     print("*", end=" ")
#      print()


# Eg:5
#sum = 0
#for row in range(5):
#    for col in range(5):
 #       sum =sum+1
#        print(row, end=" ")
#        
#    print()

# Eg:6
# ! to print start in rights in right angled trinagle

#for row in range(0,6):
#    for col in range(0,row):
#        print("*", end=" ")
#    print()

#for row in range(0, 6):
#   for col in range(row, 6):
#        print("*", end=" ")
#print()

#Eg:6

#for row in range(5):
 #   for col in range(5):
#        if col==0 or col==5-1 or row ==0 or row ==5-1:
 #        print("*", end=" ")
#    else:
  #       print(" ", end=" ")
 #   print()

#Eg:7

#for row in range(0, 5):
 #    for col in range(0, 6):
 #       if((row==0 and col==3) and (row==1 and col==2) and (row==2 and col==3) and (row==3 or col==4) and (row==4 or col==5)):
 #           print("*",end=" ")
 #       else:
 #           print(" ", end=" ")
 #       print()

 # ! ----> Datatypes
 # Primary,

 # Number --> int, float complex
 # String
 # Boolean
# None

 # Collection
 # List
 # tuple
 # set
# dictionary
             

 # ------> List

 #1.) if the collection of elements are surrounded by square brackets,
 #to be list

 # ! Eg:1,
  # 11 =[4, 7, 9.89], "hello", 7+9j, [8, 9, 0]]

# characterictics of list
# 1.) list have to be surrounded by []
# 2.) it is mutable (the elements in the list are changable)
# 3.) Every element inside list is indexed
# 4.) The elements inside list will be ordered format
# 5.) It can hold duplicate values
# 6.) Its heterogenous

 #To access the elements in list
#11 = [1, 4, 1, 7, 89.7, 7[5, "p", "i"]
 #  print(11) 
 
# -------> indexing

# In the collection datatypes like list, tuple, string, the elements will be alloted
# with predefined unique value called index value
# We have 2 types of indexing
# Positive indexing --> starts with 0from left hand side
# Negative indexing --> starts with -1 from right hand side

#?--> Positive indexing

# 1ist1 = [1, 4, 1, 7, 89.7, 7[5, "p", "i"]
#print(1st1[0])
#print(1st1[4])
#print(1st1[20]) --> error


# ---> Negative indexing

#1st1 [1, 4, 1, 7,89.7, 7.5, "p", "1"1
# print(1sti[-1])
#print(1st1[-5])

# ? -------> slicing

#lst = [1, 4, 1, 7,89.7, 7.5, "p", "i"]
#Ist[start_index:end_index: step]

#print(1st1[0:4])
#print(lst1[6:8])
#print(lst1[3:6])
#print(lst1[:5])
#print(lst1[3:])

#print(lst1[0:7:1]) # lst[0:7]----> both are same
#print(lst1[0:7:2])

lst = [1, 4, 1, 7,89.7, 7.5, "p", "i"]
#print(lst[-4:-1])
#print(lst[-1-4]) ---> []
#print(lst[-7:-1])
#print(1st1[-7:-1:2])

#! To insert ot add element inside list

# append()-> used to add elelement at last position of list
# 11 [9, 8, 0, 6]
# 11.append("car")
#print(l1)

I






      
   





    
