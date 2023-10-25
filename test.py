from math import log10, trunc

print(log10(10))
print(log10(100))
print(log10(1000))
print(log10(10000))
print(log10(100000))
print(log10(1000000))
print(trunc(log10(543212345)))

N = 543212345
n = trunc(log10(N))
start = pow(10, n)+1
end = N

print(n, start, end)