v1=int(input())
v2=[]
for h in range(0,v1):
 pan=input()
 v2.append(pan)
v3=[]
for h in zip(*v2):
 if(h.count(h[0])==len(h)):
  v3.append(h[0])
 else:
  break
print(''.join(v3))
