#!/usr/bin/env python3
import requests


def geocode(address):
    base = 'https://nominatim.openstreetmap.org/search'
    parameters = {'q': address, 'format': 'json'}
    user_agent = 'Search2.py'
    headers = {'User-Agent': user_agent}
    response = requests.get(base, params=parameters, headers=headers)
    reply = response.json()
    print(reply[0]['lat'], reply[0]['lon'])
    print('Endereço buscado: {0}\n'.format(address))
    for i in range(len(reply)):
        print('\tResultado {0}:\n'.format(str(i + 1)))
        print('\t\tCEP: {0}\n'.format(reply[i]['display_name'].split(', ')[-2]))
        print('\t\t(Latitude, Longitude): ({0}, {1})\n'.format(str(reply[i]['lat']), str(reply[i]['lon'])))


if __name__ == '__main__':
    address = 'Belarmino Vilela Junqueira, Ituiutaba, MG'
    geocode(address)
