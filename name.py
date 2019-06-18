# -*- coding: utf-8 -*-

name = input ("enter name:")
print (type(name))
print("your name is",name)

age = int(input ("enter age:"))
print (type(age))
print("your age is",age)

amount = float(input ("enter amount:"))
print (type(amount))
print("your have to pay",amount)

num1 = int(input("enter number 1:"))
num2 = int(input("enter number 2:"))
result = num1 + num2
print("result of addition of ",num1,"and",num2,"is",result)

print(10/3)
print(10//3)

sum = 0
sum = sum + 10
sum +=10
print (sum)

product = 1
product = product * 10
product *=10
print (product)

#relational
# >,<,>=,<=,!=
num1 = 100
num2 = 200
print(num1>num2)
print(num1!=num2)

# ==,===
num3=150
num1=300
print(num1==num2)

#logical opertors and,or,not
num3=150
num1=300
num2 = 200
print(num1>num2 and num1>num3)

