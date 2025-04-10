# Sum Mixed Array
def sum_mix(arr):
    return sum(map(int, arr))

# Example usage:
# sum_mix([1, '2', 3, '4', 5])  # Output: 15
# sum_mix([1, 2, 3])            # Output: 6

# Exclamation Marks Series #2: Remove All Exclamation Marks from the End of Sentence
def remove(st):
    return st.rstrip('!')

# Example usage:
# remove("Hello!")  # Output: "Hello"
# remove("Hello")   # Output: "Hello"

# List Filtering: Filter out non-integer elements from the list
def filter_list(l):
    return [i for i in l if type(i) == int]

# Example usage:
# filter_list([1, '2', 3, 'a', 4])  # Output: [1, 3, 4]


# You Can't Code Under Pressure #1: Double the integer
def double_integer(i):
    return i * 2

# Example usage:
# double_integer(3)  # Output: 6



# Basic Mathematical Operations
def basic_op(operator, value1, value2):
    if operator == '+':
        return value1 + value2
    elif operator == '-':
        return value1 - value2
    elif operator == '*':
        return value1 * value2
    elif operator == '/':
        return value1 / value2

# Example usage:
# basic_op('+', 3, 5)   # Output: 8
# basic_op('-', 10, 4)  # Output: 6



# Beginner - Lost Without a Map: Multiply each element by 2
def maps(a):
    return [x * 2 for x in a]

# Example usage:
# maps([1, 2, 3])  # Output: [2, 4, 6]


# Convert a Number to a String!
def number_to_string(num):
    return str(num)

# Example usage:
# number_to_string(5)  # Output: "5"



# Is He Gonna Survive? (Check if bullets are enough to defeat dragons)
def hero(bullets, dragons):
    return bullets >= 2 * dragons

# Example usage:
# hero(10, 5)  # Output: True
# hero(5, 3)   # Output: False


# DNA to RNA Conversion: Replace 'T' with 'U'
def dna_to_rna(dna):
    return dna.replace("T", "U")

# Example usage:
# dna_to_rna("ATTGC")  # Output: "AUUGC"


# Grasshopper - Basic Function Fixer: Add 5 to a number
def add_five(num):
    return num + 5

# Example usage:
# add_five(3)  # Output: 8



# Remove First and Last Character: Remove first and last character of a string
def remove_char(s):
    return s[1:-1]

# Example usage:
# remove_char("hello")  # Output: "ell"


# Convert a Boolean to a String
def boolean_to_string(b):
    return str(b)

# Example usage:
# boolean_to_string(True)  # Output: "True"
# boolean_to_string(False) # Output: "False"


# Convert a String to a Number!
def string_to_number(s):
    return int(s)

# Example usage:
# string_to_number("123")  # Output: 123
