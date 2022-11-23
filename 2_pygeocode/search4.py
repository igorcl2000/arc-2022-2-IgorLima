#!/usr/bin/env python3
import socket
import ssl
from urllib.parse import quote_plus
import json

request_text = """\
GET /search?q={}&format=json HTTP/1.1\r\n\
Host: nominatim.openstreetmap.org\r\n\
User-Agent: Search4.py\r\n\
Connection: close\r\n\
\r\n\
"""


def geocode(address):
    unencrypted_sock = socket.socket()
    unencrypted_sock.connect(('nominatim.openstreetmap.org', 443))
    sock = ssl.wrap_socket(unencrypted_sock)
    request = request_text.format(quote_plus(address))
    sock.sendall(request.encode('ascii'))
    raw_reply = b''
    while True:
        more = sock.recv(4096)
        if not more:
            break
        raw_reply += more
    reply = raw_reply.decode('utf-8')
    reply = reply[reply.find('['):]
    return json.loads(reply[:reply.find(reply[-1])])


if __name__ == '__main__':
    address = 'Belarmino Vilela Junqueira, Ituiutaba, MG'
    reply = geocode(address)
    print('Endereço buscado: {0}\n'.format(address))
    for i in range(len(reply)):
        print('\tResultado {0}:\n'.format(str(i + 1)))
        print('\t\tCEP: {0}\n'.format(reply[i]['display_name'].split(', ')[-2]))
        print('\t\t(Latitude, Longitude): ({0}, {1})\n'.format(str(reply[i]['lat']), str(reply[i]['lon'])))