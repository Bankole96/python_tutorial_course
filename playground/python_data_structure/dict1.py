#!/usr/bin/python3

empty_dict = {}

integerkey_dict = {1:"mango", 2:"apple", 3:"orange"}

mixedkey_dict = {"name":"phillins", 0:[2, 4, 3]}

print(integerkey_dict)

print(mixedkey_dict)

print(", ".join(map(str, integerkey_dict)))

