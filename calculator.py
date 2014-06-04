"""
calculator.py

Using our arithmetic.py file from Exercise02, create the
calculator program yourself in this file.
"""
#def open_file():
    #arithmetic = open("arithmetic.py")

import arithmetic

def main():
    #arithmetic = open("arithmetic.py")
	# open the file from arithmetic.py
    #my_file = open("arithmetic.py")
    # get input from user
    math_input = raw_input("Please input a prefix notation")
    array = []
    array.append(math_input)
    array = math_input.split(" ")
    print array

    character = str(array[0])
    num1 = int(array[1])
    num2 = int(array[2])
    # continue with a while loop for additional numbers

    # start with calling the add function
    if character == "+":
        print arithmetic.add(num1,num2)
    elif character == "-":
        print arithmetic.subtract(num1,num2)
    elif character == "*":
        print arithmetic.multiply(num1,num2)
    elif character == "/":
        print arithmetic.divide(num1,num2)
    elif character == "square":
        print arithmetic.square(num1)
    elif character == "cube":
        print arithmetic.cube(num1)
    elif character == "pow":
        print arithmetic.power(num1,num2)
    elif character == "mod":
        print arithmetic.mod(num1,num2)




    #math_int = int(math_input)


#    word[0] = character + - /
#    word[1] = num1
#    word[2] = num2


if __name__ == '__main__':
    main()
