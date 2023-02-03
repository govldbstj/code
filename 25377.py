n = int(input())

m = 1001

for i in range(n):
    A, B = map(int, input().split())
    if A <= B:
        if B < m:
            m = B

if m != 1001:
    print(m)
else:
    print(-1)
