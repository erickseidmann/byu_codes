'''def deposit(amount):
    # In order for this program to work correctly and
    # for the bank records to be correct, we must not
    # allow someone to deposit a zero or negative amount.
    assert amount > 0
      
    assert temperature < 0

    assert len(given_name) > 0

    assert balance == 0

    assert school_year != "senior"'''
# weather.py

def cels_from_fahr(fahr):
    """Convert a temperature in Fahrenheit to
    Celsius and return the Celsius temperature.
    """
    cels = (fahr - 32) * 5 / 9
    return cels