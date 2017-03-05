"""In this little assignment you are given a string of space separated numbers,
and have to return the highest and lowest number."""

def high_and_low(numbers):
    number_list = [int(i) for i in numbers.split(" ")]
    return "{} {}".format(max(number_list), min(number_list))
