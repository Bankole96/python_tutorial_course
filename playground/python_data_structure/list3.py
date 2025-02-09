#!/usr/bin/python3

subjects = ["maths", "physics", "chemistry"]
print("list of subject:", subjects)

subjects[2] = "biology"
print("new list of subjects:", subjects)

subjects = ["maths", "physics", "chemistry"]
print("list of subjects:", subjects)

subjects.append("biology")
print("new element of subject:", subjects)
