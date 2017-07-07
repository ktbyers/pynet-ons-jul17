#!/usr/bin/env python
from __future__ import print_function

try:
    # PY2
    num1 = int(raw_input("Enter first number: "))
    num2 = int(raw_input("Enter second number: "))
except NameError:
    # PY3
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))

print("\n\nSum: {}".format(num1 + num2))
print("Difference: {}".format(num1 - num2))
print("Product: {}".format(num1 * num2))
print("Division: {:.2f}".format(num1/float(num2)))

print()
