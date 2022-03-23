# Azure-IoT-Hub
Example on how to collect data from a Raspbarry Pi via Azure IoT hub 

# Set up Azure
create IoT hub and device
In the Azure CLI:
az extension add --name azure-iot

# Set up raspberry pi
sudo pip3 install azure-iot-device  
sudo pip3 install azure-iot-hub  
Import code, test run

# Validate
open Azure CLI
az iot hub monitor-events --hub-name XYZ --device-id XYZ

# transfer data
Create Service bus
message routing
