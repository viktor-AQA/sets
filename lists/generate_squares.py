def generate_squares(n):
    results = list()
    i = 1
    while i <= n:
        results.append(i ** 2)
        i += 1
    return results

results = generate_squares(5)
print(generate_squares(5))