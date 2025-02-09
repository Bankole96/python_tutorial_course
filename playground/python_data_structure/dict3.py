#!/usr/bin/python3

student = {"name":"phillins bankole", "age":25, "grade":"b+", "sex":"male"}

print("before update", student)

print("\nchange age to 30:\n add sex key:value pair")

student["age"] = 30

student["sex"] = "female"

print("\nafter update:", student)

print("delete grade entry:")

del student["grade"]

print("after deleting grade:", student)

student.update({"animal":"lion"})

print(student)
