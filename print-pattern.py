n = int(input("Enter a number: "))
for i in range(n):
        s = ''
        for j in range(i+1):
            s = s + '*'
        print(s)