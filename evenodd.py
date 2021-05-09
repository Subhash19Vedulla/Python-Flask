a = [121, 122, 123, 124, 125]
even_count = 0
odd_count = 0
for i in a:
    if i % 2 == 0:
        even_count += 1
    else:
        odd_count += 1

print("Even Count:",even_count)
print('Odd Count:',odd_count)
