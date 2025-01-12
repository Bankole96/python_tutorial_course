#!/usr/bin/python3

#using default order

student1 = "{}, {} and {}".format("phillins", "bankole", "pen")
print("\n\nstudent by default order")
print(student1)

#using positional argument

student2 = "{1}, {0} and {2}".format("phillins", "bankole", "pen")
print("\n\nstudent by positional order")
print(student2)

#using keywords argument

student3 = "{e}, {p} and {b}".format(p="phillins", b="bankole", e="pen")
print("\n\nstudent by keywords order")
print(student3)
