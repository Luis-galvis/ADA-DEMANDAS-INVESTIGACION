import pandas as pd
import numpy as np
import re

# Cargar dataset
df = pd.read_excel('accesibilidad.xlsx', sheet_name='Hoja1')

print(f"Dataset cargado con {len(df)} filas y {len(df.columns)} columnas")
print("Columnas:", list(df.columns))

# Limpiar columnas numéricas (similar antes)
def clean_percentage(x):
    if pd.isna(x):
        return np.nan
    m = re.search(r'(\d+(\.\d+)?)%', str(x))
    return float(m.group(1))/100 if m else np.nan

if 'Widgets (%)' in df.columns:
    df['Widgets (%)'] = df['Widgets (%)'].apply(clean_percentage)

def clean_money(x):
    if pd.isna(x):
        return np.nan
    s = str(x).replace('$','').replace(',','').strip()
    try:
        return float(s)
    except:
        return np.nan

if 'Monto ($)' in df.columns:
    df['Monto ($)'] = df['Monto ($)'].apply(clean_money)

def clean_demandas(x):
    if pd.isna(x):
        return np.nan
    s = str(x)
    if any(k in s.lower() for k in ['no especificado','n/a','nan']):
        return np.nan
    s = re.sub(r'[^\d\.]', '', s)
    try:
        return float(s) if s else np.nan
    except:
        return np.nan

if 'Nº Demandas' in df.columns:
    df['Nº Demandas'] = df['Nº Demandas'].apply(clean_demandas)

# Extraer año numérico
def extract_year(x):
    if pd.isna(x):
        return np.nan
    m = re.search(r'(\d{4})', str(x))
    return int(m.group(1)) if m else np.nan

if 'Año / Periodo' in df.columns:
    df['Año'] = df['Año / Periodo'].apply(extract_year)

# Función mejorada para expandir columnas con múltiples separadores
def expand_column(df, column_name, prefix, max_cols=10):
    if column_name not in df.columns:
        print(f"Advertencia: La columna '{column_name}' no existe en el dataset")
        return df
    
    print(f"\n--- Procesando columna: {column_name} ---")
    
    # Crear una copia del dataframe
    result_df = df.copy()
    
    # Inicializar las nuevas columnas
    new_columns = []
    for i in range(1, max_cols + 1):
        col_name = f'{prefix}_{i}'
        result_df[col_name] = np.nan
        new_columns.append(col_name)
    
    # Procesar cada fila
    for idx in range(len(df)):
        cell_value = df.loc[idx, column_name]
        
        # Saltar valores nulos o vacíos
        if pd.isna(cell_value) or str(cell_value).strip() in ['', 'nan', 'NaN']:
            continue
        
        # Convertir a string y limpiar
        cell_str = str(cell_value).strip()
        
        # Múltiples patrones de separación
        # Primero reemplazar " y " por ","
        cell_str = cell_str.replace(' y ', ',')
        # También manejar punto y coma
        cell_str = cell_str.replace(';', ',')
        
        # Dividir por comas
        values = [v.strip() for v in cell_str.split(',') if v.strip()]
        
        # Si no hay comas, intentar dividir por otros patrones comunes
        if len(values) == 1:
            # Intentar dividir por espacios si hay palabras clave repetidas
            original_value = values[0]
            # Buscar patrones como "Web Apps" repetidos
            if any(keyword in original_value.lower() for keyword in ['web', 'app', 'plataforma', 'tecnología']):
                # Intentar separar por palabras clave comunes
                import re
                # Buscar patrones de repetición
                pattern = r'([^,]+?)(?=\s+(?:Web|App|Plataforma|Tecnología|API|Mobile|Desktop)|\s*$)'
                matches = re.findall(pattern, original_value, re.IGNORECASE)
                if len(matches) > 1:
                    values = [m.strip() for m in matches if m.strip()]
        
        # Asignar valores a las columnas
        for i, value in enumerate(values[:max_cols]):
            if i < len(new_columns):
                result_df.loc[idx, new_columns[i]] = value
        
        # Mostrar progreso para las primeras filas
        if idx < 5 and values:
            print(f"Fila {idx}: '{cell_value}' -> {values}")
    
    # Mostrar resumen
    filled_cols = []
    for col in new_columns:
        non_null_count = result_df[col].notna().sum()
        if non_null_count > 0:
            filled_cols.append(f"{col}: {non_null_count} valores")
    
    print(f"Columnas creadas con datos: {filled_cols}")
    
    return result_df

# Primero, veamos qué columnas tenemos exactamente
print("\nColumnas disponibles en el dataset:")
for i, col in enumerate(df.columns):
    print(f"{i}: '{col}'")

# Intentar encontrar las columnas correctas (pueden tener nombres ligeramente diferentes)
target_columns = []

# Buscar columnas que contengan estas palabras clave
keywords = {
    'industria': ['industria', 'sector'],
    'plataforma': ['plataforma', 'tecnologia', 'tecnología'],
    'estado': ['estado', 'ambito', 'ámbito']
}

for category, keys in keywords.items():
    for col in df.columns:
        col_lower = col.lower()
        if any(key in col_lower for key in keys):
            target_columns.append((col, category))
            break

print(f"\nColumnas identificadas para expandir: {target_columns}")

# Expandir cada columna encontrada
for col_name, category in target_columns:
    print(f"\nExpandiendo '{col_name}' como categoría '{category}'...")
    df = expand_column(df, col_name, category.capitalize(), max_cols=8)

# Si no se encontraron columnas automáticamente, intentar con nombres específicos
if not target_columns:
    print("\nNo se encontraron columnas automáticamente. Intentando con nombres específicos...")
    possible_columns = [
        ('Industria / Sector', 'Industria'),
        ('Plataforma / Tecnología', 'Plataforma'), 
        ('Estado / Ámbito', 'Estado')
    ]
    
    for col_name, prefix in possible_columns:
        df = expand_column(df, col_name, prefix, max_cols=8)

# Guardar resultado
output_file = 'accesibilidad_dividido.csv'
df.to_csv(output_file, index=False, encoding='utf-8-sig')
print(f"\n✅ Dataset guardado como '{output_file}'")

# Mostrar resumen final
print(f"\nDataset final: {len(df)} filas, {len(df.columns)} columnas")

# Mostrar algunas columnas nuevas creadas
new_cols = [col for col in df.columns if any(prefix in col for prefix in ['Industria_', 'Plataforma_', 'Estado_'])]
if new_cols:
    print(f"\nNuevas columnas creadas: {new_cols}")
    print("\nPrimeras 3 filas de las nuevas columnas:")
    print(df[new_cols].head(3).to_string())
else:
    print("\n⚠️  No se crearon nuevas columnas. Revisa los nombres de las columnas originales.")