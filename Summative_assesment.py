#Import random library to gerenate random sensor data
import random as rand

#Import Json Library to be used to write sensor data in a file
import json

#Import date time and time library to add date time to sensor data when saving in file
import datetime
import time

#Import logging module to create error logs
import logging

#create a dictionary to handle sensor data
sensor_cluster = dict()

#create dummy sensor data
#32 entries
for i in range(32):
    sensor_data = rand.random()
    #Generate 16 random sensor data for every sensor cluster

    #custom names for sensor readings
    #sensor_cluster[i] = { 'sensor'+str(n): [rand.random()] for n in range(16)}

    sensor_cluster[i] = { n : [rand.random()] for n in range(16)}


#Store sensor data in a Json file
with open("e://Dev//summative_assesment//venv//sensor_data.txt", "a") as f:
    now = datetime.datetime.today()
    f.write("Sensor data as of {}".format(now))
    for row in sensor_cluster:
        f.write("\n\nSensor data for cluster {}\n".format(row))
        json.dump(sensor_cluster[row], f)
    f.write("\n\n\n\n")

#print sensor data in console
# print ("sensor data as of {}".format(now))
# for row in sensor_cluster:
#     print("sensor data for cluster {}".format(row))
#     print sensor_cluster[row]


#create copy of corrupted sensor data
#32 entries
corrupt_sensor_cluster = dict()
for i in range(32):
    #Generate 16 random sensor data for every sensor cluster
    # if i%2 == 0:
    #     corrupt_sensor_cluster[i] = { n : [rand.random()] for n in range(16)}
    # else:
    #     corrupt_sensor_cluster[i] = { n: "err" for n in range(16) if n%2 == 0}
    #     corrupt_sensor_cluster[i] = { n: [rand.random()] for n in range(16)}
    corrupt_sensor_cluster[i] = { n : [rand.random()] for n in range(16)}
    for val in corrupt_sensor_cluster[i]:
        if val%2 == 0:
            corrupt_sensor_cluster[i].update({val : "err"})


#create a function that checks for errors from sensor data
def err_check():
    #Configuring error logs
    logging.basicConfig(filename='error.log', level=logging.DEBUG, format='%(asctime)s:%(levelname)s:%(message)s')
    #Checking for errors in sensor readings
    for clusters, sensor_readings in corrupt_sensor_cluster.items():
        print("\n\nsensor readings for  cluster {}".format(clusters))
        for key, value in sensor_readings.items():
            if value == "err":
                logging.debug("Sensor {} from cluster {} is having an error".format(key,clusters))

            #updating an error to a unique integer
            sensor_readings.update({val : 10})
            print (key,value)
err_check()
