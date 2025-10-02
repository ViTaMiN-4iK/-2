def find_primes(limit):
    if limit < 2:
        return "Нет простых чисел"
    
    is_prime = [True] * (limit + 1)
    is_prime[0] = is_prime[1] = False
    
    for current_num in range(2, int(limit ** 0.5) + 1):
        if is_prime[current_num]:
            for multiple in range(current_num * current_num, limit + 1, current_num):
                is_prime[multiple] = False
    
    primes = [num for num in range(2, limit + 1) if is_prime[num]]
    
    return primes

limit = 100
primes = find_primes(limit)
    
print(f"Простые числа до {limit}:")
print(primes)
    