import numpy as np
from numpy import genfromtxt as readCSV

for netId in range(1, 4):
    for Nv in range(5, 11):
        filename = "VN Embeddings/Net" + str(netId) + "_VN" + str(Nv) + ".csv"
        substrate = readCSV("Net" + str(netId) + ".csv", delimiter=',')
        Ns = substrate.shape[1]
        vn_request = readCSV("VN" + str(Nv) + ".csv", delimiter=',')

        Vs_to_Vv = np.full((Ns, 1), -1, dtype=np.int)
        Vv_to_Vs = np.full((Nv, 1), -1, dtype=np.int)
        edge_map = np.random.random((Ns, Ns, 2))

        # Embedding code

        combined = np.concatenate((edge_map[:,:,0], edge_map[:,:,1]), axis=1)
        lastRow = np.full((2*Ns, 1), -2, dtype=int)
        lastRow[0:Ns] = Vs_to_Vv
        lastRow[Ns:Nv+Ns] = Vv_to_Vs
        combined = np.concatenate((combined, lastRow.T))
        np.savetxt(filename, combined, fmt='%d', delimiter=",")