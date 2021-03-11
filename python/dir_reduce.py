# recursive solution
def dirReduce(arr):
    pairs = [set(['NORTH', 'SOUTH']), set(['EAST', 'WEST'])]
    for i in range(len(arr) - 1):
        if set(arr[i:i+2]) in pairs:
            del arr[i:i+2]
            return dirReduce(arr)

    return arr

print(dirReduce(["NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH", "WEST"]))
