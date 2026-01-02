# 🚀 BruteForce Pro - Descompresor de Archivos Protegidos

## ✨ Visión General

BruteForce Pro es una herramienta de Python diseñada para ayudar a recuperar contraseñas de archivos comprimidos (principalmente ZIP, RAR, 7z, etc., compatibles con 7-Zip) utilizando un ataque de diccionario. Este script optimizado soporta procesamiento paralelo para acelerar la búsqueda de contraseñas, guarda el progreso y, para los usuarios de Windows, incluye una alarma sonora al encontrar la contraseña.

¡No más esperas interminables sin saber si tu archivo se está descomprimiendo! Con BruteForce Pro, serás notificado al instante.

[http://googleusercontent.com/image_generation_content/](https://drive.google.com/file/d/1ZRIvR3hkUSZZAW4rLgFUbDpqhDATXKZv/view?usp=sharing)0

## 📋 Requisitos

Antes de usar BruteForce Pro, asegúrate de tener lo siguiente:

* **Python 3.x**: Descárgalo desde [python.org](https://www.python.org/downloads/).
* **7-Zip**: La herramienta de línea de comandos `7z.exe` es esencial. Puedes descargarla e instalarla desde [7-zip.org](https://www.7-zip.org/download.html). Asegúrate de que la ruta a `7z.exe` esté configurada correctamente en el script (`RUTA_7Z`).
* **Módulos de Python**:
    * `tqdm`: Para barras de progreso elegantes.
    * `winsound` (Solo Windows): Para las alarmas de sonido.

Puedes instalar `tqdm` usando pip:

```bash
pip install tqdm

⚙️ Configuración
Instala 7-Zip: Asegúrate de que 7-Zip esté instalado en tu sistema. La ruta predeterminada esperada por el script es C:\Program Files\7-Zip\7z.exe. Si lo instalaste en una ubicación diferente, actualiza la variable RUTA_7Z en el script:

Python

RUTA_7Z = r"C:\Program Files\7-Zip\7z.exe" # ¡Cambia esto si es necesario!
Crea un Diccionario: Necesitarás un archivo de texto (.txt) que contenga una lista de posibles contraseñas, una por línea.

🚀 Uso
Guarda el script: Guarda el código como bruteforce_pro.py.

Ejecuta el script desde la terminal:

Bash

python index.py
Sigue las instrucciones:

El script te pedirá la ruta del archivo comprimido a descifrar.

Luego, te pedirá la ruta de tu archivo de diccionario.

Podrás elegir entre "Máximo Poder (Todos los núcleos)" para un rendimiento más rápido o "Ahorro (1 núcleo)" para usar menos recursos.

Reanudar el progreso: Si el script se interrumpe, creará un archivo progreso_linea.txt y ultimo_intento.txt. La próxima vez que ejecutes el script, te preguntará si deseas reanudar desde el último punto.

🔔 Alarma de Éxito (Solo Windows)
Cuando se encuentra la contraseña, BruteForce Pro no solo la mostrará en la consola, sino que también activará una alarma sonora del sistema Windows para que no te pierdas el momento. Además, mostrará una alerta visual constante en la terminal. Presiona Ctrl+C para detener la alarma.

📂 Archivos Generados
progreso_linea.txt: Guarda la última línea del diccionario procesada, permitiendo reanudar el ataque.

ultimo_intento.txt: Registra la línea y la clave del último intento.

extracccion_exitosa/: Carpeta donde se descomprimirá el contenido si se encuentra la contraseña.

REPORTE_EXITO.txt: Contiene el nombre del archivo, la contraseña encontrada y el tiempo total del proceso.

🤝 Contribuciones
¡Las contribuciones son bienvenidas! Si tienes ideas para mejorar, optimizaciones o nuevas características, no dudes en abrir un issue o enviar un pull request.

📄 Licencia
Este proyecto está bajo la Licencia MIT. Consulta el archivo LICENSE para más detalles.
