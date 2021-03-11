"""
    Here are the conditions:

        Your message is a string containing space separated words.
        You need to encrypt each word in the message using the following rules:
            The first letter needs to be converted to its ASCII code.
            The second letter needs to be switched with the last letter
        Keepin' it simple: There are no special characters in input.

    Examples:

    encrypt_this("Hello") == "72olle"
    encrypt_this("good") == "103doo"
    encrypt_this("hello world") == "104olle 119drlo"
"""

# still working on it
# encrypts but need to work on edge cases
def encrypt_this(text):
    words = text.split()
    coded = []
    # Change this to be map on words 
    for i in words:        
        new_word = str(ord(i[0]))
        new_word += (i[-1])
        new_word += (i[1:-1])
        coded.append(new_word)
    return ' '.join(coded)