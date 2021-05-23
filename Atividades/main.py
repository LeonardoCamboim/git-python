a = [[0, 0, 0],
     [0, 0, 0],
     [0, 0, 0]]

for l in range(len(a)):
    for c in range(3):
        a[l][c] = float(input(f'Digite um valor para {[l]}, {[c]}'))

for l in range(len(a)):
    for c in range(3):
        print(f'{a[l][c]}', end='  ')
    print()