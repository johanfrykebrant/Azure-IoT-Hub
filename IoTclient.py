import random as r  
from datetime import datetime as dt
import time as t
from azure.iot.device import IoTHubDeviceClient, Message

CONNECTION_STRING = 'HostName=<iot hub name>.azure-devices.net;DeviceId=<device id>;SharedAccessKey=<Access key>'
#Message format can be any JSON string, customize to suit your needs
MSG = '{{"timestamp": {time},"datapoint 1": {dp1}}}'

def iothub_client_connect():  
    client = IoTHubDeviceClient.create_from_connection_string(CONNECTION_STRING)  
    return client

def get_data():
    #Swap the random value for something that is valuable to you
    dp1 = r.random()
    time = dt.now()
    msg = MSG.format(time=time, dp1=dp1) 
    return msg

def iothub_client_stream_data():  
    try:  
        client = iothub_client_connect()  
        print ( "Sending data to IoT Hub, press Ctrl-C to exit" )  
        while True: 
            message = Message(get_data())  
            print( "Sending message: {}".format(message) )  
            client.send_message(message)  
            print ( "Message successfully sent" )  
            t.sleep(3)
    except KeyboardInterrupt:  
        print ( "Data stream stopped by user" )
    except Exception:
        raise
            
def main():
    iothub_client_stream_data()

if __name__ == "__main__":
    main()
