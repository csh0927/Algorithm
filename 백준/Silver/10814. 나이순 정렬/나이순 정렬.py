n = int(input())

data = {}

for _ in range(n):
    age, name = input().split()
    age = int(age)
    if age in data:
        data[age].append(name)
    else:
        data[age] = [name]

for age in sorted(data.keys()):
    for name in data[age]:
        print(age, name)