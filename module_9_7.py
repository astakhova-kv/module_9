def is_prime(func):
    def wrapper(*args):
        origin_result = func(*args)
        count = 0
        for i in range(2, origin_result):
            if origin_result % i == 0:
                count += 1
        if count > 0:
            print('Составное')
        else:
            print('Простое')
        return origin_result

    return wrapper


@is_prime
def sum_three(*args):
    return sum(args)


result = sum_three(2, 3, 7)
print(result)
