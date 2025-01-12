#!/usr/bin/python3

x, y, z, f = 27, 10, -9, 4

a = x + y 
print("when you add x and y you get", a)

b = x - y
print("when you subtract y from x you get", b)

c = x * y
print("when you multiply x and y you get", c)

d = x / z
print("when you divide x by z you get", d)

e = x % y
print(e, "is the remainder when x is divide by y")

g = x ** f
print("x to the power of f is", g)

h = x // y
print("the floor division value of x divided by y is", h)

if (x == y) :
    print("1. x is equal to y")
else :
    print("1. x is not equal to y")

if (x != y) :
    print("2. x is not equal to y")
else :
    print("2. x is equal to y")

if (x < y) :
    print("3. x is less than y")
else :
    print("3. x is not less than y")

if (x > y) :
    print("4. x is greater than y")
else :
    print("4. x is not greater than y")

if (x <= y) :
    print("5. x is either less than or equal to y")
else :
    print("5. x is neither less than nor equal to y")

if (x >= y) :
    print("6. x is either greater than or equal to y")
else :
    print("6. x is neither greater than nor equal to y")


z = x + y
print("1. value of z is", z)

z += x
print("2. value of z is", z)

z *= x
print("3. value of z is", z)

z /= x
print("4. value of z is", z)

z %= x
print("5. value of z is", z)

z **= x
print("6. value of z is", z)

z //= x
print("7. value of z is", z)




