# 🚀 BruteForce Pro - Descompresor de Archivos Protegidos

## ✨ Visión General

**BruteForce Pro** es una herramienta de alto rendimiento desarrollada en Python para la recuperación de contraseñas de archivos comprimidos (**ZIP, RAR, 7z**) mediante ataques de diccionario. Diseñada para ser eficiente y resiliente, utiliza procesamiento paralelo y un sistema de guardado automático para optimizar cada segundo de procesamiento.

> [!IMPORTANT]
> **Optimizado para Windows**: Incluye una alarma sonora de sistema y notificaciones visuales inmediatas al encontrar la clave.

![Banner BruteForce Pro](https://drive.google.com/file/d/1ZRIvR3hkUSZZAW4rLgFUbDpqhDATXKZv/view?usp=sharing) 

---

## ⚡ Características Principales

* **Multiprocesamiento**: Aprovecha todos los núcleos de tu CPU para acelerar el descifrado.
* **Sistema de Persistencia**: Si el proceso se detiene, el script guarda la línea exacta para reanudar después.
* **Interfaz Visual**: Barras de progreso dinámicas con tiempo estimado mediante `tqdm`.
* **Alarma Sonora**: Notificación auditiva persistente en Windows al completar con éxito.
* **Extracción Automática**: Descomprime el contenido inmediatamente al hallar la clave correcta.

---

## 📋 Requisitos

Antes de comenzar, asegúrate de tener instalado:

1.  **Python 3.x**: [Descargar aquí](https://www.python.org/downloads/)
2.  **7-Zip (CLI)**: Es obligatorio tener acceso al ejecutable `7z.exe`. [Descargar aquí](https://www.7-zip.org/download.html)
3.  **Dependencias de Python**:
    ```bash
    pip install tqdm
    ```

---

## ⚙️ Configuración

1.  **Ruta de 7-Zip**: Por defecto, el script busca en `C:\Program Files\7-Zip\7z.exe`. Si tu instalación es diferente, modifica la variable `RUTA_7Z` en el código.
2.  **Diccionario**: Prepara un archivo `.txt` con una contraseña por línea.

---

## 🚀 Guía de Uso

1.  **Ejecución**: Inicia el script desde tu terminal:
    ```bash
    python index.py
    ```
2.  **Configuración de sesión**:
    * Indica la ruta del archivo comprimido.
    * Indica la ruta del archivo de diccionario.
    * **Selecciona el modo**: 
        * `[1] Máximo poder`: Usa todos los hilos del procesador.
        * `[2] Ahorro`: Usa un solo núcleo para tareas en segundo plano.

3.  **Reanudación**: Si el programa detecta el archivo `progreso_linea.txt`, te preguntará automáticamente si deseas continuar desde el último punto.

4.  **Alarma de Éxito**: Al encontrar la clave, sonará una alarma. Presiona `Ctrl + C` para detener el sonido.

---

## 📂 Archivos y Carpetas Generados

| Recurso | Función |
| :--- | :--- |
| `progreso_linea.txt` | Índice de la última línea procesada. |
| `ultimo_intento.txt` | Registro de la última contraseña probada. |
| `extraccion_exitosa/` | Carpeta con los archivos ya descomprimidos. |
| `REPORTE_EXITO.txt` | Informe final con la clave encontrada y estadísticas. |

---

## ⚠️ Aviso Legal

Este proyecto está destinado exclusivamente a la recuperación de archivos propios, auditorías de seguridad autorizadas o fines educativos. **El autor no se hace responsable del uso indebido o ilegal de esta herramienta.**

---

## 🤝 Contribuciones e Ideas

¡Las mejoras son bienvenidas! Siéntete libre de abrir un **Issue** o enviar un **Pull Request** para:
* Optimizar el motor de búsqueda.
* Agregar compatibilidad nativa con Linux/macOS.
* Implementar soporte para otros formatos de archivo.

---

## 📄 Licencia

Este proyecto está bajo la **Licencia MIT**. Consulta el archivo `LICENSE` para más información.
