"""
Challenge #10:

Given a string of space separated integers, write a function that returns the
maximum and minimum integers.

Example:
- max_and_min("1 2 3 4 5") -> "5 1"
- max_and_min("1 2 -3 4 5") -> "5 -3"
- max_and_min("1 9 3 4 -5") -> "9 -5"

Notes:
- All inputs are valid integers.
- There will always be at least one number in the input string.
- The return string must be two numbers separated by a single space, and
the maximum number is first.
"""
def max_and_min(input_str):
    # Your code here
    # maxS=max(input_str)
    # minS=min((input_str.split()))
    # return "{} {}".format(maxS,minS)
    # new_str=input_str.split(" ")
    # #convert to array of integers
    # print(new_str)
    # nums = list(map(int,new_str)) # to be iterable
    # print(nums)
    nums=[int(item) for item in input_str.split(' ')] # int function on the item is what gets added to the list
    return f'{max(nums)} {min(nums)}'


print(max_and_min("1 2 3 4 5"))
print(max_and_min("1 2 -3 4 5"))
print(max_and_min("1 9 3 4 -5"))

