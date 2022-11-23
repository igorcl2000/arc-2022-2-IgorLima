#!/usr/bin/env python3
import http.client
import json
from urllib.parse import quote_plus

base = '/search'


def geocode(address):
    path = '{}?q={}&format=json'.format(base, quote_plus(address))
    user_agent = b'Search3.py'
    headers = {b'User-Agent': user_agent}
    connection = http.client.HTTPSConnection('nominatim.openstreetmap.org')
    connection.request('GET', path, None, headers)
    rawreply = connection.getresponse().read()
    reply = json.loads(rawreply.decode('utf-8'))
    print(reply[0]['lat'], reply[0]['lon'])


if __name__ == '__main__':
    address = 'Belarmino Vilela Junqueira, Ituiutaba, MG'
    reply = geocode(address)
    print('Endereço buscado: {0}\n'.format(address))
    for i in range(len(reply)):
        print('\tResultado {0}:\n'.format(str(i + 1)))
        print('\t\tCEP: {0}\n'.format(reply[i]['display_name'].split(', ')[-2]))
        print('\t\t(Latitude, Longitude): ({0}, {1})\n'.format(str(reply[i]['lat']), str(reply[i]['lon'])))