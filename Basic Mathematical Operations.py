"""Your task is to create a function - basic_op().
The function should take three arguments - operation(string/char),
 value1(number), value2(number).
 The function should return result of numbers after applying the chosen operation."""


def basic_op(operator, value1, value2):
    if operator == '+':
        return value1+value2
    if operator == '-':
        return value1-value2
    if operator == '*':
        return value1*value2
    if operator == '/':
        return value1/value2

'''
can also do this
def basic_op(o, a, b):
    return {'+':a+b,'-':a-b,'*':a*b,'/':a/b}.get(o)'''