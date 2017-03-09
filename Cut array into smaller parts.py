'''Write function makeParts that will take
an array as argument and the size of the chunk.
Example: if an array of size 123 is given and
 chunk size is 10 there will be 13 parts,
 12 of size 10 and 1 of size 3.'''

def makeParts(arr, chunkSize):
    y = list(map(lambda a: arr[chunkSize * a:(a + 1) * chunkSize], range(len(arr))))
    return list(filter(([]).__ne__, y))

'''also we can do : return [ arr[i: i + csize] for i in range(0, len(arr), csize)]'''