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
    #rray = []
    math_input = raw_input("> ")
    array = []
    array = math_input.split(" ")
    print array

    character = str(array[0])
    num1 = int(array[1])
    if len(array) == 3:
        num2 = int(array[2])
#    elif len(array) == 1:
#        print "Please enter at least one character and one number."
#    else:
#        print "Please only use one character and two numbers."



#    for character in array:

    #pass_stmt = str(array[0])

    if character == "+" or "-" or "*" or "/" or "square" or "cube" or "pow" or "mod":
        if character == "+":
            print arithmetic.add(num1,num2)
            #break
        elif character == "-":
            print arithmetic.subtract(num1,num2)
            #break
        elif character == "*":
            print arithmetic.multiply(num1,num2)
            #break
        elif character == "/":
            print arithmetic.divide(num1,num2)
            #break
        elif character == "square":
            print arithmetic.square(num1)
            #break
        elif character == "cube":
            print arithmetic.cube(num1)
            #break
        elif character == "pow":
            print arithmetic.power(num1,num2)
            #break
        elif character == "mod":
            print arithmetic.mod(num1,num2)
            #break
        else:
            print "Sorry, I do not understand. Please give me a mathematical character for calculation."


    # continue with a while loop for additional numbers
    
    #if pass_stmt == "+" or "-" or "*" or "/" or "square" or "cube" or "pow" or "mod":
    #    return math_functions()
    #else:
    #    print "Sorry, I do not understand. Please try again."

    #condition = True

    # start with calling the add function



    #math_int = int(math_input)


#    word[0] = character + - /
#    word[1] = num1
#    word[2] = num2


if __name__ == '__main__':
    main()
