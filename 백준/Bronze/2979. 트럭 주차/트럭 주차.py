A,B,C = map(int,input().split())
hours = [0]*101

for _ in range(3):
    time1,time2 = map(int,input().split())
    for i in range(time1,time2):
        hours[i] += 1

result = 0
for i in hours:
    if i == 3:
       result += C*3
    elif i == 2:
        result += B*2
    elif i == 1:
        result += A*1

print(result)
