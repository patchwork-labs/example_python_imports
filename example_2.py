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

def new_doubled_function():
    return 8

# consumer = KafkaConsumer(
#     'my-topic',
#      bootstrap_servers=['kafka:9092']
# )

# greg = k.KafkaProducer(
#     bootstrap_servers=['kafka:9092']
# )

# I()
def call_me_baby():
 return call_calculate()

def call_calculate():
 answer = example_1.calculate_size()
 return answer
calc = call_me_baby()
print("wowza")
g(4,2)
