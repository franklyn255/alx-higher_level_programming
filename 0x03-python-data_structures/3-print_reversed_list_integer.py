#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
	lg = len(my_list) - 1
	for i in my_list:
		print("{}".format(my_list[lg]))
		lg -= 1
