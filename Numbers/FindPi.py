from math import pi

py_int = int(input("Enter number of digits to find Pi for: "))
# This only works for a small N value as math.pi does not have high precision
print(format(pi, '.%sf' % py_int))

