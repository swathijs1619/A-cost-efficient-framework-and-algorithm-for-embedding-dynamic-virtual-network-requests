import numpy as np
from numpy import genfromtxt as readCSV
import math

def createEvolvedRequest(Nv, DC, DRR, AC, ARR, filename, bandV, req):
    indices = np.asarray([i for i in range(0, Nv)])
    newNv = Nv + AC
    existingNode = np.full((1, newNv), 1, dtype=int)
    newReq = np.random.randint(15, high=21, size=(1, newNv), dtype=np.uint32)
    newBandV = np.full((newNv, newNv), 0, dtype=int)
    newBandV[0:Nv, 0:Nv] = bandV

    # AC
    for index in indices[AC:]:
        newReq[0,index] = req[0,index]

    for row in range(Nv, newNv):
        col = np.random.randint(0, high=newNv, dtype=np.uint32)
        while col == row:
            col = np.random.randint(0, high=newNv, dtype=np.uint32)
        newBandV[row][col] = newBandV[col][row] = np.random.randint(10, high=16, dtype=np.uint32)
        col = np.random.randint(0, high=newNv, dtype=np.uint32)
        while col == row:
            col = np.random.randint(0, high=newNv, dtype=np.uint32)
        newBandV[row][col] = newBandV[col][row] = np.random.randint(10, high=16, dtype=np.uint32)

    # ARR
    for index in indices[0:ARR]:
        newReq[0,index] += 2
    while ARR > 0:
        row = np.random.randint(0, high=Nv, dtype=np.uint32)
        col = np.random.randint(0, high=Nv, dtype=np.uint32)
        if newBandV[row][col] > 0:
            newBandV[col][row] = newBandV[row][col] = newBandV[row][col] + 3
            ARR -= 1

    # DC
    for index in indices[DC:2*DC]:
        existingNode[0, index] = 0
    for index in range(0,Nv):
        if existingNode[0, index] == 1:
            continue
        for itr in range(0, newNv):
            newBandV[itr][index] = newBandV[index][itr] = 0
    DC = 2
    while DC > 0:
        row = np.random.randint(0, high=Nv, dtype=np.uint32)
        col = np.random.randint(0, high=Nv, dtype=np.uint32)
        if newBandV[row][col] > 0:
            newBandV[row][col] = newBandV[col][row] = 0
            DC -= 1

    # DRR
    for index in indices[2*DRR:3*DRR]:
        newReq[0,index] -= 3
    while DRR > 0:
        row = np.random.randint(0, high=Nv, dtype=np.uint32)
        col = np.random.randint(0, high=Nv, dtype=np.uint32)
        if newBandV[row][col] > 0:
            newBandV[col][row] = newBandV[row][col] = newBandV[row][col] - 2
            DRR -= 1

    newGv = np.full((newNv, newNv), 0, dtype=np.int)
    for row in range(0, newNv):
        for col in range(0, newNv):
            if newBandV[row][col] > 0:
                newGv[row][col] = 1
    combined = np.concatenate((newGv, newBandV, newReq, existingNode))
    np.savetxt(filename, combined, fmt='%d', delimiter=",")

for netId in range(1, 4):
    substrate = readCSV("Net" + str(netId) + ".csv", delimiter=',')
    Ns = substrate.shape[1]
    for Nv in range(5, 11):
        # r = 1:1
        DC = DRR = ARR = math.floor(Ns/4)
        AC = Ns

        initialVNR = readCSV("VN" + str(Nv) + ".csv", delimiter=',')
        bandV = initialVNR[Nv:2*Nv,:]
        req = initialVNR[2*Nv]

        filename = "VN Evolved Requests/Net" + str(netId) + "_VN" + str(Nv) + "_r11.csv"
        createEvolvedRequest(Nv, DC, DRR, AC, ARR, filename, bandV, req)

        # r = 2:3
        DC = DRR = ARR = math.floor(Ns / 4)
        AC = math.floor(Ns*1.5)

        initialVNR = readCSV("VN" + str(Nv) + ".csv", delimiter=',')
        bandV = initialVNR[Nv:2 * Nv, :]
        req = initialVNR[2 * Nv]

        filename = "VN Evolved Requests/Net" + str(netId) + "_VN" + str(Nv) + "_r23.csv"
        createEvolvedRequest(Nv, DC, DRR, AC, ARR, filename, bandV, req)

        # r = 3:2
        DC = DRR = ARR = math.floor(Ns / 4)
        AC = math.floor(Ns/1.5)

        initialVNR = readCSV("VN" + str(Nv) + ".csv", delimiter=',')
        bandV = initialVNR[Nv:2 * Nv, :]
        req = initialVNR[2 * Nv]

        filename = "VN Evolved Requests/Net" + str(netId) + "_VN" + str(Nv) + "_r32.csv"
        createEvolvedRequest(Nv, DC, DRR, AC, ARR, filename, bandV, req)
