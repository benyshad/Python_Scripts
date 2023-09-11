from standard_to_army import convert

def test_format_A():
    assert convert("9 am to 7 pm") == "09:00 to 19:00"
    assert convert("9am to 7pm") == "09:00 to 19:00"
    assert convert("7pm to 9am") == "19:00 to 09:00"
    assert convert("7 pm to 9 am") == "19:00 to 09:00"
    assert convert("11am to 6 pm") == "11:00 to 18:00"
    assert convert("8pm to 5am") == "20:00 to 05:00"

def test_format_B():
    assert convert("4:00 am to 4:00 pm") == "04:00 to 16:00"
    assert convert("4:00 pm to 4:00 am") == "16:00 to 04:00"
    assert convert("4:00am to 4:00pm") == "04:00 to 16:00"
    assert convert("4:00pm to 4:00am") == "16:00 to 04:00"

def test_corner():
    assert convert("12 am to 10 am") == "00:00 to 10:00"
    assert convert("6pm to 12am") == "18:00 to 00:00"
    assert convert("12am to 12:00pm") == "00:00 to 12:00"
    assert convert("12:00 am to 12pm") == "00:00 to 12:00"
