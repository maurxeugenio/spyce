def fat(n):
    if n < 2:
        return 1
    else:
        return n * fat(n-1)
        
n = int(input('N: '))
print(fat(n))
