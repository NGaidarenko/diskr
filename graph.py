n, m = map(int, input().split())
g = [[False for _ in range(n)] for _ in range(n)]
transitive, antitransitive = True, True
symmetrical, antisymmetrical = True, True
reflective, antireflective = True, True
for _ in range(m):
    a, b = map(int, input().split())
    g[a - 1][b - 1] = True

for i in range(0, n):
    for j in range(i + 1, n):
        for k in range(0, n):
            if k == i or k == j:
                continue

            if g[i][k] and g[k][j]:
                transitive &= g[i][j]
                antitransitive &= not g[i][j]

        symmetrical &= not (g[i][j] ^ g[j][i])
        antisymmetrical &= not (g[i][j] & g[j][i])
    reflective &= g[i][i]
    antireflective &= not g[i][i]

if reflective:
    print("Рефлексивное")
elif antireflective:
    print("Антирефлексивное")
else:
    print("Нерефлексивное")

if transitive:
    print("Транзитивное")
elif antitransitive:
    print("Антитранзитивное")
else:
    print("Нетранзитивное")

if symmetrical:
    print("Симметричное")
elif antisymmetrical:
    print("Антисимметричное")
else:
    print("Несимметричное")
