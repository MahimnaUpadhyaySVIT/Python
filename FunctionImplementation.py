''' Default Arugments means a argument which has a default value. Example dept has default value of MCA '''

def defaultArugments(name, dept="MCA"):
    print("Your good name " + name)
    print("You are from " + dept)

defaultArugments('Mahimna')

''' Positional Arguments means the order of arugment value should be same as order of arguments in function '''

def positionalArugments(name, age):
    print("Your good name " , name , "and you are " , age , " years old")

positionalArugments('Mahimna', 21)

''' Keyword Arugments means we can specify argument name along with its value '''

def keywordArugments(happy, alone):
    print("Are you happy? " , happy)
    print("So you are lonely " , alone)

keywordArugments(happy=False, alone=True)

''' 
    Variable Length Arguments means arguments that can accept n number of data as a input two type
    1. *args (can pass n number of arguments) 
    2. **kwargs (can pass n number of keyword arguments)
'''

def argsArugment(*students):
    print("Highest marks goes to " + students[1])

argsArugment('Mahimna', 'Ved', 'Abhi', 'Dhruv')

def kwargsArugment(**students):
    print("Top student last name " , students[lname])

kwargsArugment(fname = 'Ved', lname = "Patel")
