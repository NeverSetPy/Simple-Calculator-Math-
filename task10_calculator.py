# Functions for each equation operator, with f strings to display calculations to user.
# All lopps embedded in outer loop.
# Loop 1 - Takes num values for calculation. Once both numbers taken, moves to next loop.
# Loop 2 - Asks equation operator, calls respective function to calculate according to chosen operator. 
# Then creates and writes to a file called 'my_equations.txt'.
# Loop 3 - Gives user option to read written equations from the text file, or to enter more equations or to Quit programme.


def add(x, y):
    total = x + y
    return ('{} + {} = {}'.format(x, y, total))

def subtract(a, b, ):
    total = a - b
    return ('{} - {} = {}'.format(a, b, total))

def divide(c, d):
    total = c / d
    return ('{} / {} = {}'.format(c, d, total))

def multiply(e, f):
    total = e * f
    return ('{} * {} = {}'.format(e, f, total))

programme = True

while programme:
    while True:
        try:
            num_1 = (float(input('Enter first number:')))
        except ValueError:
            print('Enter a number.')
            continue
        try:
            num_2 = (float(input('Enter second number:')))
        except ValueError:
            print('Enter a number.')
            continue
        if num_1 and num_2:
            break

    while True:
        
        equation_operator = input('Do you want to add \'+\', subtract\'-\' multiply \'*\' or divide \'/\'?:\n')
        if equation_operator == '+':
            e_1 = add(num_1, num_2)
            with open('my_equations.txt', 'a') as f: 
                f.write(str(e_1) + '\n')
                print(e_1)
                break
        elif equation_operator == '-':
            e_2 = subtract(num_1, num_2)
            with open('my_equations.txt', 'a') as f: 
                f.write(str(e_2) + '\n')
                print(e_2)
                break
        elif equation_operator == '/':
            try:
                e_3 = divide(num_1, num_2)
                with open('my_equations.txt', 'a') as f: 
                    f.write(str(e_3) + '\n')
                    print(e_3)
                    break
            except ZeroDivisionError:
                print('Can\'t divide by zero try again.')
        elif equation_operator == '*':
            e_4 = multiply(num_1, num_2)
            with open('my_equations.txt', 'a') as f:
                (f.write(str(e_4)))
                print(e_4)
            break
        else:
                print('Enter an equation operator please.')

    while True:
                        
            question_2 = input('Do you want to view all previous calculations? Y or N (go back and enter more equations) or Q(uit): \n').lower()
                    
            if question_2 == 'y':
                while True:
                    user_input_1 = input('Please enter file name \'my_equations.txt\' \n> ')
                    try:
                            file_1 = open(user_input_1, 'r')
                            read_content = str(file_1.read())
                            print(read_content)  
                            break  
                    except FileNotFoundError:
                            print('File doesn\'t exist. Enter file name.')

            elif question_2 == 'n':
                break
            elif question_2 == 'q':
                print('Goodbye!')
                programme = False
                break
            else:
                print('Enter Y, N or Q please.')