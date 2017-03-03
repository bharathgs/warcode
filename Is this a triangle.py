"""Implement a method that accepts 3 integer values a, b, c.
The method should return true if a triangle can be built with
the sides of given length and false in any other case.
(In this case, all triangles must have surface greater than 0 to be accepted)."""


def is_this_a_triangle(a, b, c):
    if (a + b > c) and (b + c > a) and (c + a > b):
        print("Yes these sides can form a triangle")
    else:
        print("These sides do not make a triangle")


