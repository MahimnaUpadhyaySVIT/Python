''' 
    It is powerful and expressive way to modify or enhance the
    behavior of functions or methods. They provide concise 
    syntax for wrapping function with additional functionality
    such as logging, access control or instrumentation without
    directly altering the original functions code.

    It essentially takes another function as a input, adds some
    functionality to it, and returns the modified function.
'''

def decorator(FunctionAsArugment):
    def wrapperFunction():
        print("Before the FunctionAsArugment is called")
        FunctionAsArugment()
        print("After the FunctionAsArugment is called")
    return wrapperFunction

@decorator
def decoratorFunction():
    print("Hello")

decoratorFunction()
