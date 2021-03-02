def persistence(n):
    count = 0
    while n > 9:
        A = str(n)
        N = 1
        L = []
        for i in range(len(A)):
            L.append(A[i])
            N = N * int(L[i])
        n = N
        count += 1
    return count


print(persistence(78))

# Max string important

def f(strarr, k):
    l = []
    if k > 0 and len(strarr) >= k:
        for i in range(len(strarr) - (k - 1)):
            m = ''.join(strarr[i:i + k])
            l.append(m)  # Pay attention to this usage, don’t write l=l.append(m)
        return max(l, key=len)
    else:
        return ''


def split(word):
    return [char for char in word]

H = "abba"

# Driver code
word = 'geeks'
N=(split(H))
print(N)
N2 = []
words = ['aabb', 'abcd', 'bbaa', 'dada']
for i in range(len(words)):
    N2.append((split(words[i])))

print(N2)


N.sort()
sL = N
print(sL)

for i in range(len(N2)):
    N2[i].sort()
print(N2)
R = []
for i in range(len(N2)):
    if sL == N2[i]:
        R.append(words[i])
print(R)


import itertools


def get_pins(pin):
    adjacent = {
        '1': ['2', '4'],
        '2': ['1', '3', '5'],
        '3': ['2', '6'],
        '4': ['1', '5', '7'],
        '5': ['2', '4', '6', '8'],
        '6': ['3', '5', '9'],
        '7': ['4', '8'],
        '8': ['5', '7', '9', '0'],
        '9': ['6', '8'],
        '0': ['8'],
    }
    L = [[digit] + adjacent[digit] for digit in pin]
    print(L)
    print([''.join(ele) for ele in list(itertools.product(*L))])


get_pins("12")

