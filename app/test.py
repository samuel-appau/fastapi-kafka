# from aiokafka import AIOKafkaConsumer, AIOKafkaProducer
import kafka as kf
import json
# import asyncio

KAFKA_BOOTSTRAP_SERVERS= 'broker:9092'
KAFKA_TOPIC="messages_data"
KAFKA_CONSUMER_GROUP="group-id"

message = {"message": "hello world"}



def start_producer():
    producer = kf.KafkaProducer(bootstrap_servers=KAFKA_BOOTSTRAP_SERVERS)
    # await producer.start()
    # try:
    print(f'Sending message with value: {message}')
    value_json_in_bytes = json.dumps(dict(message)).encode('utf-8')
    # await producer.send_and_wait(topic=KAFKA_TOPIC, value=value_json_in_bytes)
    producer.send(topic=KAFKA_TOPIC, value=value_json_in_bytes)

    # finally:
    #     await producer.stop()


# async def start_consumer():
#     consumer = AIOKafkaConsumer(KAFKA_TOPIC,
#                             bootstrap_servers='192.168.124.190:9092', group_id=KAFKA_CONSUMER_GROUP)
#     await consumer.start()
#     try:
#         async for msg in consumer:
#             print(f'Consumer msg: {msg}')
#     finally:
#         await consumer.stop()


start_producer()
    # asyncio.run(start_consumer())