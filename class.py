# # a=int(input("enter the balance: "))
# # if a >=1000:
# #     print("sufficient balance")
# # else:
# #     print("low balance")

# # ch=(input("ch: "))
# # if (ch.isalpha()):
# #     print("alphabet")
# # elif(ch.isnumeric()):
# #     print("digit")
# # else:
# #     print("neither alphabet nor digit")

# # num=int(input('num: '))
# # sum=0
# # i=1
# # while(i <=num):
# #     if(i % 2==0):
# #         sum=sum+i
# #     i = i + 1
# # print("sum:",sum)

# # generate a sequence of k integer

# # x=int(input("k: "))
# # i=0
# # while(i<x):
# #     if(i%2==0):
# #         print(i,"even number")
# #     else:
# #         print(i,"odd number")
# #     i=i+1
 
# #  dec,bin use krne ke liye
        
# x=int(input('x: '))
# print("decimal: ",x)
# print("Binary: ",bin(x))
# print("octal: ",oct(x))
# print("hexadecimal: ",hex(x))

# # for math in python

# import math 
# num = float(input('num:'))
# if num-int(num)>=0.5:
#     print('result: ',math.ceil(num))
#     print("result: ",math.trunc(num))

# # random numbers in python

# import random
# x=[1,2,3,4,5,6,7,8]
# print(random.choice(x))
# random.shuffle(x)
# print(x)

# # fibnoci series

# a=0                                         
# b=1                                          
# n=int(input('n: '))                          
# c=a                                      
# while(c<=n):                                                                       
#     print(c)                                   
#     a=b                                         
#     b=a                                         
#     c=a+b

# # #consonent or vovels

# t")ch=input('ch: ')
# vovles=['a','e','i','o','u','A','E','I','O','U']
# if ch.isalpha():
#     if(ch in vovles):
#         print("vovels")
#     else:
#         print("consonent")
# else:
#     print("not an alphabe

# # sum of num

# # num=int(input("num: "))
# # sum=0
# # temp=num
# # while(num):
# #     sum=sum+(num%10)
# #     num=num//10
# # print("sum:",sum)

# # pascals triangle

# # rows = int(input("rows: "))
# # for index in range(0, rows):
# #     for spaces in range(rows, index, -1):
# #      print(' ', end='')
# #     number = 1
# #     for col in range(0, index + 1):
# #         print("%d" % number, end='')
# #         number = number * (index - col)/(col+1)
# #     print()

# # to find greater number 

# # a,b,c = (input("a,b,c: ").split(","))
# # a,b,c = [int(a),int(b),int(c)]
# # if(a>b and a > c):
# #     print(a)
# # elif (b > c and b > a):
# #     print(b)
# # else:
# #     print(c)
    
    
# # i =1
# # while i<=10:
# #     print(i)
# #     i +=1


# a=input("x: ")
# z=len(a)
# print(z)

# # list=[10,20,30,40,50]
# # list.reverse()
# # print(list)
    
# for num in range(-10,0,1):
#     print(num)

# for i in range(5):  
#     print(i)
# else:
#     print
#     ("done")

# # first two numbers
# # num1,num2=0,1
# # print("fibnoici sequense")
# # for i in range(20):
# #     print(num1)
# #     res=num1+num2
    
# #     num1=num2
# #     num2=res

# # num =int(input("a: "))
# # factorial = 1
# # if num < 0:
# #     print("Factorial does not exist for negative numbers")
# # elif num == 0:
# #     print("The factorial of 0 is 1")
# # else:
# #     # run loop 5 times
# #     for i in range(1, num + 1):
# #         # multiply factorial by current number
# #         factorial = factorial * i
# #     print("The factorial of", num, "is", factorial)


# # list=[1,2,3,4,5,6]
# # list.reverse()
# # print(list)


# a=[10,20,30,40,50,60,70,80,90]
# print(a[1::5])

# # num=5
# # start=2
# # sum_seq=0
# # for i in range(num):
# #     print(start,start*10+2)
# #     sum_seq += start
# #     start= start*10+2
    
# # num1=int(input("enter the value: "))
# # num2=int(input("enter the value:"))
# # if num1>num2:
# #     print(num1,"is greater than",num2)
# # else:
# #     print("num1 is smaller")
    
# # import random
# # r=random.randint(1,20)

# # while(True):
# #     inr=int(input())
# # if(inr<r):
# #     print("sorry guess a larger number")
# # elif(inr>r):
# #     print("sorry guess a smaller number")
# # else:
# #     print("oh great guessed a right number") 
       
       
# # i=int(input("enter the value: "))
# # while i<=38:
# #     print("raju")
# #     break
# # else:
# #     print("jaggu")


# # count=5
# # while count>0:
# #     print(count)
# #     count=count-1

# x=int(input("Enter the year: "))
# result="leap year" if x%400==0 else "leap year" if x%4==0 and x%100 !=0 else "non leap year"
# print(result)




# count=20
# while count>10:
#     print(count)
#     count=count-1
# else:
#     print("im inside the else")

# gcd of tow numbers
# a=int(input("enter first number"))
# b=int(input("enter second number"))
# while b>0:
#     r=a%b
#     a=b
#     b=r
# GCD=a
# print("gcd is", GCD)


# a=0
# b=1
# c=a+b
# num=int(input('Enter the value: '))
# if num==1:
#     print(a)
# else:
#     print(a)
#     print(b)
#     for i in range(1,num+1):
#     a=b
#     b=c
#     c=a+b
#     print(c)
    
    
    
# sumfact nikalne ke liye

# sumfact=0
# num= int(input("num: "))
# temp=num
# while(num):
#     i=1
#     fact=1
#     digit=num % 10
#     while(i<= digit):
#             fact= fact*i
#             i=i+1
#     sumfact= sumfact+fact
#     num=num//10
# if(sumfact== temp):
#     print("strong number")
# else:
#     print("not a strong number")
    
# to check weather the nmber is perfect or not

# sum=num(perfect)
# sum>num(abundent)
# sum<num(deficient)

# num=int(input("num:"))
# s=0
# li=[]
# for i  in range (1,num):
#     if num%i==0:
#         s+=i
#         li+=[i]
# print("factors:",li)
# print("sum:",s)
# if s==num:
#     print("perfect")
# elif s>num:
#     print("abundant")
# else: 
#     print("deficient")




# armstrong number

# num=int(input("enter a number: "))
# sum=0
# temp=num
# while temp >0:
#     digit= temp%10
#     sum+=digit**3
#     temp//=10
# if num == sum:
#     print(num,"is an Angastrom number")
# else:
#     print("is not a Angastrom number") 

# basic of function

# def add(x,y):
#     s=x+y
#     print(s)
# def sub(x,y):
#     d=(x-y)
#     print(d)
# def mul(x,y):
#     p=(x*y)
#     print(p)
# x=int(input("x: "))
# y=int(input("y: "))
# add(x,y)
# sub(x,y)
# mul(x,y)

# function by name

# def helloworld():
#     print("hello world")
#     print("good morning")
#     print("have a nice day")
#     print("the function end")
# helloworld()


# def addavg(x,y):
#     s=x+y
#     avg=s/2
#     return s, avg
# def sub(x,y):
#     s=x-y
#     return s
# def mul(x,y):
#     m=x*y
#     return m

# a=int(input("a: "))
# b=int(input("b: "))

# average=addavg(a,b)
# subtraction=sub(a,b)
# multiplication=mul(a,b)

# print("sum, average:",(average))
# print("subtration:",(sub))
# print("multiplication:",(multiplication))


# n=int(input())
# for i in range(1,n):
#     b=n*(n-1)
#     print(i)

#arguments and parameters 


# def sayhello(username):
#     greet="hello"
#     print(greet+" "+username)
    
# users=['ram','raju','rajiv','anvesha']
# for i in users:
#     sayhello(i)


# simplecalc()

# def simplecalc(num1,num2=100):
#     print("addition",num1+num2)
#     print("subtraction",num1-num2)
#     print("multiplication",num1*num2)
    
# num1=int(input("num1:"))

# simplecalc(num1,num2=100)

# tax calculator

# def calculatetax(salary,percent=20):
#     taxamount=salary*percent/100
#     print(taxamount)
# salary=int(input("salary: "))
# percent=int(input("percent: "))
# calculatetax (salary)
# calculatetax(salary,percent)

# function questions

# def fun1(name='aruna',age=12):
#     print(name,"is",age,"years old")
# fun1("ajay",13)
# fun1("karuna",)

# lambda function

# def demo(name,age):
#     print(name,age)
    
# demo("ben",90)

# def dispency(name,age):
#     print(name,age)
    
# dispency("raju",30)
    
    
# for i in range(4,30):
#     if (i%2==0):
#         print(i)
    
# x= [4,3,45,6,8]
# print(max(x))

    
# import module1

# print(module1.mul(6,5))


# a=("this is my first String")
# print(a[11])

# import random
# r=random.randint(1,20)

# while(True):
#     a=int(input())
#     if a<r:
#         print("guess a greater number")
#     elif a>r:
#         print("guess a smaller number")
#     else:
#         print("good")

# h=int(input())

# while(h>10):
#     print("yeah")
#     h=h-1


# c="ABCD"
# b='C'
# a=c.find(b)
# print(a)


# program for dictionary

# list1=input("data1: ").split(",")
# list2=input("data2: ").split(",")
# if len(list1)!=(list2):
#     print("list are different length")
# else:
#     outstr="{"
#     for i in range(len(list1)):
#         outstr=f"'{list1[i]}':'{list2[i]}',"
#     outstr=outstr[:-2]
#     outstr +="}"
#     print(outstr)


# list1=input("data1: ")
# list2=input("data2: ")
# if len(list1)!=(list2):
#     print("list of different length")
# else:
#     outstr="]"
#     for i in range(len(list1)):
#         outstr=f"'"

# data1=input("data1: ").split(',')
# e=input("element: ")
# data1.append(e)

# print("after append: ",data1).split(',')
# data2=input("data2: ")
# e=input("element: ")
# data1.append(data2)
# print("after append:"data1)
# data1.extend(data2)

# prime number code

# num=13
# # for i in range(2,num):
# if num % 2== 0:
#     print("not a prime number")
        
# else:
#     print("prime number")



# num=[11,12,13,14,15]
# even= list(filter(lambda  n:n%2==0,num))
# print(even)

# doubles=list(map(lambda n:n**2,num))
# print(doubles)


 
# def fib(n):
#     a=0
#     b=1

#     for i in range(2,n):
#         c=a+b
#         a=b
#         b=c
#         print(c)
# fib(9)



# def fact(x):
#     f=1
#     for i in range(1,x+1):
    
#         f = f*i
        
#     return f
# x=4
# result=fact(x)
# print(result)








        



# for append

# list=['123','145','789']
# t=[]
# print(len(list))
# for i in range(3):
#     ele= input("element: ")                          
#     t.append(ele)
# print("list: ",t)

# ############

# list=input("data: ").split(",")
# mytuple=tuple(list)
# print(mytuple)


# list=[1,2,5,24,58,6,3]
# print(sorted(list))



# data=tuple(map(int,input("data:").split(",")))

# print(tuple(data))
# print(sum(data))




# list=tuple(map(int,input("data:").split(",")))
# print(sum(list))
# print(tuple(list))


# d1=input('data1: ')
# d2=input("data2: ")
# d3=input("data3: ")
# d4:input("data4: ")

# dict1=dict(zip(d1.split(",")),d2.split(","))
# dict2=dict(zip(d3.split(","))),d4.split(",")

# key=input("key: ")
# if key in dict1 and key in dict2:
#     print("key present in both dictionaries")
# elif key in dict1:
#     print("key present in first dictionary")
# elif key in dict2:
#     print("key present in second dictionary")
# else:
#     print("key is not present")
    
    
    
# data1=1,2,3,4
# data2="apple","grapes","mango"
# print("element: ",list(zip(data1,data2)))

# def fib(n):   
#     a=0
#     b=1
#     print(a)
#     print(b)
#     for i in range(2,n):
#         c=a+b
#         a=b
#         b=c
#         print(c)
# fib(9)



# class type question

# 1st

# class Student:
#     pass
# Stud_1= Student()
# Stud_1.name = input("enter name: ")
# Stud_1.branch = input("enter branch: ")
# Stud_1.rank = int(input("enter rank"))
# print("Stud_1.name:",Stud_1.name)
# print("Stud_1.branch:",Stud_1.branch)
# print("Stud_1.rank:",Stud_1.rank)


# 2nd


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



class Student():
    
    bday=5
    
    def __init__(self):
        self.name="sanju"
        self.age=34
        
    def config(self):
        print("what is your name:",self.name)
        print("what is your age:",self.age)
    
    
   
com1=Student()        
com2=Student()

print(com1.config,com1.name,com1.age,com1.bday)
print(com2.config,com2.name,com1.age,com2.bday)
# com1.config()
# com2.config()
    
class Student():
    def __init__(self,name,age):
        self.name=name
        self.age=age
        
    def config():
        print("what is your details:")











