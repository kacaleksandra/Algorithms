from math import inf

# lista sasiedztwa
neighb_list = [
    [[1, 2], 2],
    [[1, 3], 1],
    [[2, 3], 3],
    [[2, 4], 4],
    [[3, 5], 2],
    [[4, 5], 5],
]
# zmienne
top = (1, 0)
numb_tops = 5
used = []
# tablica zawierajaca numer wierzcholka, poprzednika i koszt przejscia
result = []
for i in range(1, numb_tops + 1):
    if i == top[0]:
        result.append([i, None, 0])
    else:
        result.append([i, None, inf])

while len(used) != numb_tops:
    # tablica "sasiadow" zawierajaca sasiada i wage przejscia
    neighbours = []
    for i in neighb_list:
        if i[0][0] == top[0]:
            neighbours.append((i[0][1], i[1]))

    for neighb in neighbours:
        if neighb[0] not in used:
            for res in result:
                # jezeli element w wynikowej tablicy jest rowny sasiadowi
                # oraz suma wagi przejscia sasiada + rozpatrywanego wierzcholka
                # jest mniejsza od wagi przejscia sasiada.
                if res[0] == neighb[0] and (neighb[1] + top[1] < res[2]):
                    # zamieniam wage na sume wagi sasiada i wierzcholka.
                    res[2] = neighb[1] + top[1]
                    # zamieniam poprzednika
                    res[1] = top[0]
    # dodaje do tablicy zuzyty wierzcholek
    used.append(top[0])
    # szukam nowego wierzcholka do analizy
    top = (None, inf)
    for res in result:
        if res[0] not in used and res[2] < top[1]:
            top = (res[0], res[2])

print(result)
