# initial, very rough recursive solution
def dirReduce(arr):
    NS = set(['NORTH', 'SOUTH'])
    WE = set(['EAST', 'WEST'])
    for i in range(len(arr) - 1):
        comp = set([arr[i], arr[i+1]])
        if comp == NS or comp == WE:
            del arr[i:i+2]
            return dirReduce(arr)

    return arr

print(dirReduce(["NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH", "WEST"]))
