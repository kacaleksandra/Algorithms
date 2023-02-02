from math import inf
from queue import PriorityQueue

# analizowany graf
neighb_list = [
    [[1, 2], 5],
    [[1, 4], 1],
    [[2, 3], 2],
    [[2, 5], 1],
    [[3, 8], 3],
    [[4, 5], 1],
    [[4, 6], 2],
    [[5, 3], 4],
    [[6, 1], 4],
    [[6, 7], 2],
    [[7, 5], 1],
    [[7, 8], 1],
    [[8, 5], 2],
]

vertices = 8
# wybieram wierzcholek startowy i koncowy
start = 1
end = 8
# tablica szacowanych odleglosci dla kolejnych wierzcholkow
distances = [4, 8, 3, 4, 5, 2, 1, 0]

# tablica zawierajaca wierzcholki, szacowana odleglosc, dokladna odleglosc
# oraz laczna dlugosc trasy i poprzednika.

informationTable = []
i: int
for i in range(0, vertices):
    if i + 1 == start:
        informationTable.append([i + 1, distances[i], 0, distances[i], 0])
    else:
        informationTable.append([i + 1, distances[i], inf, inf, 0])

# zbior wezlow otwartych (znalezionych na trasie) i zamknietych (juz dodanych do sciezki)
opened = PriorityQueue()
closed = []

# algorytm ma sie wykonywac, az do closed[] dolaczymy wierzcholek end

while not end in closed:
    # poszukuje sasiadow i dodaje ich do kolejki
    for x in neighb_list:
        if (x[0][0] == start) and (x[0][1] not in closed):
            # dodatkowe zmienne dla wiekszej czytelnosci
            foundTopIndex = x[0][1] - 1
            # przeliczanie dlugosci trasy: g(x) poprzednika + waga polaczenia
            fullLength = informationTable[start - 1][2] + x[1]
            # sprawdzenie czy ta trasa jest krotsza od zapisanej
            if fullLength < informationTable[foundTopIndex][2]:
                # ustalanie poprzednika sasiada
                informationTable[foundTopIndex][4] = start
                # ustalanie g(v)
                informationTable[foundTopIndex][2] = fullLength
                # przeliczanie f(v)
                informationTable[foundTopIndex][3] = informationTable[foundTopIndex][1] + informationTable[foundTopIndex][2]

            opened.put([informationTable[foundTopIndex][3], foundTopIndex + 1])
    # wyznaczam nowy wierzcholek, ktory ma najmniejsze f(v)
    start = opened.get()[1]
    while start in closed:
        start = opened.get()
    # dodaje "zuzyty" wierzcholek do zbioru zamknietych
    closed.append(start)

headers = ["wierz.", "h(v)", "g(v)", "f(v)", "poprz."]
for i in range(len(informationTable[i])):
    print("%6s |" % (headers[i]), end=' ')
    for j in range(len(informationTable)):
        print("%6s | " % (str(informationTable[j][i])), end=' ')
    print()

now = end
print("Sciezka pomiedzy dwoma wybranymi punktami to: ", end=' ')
while informationTable[now - 1][4] != 0:
    print(informationTable[now - 1][4], end=', ')
    now = informationTable[now - 1][4]
