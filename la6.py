che=input()
set=0
for i in range(len(che)):
  if(che[i].isdigit() or che[i].isalpha() or che[i]==(" ")):
    continue
  else:
    set+=1
print(set)

