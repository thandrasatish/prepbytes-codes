for _ in range(int(input())):
  n = int(input())
  print(n,end=" ")
  while(n!=1):
      if(n%2 == 0):
        n = int(n**(1/2))
        print(n,end = " ")
  
      else:
        n = int(n**(3/2))
        print(n,end = " ")
  
  print("")
