from LoadFiles import load, dist

data = load("flaredata2.txt")

# 10 dimensional matrix, to be filled with the count of each potential data element
gridcounts = [[[[[[[[[[0 for u in range(2)] for y in range(2)] for t in range(2)] for r in range(2)] for e in range(3)] for w in range(3)] for q in range(2)] for i in range(4)] for j in range(6)] for x in range(7)]

# populate the data
for e in data:
    gridcounts[e[0]][e[1]][e[2]][e[3]-1][e[4]-1][e[5]-1][e[6]-1][e[7]-1][e[8]-1][e[9]-1] = gridcounts[e[0]][e[1]][e[2]][e[3]-1][e[4]-1][e[5]-1][e[6]-1][e[7]-1][e[8]-1][e[9]-1] + 1

# collapse data into a useable list
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
                                        gridlist.append([gridcounts[a][b][c][d][e][f][g][h][j][k], a/6, b/5, c/3, d, e/2, f/2, g, h, j, k])

# sort by count
gridlist.sort(key = lambda el: el[0], reverse = True)

#for x in range(len(gridlist)):
#    print(gridlist[x])

total = len(data)
count = 0
previousCount = 0
cutoff = int(0.75*total)
noiseCutOff = gridlist[0][0]
previousCutOff = noiseCutOff
i = 0

while(count < cutoff):
    previousCutOff = noiseCutOff
    noiseCutOff = gridlist[i][0]
    previousCount = count
    while(noiseCutOff == gridlist[i][0]):
        count = count + gridlist[i][0]
        i = i + 1
#print(previousCutOff)
#print(count)
#print(previousCount)
#print(cutoff)
#print(i/len(gridlist))

def NonNoise(data, cutoff):
    for ele in data:
        if(ele[0] > cutoff):
            yield ele
        else:
            break


def addToCluster(nx, clusters, max_dist):
    candidateClusters = []
    distanceToNeighbor = max_dist + 1
    for cluster in clusters:
        closest = min(cluster, key = lambda x: dist(x[1:], nx[1:]))
        if(dist(closest[1:], nx[1:]) < distanceToNeighbor):
            candidateClusters = []
            candidateClusters.append(cluster)
            distanceToNeighbor = dist(closest[1:], nx[1:])
        elif(dist(closest[1:], nx[1:]) == distanceToNeighbor):
            candidateClusters.append(cluster)
    if(distanceToNeighbor > max_dist):
        return True
    else:
        #print(candidateClusters).append(cluster)
        max(candidateClusters, key = lambda x: min(x, key = lambda y: dist(y[1:], nx[1:]))[0]).append(nx)
        return False

clusters = []

for nc in NonNoise(gridlist, noiseCutOff):
    if(addToCluster(nc, clusters, 1)):
        clusters.append([nc])
        #print(clusters)

def dataEqauls(e, o):
    return e[0]/6 == o[1] and e[1]/5 == o[2] and e[2]/3 == o[3] and e[3]-1 == o[4] and (e[4]-1)/2 == o[5] and (e[5]-1)/2 == o[6] and e[6]-1 == o[7] and e[7]-1 == o[8] and e[8]-1 == o[9] and e[9]-1 == o[10]

Csets = [dict() for x in range(len(clusters))]
for e in data:
    for i in range(len(clusters)):
        for o in clusters[i]:
            if dataEqauls(e, o):
                if (e[10], e[11], e[12]) in Csets[i]:
                    Csets[i][(e[10], e[11], e[12])] = Csets[i][(e[10], e[11], e[12])] + 1
                else:
                    Csets[i][(e[10], e[11], e[12])] = 1




print("number of clusters: ", end = "")
print(len(clusters))



for i in range(len(clusters)):
    print("CLUSTER:")
    for grid in clusters[i]:
        print("\t", end = "")
        print('{:3d}, {:.2f}, {:.2f}, {:.2f}, {:.2f}, {:.2f}, {:.2f}, {:.2f}, {:.2f}, {:.2f}, {:.2f}'.format(grid[0], grid[1],grid[2], grid[3],grid[4], grid[5],grid[6], grid[7],grid[8], grid[9],grid[10]))
    print("Classifiers:")
    for d in iter(Csets[i]):
        print("\t", end = "")
        print(d, end = ": ")
        print(Csets[i][d])
