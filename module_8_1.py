def add_everything_up(a, b):
    try:
        a + b
    except TypeError as err:
        return f'{str(a)}{str(b)}'
    else:
        if type(a) and type(b) is int or float:
            return a + b
    finally:
        if type(a) is int and type(b) is str:
            print(f'Если очень хочется можно сложить число и строку, результат: {a + len(b)}')
        elif type(a) is str and type(b) is int:
            print(f'Если очень хочется можно сложить число и строку, результат: {len(a)+b}')


print(add_everything_up(123.456, 'строка'))
print(add_everything_up('яблоко', 4215))
print(add_everything_up(123.456, 7))