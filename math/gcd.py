def gcdoftwonumbers(a,b):
    while(a!=b):
        if(a>b):
            a=a-b
        else:
            b=b-a
    return b
    

test=int(input())
for i in range(test):
    a,b=map(int,input().split())
    print(gcdoftwonumbers(a,b))
