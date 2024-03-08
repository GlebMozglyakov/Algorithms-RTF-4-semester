def compute_prefix_function(s):
    n = len(s)
    pi = [0] * n

    for i in range(1, n):
        j = pi[i - 1]
        while j > 0 and s[i] != s[j]:
            j = pi[j - 1]
        if s[i] == s[j]:
            j += 1
        pi[i] = j

    return pi


def find_repeat(s):
    pi = compute_prefix_function(s)
    n = len(s)

    if n % (n - pi[-1]) == 0:
        k = n // (n - pi[-1])
        t = s[:n // k]
        return k, t

    return 1, s


s = input().strip()
k, t = find_repeat(s)
print(k, t)
