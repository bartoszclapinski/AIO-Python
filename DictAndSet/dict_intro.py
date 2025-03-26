vehicles = {
    'dream': 'Honda',
    'roadster': 'BMW R1100',
    'er5': 'Kawasaki ER5',
    'can-am': 'Bombardier Can-Am',
    'virago': 'Yamaha XV250',
    'tenere': 'Suzuki Ténéré',
    'jimny': 'Suzuki Jimny',
    'fiesta': 'Ford Fiesta',
    'roadster': 'Triumph Street Triple'
}

my_car = vehicles['fiesta']
print(my_car)

commuter = vehicles['virago']
print(commuter)

learner = vehicles.get('er5')
print(learner)

learner = vehicles.get('ER5', 'Not found')
print(learner)

print('-' * 40)

for key in vehicles:
    print(key)

print('-' * 40)

for key in vehicles:
    print(key, vehicles[key])

print('-' * 40)
    
for key, value in vehicles.items():
    print(key, value)

print('-' * 40)

vehicles['starfighter'] = 'Lockheed F-104'
vehicles['learjet'] = 'Bombardier Learjet 75'
vehicles['toy'] = 'Glider'

print('-' * 40)

vehicles['virago'] = 'Yamaha XV535'

