def is_prime(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        sum_result = func(*args)
        k = 0
        for i in range(2, sum_result // 2 + 1):
            if sum_result % i == 0:
                k = k + 1
        if k <= 0:
            print('Простое')
        else:
            print('Составное')
        return result

    return wrapper


@is_prime
def sum_three(*args):
    sum_result = sum(args)
    return sum_result


result = sum_three(2,3,6)
print(result)