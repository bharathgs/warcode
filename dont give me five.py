''''''

x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

def dont_give_me_five(start, end):
    return sum('5' not in str(i) for i in range(start, end + 1))