from LoadFiles import load

data = load("flaredata2.txt")

gridcounts = [[[[[[[[[[0 for u in range(2)] for y in range(2)] for t in range(2)] for r in range(2)] for e in range(3)] for w in range(3)] for q in range(2)] for i in range(4)] for j in range(6)] for x in range(7)]

for e in data:
    gridcounts[e[0]][e[1]][e[2]][e[3]-1][e[4]-1][e[5]-1][e[6]-1][e[7]-1][e[8]-1][e[9]-1] = gridcounts[e[0]][e[1]][e[2]][e[3]-1][e[4]-1][e[5]-1][e[6]-1][e[7]-1][e[8]-1][e[9]-1] + 1

gridlist = []
for a in range(len(gridcounts)):
    for b in range(len(gridcounts[a])):
        for c in range(len(gridcounts[a][b])):
            for d in range(len(gridcounts[a][b][c])):
                for e in range(len(gridcounts[a][b][c][d])):
                    for f in range(len(gridcounts[a][b][c][d])):
                        for g in range(len(gridcounts[a][b][c][d][e][f])):
                            for h in range(len(gridcounts[a][b][c][d][e][f][g])):
                                for j in range(len(gridcounts[a][b][c][d][e][f][g][h])):
                                    for k in range(len(gridcounts[a][b][c][d][e][f][g][h][j])):
                                        gridlist.append([gridcounts[a][b][c][d][e][f][g][h][j][k], a, b, c, d+1, e+1, f+1, g+1, h+1, j+1, k+1])

gridlist.sort(key = lambda el: el[0], reverse = True)

for x in range(len(gridlist)):
    print(gridlist[x])