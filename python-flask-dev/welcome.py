'''
this module is a practice python module
'''

# naming convention for files and functions: this_is_a_file_or_function
# naming convention for classes: CamelCase with first word capitalized; class ThisClassIsAClass
# naming convention for constants: SCREAMING_SNAKE_CASE; ex. MAX_FILE_UPLOAD_SIZE
# use four spaces for indentation
# use functions for blocks of code

def add(number1, number2):
    '''
    adds numbers
    '''
    return number1 + number2

NUM1 = 4

NUM2 = 5

TOTAL = add(NUM1, NUM2)

print(f"The sum of {NUM1} and {NUM2} is {TOTAL}")
