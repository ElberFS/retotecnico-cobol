import csv
import argparse

# Función para procesar el archivo CSV y generar el reporte
def procesar_csv(archivo):
    balance = 0  # Inicializamos el balance en 0
    transacciones = []  # Lista para almacenar las transacciones
    conteo = {"Crédito": 0, "Débito": 0}  # Diccionario para contar tipos de transacción
    
    # Abrimos el archivo CSV y leemos los datos
    with open(archivo, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)  # Leemos el archivo como diccionario
        for fila in reader:
            tipo = fila['tipo']  # Obtenemos el tipo de transacción (Crédito o Débito)
            monto = float(fila['monto'])  # Convertimos el monto a número flotante
            transacciones.append((fila['id'], tipo, monto))  # Agregamos la transacción a la lista
            conteo[tipo] += 1  # Incrementamos el conteo del tipo de transacción
            balance += monto if tipo == "Crédito" else -monto  # Sumamos o restamos según el tipo
    
    # Identificamos la transacción con el monto más alto
    transaccion_mayor = max(transacciones, key=lambda x: x[2])
    
    # Mostramos el reporte en la terminal
    print("Reporte de Transacciones")
    print("-" * 45)
    print(f"Balance Final: {balance:.2f}")
    print(f"Transacción de Mayor Monto: ID {transaccion_mayor[0]} - {transaccion_mayor[2]:.2f}")
    print(f"Conteo de Transacciones: Crédito: {conteo['Crédito']} Débito: {conteo['Débito']}")

# Punto de entrada del programa
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Procesar un archivo CSV de transacciones bancarias.")
    parser.add_argument("archivo", help="Ruta del archivo CSV")  # Argumento para recibir el archivo CSV
    args = parser.parse_args()  # Analizamos los argumentos pasados al script
    procesar_csv(args.archivo)  # Llamamos a la función con el archivo proporcionado
