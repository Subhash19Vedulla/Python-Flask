def prime(n):
    if n>1:
        for i in range(2,n):
            if (n%i==0):
                print("Not Prime")
            else:
                print("{} is prime".format(n))

n = int(input())
prime(n)