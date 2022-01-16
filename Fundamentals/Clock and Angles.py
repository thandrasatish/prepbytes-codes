testCases=int(input())
for i in range(testCases):
    h, m = map(int,input().split())
    ma=m*6
    ha=(h%12)*30+(m/2)
    angle = abs(ha - ma);
    angle = min(angle, 360 - angle)
    print(int(angle))
