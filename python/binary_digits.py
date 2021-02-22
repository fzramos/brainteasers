# Create a code that encodes a string of numbers into binarY BY DIGIT

def to_binary(n):
    result = ''
    while n > 0:
        result += str(n%2)
        n = n//2
    return result.zfill(4)

# binary by DIGIT! 
def code(strng):
    coded = ''
    for i in strng:
        coded += to_binary(int(i))
    return coded
              
def decode(strng):
    decoded = ''
    for i in strng:
        sum = 0
        for i in range(1,5):
            sum += strng[-i] * (2 ** (i-1))
        decoded += str(sum)
    return decoded   