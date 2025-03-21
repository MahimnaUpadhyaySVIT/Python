''' 
    In python we pass the object reference not the value or reference. 
    Depending on the type of the object you pass in the function, the
    function behaves differently.

    Immutable objects show "pass by value" whereas Mutable objects show
    "pass by reference"
'''

def PassByValue(x):
    x*=2
    print("Value of X updated ", x)
    return

def PassByReference(list):
    list.append("D")
    print("Value of list updated ", list)
    return

my_list = ["A", "B", "C"]
my_num = 5

print("Number before PassByValue function " , my_num)
PassByValue(my_num)

print("List before PassByReference function " , my_list)
PassByReference(my_list)
