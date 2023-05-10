#!/usr/bin/python3
def fizzbuzz():
    for n in range(1, 101):
        if n % 3 == 0 and n % 5 == 0:
            print("FuzzBuzz", end=" ")
        elif n % 3 == 0:
            print("Fuzz", end=" ")
        elif n % 5 == 0:
            print("Buzz", end=" ")
        else:
            print(n, end=" ")
