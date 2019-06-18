sum=0
data=[2,4,1,47,38]
for i in range(0,5):
    sum=sum+data[i]
print("sum is",sum)

data=[2,4,6,8]
for i in range(0,len(data)):
    for j in range(i+1,len(data)):
        if(data[i]>data[j]):
            max=data[i]
        else:
            max=data[j]
print("max element is",max)



list=[2,4,6,8]
max=list[0]
for num in list:
    if num>max:
        max=num
print("max element is ",max)

list=[2,4,6,8]
list.sort()
print("max is ",list[-1])


list=[2,4,6,8]
list.sort()
print("min is ",list[0])


list=[2,4,6,8]
min=list[0]
for num in list:
    if num<min:
        min=num
print("min element is ",min)

sum=0
avg=0
data=[2,2,2,2,2]
for i in range(0,len(data)):
    sum=sum+data[i]
avg=sum/len(data)
print('avg is',avg)


data=[2,4,1,47,38]
flag=0
element=int(input("enter the element "))
for i in range(0,len(data)):
    if(element==data[i]):
         flag=1
    else:
         flag=0
if(flag==1):
    print("found")        
else:
    print("not found")      