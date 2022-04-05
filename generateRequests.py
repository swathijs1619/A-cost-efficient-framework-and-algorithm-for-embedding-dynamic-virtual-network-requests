# Generate a set of virtual network requests and write to file
import numpy as np
from random import randint # Import randint from random

iterations = 1000
filename = 'small_dist_02_03_05.txt'

#  VN Requests
VN_frequency_min = 1
VN_frequency_max = 3
VN_time_min = 1
VN_time_max = 3
VN_priority_min = 1
VN_priority_max = 3

average_lifespan = 10
average_arrivals = 3

fileID = open(filename, 'w')
fileID.write('Priority | Area | Timeslot | Duration | Frequency | Time | ID | Operator\n')

print(filename)
request_id = 1

for time_window in range(0,iterations):
# Number of new requests
    Number_of_VN_arrivals = np.random.poisson(average_arrivals)

    # Create a number of new VN requests
    if Number_of_VN_arrivals > 0:
        # VN_requests have area, duration, and priority level
        
        for vn_requests in range(1, Number_of_VN_arrivals):
            
            New_VN_requests = np.zeros((1, 8))
            num = randint(1, 100)
            
            if(num < 20):
                New_VN_requests[0][0] = 1
            elif(num<50):
                New_VN_requests[0][0] = 2
            else:
                New_VN_requests[0][0] = 3
            New_VN_requests[0][4] = randint(VN_frequency_min, VN_frequency_max)%3+1
            New_VN_requests[0][5] = randint(VN_time_min, VN_time_max)%3+1
            New_VN_requests[0][1] = round(New_VN_requests[0][4]*New_VN_requests[0][5])
            # print(New_VN_requests[0][1])
            New_VN_requests[0][2] = time_window
            New_VN_requests[0][3] = randint(1, min(average_lifespan, 1000))
            New_VN_requests[0][6] = request_id
            r = randint(1, 1000)
            op=0
            if(r <= 400):
                op = 1
            elif(r<=800):
                op = 2
            elif(r<=1000):
                op = 3
            New_VN_requests[0][7] = op

            if New_VN_requests[0][3] == 0:
                New_VN_requests[0][3] = 1
            fileID.write(str(New_VN_requests)+'\n')
            request_id = request_id +1
            break

fileID.close()