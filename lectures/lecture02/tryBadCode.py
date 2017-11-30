try:
    print('let us try some code to break the Python syntax')
    x = 0
    x/x
except e:
    print('The code that I tried broke. Here is my error message')
    print(repr(e))
    
