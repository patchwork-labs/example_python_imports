from resources import test_python

def calculate_size():
    return 4
print("size calculated")

def new_doubled_function():
    return 6

class clothing:
    def __init__(self):
        self.material = "cloth"

class pants(clothing):
    def __init__(self):
        self.size = 100

    def string_version(self):
        return "Pant of size "+str(self.size)
    
class shirts(clothing):
    def __init__(self):
        self.size = 50

    def string_version(self):
        return "Shirt of size "+str(self.size)
    
def make_pants_and_shirt():
    jeans = pants()
    polo = shirts()
    print(jeans.string_version())
    print(polo.string_version())

make_pants_and_shirt()
answer = test_python.test_python_print()

