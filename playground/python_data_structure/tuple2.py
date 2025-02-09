#!/usr/bin/python3

continent = ("asia", "africa", "america", "europe", "australia")

print("continent[0]", continent[0])

print("continent[2:]", continent[2:])

print("continent[:-3]", continent[:-3])

#updating tuple

continent2 = ("north america",)

all_continent = continent + continent2

print(all_continent)

#deleting tuple element

all_continent = ("asia", "america", "australia")

empty_tuple = ()

empty_tuple = all_continent

print(empty_tuple)
