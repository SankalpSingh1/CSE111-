# 1st method
 
 
# class computer():
#     def config():
#         print("1Tb,512gb,33w")
        
# com1=computer

# com1.config()      


# 2nd method


# class computer:
    
#     def __init__(self,cpu ,ram):
#         self.cpu=cpu
#         self.ram=ram
        
#     def config(self):
#         print("config is ",self.cpu,self.ram)
        
# com1=computer('i5',18)       
# com2=computer('i7',9)

# com1.config()
# com2.config()



# 3rd type


# class computer:
#     def __init__(self):
#         self.name="Sanju"
#         self.age=21
    
#     def config(self):
#         print("config is",self.name,self.age)
    
#     # if u want to update any value
        
    # def update(self):
    #     self.name="Sajal"   
        
#         # if u want to compare two self's
    
#     def compare(self,other):
#         if self.name== other.name:
#             return True
#         else:
#             False
# com1 = computer()
# com2 = computer()

# if com1.compare(com2):
#     print("they are same")

# com1.config()
# com2.config()


# 4th type

# class Student:
#     pass

# Stud_1=Student()
# Stud_1.name=input("enter name:")
# Stud_1.age=input("enter age:")
# Stud_1.degree=input("enter degree:")

# Stud_2=Student()
# Stud_2.name=input("enter name:")
# Stud_2.age=input("enter age:")
# Stud_2.degree=input("enter degree:")

# print("Stud_1.name:",Stud_1.name)
# print("Stud_1.age:",Stud_1.age)
# print("Stud_1.degree:",Stud_1.degree)
# print("Stud_2.name:",Stud_2.name)
# print("Stud_2.age:",Stud_2.age)
# print("Stud_2.degree:",Stud_2.degree)








# class Student:
#         pass
        
# stud_1=Student()
# name=input("Name: ")
# age=int(input("Age: "))
# degree=input("Grade: ")
# print("details of student:",name,age,degree)



# class Student:
#     pass
# stud_1=Student()
# name=input("Name: ")
# branch=input("Branch: ")
# rank=input("Rank: ")
# print("His name:",name)



# class Manager:
#     pass
# Stud_1=Manager()
# name=input("name: ")
# # department=input("department: ")
# # salary=input("salary: ")
# print('emp_1.name:',name)









# class Student:
#     def __init__ (self,name,age,email):
#         self.name=name
#         self.age=age
#         self.email=email
        
#     def studentdetails (self):
#         print("name:",self.name,", age:",self.age,", email:",self.email)
        
# name=input("name: ")
# age=int(input("age: "))
# email=input("email: ")
# s1=Student(name,age,email)
# s1.studentdetails()









# class Greeting:
#     def sayhello (self,name=None,wish=None):
#         if name is not None and wish is not None:
#             print("Hello"+name+wish)
#         elif name is not None and wish is None:
#             print("Hello"+name)    
#         else:
#             print('declined')
# greet=Greeting()
# a=input()
# b=input()
# greet.sayhello(a,b)
# greet.sayhello(a)












# class Student:
#     __group="ECE"
#     __report="fail"
    
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#     def setdetails(self,__group,__report):
#         self.__group=__group
#         self.__report=__report
#     def getdetails(self):
#         print(self.name,self.age,self.__group,self.__report)
# name=input("name: ")
# age=int(input("age: "))
# group=input("group: ")        
# report=input("pass/fail: ")
# s1=Student(name,age)
# s1.setdetails(group,report)
# s1.getdetails()







# class Car:
#     __engineno='EK1'
#     __modelno="VX6"
    
#     def setcarinfo(self,__engineno,__modelno):
#         self.__engineno=__engineno
#         self.__modelno=__modelno
        
#     def getcarinfo(self):
#         print(self.__engineno,self.__modelno,self.color,self.year)
        
# hc=Car()
# engnum=input("engine number: ")
# hc.setcarinfo(engnum,"SX6")
# hc.color="Blue"
# hc.year=2024
# hc.getcarinfo()







# class Employee:
#     pass
# Emp_1=Employee()
# a=input("Name: ")
# salary=25000
# print("Emp_1.name:",a)
# print("Emp_1.salary:",salary)





# class Car:
#     def setname(self,name):
#         self.name=name
#     def getname(self):
#         return
    
# H=Car()
# name=input("name: ")
# H.setname("name")
# H.getname()
# print("Honda car name:",name)



# class Student:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#     def studentdetails():
#         print(self.name,self.age)
# name=input("name: ")
# age=int(input("age: "))
# s1=Student(name,age)
# s1.studentdetails()
        
# class Student:
#     def setdetails(self,name,age,degree):
#        self.name=name
#        self.age=age
#        self.degree=degree
#     def getdetails(self):
#         print(self.name,self.age,self.degree)
   
# Stud_1=Student()     
# a1=input("name: ")
# b1=int(input("age: "))
# c1=input("degree: ")

# Stud_2=Student()
# a=input("name: ")
# b=int(input("age: "))
# c=input("degree: ")

# Stud_1.setdetails(a1,b1,c1)
# Stud_2.setdetails(a,b,c)
# Stud_1.getdetails()
# Stud_2.getdetails()





class Employee:
    def setdetails(self,Empid):
        self.Empid=Empid
    def getdetails(self):
        print("Employee ID:",self.Empid)
        
emp1=Employee()
emp2=Employee()
a=int(input("Empid: "))
b=int(input("Empid2: "))
emp1.setdetails(a)
emp2.setdetails(b)
emp1.getdetails()
emp2.getdetails()