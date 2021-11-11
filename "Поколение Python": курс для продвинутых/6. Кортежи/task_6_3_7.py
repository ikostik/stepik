def sequence(n):
    """Последовательность Трибоначчи
    Sample Input 1:
    10
    Sample Output 1:
    1 1 1 3 5 9 17 31 57 105
    """
    f1, f2, f3 = 1, 1, 1
    for _ in range(n):
        print(f1, end=' ')
        f1, f2, f3 = f2, f3, f1 + f2 + f3


sequence(10)
