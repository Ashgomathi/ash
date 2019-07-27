v1,v2=map(str,input().split())
v3=0
if len(v1)>len(v2):
  v1,v2=v2,v1
r=0
while r<len(v1):
  v3+=(ord(v2[r])-ord(v1[r]))
  r+=1
for r in range(r,len(v2)):
  v3+=ord(v2[r])-ord('a')+1
print(v3)
