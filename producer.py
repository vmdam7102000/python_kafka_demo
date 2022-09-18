from email.message import Message
from ensurepip import bootstrap
import time
import json
import random
from datetime import date, datetime
from data_generator import generate_message
from kafka import KafkaProducer

# message will be serialized as json
def serializer(message):
    return json.dumps(message).encode('utf-8')

# kafka producer
producer = KafkaProducer(
    bootstrap_servers = ['localhost:9092'],
    value_serializer = serializer
)

if __name__ == '__main__':
    # infinite loop run until stop the program
    while True:
        # generate message
        dummy_message = generate_message()

        # send it to 'message' topic
        print(f'producing message @{datetime.now()}| Message ={str(dummy_message)}')
        producer.send('message',dummy_message)

        # sleep for a random number of seconds
        time_to_sleep = random.randint(1,11)
        time.sleep(time_to_sleep)

