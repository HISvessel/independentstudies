#!/usr/bin/python3

def is_a_palindrome(input):
    """this function analyzes the input given
    in order to determine that it is or not a palindrome
    
    A palindrome is a word, phrase or number that is read exactly the same
    in forward and reverse. This method converts the input to a string
    and reverses the string.
    
    A harder version of the challenge would be to analize if it is a palindrome
    without converting it to a string."""
    x = str(input)
    palindrome = x[::-1]
    if palindrome == x:
        return True
    else:
        return False

input = 10
palindrome = is_a_palindrome(input)
print(palindrome)