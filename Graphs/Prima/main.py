from queue import PriorityQueue

#analizowana lista
neighb_list = [
    [[1, 2], 6],
    [[1, 5], 1],
    [[1, 6], 2],
    [[2, 3], 2],
    [[2, 5], 2],
    [[3, 4], 5],
    [[4, 5], 3],
    [[4, 6], 6],
    [[5, 6], 7],
]
#zmienne
numb_tops = 6
top = 1
used = []
#inicjuje tablice i kolejke
result = []
for i in range(1, numb_tops + 1):
    if i == top:
        result.append([i, 0, 0])
    else:
        result.append([i, 0, None])
queue = PriorityQueue()

while len(used) != numb_tops:
    for x in neighb_list:
        if (x[0][0] == top and x[0][1] not in used) or (x[0][1] == top and x[0][0] not in used):
            if x[0][0] == top:
                temp = x[0][1] - 1
            else:
                temp = x[0][0] - 1
            if (result[temp][2] is None) or (result[temp][2] > x[1]):
                result[temp][2] = x[1]
                result[temp][1] = top
            queue.put((x[1], x[0]))
    used.append(top)
    last_el = queue.get()
    while {last_el[1][1], last_el[1][0]} in used:
        last_el = queue.get()
    if last_el[1][1] in used:
        top = last_el[1][0]
    else:
        top = last_el[1][1]

sum = 0
for i in result:
    sum += i[2]

print(f"Tablica zawierajaca numer wierzcholka, poprzednika i wage: {result} ")
#dodatkowe informacje
print(f"Najmniejsza ilosc wag to: {sum}")
print(f"Kolejnosc analizowania wierzcholkow: {used}")
