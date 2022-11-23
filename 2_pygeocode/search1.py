#!/usr/bin/env python3

from geopy.geocoders import Nominatim

if __name__ == '__main__':
    address = 'Belarmino Vilela Junqueira, Ituiutaba, MG'
    user_agent = 'Search1'
    location = Nominatim(user_agent=user_agent).geocode(address, exactly_one=False)
    print('Endereço buscado: {0}\n'.format(address))
    for i in range(len(location)):
        print('\tResultado {0}:\n'.format(str(i + 1)))
        print('\t\tCEP: {0}\n'.format(location[i].address.split(', ')[-2]))
        print('\t\t(Latitude, Longitude): ({0}, {1})\n'.format(str(location[i].latitude), str(location[i].longitude)))
