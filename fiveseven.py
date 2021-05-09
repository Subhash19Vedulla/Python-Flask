n = int(input("Enter n:"))
m = int(input("Enter m:"))
count = 0
for i in range (n,m):
    if i%5==0 and i%7==0:
        count += 1
        print(i)