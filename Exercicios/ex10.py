"""
-Fizz Buzz- Se o parametro da função for dividivel por 3, retorne fizz,
se o parametro da função for divisivel por 5 e por 3, retorne fizz buzz
caso contrario retorne numero enviado
"""
def fb(num):

    if num % 5 == 0 and num % 3 == 0:
        return 'Fizz buzz'
    if num % 5 == 0:
        return 'fizz'
    if num % 3 == 0:
        return 'buzz'

    return num


fizzbuzz = fb(50)
print(fizzbuzz)