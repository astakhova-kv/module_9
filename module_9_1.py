def apply_all_func(int_list, *functions):
    results = dict()
    try:
        for func in functions:
            results[func.__name__] = func(int_list)
        return results
    except TypeError:
        return 'Используйте список чисел'

print(apply_all_func([6, 'gh', 15, 9], max, min))
print(apply_all_func([6, 20, 15, 9], len, sum, sorted))
