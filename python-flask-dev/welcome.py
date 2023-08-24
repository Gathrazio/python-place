'''
this module is a practice python module
'''

# naming convention for files and functions: this_is_a_file_or_function
# naming convention for classes: CamelCase with first word capitalized; class ThisClassIsAClass
# naming convention for constants: SCREAMING_SNAKE_CASE; ex. MAX_FILE_UPLOAD_SIZE
# use four spaces for indentation
# use functions for blocks of code

from mypackage.module1 import square, doubler
from mypackage import module2

print("4^2 =", square(4))
print("2 * 4 =", doubler(4))
print("(2 + 1 + 3) / 3 =", module2.mean([2, 1, 3]))
