#Import random library to gerenate random sensor data
import random as rand
#create a dictionary to handle sensor data
sensor_cluster = dict()

#create dummy sensor data
#32 entries
for i in range(3):
    sensor_data = rand.random()
    #Generate 16 random sensor data for every sensor cluster
    sensor_cluster[i] = { n: [rand.random()] for n in range(16+1)}

for k in sensor_cluster:
    print sensor_cluster[k]
