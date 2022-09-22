#!/.venv/bin/python


import sys
import socket
import geocoder
from phone_iso3166.country import *


def get_address(domain):
    return socket.gethostbyname(domain)


def get_location(host):
    location = geocoder.ip(host)
    return location.city


def get_country(number):
    country = phone_country(number)
    return country


def main():
    if len(sys.argv) > 1:
        print(type(sys.argv[1]))
        param = sys.argv[1]      
        country = get_country(param)
        # host = get_address(sys.argv[1])        
        # city = get_location(host)
        # print(host)
        # print(city)
        print(country)
    else:
        print('you must enter one domain name')


if __name__ == '__main__':
    main()

