# Boyer - Moore

text = "CSFBADXBCABDZABDABC"
pattern = "ABDABC"
# text = "ABDAABDAABDAABDA"
# pattern = "ABDA"
repeats = []

# tabela wystepowania ostatniego znaku w patternie dla kazdej litery
chars = []
lastcharindex = []
# wypelnienie tabeli
for i in range(len(pattern)):
    if pattern[i] not in chars:
        chars.append(pattern[i])
        lastcharindex.append(pattern.rindex(pattern[i]))

# funkcja liczaca przesuniecie
def shift(i_, j_, l=len(pattern), t=text, c=chars, lc=lastcharindex):
    return (i_) + l - min(j_, 1 + lc[c.index(text[j_])])

# algorytm
lenp = len(pattern)
i = lenp - 1
while i < len(text):
    correct = True
    for j in range(lenp):
        if text[i-j] not in pattern:
            i += lenp - j
            correct = False
            break
        elif text[i-j] != pattern[lenp - j - 1]:
            i = shift(i, i-j)
            correct = False
            break
    if correct is True:
        repeats.append(i - lenp + 1)
        i += lenp

print(f"Podtekst {pattern} występuje w podanym tekście {len(repeats)} razy na indeksach {repeats}")
