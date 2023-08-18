def distance_between_cities(cityA, cityB):
    #Distance is rounded to 100 kilometers
    distance = ((cityA[0] - cityB[0])**2 + (cityA[1] - cityB[1])**2)**0.5 * 100
    return distance

def print_distance_dataset(cities):
    distance_max = 120

    print('\t\t' + '\t'.join(cities.keys()))
    print('--------' + len(cities) * '----')
    for cityA in cities.keys():
        print(cityA, end='\t\t')
        for cityB in cities.keys():
            # If cities are different, compare distance
            if cityA != cityB:
                distance = round(distance_between_cities(cities[cityA], cities[cityB]), 2) # Au mètre près chacal
                print(distance, end='\t') if distance < distance_max else print(' ', end='\t')
            else:
                print(' ', end='\t')
        print("")

cities = {
    'Bru': [50.8333, 4.3333],   # Bruxelles
    'Lie': [50.6497, 5.5706],   # Liege
    'Mon': [50.4550, 3.9520],   # Mons
    'Nam': [50.4667, 4.8667],   # Namur
    'Arl': [49.6836, 5.8167],   # Arlon"
    'Anv': [50.2252, 5.7986]    # Anvers
}

print_distance_dataset(cities)
