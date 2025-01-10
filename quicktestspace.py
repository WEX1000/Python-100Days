def is_prime(num):
    suma = 0
    for i in range(1, num+5):
        if num % i == 0:
            suma += 1
    print(suma)
    if suma == 2:
        print('T')
    else:
        print('F')

is_prime(4)