hash_map = {}

# Inserting key-value pairs
hash_map['name'] = 'Rizwan'
hash_map['age'] = 25
hash_map['location'] = 'Pakistan'

# Accessing values
print(hash_map['name'])  # Output: Rizwan

# Deleting a key-value pair
del hash_map['age']

# Iterating over key-value pairs
for key, value in hash_map.items():
    print(f"{key}: {value}")

# Output:
# name: Rizwan
# location: Pakistan
