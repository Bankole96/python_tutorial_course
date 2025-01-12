#!/usr/bin/python3

greeting = "hello world"

print(greeting)

greeting = greeting[:6] + "john"

print("updated string = ", greeting)

greeting = greeting[0:0] + "y" + greeting[1:]

print("updated string = ", greeting)

greeting = greeting[0:1] + "a" + greeting[2:]
print(greeting)

greeting = greeting[0:7] + "e" + greeting[8:]
print(greeting)


