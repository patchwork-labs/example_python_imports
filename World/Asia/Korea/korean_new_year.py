def date():
    return "1 January"

def celebrate(num_people, location, date):
    """Celebrate the new year in Korea."""
    if num_people > 3:
        print("You'll need to book a table.")
    else:
        print("You can just walk in.")

    # Check age
    age = 19
    police_check(age)

    print("The location is", location)
    print("The date is", date)

def police_check(age):
    """Check if a person is over 18."""
    if age > 18:
        print("You are over 18")
    else:
        print("You are under 18")

celebrate()