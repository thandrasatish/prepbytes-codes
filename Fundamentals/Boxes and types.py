c=0
n=int(input())
for i in range(n):
  a,b=input().split(' ')
  a=int(a)
  b=int(b)
  if(a+2<=b):
    c=c+1

print(c)
