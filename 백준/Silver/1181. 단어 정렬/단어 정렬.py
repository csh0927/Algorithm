n = int(input())
words = []

for _ in range(n):
    w = input()
    words.append(w)

words = set(words)
words = sorted(words)
words = sorted(words, key = lambda x : len(x))

for i in words:
    print(i)