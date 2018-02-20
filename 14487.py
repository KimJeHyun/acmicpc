"""
##########
## CASE 1
# a = [1, 6, 5, 2, 4]
# b = 5
a = list(map(int, input().split()))
b = int(input())
c = 0
a.sort()
print(a)
for i in range(b-1):
    c = c + a[i]
print(c)
"""

##########
## CASE 2

a = [1, 6, 5, 2, 4]
b = []
for i in range(len(a) + 10):
    b.append('_')

for i in range(len(a)):
    if (b[a[i]] != '_'):
        b[a[i]].append(a[i], b[a[i]])

    if (b[a[i]] == '_'):
        b[a[i]] = 0
        b[a[i]] = b[a[i]] + a[i]

print(b)

# print(b)

"""
a = list(map(int, input().split()))

index = list(map(int, input().split()))
print(ret1 + index1)


"""
