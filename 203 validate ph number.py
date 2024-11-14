# 5-Validate phone numbers:
# -Create a regular expression to match valid US phone numbers in different formats
# (e.g., "123-456-7890", "(123) 456-7890", "1234567890").

import re

phone_pattern = r'^(\(\d{3}\)|\d{3}-|\d{3}\s)\d{3}(-|\s)\d{4}$'

phone_numbers = [
    '123-456-7890',
    '(123) 456-7890',
    '1234567890',
    '123 456 7890',
    'invalid phone'
]

for phone in phone_numbers:
    if re.match(phone_pattern, phone):
        print(f'Valid phone: {phone}')
    else:
        print(f'Invalid phone: {phone}')
