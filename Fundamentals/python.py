n=int(input())
for i in range(n):
  m=int(input())
  if(m%4==0 and m%100!=0 or m%400==0):
    print("Yes")
  else:
    print("No")
