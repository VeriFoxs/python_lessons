# def pripev():
#     print('припев 1')
#     print('припев 2')
#     print('припев 3')
#     print('припев 4')

# print('куплет 1')
# pripev()
# print('куплет 2')
# pripev()
# print('куплет 3')
# pripev()

def summa(a, b):
    s = a+b
    print(f'Сумма числа {a} и числа {b} равна {s}')

summa(28,563)


def cool_summa(*args):
    s = 0
    text = 'Сумма чисел'
    
    for digit in args:
        s += digit
        text += f' {digit}'
    
    text += f' равна {s}'
    print(text)

cool_summa(2,34,876,5,56,47,1259)

