import shutil

def obtener_ruta_chrome():
    try:
        # Buscar la ruta del ejecutable de Chrome en el sistema
        ruta_chrome = shutil.which('google-chrome') or shutil.which('chrome') or shutil.which('chromium')
        return ruta_chrome
    except Exception as e:
        print(f"Error al obtener la ruta de Chrome: {e}")
        return None

# Obtener la ruta de Chrome
ruta_chrome = obtener_ruta_chrome()
print(f"Ruta de Chrome: {ruta_chrome}")
