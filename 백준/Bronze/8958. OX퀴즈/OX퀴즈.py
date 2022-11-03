n = int(input())

for i in range(n):
    ox_list = input()
    sco = 0
    ox_sco = 0

    for j in ox_list:
        if j == 'O':
            sco += 1
        else:
            sco = 0
        ox_sco += sco
    print(ox_sco)