# l = [1,2,3,4,5,6,7,8,9]
# s=sum(l)
# print(s)

# l = [1,2,3,4,5,6,7,8,9]
# total = 0
# for i in l:
#     total += i
# print(total)

#-----------------------tuple--------------------------------------------------
# t = tuple('Darshan')
# print(t) #---> ('D', 'a', 'r', 's', 'h', 'a', 'n')


# t = (1,2,3,2,4,5,6)
# print(t.count(2))
# print(t.index(2))
# for i in t:
#     print(i)
# for i in t:
#     print(i ** 2)

# ----------------------Dictinory----------------
# name = ['apple','mango','ornage']
# price = [120,100,130]

# fruite  = dict(zip(name,price))
# print(fruite)

# fruite = {'apple':120, 'mango':100, 'papayi':20}
# p = fruite.get('apple')
# print(p)

# fruite['gova']=80

# print(fruite)
# new = {'grapes':220, 'orange':22, 'banana': 20}
# fruite.update(new)
# print(fruite)

# for i in fruite:
#     print(i)

# for i in fruite:
#     print(i) #--> key prints

# for i in fruite:
#     print(fruite[i]) #--> value print

# for i in fruite:
#     print(i, fruite[i]) #--> key value print


# for key, value in fruite.items():
#     print(key, value) #--> all key value print

# print(fruite.keys())
# print(fruite.values())
# -----------------------
# d = {'r':12, 'r': 13}
# print(d) # latest value display
# -------------------------
# name = input()
# for i in name:
#     print(i)
#  --------------------------------
# name = input()
# freq  = {}
# for i in name:
#     if i not in freq:
#         freq[i] = 1
#     else:
#         freq[i] += 1
# print(freq)

# --------------------sets----------------------

# d = {'aa','ss','f','g'}
# g = {'aa','w','f','y'}
# p = d.union(g)
# c = d.difference(g)
# print(c)
# print(p)

# ================ Functions =======
# user define function
# built-in  function

# def greet():
#     '''
#     thusfs kjsjfjsa sajdf
#     '''
#     print('hi hallo')

# # print(greet)
# # calling function
# greet()
# -----------------------------------

# def greet(name):
#     print("hi", name , 'sir')

# greet('darshan')
# -------------multiple parameters--------

# def add(a,d):
#     c = a + d
#     print(c)

# add(1,2)
# d = add(1,2)
# print(d,type(d)) #--> it is give nontype
# --------------return function-----------

# def add(a,b):
#     c = a + b
#     return c

# add(1,2)
# d = add(1,2)
# print(d, type(d)) #--> it will not  give non type its give type value
# ------------code after return doesn't get executed---------
# def func():
#     c ='before return'
#     return "retuorn", c
#     print('after return')

# func()

# -------------------------returning multiple valudes---------
# def intro(name, age, hobby):
#     return name, age, hobby

# c, d, e = intro('darshan', 25, 'travl')
# print(c, d, e)
# m = intro('darshan', 25, 'travl')
# print(m, type(m))
# --------------------scope variavble---------

# a = 5
# def func():
#     a = 30
#     print(a)

# func()
# print(a)
# ------if you want chenge a global variable ---
# a = 5
# def func():
#     global a
#     a = 20
#     print(a)

# print(a)
# func()
# print(a)
# ------lambda function-----------

# c = (lambda a, b : a + b) (2,3)
# print(c)
# ------------

# func = lambda a, b : a + b
# print(type(func))
# print(func(4,5))

# ----------largeer value------------
# def large(a,b):
#     if a > b:
#         return a
#     else:
#         return b
    
# print(large(5,6))
# print(large(55,6))
# ----------lager use lambda-----------
# func = (lambda a, b : a if a > b else b) (2,3)
# print(func)
# ------------------

# func = (lambda a, b : a if a > b else b)
# print(func(12,3))
# ----------------------------
# def even(li):
#     for i in li:
#         if i % 2 == 0:
#             print(i)

# lst = [1,2,3,4,5,6,7]
# even(lst)
# ------------------

# lis = lambda a: a % 2 == 0
# b = [1, 2, 3, 4, 5]
# print(list(filter(lis, b)))

# ------------------take a unicq list-------------------

# def uniq(li):
#     new = []
#     for i in li:
#         if i not in new:
#             new.append(i)
#     return new

# lst = [1,2,3,4,1,2,3,4,4,5,6,7]
# print(uniq(lst))
# --------------aribitary arguments----------

# def test(*args):
#     print(args)
#     print(type(args))

# test(2)
# test(2,3,4,5)
# test(2,'darsh')
# ------------------

# def test(*args):
#     for i in args:
#         print(i, end=' ')

# test(2,3,4,5,6,7,8)
# ------------Keey argument stored in dictinary form---
# def intro(**kwargs):
#     print(kwargs)

# intro()
# intro(name = 'dash', age = 25)
# -----------------parameter and *args and **kwargs all mix one----
# def mix(a,b,*args, **kwargs):
#         print(a,b)
#         print(args)
#         print(kwargs)

# mix(10,20, 30, name='drsh', psss=7)
# ===================OOPS========================
# oops object oriented progrm it
# main 4 pillors apart from class and object
# --> Abstraction == tis is like car eggin not display hiding the information
#     means displaying only essential information and hiding the details
# --> Encapsulaction == like car desing color breck tair
#     Bulinding of data into a single unit
#     building of all methods that can on an object of that data
#     car can have colors, brake, engine, and a lot of other methods
# -->Innheritance == cars relse number of car one one car have one future
#    when a class derives from another class
#    any new car company can inherit all the information from car methods
# --> Polimarphisim == human class but one person one one future
#    the word polymorphisum means having manuy forms
#    same class method can work diffrently for diffrent objects
# -->
# ================calss object constractor============

# class Human:
#     def __init__(self,name,age,hobby):
#         self.name = name
#         self.age = age
#         self.hobby = hobby
#         # print(name,age,hobby)

# cl = Human('darshan', 25, 'swim')
# cl1 = Human('shakti', 26, 'run')

# print(cl.name)
# print(cl1.name)
# print(cl.age)
# print(cl1.age)
# print(cl.hobby)
# print(cl1.hobby)
# ----------------------constractor method-----------
# class Human:
#     def __init__(self,name,age,hoddy):
#         self.name = name
#         self.age = age
#         self.hoddy = hoddy

#     def greet(self): 
#         print(f'hi{self.name}, gm')

# cl = Human('darshu',23, 'run')

# cl.nationality = 'india'
# cl.hoddy = 'cow boy'
# print(cl.name,cl.age,cl.hoddy)

# cl1 = Human('shakti', 26, 'swim')
# cl1.greet()    

#----------------class veriable-------  
# class Human:
#     # class veriable
#     papupation = 0
#     data = []

#     #constractor 
#     def __init__(self,name,age,hoddy):
#         self.name = name
#         self.age = age
#         self.hoddy = hoddy
#         self.papupation += 1 # it can cheng only constrocter
#         Human.papupation += 1 # it can chenge hole class

#         Human.data.append(self.name)

#     #methods
#     def greet(self): 
#         print(f'hi{self.name}, gm')

# cl = Human('darshu',23, 'run')
# print(cl.papupation) # 1
# print(Human.papupation) #1


# cl1 = Human('shakti', 26, 'swim')

# print(Human.data) #['darshu', 'shakti']
# -------------adding more methods in same class----

# class Human:

#     # class variable
#     papulation = 0

#     #constractor
#     def __init__(self, name, age, alive=True):
#         self.name = name
#         self.age = age
#         self.alive= alive
#         Human.papulation +=1 

#     # methods
#     def dead(self):
#         if self.alive:
#             print(self.name, "is no more")
#             Human.papulation -= 1
#             self.alive = False
#         else:
#             print("this parson alredy  no more")

#     def child(self, number):
#         self.number = number
#         Human.papulation += number

# h1 = Human('H1', 70)
# h2 = Human('H2', 60)
# h3 = Human('H3', 40)
# h1.dead()
# print(Human.papulation)
# h1.dead()
# print(Human.papulation)
# h1.dead()
# h3.child(9)
# print(Human.papulation)
# h3.dead()
# h3.dead()
# print(Human.papulation)

# ============inheritance===================
# class Human:
#     # class veriable
#     papupation = 0
#     data = []

#     #constractor 
#     def __init__(self,name,age,alive=True):
#         self.name = name
#         self.age = age
#         self.alive = alive
#         self.papupation += 1 # it can cheng only constrocter
#         Human.papupation += 1 # it can chenge hole class

#         Human.data.append(self.name)

#     #methods
#     def greet(self): 
#         print(f'hi{self.name}, gm')

#     def dead(self):
#         if self.alive:
#             print(self.name, "is no more")
#             Human.papupation -= 1
#             self.alive = False
#         else:
#             print('this parsone alrdy daied')

#     def child(self, number):
#         self.number = number
#         Human.papupation += number

# # # ----------------inheritance-----------------
# class Employee(Human):
#     def emp(self, name, age, company, post):
#         super().__init__(name,age)
#         a
#         self.data += 'haresh'

# h1 = Human('h1',25)
# h2 = Human('h2', 30)

# print(Human.papupation) #2 
# h1.dead() # -1 person no more
# print(Human.papupation)# 1
# h1.dead() # this parson alredy daed

# h3 =  Human('h3', 58)
# print(Human.papupation) #2
# h3.child(1) 
# print(Human.papupation) #3

# # ----hineriting Employe class acess-----
# h4 = Employee('h4', 77)
# h4.emp()
# print(Human.data)
# ==================Adding atributes======================
# class Human:
#     # class veriable
#     papupation = 0
#     data = []

#     #constractor 
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
#         Human.papupation += 1 # it can chenge hole class
#         Human.data.append(self.name)

#     #methods
#     def greet(self): 
#         print(f'hi{self.name}, gm')

# #  ----------------inheritance-----------------
# class Employee(Human):
#     def __init__(self, name, age, company, post):
#         super().__init__(name, age)
#         self.company = company
#         self.post = post

# h1 = Human('h1',25)
# h2 = Human('h2', 30)
# print(Human.papupation)
# # ----hineriting Employe class acess-----
# h4 = Employee('h4', 77, 'ibm', 'ceo')
# print(Human.papupation)
# print(h4.name)
# print(h4.age)
# print(h4.company)
# print(h4.post)

# print(Human.data)
# ===========Adding methods in drived class===========
# class Human:
#     # class veriable
#     papupation = 0
#     data = []

#     #constractor 
#     def __init__(self,name,age,alive=True):
#         self.name = name
#         self.age = age
#         self.alive = alive
#         Human.papupation += 1 # it can chenge hole class
#         Human.data.append(self.name)

#     #methods
#     def greet(self): 
#         print(f'hi{self.name}, gm')

#     def dead(self):
#         if self.alive:
#             print(self.name, "is no more")
#             Human.papupation -= 1
#             self.alive = False
#         else:
#             print('this parsone alrdy daied')

#     def child(self, number):
#         self.number = number
#         Human.papupation += number

# #  ----------------inheritance-----------------
# class Employee(Human):
#     def __init__(self, name, age, company, post):
#         super().__init__(name, age)
#         self.company = company
#         self.post = post

#     def hire(self, person):
#         print(f"{person} has been hired in company")
#         Human.data.append(person)
#         Human.papupation += 1

# h1 = Human('h1',25)
# h2 = Human('h2', 30)
# print(Human.papupation)
# # ----hineriting Employe class acess-----
# h4 = Employee('h4', 77, 'ibm', 'ceo')
# print(Human.papupation)
# print(h4.name)
# print(h4.age)
# print(h4.company)
# print(h4.post)
# h3 = Employee('h3', 99, 'google', 'ceo')
# print(Human.data)
# h3.hire('harry')
# print(Human.papupation)
# print(Human.data)

# h3.dead()
# h3.dead()
# ===========file handling=======================
# creat file and write
# file = open("tect.txt", 'w')
# file.write("name\nnumber \nbirth \nplace")
# file.close()

# # file reading file
# filere = open('C:/Users/darsh/PycharmProjects/pythonprogram/classprogram/oops/file handling/tect.txt','r')
# filedata = filere.read()
# print(filedata)

# ---------------------------------
# with open('tect.txt') as f:
#     print(f.read()) # read the file text

# print(f.closed) # True

# with open('tect.txt', 'w') as f:
#     f.write('he am wirte')

# # ------------------writing file --------------
# # we are creating new file here

# with open("new.txt", 'w') as file:
#     file.write('hey new file created')

# #weitw in exisiting file

# with open('new.txt', "w") as file:
#     file.write("this is update content of oure file \n")
#     file.write("one more nesxt line will be adding \n")

# ----------------read------------------

# with open('new.txt','r') as f:
#     # data = f.read()
#     # print(data)# read all the line

#     data = f.read(4)
#     print(data) # read the starting 4 character
#     print(f.tell()) #4
    
#     data = f.read(10)
#     print(data) # read the after  4 character un till 10 char

#     # tell : tell you the position of your file handle
#     print(f.tell()) #14

#     #using seek you can reset your file handler

#     f.seek(0)

#     print(f.tell())
#     print(f.read())

#     #  readlines 
# with open('new.txt', 'r') as f:
#     data = f.readlines()
#     print(data)
#     for i in data:
#         print(i)

# -------------read and weite binary formet--------------------
# with open('darsh.jpg', 'rb') as f:
#     data = f.read()
#     print(data)

#     with open('file.jpeg', 'wb') as d:
#         d.write(data)# this wil image format 
# --------------------appendig in a file-------------------
# with open('new.txt', 'a') as f:
#     data = f.write('ADasdsad')
#     print(data)
# =================Try and Except ==============
# a = 5
# b = 0

# try:
#     print(a/b)
# except:
#     print('error the code')

# print('am darshan')
# ----------------Exception---------------------
# a = 5
# b = 0

# try:
#     print(a/b)
# except Exception as e:
#     print('error the code', e)

# print('am darshan')
# ----------------Finally----------------------
a = 5
b = 0

try:
    print('open file')
    print(a/b)
    print('close file')
except Exception as e:
    print('this will erorr')
finally:
    print('close file')