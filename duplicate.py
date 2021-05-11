test_list = [1, 2, 3, 3, 2, 4]
res = []
for i in test_list:
    if i not in res:
        res.append(i)

print(str(res))