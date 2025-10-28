from umqtt.simple import MQTTClient
from machine import Pin
import network
import ujson
import time
import dht

MQTT_BROKER = "test.mosquitto.org"
CLIENT_ID = "mqtt-demo"
TOPIC_SENSOR = "mqtt-demo/sensors_168"


ldr = ADC(Pin(34))          
temp_sensor = ADC(Pin(35))  
led_light = Pin(23, Pin.OUT)  
led_temp = Pin(22, Pin.OUT)   

LIGHT_THRESHOLD = 2000  
TEMP_THRESHOLD = 35.0    

def connect_wifi():
    wifi = network.WLAN(network.STA_IF)
    wifi.active(True)
    wifi.connect('Wokwi-GUEST', '')
    
    while not wifi.isconnected():
        time.sleep(1)

    print("WiFi Connected:", wifi.ifconfig())
    return True

def connect_mqtt():
    client = MQTTClient(CLIENT_ID, MQTT_BROKER,port=1883)
    client.connect()
    print("Connected to MQTT broker:", MQTT_BROKER)
    return client


def read_sensors():
    light_value = ldr.read()
    temp_value = temp_sensor.read()   
    voltage = (temp_value / 4095) * 3.3  
    temperature = voltage * 100          
    return light_value, temperature

def main():
    connect_wifi()
    client = connect_mqtt()

    while True:
        light, temperature = read_sensors()
        print(f"Light: {light}, Temperature: {temperature:.2f}°C")

        data = {"light": light, "temperature": temperature}
        client.publish(TOPIC_SENSOR, ujson.dumps(data))
        print("Published to MQTT:", data)

        # Auto control logic
        if light < LIGHT_THRESHOLD:
            led_light.value(1)  # Turn ON LED1 if dark
        else:
            led_light.value(0)  # Turn OFF if bright

        if temperature > TEMP_THRESHOLD:
            led_temp.value(1)   # Turn ON LED2 if hot
        else:
            led_temp.value(0)   # Turn OFF if cool

        time.sleep(3) 

main()
