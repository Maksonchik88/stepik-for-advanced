from pprint import pprint
pets = [('Hatiko', 'Parker', 'Wilson', 50),
        ('Rusty', 'Josh', 'King', 25),
        ('Fido', 'John', 'Smith', 28),
        ('Butch', 'Jake', 'Smirnoff', 18),
        ('Odi', 'Emma', 'Wright', 18),
        ('Balto', 'Josh', 'King', 25),
        ('Barry', 'Josh', 'King', 25),
        ('Snape', 'Hannah', 'Taylor', 40),
        ('Horry', 'Martha', 'Robinson', 73),
        ('Giro', 'Alex', 'Martinez', 65),
        ('Zooma', 'Simon', 'Nevel', 32),
        ('Lassie', 'Josh', 'King', 25),
        ('Chase', 'Martha', 'Robinson', 73),
        ('Ace', 'Martha', 'Williams', 38),
        ('Rocky', 'Simon', 'Nevel', 32)]

"""
result = {
('Parker', 'Wilson', 50): ['Hatiko'],
('Josh', 'King', 25): ['Rusty', 'Balto','Barry', 'Lassie'],
('John', 'Smith', 28): ['Fido'],
('Jake', 'Smirnoff', 18): ['Butch']
.......
}
"""

result = {}
for key in pets:
        if key[1:] not in result:
                result[key[1]] = [key[0]]
        else: # if key in result
                result[key[1:]].append(key[0])

pprint(result)





