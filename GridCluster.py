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
                                        gridlist.append([gridcounts[a][b][c][d][e][f][g][h][j][k], a, b, c, d+1, e+1, f+1, g+1, h+1, j+1, k+1])

# sort by count
gridlist.sort(key = lambda el: el[0], reverse = True)

#for x in range(len(gridlist)):
#    print(gridlist[x])

total = len(data)
count = 0
previousCount = 0
cutoff = int(0.85*total)
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
    distanceToNeighbor = 100000
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
print("number of clusters: ", end = "")
print(len(clusters))

for cluster in clusters:
    print("CLUSTER:")
    for grid in cluster:
        print("\t", end = "")
        print(grid)
