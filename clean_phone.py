import pandas as pd


def validate_phone(phone_number):
    """

    Tests if phone numbers are valid

    Arguments:
    phone_number A Pandas Series of phone numbers as string objects

    Returns:
    A boolean Pandas Series
    """
    bool_phone = phone_number.str.contains(r"^\d{3}[-]?\d{3}[-]?\d{4}")
    return bool_phone


numbers = pd.Series(['609-713-3421', '555-555-5555',
                     '123-456-7890', '1898-48-47454'])
print(validate_phone(numbers))
