people = {
    'Rajat': {
        'phone': '229283844',
        'addr': 'New York'
    },
    'Parul': {
        'phone': '910223442',
        'addr': 'LA'
    },
    'Mansi': {
        'phone': '315333138',
        'addr': 'Brazil'
    }
}
labels = {
'phone': 'phone number',
'addr': 'address'
}
name = input('Name: ')
request = input('Phone number (p) or address (a)? ')
if request == 'p': key = 'phone'
if request == 'a': key = 'addr'

if name in people: print("%s's %s is %s." % (name, labels[key], people[name][key]))