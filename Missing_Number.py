n = int(input())
a = []
z = list(map(int, input().split()))

sum = 0
sum2 = 0

for i in range(1, n + 1):
    sum += i

for j in z:
    sum2 += j

print(sum - sum2)
