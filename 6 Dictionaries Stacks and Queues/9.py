# Create a dictionary describing a mobile phone. Use at least 6 key-value pairs of data. Use different value types. Then, using 'for' loop, display the contents of the dictionary. To read a key and value, use the items() method.

mobile_phone = {
    'OS': 'Android',
    'memory_GB': 12,
    'storage_GB': 512,
    'release_date': 2021,
    'screen_size_in': 6.1,
    'screen_type': "AMOLED",
    'has_headphone_jack': True
}

for key, value in mobile_phone.items():
    print(key, '=', value)