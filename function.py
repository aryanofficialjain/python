import math
def square(num):
    return num**2

def SUM(num1, num2):
    return num1+num2

def AreaCum(radius):
    area = math.pi * radius ** 2
    cum  = 2 * math.pi * radius 

    return area, cum


area, cum = AreaCum(10);
print(area, cum);

print(square(34));
print(SUM(10,10));


cube = lambda x: x **3;

print(cube(3));


def agruments(*args):
    return sum(args)


print(agruments(1,2,3,4,))


def Kwargs(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")


Kwargs(name="Hello", surname="World", planet="Earth");

