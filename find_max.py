def find_max(value_1, value_2):
    try:
        if value_1 > value_2:
            return value_1
        elif value_1 == value_2:
            print('the values are equivalent')
        else:
            return value_2
    except ValueError:
        print('values should be integers and/or floats')

if __name__ == "__main__":
    while True:
        value_1 = int(input('enter your first value: '))
        value_2 = int(input('enter your second value: '))
        output = find_max(value_1, value_2)
        print(f'max value\t{output}')
       
        advance = str(input('type (y)es to continue of (n)o to exit: '))
        if advance == 'y':
            print('---enter another set of values ---')
            pass
        else:
            print('--- goodbye ---')
            break
