hello=int(input())
v1,v2=0,1
print(v2,end=" ")
for i in range(1,hello):
 v3=v1+v2
 print(v3,end=" ")
 v1,v2=v2,v3
