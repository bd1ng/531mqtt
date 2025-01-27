# subscriber.py
import paho.mqtt.client as mqtt
import time
import requests
import google.generativeai as genai
from dotenv import load_dotenv, find_dotenv
import os

dotenv_path = find_dotenv()
load_dotenv(dotenv_path=dotenv_path)

key = os.getenv("KEY")

genai.configure(api_key=key)
model = genai.GenerativeModel('gemini-1.5-flash')

chat = model.start_chat(history=[])

def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Successfully connected to broker")
        # Subscribe to topic
        client.subscribe("pythontest/sensors/mysensor")
    else:
        print(f"Connection failed with code {rc}")

def on_message(client, userdata, msg):
    response = chat.send_message(f"In one word, what's the ideal animal that lives in these conditions that is NOT a human: {msg.payload.decode()}")
    if hasattr(response, "candidates") and response.candidates:  
        ideal_animal = response.candidates[0].content.parts[0].text.strip()
    else:
        ideal_animal = "Unknown" 

    print(f"The ideal animal is: {ideal_animal}.")

# Create subscriber client
subscriber = mqtt.Client()
subscriber.on_connect = on_connect
subscriber.on_message = on_message

# Connect to public broker
print("Connecting to broker...")
subscriber.connect("test.mosquitto.org", 1883, 60)

# Start the subscriber loop
subscriber.loop_start()

try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    print("Stopping subscriber...")
    subscriber.loop_stop()
    subscriber.disconnect()

