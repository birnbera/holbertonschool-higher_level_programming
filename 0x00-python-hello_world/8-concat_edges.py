#!/usr/bin/python3
str = "Python is an interpreted, interactive, object-oriented programming\
 language that combines remarkable power with very clear syntax"
str = " ".join([str.split()[i] for i in [5,6,-4,0]])
print(str)
