a = [input() for _ in range(int(input()))]
print(*a, sep='\n')
print()
[print(i) for i in a if int(i.split()[1]) > 3]