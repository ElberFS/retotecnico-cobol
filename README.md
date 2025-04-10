# Reporte de Transacciones Bancarias

## Introducción
Este proyecto es una aplicación de línea de comandos (CLI) que procesa un archivo CSV con transacciones bancarias y genera un reporte con la siguiente información:
- **Balance Final**: Calculado como la suma de los montos de transacciones de tipo "Crédito" menos la suma de los montos de tipo "Débito".
- **Transacción de Mayor Monto**: Identifica el ID y el monto de la transacción más alta.
- **Conteo de Transacciones**: Número total de transacciones de cada tipo.

## Instrucciones de Ejecución
### Requisitos
- Tener instalado **Python 3**

### Instalación
No se requieren dependencias adicionales. Solo necesitas clonar el repositorio y ejecutar el script.

```bash
# Clonar el repositorio
https://github.com/ElberFS/retotecnico-cobol.git
cd retotecnico-cobol
```

### Uso
Para ejecutar la aplicación, usa el siguiente comando en la terminal:

```bash
python script.py transacciones.csv
```

Donde `transacciones.csv` es el archivo con los datos de las transacciones.

## Enfoque y Solución
El programa sigue estos pasos:
1. **Lectura del archivo CSV**: Se carga el archivo y se procesan sus datos.
2. **Cálculo del balance final**: Se suman los montos de las transacciones de tipo "Crédito" y se restan los de tipo "Débito".
3. **Detección de la transacción con mayor monto**: Se busca la transacción con el monto más alto.
4. **Conteo de transacciones por tipo**: Se contabilizan cuántas transacciones hay de cada tipo.
5. **Impresión del reporte en la terminal**.

Se ha diseñado la aplicación con código claro y estructurado para facilitar su mantenimiento y escalabilidad.

## Estructura del Proyecto
```
retotecnico-cobol/
│── script.py         # Código principal de la aplicación
│── transacciones.csv # Archivo de ejemplo con datos de transacciones
│── README.md         # Documentación del proyecto
```

## Contacto
Si tienes dudas o sugerencias, puedes abrir un issue en el repositorio o contactarme. 🚀

