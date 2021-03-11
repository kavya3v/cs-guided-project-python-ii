"""
Challenge #9:

Given a string, write a function that returns the "middle" character of the
word.

If the word has an odd length, return the single middle character. If the word
has an even length, return the middle two characters.

Examples:
- get_middle("test") -> "es"
- get_middle("testing") -> "t"
- get_middle("middle") -> "dd"
- get_middle("A") -> "A"
"""
def get_middle(input_str):
    # Your code here
    mid=len(input_str)%2
    if(mid==0): #even so return two middle char
        return input_str[(int(len(input_str)/2)-1):(int(len(input_str)/2))+1]
    return input_str[int(len(input_str)/2)]

print(get_middle("test"))
print(get_middle("testing"))
print(get_middle("middle"))
print(get_middle("A"))
