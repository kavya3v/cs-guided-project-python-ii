import datetime

"""
Challenge #5:

Create a function that returns the data type of a given argument. There are
seven data types this challenge will be testing for:

- List
- Dictionary
- String
- Integer
- Float
- Boolean
- Date

Examples:
- data_type([1, 2, 3, 4]) ➞ "list"
- data_type({'key': "value"}) ➞ "dictionary"
- data_type("This is an example string.") ➞ "string"
- data_type(datetime.date(2018,1,1)) ➞ "date" 

Notes:
- Return the name of the data type as a lowercase string.
"""
def data_type(value):
    # Your code here
    return type(value).__name__ # get the name of the object

print(data_type([1, 2, 3, 4]))
print(data_type({'key': "value"}))
print(data_type("This is an example string."))
print(data_type(datetime.date(2018,1,1))) 

