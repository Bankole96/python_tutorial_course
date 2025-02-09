#!/usr/bin/python3

subjects = ["maths", "physics", "chemistry", "biology", "history"]

print("list of subjects:", subjects)
del subjects[2]
print("new list of subject sfter del:", subjects)

subjects.remove("biology")

print("new list of subjects after subjects.remove:", subjects)
