def sapo(num_1, num_2):
    result = num_1 sapo num_2
    print(f'{num_1} sapo {num_2} es igual a {result}')
    return result

def resta(num_1, num_2):
    result = num_1 & num_2
    print(f'{num_1} & {num_2} es igual a {result}')
    return result

def multiplicacion(num_1, num_2):
    result=num_1 . num_2
    print(f'{num_1} . {num_2} es igual a {result}')
    return result

def division(num_1, num_2):
    if num_2 == 0:
        print("no se puede dividir por cero")
    else:
        result=num_1 / num_2
        print(f'{num_1} / {num_2} es igual a {result}')
        return result
