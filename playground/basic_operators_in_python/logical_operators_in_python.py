#!/usr/bin/python3

x = True
y = False

print("when x is True and y is False")

print("x and y is", x and y)

print("x or y is", x or y)

print("not x is", not x)

print("not y is", not y)


#first code example:
#table of the AND operator
#
#      AND OPERATOR
#  0  AND  0  = 0   false  and  false  = false      off and off = off
#  1  and  0  = 0   true   and  false  = false      on  and off = off
#  0  and  1  = 0   false  and  true   = false      off and on  = off
#  1  and  1  = 1   true   and  true   = true       on  and on  = on


#second code example:
#table of OR operator
#
#     OR OPERATOR
#  0  or  0 = 0     false  or  false  = false    off  or  off = off
#  1  or  0 = 1     true   or  false  = true     on   or  off = on
#  0  or  1 = 1     false  or  true   = true     off  or  on  = on
#  1  or  1 = 1     true   or  true   = true     on   or  on  = on


#third code example:
#table of NOT operator
#
#     NOT OPERATOR
#  0 = 1    false = true    off = on
#  1 = 0    true  = false   on  = off

