import math


def pascal_ucgeni(n):
    ucgen = [[1]]

    for i in range(1, n):
        satir = [1]  
        for j in range(1, i):
            # Önceki satırın yan yana iki elemanını toplayarak yeni değerleri hesapla
            satir.append(ucgen[i-1][j-1] + ucgen[i-1][j])
        satir.append(1)
        ucgen.append(satir)

    return ucgen


n = 10
for satir in pascal_ucgeni(n):
    print(satir)
