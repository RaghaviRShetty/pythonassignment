# -*- coding: utf-8 -*-
def seq(length):
    if(length <= 1):
        return length
    else:
        return (seq(length-1) + seq(length-2))

length = int(input("Enter number of terms:"))

print("Fibonacci sequence using Recursion :")
for i in range(length):
    print(seq(i))