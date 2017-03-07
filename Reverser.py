'''Impliment the reverse function, which takes in input n and reverses it.
 For instance, reverse(123) should return 321.
 You should do this without converting the inputted number into a string.'''


def reverse(n):
    reversed = ''
    while n > 0:
        n, y = divmod(n, 10)
        reversed += str(y)
    return int(reversed)


