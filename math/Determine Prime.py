def isprime(num):
  if(num==1):
    return "No"
  elif(num==2 or num==3):
    return "Yes"
  elif(num%2!=0 and num%3!=0):
    return "Yes"
  else:
    return "No"

test=int(input())
for i in range(test):
  num=int(input())
  print(isprime(num))
  
#but fails at some conditions so it is better to use normal method 
