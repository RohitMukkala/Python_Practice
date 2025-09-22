import math

def circle_calc(radius):
    area = math.pi * (radius ** 2)
    circumference = 2 * math.pi * radius
    diameter = 2 * radius
    return area, circumference, diameter

if __name__ == "__main__":
    try:
        r = float(input("Enter a radius: "))
        area, c, d = circle_calc(r)
        print(f"Area: {area:.2f}, Circumference: {c:.2f}, Diameter: {d:.2f}")
    except ValueError:
        print("Invalid input. Please enter a numeric value for the radius.")
