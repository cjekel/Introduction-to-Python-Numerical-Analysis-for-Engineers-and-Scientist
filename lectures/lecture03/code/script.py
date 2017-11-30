#   import my_simple_library.py as msl
import my_simple_library as msl

# access a class within my library
a = msl.my_simple_class()

#  access an instance of this class function
a.my_class_function()

#   outside functions in the library that are outside of the class
msl.function_outside_class()
msl.another_function_outside()
