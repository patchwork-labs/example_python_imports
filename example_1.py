from resources import test_python

def calculate_size():
    return 4
print("size calculated")

class pants:
    def __init__(self):
        self.size = 100

    def string_version(self):
        return "Pant of size "+str(self.size)
    
class shirts:
    def __init__(self):
        self.size = 50

    def string_version(self):
        return "Shirt of size "+str(self.size)

jeans = pants()
polo = shirts()
print(jeans.string_version())
print(polo.string_version())

