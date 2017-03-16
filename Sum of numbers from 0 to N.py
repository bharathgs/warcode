'''We want to generate a function that computes the series starting
from 0 and ending until the given number following the sequence:
0 1 3 6 10 15 21 28 36 45 55 ....
which is created by
0, 0+1, 0+1+2, 0+1+2+3, 0+1+2+3+4, 0+1+2+3+4+5, 0+1+2+3+4+5+6, 0+1+2+3+4+5+6+7 etc..'''

def show_sequence(n):
    if n>0:
        l = list(range(0, n + 1))
        x = sum(l)
        sequence = ''
        for i in l:
            sequence += str(i)
        return '{} = {}'.format(sequence, x)
    if n==0:
        return '0=0'
    else:
        return '{}<0'.format(n)



print(show_sequence(6))

li_str = ''
for i in list(range(0, 7)):
    li_str += str(i)
print(li_str)
