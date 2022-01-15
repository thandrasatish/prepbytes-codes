n=int(input())
for i in range(n):
  a,b=input().split(' ')
  a=int(a)
  b=int(b)
  if(a>100):
    p=a*b-0.2*a*b
    print(float(p))
  else:
    print(float(a*b))
