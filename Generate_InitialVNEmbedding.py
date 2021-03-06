import numpy as np
from numpy import genfromtxt as readCSV

for netId in range(1, 4):
    for Nv in range(5, 11):
        filename = "Net" + str(netId) + "_VN" + str(Nv) + ".csv"
        substrate = readCSV("Net" + str(netId) + ".csv", delimiter=',')
        Ns = substrate.shape[1]
        Gs = substrate[:Ns, ]
        BandS = substrate[Ns:2*Ns,]
        newBandS = substrate[Ns:2 * Ns, ]
        newCapa = Capa = np.full((1, Ns), 0, dtype=int)
        Capa[:] = newCapa[:] = substrate[2*Ns]

        vn_request = readCSV("VN" + str(Nv) + ".csv", delimiter=',')
        Nv = vn_request.shape[1]
        Gv = vn_request[:Nv, ]
        bandV = vn_request[Nv:2 * Nv, ]
        req = vn_request[2 * Nv,]

        '''
        Embedding code start
        '''



        Vs_to_Vv = np.full((Ns, 1), -1, dtype=np.int)
        Vv_to_Vs = np.full((Nv, 1), -1, dtype=np.int)
        edge_map = np.random.random((Ns, Ns, 2))

        #Set non-edge values to -1
        edge_map[:,:,0] = (edge_map[:,:,0]*Gs) + (Gs-1)
        edge_map[:,:,1] = (edge_map[:,:,1]*Gs) + (Gs-1)
        edge_map = edge_map.astype(int)
        '''
        Embedding code end
        '''

        for index in range(0, Ns):
            if Vs_to_Vv[index] > -1:
                newCapa[index] -= req[Vs_to_Vv[index]]

        for row in range(0, Ns):
            for col in range(0, Ns):
                if edge_map[row][col][0] > -1:
                    newBandS[row][col] -= bandV[edge_map[row][col][0]][edge_map[row][col][1]]


        combined = np.concatenate((edge_map[:,:,0], edge_map[:,:,1]), axis=1)
        lastRow = np.full((2*Ns, 1), -2, dtype=int)
        lastRow[0:Ns] = Vs_to_Vv
        lastRow[Ns:Nv+Ns] = Vv_to_Vs
        combined = np.concatenate((combined, lastRow.T))
        np.savetxt("VN Embeddings/" + filename, combined, fmt='%d', delimiter=",")
        np.savetxt("VN Embeddings/UpdatedSubstrate_" + filename, np.concatenate((newBandS, newCapa)), fmt='%d', delimiter=",")