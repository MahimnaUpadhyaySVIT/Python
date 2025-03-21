''' 
    Lambda function are anonymous function. They can take
    any number of arguments but can only have one expression
'''

add = lambda x, y : x+y
print(add(5,5))

''' 
    In above example I have created one variable name add which
    is using lambda function. It contains 2 arguments i.e. x and y
    but only one argument i.e. x+y
'''

list = [1,2,3,4,5,6,7,8,9,10]

filterData = map(lambda x:x%2==0, list)
print(filterData(list))
