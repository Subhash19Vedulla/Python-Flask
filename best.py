a = "python programming language is best programming language"
for i in range(len(a)):
    end_value = '-'

    if a[i] == ' ' or i==len(a)-1 or a[i+1]= ' ':
        end_value= ''

    if i%2==0:
        print(a[i].upper(),end = end_value)
    else:
        print(a[i],end = end_value)

print()
