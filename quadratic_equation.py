import math

def equationroots(a, b, c):
    dis = b * b - 4 * a * c
    sqrt_val = math.sqrt(abs(dis))
    
    if dis > 0:
        print("Real and different roots")
        print((-b + sqrt_val) / (2 * a))
        print((-b - sqrt_val) / (2 * a))
    
    elif dis == 0:
        print("Real and same roots")
        print(-b / (2 * a))
    
    else:
        print("Complex Roots")
        real_part = -b / (2 * a)
        imaginary_part = sqrt_val / (2 * a)
        print(f"{real_part} + {imaginary_part}i")
        print(f"{real_part} - {imaginary_part}i")

a = int(input("Enter a: "))
b = int(input("Enter b: "))
c = int(input("Enter c: "))

if a == 0:
    print("Input correct quadratic equation")

else:
    equationroots(a, b, c)
