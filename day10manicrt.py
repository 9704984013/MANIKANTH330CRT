
##1 Tasks
## Write the code for the below tasks using function
##1.) dl ("shirt": 1000, "pant": 1500, "Shoes": "900", "handkey": 30}
##a.) Find the min ans max priced product
##b.) Find the product starts with 's' and 'S'

##2.) Find then 67, is strong number or not
##
##3.) 11 [1,2,3,4,5,6]
##n=2> [5, 6, 1,2,3,4]
##n=3--> [4,5,6, 1,2,3]

## ! method riding
## * Polymorphism in classes using inheritance

## ? Eg:1
##class bank :
##    def ratio(self):
##        print(" All banks has repo rate")
##
##class SBI(bank):
##    def ratio(self):
##        print("SBI rate is 9%")
##
##class IOB(bank):
##    def ratio(self):
##        print("IOB rate is 7.5%")
##
##i = IOB()
##i.ratio()
##
##s= SBI()
##s.ratio()

## ? Eg:2
##class USA:
##    def language(self):
##        print("ENGLISH")
##
##    def captail(self):
##        print("Washington DC")
##
##class India(USA):
##    def language(self):
##        print("sansrit")
##
##    def captail(self):
##        print("New delhi")
##
##I = India()
##I.language()
##I.captail()


## ? Eg:3
#polymorphism using objects

#c1, c2---->c1 = print(c1), print(c2)
#f1, f2


##class c1:
##    def f1(self):
##        print("c1") 
##
##
##class c2(c1):
##    def f1(self):
##        super().f1()
##        print("c2") 

##obj1 =c2()
##obj1.f1()

##obj2 =c1()
##obj2.f1()

##def  display(a):
##    a.f1()
##display(obj1)
##display(obj2)

# * changing the functionality of builtin functions
#a = 9
#b = 6
##print(a+b)
##print(a.__add__(b))

#print(a.__sub__(b))

##class shopping:
##    def __init__(self, l1):
##        self.items = l1
##
##    def __len__(self):
##        length = len(self.items)
##        return length
##s = shopping([1,2,3,4,5])
##print(len(s))


# ! Method overloading
# ! Eg:1
##class suming:
##    def add(self, a, b, c):
##        print(a+b)
##
##    def add(self, a, b, c):
##        print(a+b+c)
##
##s = suming()
##s.add(4, 3)
##s.add)4, 5, 1)

# ! Eg:2
##class summing:
##    def add(self, a=None, b=None, c=None):
##        if a!=None and b!=None and c!=None:
##            print(a+b+c)
##        elif a!=None and b!=None:  
##            print(a+b)
##        else:
##            print(a)
##obj= summing()
##obj.add(2)
##obj.add(3, 4)
##obj.add(1,2,3)






