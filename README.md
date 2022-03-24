# Azure-IoT-Hub
Azure IoT hub is, as its name suggests, a hub for aggregation of data from IoT devices. In this example, the IoT device in question will be a Raspberry Pi but it could be almost any type of device with an internet connection.
The Azure IoT hub will not collect, structure or vizualize the data in any way. It only serves as a aggregation point and from there be distributed out to other Azure services for storage analysis and visualization. 

## Requirements
In order to copy this example you need two things.
  * An Azure subscription
  * A Raspberry Pi with internet connection
   
## Set up Azure
The first step is to create an IoT hub in the Azue portal. Follow the steps under the *Create IoT Hub* in the Microsoft documentation ( https://docs.microsoft.com/en-us/azure/iot-hub/iot-hub-create-through-portal )

When the hub has been created, select it in the Azure portal. This will take you to the overview tab of the IoT hub. To the left, under *Device management*, select *Devices* and click on  *+ Add Device*. Use Symmetric key as Auth. type and Enable the device to be connected to the IoT hub. When the device has been created, select it from the list of devices and find the connection string. 
It should look something like this : *HostName=[iot hub name].azure-devices.net;DeviceId=[device id];SharedAccessKey=[Access key]* .
You will need to copy this string and paste it into the python script in this repo.

Later on, the Azure CLI (Command-Line Interface) will be used to validate that the hub is receving data. Before that can be done, an extensions needs to be added.
Open the Azure CLI by clicking on the CLi icon in the top right corner.
![cli icon](https://user-images.githubusercontent.com/85884666/159885857-905aafe6-caf8-479d-98c3-2207c276d950.png)

In the Azure CLI, write the following command:
```
az extension add --name azure-iot
```

## Set up Raspberry pi


```
sudo pip3 install azure-iot-device  
sudo pip3 install azure-iot-hub  
```
Import code, test run

## Validate
open Azure CLI
az iot hub monitor-events --hub-name XYZ --device-id XYZ

## Transfer data
Create Service bus
message routing
