# -*- coding: utf-8 -*-
p=int(input("enter 1st no."))
q=int(input("enter 2nd no."))
if p > 1:  
   for i in range(2,p):  
       if (p % i) == 0:  
           print(p,"is not a prime number")    
           break  
   else:  
       print(p,"is a prime number")           
if q > 1:  
   for j in range(2,q):  
       if (q % j) == 0:  
           print(q,"is not a prime number")
           break  
   else:  
       print(q,"is a prime number")  
         