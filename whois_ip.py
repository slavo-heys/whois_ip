import requests
from ipwhois import IPWhois
import socket

# Wyświetlanie informacji o adresie IP z serwisu ip-api.com
def print_ip(response):    
    print(f"Kraj: {response['country']}")
    print(f"Miasto: {response['city']}")
    print(f"Region: {response['regionName']}")
    print(f"Kod pocztowy: {response['zip']}")
    print(f"Szerokość geograficzna: {response['lat']}")
    print(f"Długość geograficzna: {response['lon']}")
    print(f"Strefa czasowa: {response['timezone']}")
    print(f"ISP: {response['isp']}")
    print(f"Organizacja: {response['org']}")

    
# Wyświetlanie informacji o adresie IP
def print_ip_info(obj, brak):
    print(f"IP: {obj['ip']}")
    try:
        print(f"Typ adresu IP: {obj['type']}")
    except:
        print(f"Typ adresu IP: {brak}")

    try:
        print(f'Kontynent: {obj["continent"]}')
    except:
        print(f'Kontynent: {brak}')

    try:
        print(f"Kraj: {obj['country']}")
    except:
        print(f"Kraj: {brak}")

    try:
        print(f"Miasto: {obj['city']}")
    except:
        print(f"Miasto: {brak}")

    try:
        print(f"Region: {obj['region']}")
    except:
        print(f"Region: {brak}")

    try:
        print(f"Kod pocztowy: {obj['postal']}")
    except:
        print(f"Kod pocztowy: {brak}")

    try:
        print(f"Szerokość geograficzna: {obj['latitude']}")
    except:
        print(f"Szerokość geograficzna: {brak}")

    try:
        print(f"Długość geograficzna: {obj['longitude']}")
    except:
        print(f"Długość geograficzna: {brak}")

    try:
        print(f"Strefa czasowa: {obj['timezone']}")
    except:
        print(f"Strefa czasowa: {brak}")

    try:
        print(f"Z Unii E: {obj['is_eu']}")
    except:
        print(f"Z Unii E: {brak}")

    try:
        print(f"Kierunkowy: {obj['calling_code']}")
    except:
        print(f"Kierunkowy telefonu: {brak}")

    try:
        print(f"Connection: {obj['connection']}")
    except:
        print(f"Connection: {brak}")
        
    try:
        print(f"Waluta: {obj['currency']}")
    except:
        print(f"Waluta: {brak}")

    try:
        print(f"Security: {obj['security']}")
    except:
        print(f"Security: {brak}")

    # zapisywanie danych do pliku
    with open("ip.txt", "a") as f:
        record = (f"\'{obj['ip']}\':\'{obj['country']}\'\n")
        f.write(record)

# Pobieranie adresu IP od użytkownika
ip_address = input("Podaj adres IP lub domeny do sprawdzenia: ")

print("-"*50)
print("\n")
print('Metoda I')
print("\n")

# Wyświetlanie informacji o adresie IP
try:
    host_name = socket.gethostbyaddr(ip_address)[0]
    print(f"Nazwa hosta: {host_name}")
except socket.herror:
    print("Nie znaleziono nazwy hosta dla tego adresu IP.")

try:
    ip = socket.gethostbyname(host_name)
    print(f"Adres IP: {ip}")
except socket.gaierror:
    print("Nie udało się znaleźć adresu IP dla tej nazwy hosta.")

try:
    geo_info = socket.getaddrinfo(ip, None, socket.AF_INET, socket.SOCK_STREAM)
    latitude, longitude = geo_info[0][4][:2]
    print(f"Szerokość geograficzna: {latitude}")
    print(f"Długość geograficzna: {longitude}")
except socket.gaierror:
    print("Nie udało się uzyskać informacji geograficznej dla tego adresu IP.")

print("-"*50)
print("\n")
print('Metoda II')
print("\n")

# Pobieranie danych z serwisu ip-api.com
try:
    response = requests.get(f"http://ip-api.com/json/{ip}").json()
    print_ip(response)
except:
    print("Nie można pobrać informacji o adresie IP z serwisu ip-api.com")



print("-"*50)
print("\n")
print('Metoda III')
print("\n")

# Pobieranie dodatkowych informacji z serwisu ipwhois
try:
    obj = requests.get(f"http://ipwho.is/{ip}").json()
    brak = "Brak danych"
    print_ip_info(obj, brak)
except:
    print("Nie można pobrać dodatkowych informacji o adresie IP")


