import math

def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

def lcm(a, b):
    return a * b // gcd(a, b)

def common_log_in_time(n, m, freq):
    l = freq[0]
    for i in range(1, n):
        l = lcm(l, freq[i])
    print(l)
    

t = int(input().strip())
for _ in range(t):
    n, m = map(int, input().strip().split())
    freq = list(map(int, input().strip().split()))
    result = common_log_in_time(n, m, freq)
    print(result)