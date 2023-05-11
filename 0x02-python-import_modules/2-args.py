#!/usr/bin/python3

import sys

arg = sys.argv[1:]
num_arg = len(arg)
a = 1

if num_arg > 0:
	print("{} arguments:".format(num_arg))
else:
	print("{} arguments.".format(num_arg))
for i in range(num_arg):
	print("{}: {}".format(a, arg[i]))
	a += 1
