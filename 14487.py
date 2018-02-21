"""
##########
## CASE 1
# b = 5
# a = [1, 6, 5, 2, 4]
b = int(input())
a = list(map(int, input().split()))
c = 0
a.sort()
print(a)
for i in range(b-1):
    c = c + a[i]
print(c)
"""

"""
##########
## CASE 2
# a = [1, 6, 5, 2, 4, 5, 5]
# b = 5
b = int(input())
a = list(map(int, input().split()))
c = 0
for i in range(len(a)):
    for ii in range(len(a)):
        if (ii > 0):
            if (a[ii-1] > a[ii]):
                a.insert(ii+1, a[ii-1])
                a.pop(ii-1)
for i in range(b-1):
    c = c + a[i]
print(c)
"""

"""
##########
## CASE 2

a = [1, 6, 5, 2, 4, 5, 5]
b = []
c = []

for i in range(len(a) + 10):
    b.append('_')
for i in range(len(a) + 10):
    c.append('_')

for i in range(len(a)):
    if (b[a[i]] != '_'):
        print(a[i])
        print(b[a[i]])
        c.insert([a[i], c.extend([a[i], b[a[i]]]))
        print(c)
        print(b)
        b.pop(a[i])
        b.insert(a[i])
        # b[a[i]].append([a[i], b[a[i]]])
        c.pop(0)

    if (b[a[i]] == '_'):
        b[a[i]] = 0
        b[a[i]] = b[a[i]] + a[i]

print(c)
print(b)


# print(b)

a = list(map(int, input().split()))

index = list(map(int, input().split()))
print(ret1 + index1)


"""
