T = int(input())
for i in range(T):
    k = int(input())
    n = int(input())
    f0 = [x for x in range(1, n + 1)]
    for x in range(k):
        for y in range(1, n):
            f0[y] += f0[y - 1]
    print(f0[-1])