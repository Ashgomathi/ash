
sam=input()
for i in range(0,len(sam)):
   if(sam[i].isalpha() and sam[i].isdigit()):
    print("No")
else:
  print("Yes")
