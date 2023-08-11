def swim(is_full):
    if is_full:
        print("I'm not swimming!")

def drown():
    is_full = is_full(11)
    if is_full:
        print("I'm drowning!")
    else:
        print("I'm not drowning!")

def is_full(food_amount):
    print("I'm eating!")
    if food_amount > 10:
        return True
    else:
        return False
    

drown()
swim(True)

