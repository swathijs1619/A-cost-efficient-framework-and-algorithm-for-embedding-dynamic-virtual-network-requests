import numpy as np
import pandas as pd

# Iterations
iterations = 1000
filename = 'small_dist_02_03_05.txt'
linenumber = 1
waiting_time_3 = 3

# Substrate resources
number_of_VMOs = 3

# total_requests_1= np.zeros((iterations, number_of_VMOs))
# total_requests_2= np.zeros((iterations, number_of_VMOs))
# total_requests_3= np.zeros((iterations, number_of_VMOs))

fileID = open(filename, 'r')
# text = textscan(fileID, '%s', 8, 'delimiter', '|')
# Requests = textscan(fileID, '%d %d %d %d %d %d %d %d', 'CollectOutput', 1);
Requests = fileID
# Priority Area Timeslot Duration Frequency Time ID Operator

print(Requests)
number_of_Requests = len(Requests.readlines())
print("number_of_Requests", number_of_Requests)

# for timeslot in range(0,iterations):
#     linestart = linenumber
#     while((Requests[linenumber][3] == timeslot) and (linenumber!=number_of_Requests)):
#         linenumber = linenumber + 1
    
#     new_requests = [Requests[linestart:linenumber-1, :]]
    
#     if(timeslot <=iterations):
#         for i in range(0,len(new_requests)):
#             operator = new_requests[i][7]
#             if(new_requests[i][0]==1):
#                 total_requests_1[timeslot][operator] = total_requests_1[timeslot][operator] + new_requests[i][1]*new_requests[i][3]
#             elif(new_requests(i, 1)==2):
#                 total_requests_2[timeslot][operator] = total_requests_2[timeslot][operator] + new_requests[i][1]*new_requests[i][3]
#             elif(new_requests(i, 1)==3):
#                 total_requests_3[timeslot][operator] = total_requests_3[timeslot][operator] + new_requests[i][1]*new_requests[i][3]


fileID.close()

# % sum(total_requests_1(:, :))
# sum(sum(total_requests_1) +sum(total_requests_2) + sum(total_requests_3))