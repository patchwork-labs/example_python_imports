from resources import test_python as tp

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
    jean_size = jeans.string_version()
    polo_size = polo.string_version()

make_pants_and_shirt()
answer = tp.test_python_print()