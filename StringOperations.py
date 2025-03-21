print("STRING CONCATENATION")
stringOne = "Mahimna"
stringTwo = "Upadhyay"
stringThree = stringOne + stringTwo
print(stringThree)

print("SLICE OPERATIONS IN STRING") 
print(stringThree[0])
print(stringThree[:])
print(stringThree[:5])
print(stringThree[0:4])
print(stringThree[1:3])

print("REVERSE SLICE OPERATIONS")
print(stringThree[-4:])
print(stringThree[-3:1])
print(stringThree[::-1])

print("STRING REPETATION")
stringFour = "Word"
stringFive = stringFour * 3
print(stringFive)

print("MEMBERSHIP IN STRING")
print('o' in stringFive)

print("LENGTH OF STRING")
print(len(stringThree))

print("COVERT THE CASE IN STRING")
print(stringThree.upper())
print(stringThree.lower())
