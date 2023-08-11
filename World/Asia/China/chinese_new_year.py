from Korea import korean_new_year

def date():
    return "1 February"

def celebrate(num_people, location, date):
    """Celebrate the new year in China."""
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

def overlapping_celebration(): # TODO: What if date was passed in as a parameter?
    date = date()
    korean_date = korean_new_year.date()
    if korean_date == date:
        print("The Korean New Year overlaps with the Chinese New Year.")
    else:
        print("The Korean New Year does not overlap with the Chinese New Year.")


overlapping_celebration()