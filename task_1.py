
def factorial(fact):
    int(fact)
    n = 1
    for i in range(1, fact+1):
        n *= i
    a = 1
    l=[]
    for x in range(1, n +1):
            a *= x
            l.append(a)
    l.reverse()
    print(f'Ответ: {l}')
    print('Для выхода не вводите не чего и нажмите Enter')

while True:
    inp = int(input('Введите число: '))
    factorial(inp)
    if not inp:
         exit()
