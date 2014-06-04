"""
calculator.py

Using our arithmetic.py file from Exercise02, create the
calculator program yourself in this file.
"""
#def open_file():
    #arithmetic = open("arithmetic.py")



def main():
    #arithmetic = open("arithmetic.py")
	# open the file from arithmetic.py
    #my_file = open("arithmetic.py")
    # get input from user
    math_input = raw_input("> ")
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
        from arithmetic import add(num1,num2)
        print add(num1,num2)
    elif character == "-":
        print subtract(num1,num2)
    elif character == "*":
        print multiply(num1,num2)
    elif character == "/":
        print divide(num1,num2)
    elif character == "square":
        print square(num1)
    elif character == "cube":
        print cube(num1)
    elif character == "pow":
        print power(num1,num2)
    elif character == "mod":
        print mod(num1,num2)




    #math_int = int(math_input)


#    word[0] = character + - /
#    word[1] = num1
#    word[2] = num2


if __name__ == '__main__':
    main()
