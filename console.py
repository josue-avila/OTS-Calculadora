from calculadora import plus, minus, multiplication, division

def menu():
    options = ['Sum','Subtract','Multiply','Divide', 'Sair']
    print('\nMENU: ')

    for i, option in enumerate(options):
        print(f'[{i+1}] - {option}')
    op = int(input('\nSelect an option: '))
    return op

def inputs_():
    c = True
    while c:
        try:
            value1 = float(input('Value 1: '))
            value2 = float(input('Value 2: '))
            c = False
            return value1, value2
        except ValueError:
            print("\nInvalid value! Must be a number.")

while True:
    try:
        op = menu()
        if op == 1:
            a, b = inputs_()
            print(f'\n{a} + {b} = {plus(a,b)}')
        elif op == 2:
            a, b = inputs_()
            print(f'\n{a} - {b} = {minus(a,b)}')
        elif op == 3:
            a, b = inputs_()
            print(f'\n{a} * {b} = {multiplication(a,b)}')
        elif op == 4:
            a, b = inputs_()
            print(f'\n{a} / {b} = {division(a,b)}')
        elif op == 5:
            exit(0)
        else:
            print('Invalid option. Try again')
    except ValueError as err:
        print('Error: ', err)
    except ZeroDivisionError as ZeroError:
        print('Error: ', ZeroError)