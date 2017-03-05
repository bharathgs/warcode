"""Sum all the numbers of the array (in F# and Haskell you get a list)
except the highest and the lowest element (the value, not the index!).
(The highest/lowest element is respectively only one element at each edge,
 even if there are more than one with the same value!)"""

def sum_array(arr):
    if arr == None or len(arr) < 3:
        return 0
    else:
        return sum(sorted(arr)[1:-1])



