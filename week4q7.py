n = int(input("Enter an amount: "))
count = 0

while n > 0:
    if n >= 500:
        count += n // 500
        n = n % 500
    elif n >= 100:
        count += n // 100
        n = n % 100
    elif n >= 50:
        count += n // 50
        n = n % 50
    elif n >= 20:
        count += n // 20
        n = n % 20
    elif n >= 10:
        count += n // 10
        n = n % 10
    elif n >= 5:
        count += n // 5
        n = n % 5
    elif n >= 2:
        count += n // 2
        n = n % 2
    elif n >= 1:
        count += n // 1
        n = n % 1

print("Total number of notes:", count)
