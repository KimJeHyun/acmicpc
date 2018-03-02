a = 5
b = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.7, 0.7, 0.8, 0.9]
# a = 10
# b = [0.137490, 0.801868, 0.995100, 0.644400, 0.427567, 0.113815, 0.880391]
c = 0
d = 1
e = d / a
f = {}
g = 0

for i in range(a):
    f[i] = 0
e = e * 1000000
for i in range(len(b)):
    b[i] = b[i] * 1000000
    g = b[i] // e
    if g in f:
        f[g] = f[g] + 1

for i in range(a):
    print(f[i])


