v1,v2=map(int,input().split())
for num in range(v1+2,v2):
  sum=0
  temp=num
  while temp>0:
    digit=temp%10
    sum+=digit**3
    temp//=10
  if num==sum:
    print(num,ends='')
