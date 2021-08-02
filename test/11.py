cars = {
    'BMW': 'x5',
    'Mercedes-Benz': 'E220',
    'Audi': 'Q7'
}

for key in cars:
    print("%s -> %s" % (key, cars[key]))

print('-' * 15)

for key in cars.keys():
    print("%s -> %s" % (key, cars[key]))