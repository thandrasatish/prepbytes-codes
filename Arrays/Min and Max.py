for _ in range(int(input())):
  n = int(input())
  val = list(map(int,input().split()))
  val.sort()
  print(val[0],end= " ")
  print(val[-1])
