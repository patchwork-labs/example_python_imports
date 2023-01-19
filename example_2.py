#from example_1 import how_many_cows
import example_1
#from kafka import KafkaConsumer, KafkaProducer
import kafka.chess as k

consumer = k.KafkaConsumer(
    'my-topic',
     bootstrap_servers=['kafka:9092']
)

greg = k.KafkaProducer(
    bootstrap_servers=['kafka:9092']
)

example_1.how_many_cows()
print("wowza")