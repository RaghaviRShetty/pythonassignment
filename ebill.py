# -*- coding: utf-8 -*-
units = int(input(" Please enter Number of Units you Consumed : "))

if(units <=100):
    amount = units * 2
elif(units > 100 and units<=200):
    amount = units*3
 elif(units > 200 and units<=300):
    amount = units*5
else:
    amount =units*6
print("\nElectricity Bill = ",amount)