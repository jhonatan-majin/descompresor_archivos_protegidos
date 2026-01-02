import subprocess
import os
import sys
import time
from concurrent.futures import ProcessPoolExecutor, as_completed
from tqdm import tqdm

# Intentar importar winsound para sonidos de Windows
try:
    import winsound
    WINDOWS = True
except ImportError:
    WINDOWS = False

# Configuración
RUTA_7Z = r"C:\Program Files\7-Zip\7z.exe"
ARCHIVO_PROGRESO = "progreso_linea.txt"
LOG_ULTIMO_TEXTO = "ultimo_intento.txt"
CARPETA_SALIDA = "extracccion_exitosa"

def intentar_descomprimir(archivo, password, salida):
    try:
        process = subprocess.run(
            [RUTA_7Z, "x", f"-p{password}", archivo, f"-o{salida}", "-y"],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
            creationflags=subprocess.CREATE_NO_WINDOW
        )
        return password if process.returncode == 0 else None
    except:
        return None

def formato_tiempo_extenso(segundos):
    horas, rem = divmod(segundos, 3600)
    minutos, segundos = divmod(rem, 60)
    return f"{int(horas)}h {int(minutos)}m {int(segundos)}s"

def main():
    print("="*60)
    print("   BRUTEFORCE PRO - ALARMA DE SISTEMA WINDOWS")
    print("="*60)

    if not os.path.exists(RUTA_7Z):
        print(f"\n[!] ERROR: No se encontró 7z.exe")
        return

    archivo_obj = input("[?] Archivo a procesar: ").strip()
    dict_obj = input("[?] Diccionario: ").strip()

    if not os.path.exists(dict_obj):
        print(f"[!] El diccionario '{dict_obj}' no existe.")
        return

    punto_inicio = 0
    if os.path.exists(ARCHIVO_PROGRESO):
        try:
            with open(ARCHIVO_PROGRESO, "r") as f_p:
                content = f_p.read().strip()
                if content:
                    punto_inicio = int(content)
                    print(f"\n[!] PROGRESO DETECTADO: Línea {punto_inicio:,}")
                    res = input("[?] ¿Deseas reanudar desde aquí? (s/n): ").lower()
                    if res != 's':
                        punto_inicio = 0
        except Exception as e:
            print(f"[*] No se pudo leer el progreso previo: {e}")
            punto_inicio = 0

    op = input("\n[1] Máximo Poder (Todos los núcleos)\n[2] Ahorro (1 núcleo)\nOpción: ").strip()
    num_nucleos = os.cpu_count() if op == "1" else 1

    print("[*] Escaneando diccionario...")
    with open(dict_obj, 'rb') as f:
        total_lineas = sum(1 for _ in f)
    
    if punto_inicio >= total_lineas:
        punto_inicio = 0

    tiempo_inicio_global = time.time()
    contrasena_final = None
    LOTE_TAMANO = 500 

    with ProcessPoolExecutor(max_workers=num_nucleos) as executor:
        with open(dict_obj, 'r', encoding='utf-8', errors='ignore') as f:
            with tqdm(total=total_lineas, 
                      desc="Analizando", 
                      unit="pw", 
                      colour="green",
                      bar_format="{l_bar}{bar}| {n_fmt}/{total_fmt} [Faltan: {remaining}]") as pbar:
                
                if punto_inicio > 0:
                    for _ in range(punto_inicio):
                        if not f.readline(): break
                    pbar.update(punto_inicio)
                
                linea_actual = punto_inicio
                batch = []
                for linea in f:
                    p = linea.strip()
                    if p: batch.append(p)
                    
                    if len(batch) >= LOTE_TAMANO:
                        futuros = {executor.submit(intentar_descomprimir, archivo_obj, pwd, CARPETA_SALIDA): pwd for pwd in batch}
                        for futuro in as_completed(futuros):
                            res = futuro.result()
                            if res:
                                contrasena_final = res
                                break
                            pbar.update(1)
                            linea_actual += 1
                        
                        if contrasena_final: break
                        
                        with open(ARCHIVO_PROGRESO, "w") as f1: f1.write(str(linea_actual))
                        with open(LOG_ULTIMO_TEXTO, "w") as f2: f2.write(f"Linea: {linea_actual}\nClave: {batch[-1]}")
                        batch = []

                if not contrasena_final and batch:
                    for p in batch:
                        if intentar_descomprimir(archivo_obj, p, CARPETA_SALIDA):
                            contrasena_final = p
                            break
                        pbar.update(1)

    tiempo_total = time.time() - tiempo_inicio_global

    if contrasena_final:
        with open("REPORTE_EXITO.txt", "w") as r:
            r.write(f"Archivo: {archivo_obj}\nClave: {contrasena_final}\nTiempo: {formato_tiempo_extenso(tiempo_total)}")
        
        print("\n" + "*"*60)
        print(f"  ¡CONTRASEÑA ENCONTRADA!: {contrasena_final}")
        print(f"  TIEMPO TOTAL: {formato_tiempo_extenso(tiempo_total)}")
        print("*"*60)
        
        if os.path.exists(ARCHIVO_PROGRESO): os.remove(ARCHIVO_PROGRESO)
        if os.path.exists(LOG_ULTIMO_TEXTO): os.remove(LOG_ULTIMO_TEXTO)
        
        # --- NUEVA ALARMA DE SISTEMA ---
        print("\n[!] Presiona Ctrl+C para detener la alarma.")
        while True:
            try:
                if WINDOWS:
                    try:
                        # Intento 1: Sonido de Nave Espacial (Beep de hardware)
                        winsound.Beep(3000, 150) 
                        winsound.Beep(4000, 150)
                        winsound.Beep(3500, 150)
                    except RuntimeError:
                        # Intento 2: Si falla el Beep, usamos sonido de sistema (Altavoces)
                        winsound.PlaySound("SystemHand", winsound.SND_ALIAS)
                        time.sleep(1)
                else:
                    sys.stdout.write('\a')
                    sys.stdout.flush()
                    time.sleep(0.5)
                
                # Alerta visual por si el sonido falla del todo
                print(" >>> CLAVE ENCONTRADA <<< ", end="\r")
                
            except KeyboardInterrupt:
                print("\n[*] Alarma apagada por el usuario.")
                break
    else:
        print(f"\n[!] Diccionario agotado tras {formato_tiempo_extenso(tiempo_total)}.")

if __name__ == "__main__":
    main()