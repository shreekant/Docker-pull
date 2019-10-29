import os
import docker
import json
import logging

logging.basicConfig(level=logging.DEBUG)
try:
    with open('dockerconfig.json', 'r') as myfile:
        data=myfile.read()
    connectToAzure = json.loads(data)

    print("url: " + str(connectToAzure['url']))
    print("username: " + str(connectToAzure['username']))
    print("password: " + str(connectToAzure['password']))
    print("email: " + str(connectToAzure['email']))

    with open('azure-containers.json', 'r') as file:
        azureContainer = json.load(file)
    client = docker.from_env()
    client.login(registry=str(connectToAzure['url']), username= str(connectToAzure['username']), password= str(connectToAzure['password']))
    for counter in range (0,len(azureContainer['list'])):
        print (azureContainer['list'][counter])
        print (str(connectToAzure['url']) + "/" + azureContainer['list'][counter] )
        print (client.containers.run(str(connectToAzure['url']) + "/"+azureContainer['list'][counter] ))
        
except: 
    print ('Error ')