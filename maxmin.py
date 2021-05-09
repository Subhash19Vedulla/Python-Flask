a=[8, 1, 7, 10, 5]
min_ele = a[0]
max_ele= a[0]
for i in range(1, len(a)):
    if a[i]<min_ele:
        min_ele=a[i]
    if a[i]>max_ele:
        max_ele=a[i]
print(min_ele)
print(max_ele)
