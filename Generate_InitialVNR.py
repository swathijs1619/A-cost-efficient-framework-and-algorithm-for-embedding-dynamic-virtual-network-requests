import numpy as np

nodes = [n for n in range(5, 11)]

for Nv in nodes:
    filename = "VN" + str(Nv) + ".csv"
    Gv = np.full((Nv, Nv), 0, dtype=np.uint32)
    countEdge = np.full((Nv, 1), 0, dtype=np.uint32)
    for row in range(0, Nv):
        for col in range(row+1, Nv):
            prob = np.random.randint(1, high=11, dtype=np.uint32)
            # Edge creation with 0.4 probability
            if prob > 6:
                Gv[row][col] = Gv[col][row] = 1
                countEdge[row] += 1
                countEdge[col] += 1
    # Just incase a VN node doesn't have any edge incident on it
    for row in range(0, Nv):
        if countEdge[row] == 0:
            col = row
            while row == col:
                col = np.random.randint(0, high=Nv, dtype=np.uint32)
            Gv[row][col] = Gv[col][row] = 1
            countEdge[row] += 1
            countEdge[col] += 1
    req = np.random.randint(15, high=21, size=(1, Nv), dtype=np.uint32)
    band = Gv * np.random.randint(10, high=16, size=(Nv, Nv), dtype=np.uint32)
    combined = np.concatenate((Gv, band, req))
    np.savetxt(filename, combined, fmt='%d', delimiter=",")