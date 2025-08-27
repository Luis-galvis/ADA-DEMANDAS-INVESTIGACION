import pandas as pd
import csv  # Importa el módulo csv estándar

# Ruta de tu archivo Excel
excel_file = 'dataset_ADA_2023_2025.xlsx'

# Leer todas las hojas
xls = pd.ExcelFile(excel_file)

for sheet_name in xls.sheet_names:
    df = pd.read_excel(xls, sheet_name=sheet_name)
    
    # Limpiar encabezado (quitar espacios, saltos de línea)
    df.columns = df.columns.str.strip().str.replace('\n',' ').str.replace('\r',' ')
    
    # Guardar CSV con comillas para textos que contienen comas, separador coma
    csv_file = sheet_name.lower().replace(' ','_') + '.csv'
    df.to_csv(csv_file, index=False, sep=',', quoting=csv.QUOTE_ALL, encoding='utf-8')
    
    print(f"Guardado {csv_file} listo para subir a BigQuery")
