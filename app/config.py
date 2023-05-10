import asyncio

# env Variable
KAFKA_BOOTSTRAP_SERVERS= "192.168.124.190:9092"
KAFKA_TOPIC="kafka"
KAFKA_CONSUMER_GROUP="group-id"
loop = asyncio.get_event_loop()
