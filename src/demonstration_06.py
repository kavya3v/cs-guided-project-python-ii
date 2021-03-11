"""
Challenge #6:

Return the number (count) of vowels in the given string.

We will consider `a, e, i, o, u as vowels for this challenge (but not y).

The input string will only consist of lower case letters and/or spaces.
"""
def get_count(input_str):
    # Your code here
    vowels='aeiou'
    count=0
    for item in input_str.lower():
        if(item in vowels):
            count=count+1
    return count
    lower_str=input_str.lower()


print(get_count("aeiou kavyaa"))

