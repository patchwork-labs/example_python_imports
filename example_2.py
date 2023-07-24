#from example_1 import calculate_size
import example_1
import math.gcd as g
#from kafka import KafkaConsumer, KafkaProducer
# import kafka.chess as k
# import kafka.query.input as i
# from kafka import KafkaConsumer, blarg
import mysql.connector
 
# Creating connection object
mydb = mysql.connector.connect(
    host = "localhost",
    user = "yourusername",
    password = "your_password"
)

# consumer = KafkaConsumer(
#     'my-topic',
#      bootstrap_servers=['kafka:9092']
# )

# greg = k.KafkaProducer(
#     bootstrap_servers=['kafka:9092']
# )

# i()
def call_calculate():
 example_1.calculate_size()
print("wowza")
g(4,2)
