from math import inf
import pprint

# analizowany graf
neighb_list = [
    [[1, 2], 1],
    [[1, 3], 5],
    [[2, 3], 2],
    [[4, 1], 7],
    [[4, 5], 1],
    [[5, 6], 1],
    [[6, 1], 2],
    [[6, 4], 4],
    [[7, 1], 6],
    [[7, 6], 3],
]
vertices = 7

# tablica dwuwymiarowa odleglosci oraz poprzednikow
# inicjalizuje 0 na przekatnej oraz inf na reszcie miejsc
distances = [[inf]*vertices for i in range(vertices)]
prev = [[inf]*vertices for i in range(vertices)]
for i in range(vertices):
    distances[i][i] = 0
    prev[i][i] = 0

# wypelniam tabele distances z wagami polaczen, cos jak macierz sasiedztwa
for x in neighb_list:
    distances[x[0][0] - 1][x[0][1] - 1] = x[1]
    # wypelniam tez tabele poprzednikow numerami wiersza, tam gdzie znalezlismy dystans
    prev[x[0][0] - 1][x[0][1] - 1] = x[0][0]

#szukamy sciezek miedzy dwoma dowolnymi wierzcholkami, ktore przechodza przez dany wierzcholek
#aktualnie analizowany wierzcholek
actual = 1
#musze znalezc takie wierzcholki ze v -> u -> w, sa ta wszystkie te, ktore w tabeli poprzednik nie maja 0 ani inf
while actual <= vertices:
    possibleV = []
    possibleW = []
    for i in range(vertices):
        if (distances[i][actual - 1] != 0) and (distances[i][actual - 1] != inf):
            possibleV.append(i+1)
        if (distances[actual - 1][i] != 0) and (distances[actual - 1][i] != inf):
            possibleW.append(i + 1)

    for v in possibleV:
        for w in possibleW:
            # odleglosc miedzy v a u
            distanceVU = distances[v - 1][actual - 1]
            distanceUW = distances[actual - 1][w - 1]
            if distanceVU + distanceUW < distances[v - 1][w - 1]:
                distances[v - 1][w - 1] = distanceVU + distanceUW
                prev[v - 1][w - 1] = prev[actual-1][w-1]

    actual += 1

# wypisywanie
pp = pprint.PrettyPrinter(indent=3)
print("Tabela dystansow: ")
pp.pprint(distances)

print("Tabela poprzednikow: ")
pp.pprint(prev)

_from = 7
_to = 5
print(f"Sciezka miedzy {_from} a {_to}: ")
path = [_to]
while True:
    if prev[_from - 1][_to - 1] == _from:
        path.append(prev[_from - 1][_to - 1])
        break
    path.append(prev[_from - 1][_to - 1])
    _to = prev[_from - 1][_to - 1]

print(path[::-1])
