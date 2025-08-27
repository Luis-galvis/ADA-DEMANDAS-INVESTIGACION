import pandas as pd

# -----------------------------
# 1. DATA PANORAMA GENERAL
# -----------------------------
data_panorama = [
    ["2023 (Total)","Federal + Estatal (EE.UU.)","4600+","eCommerce (82%), Web (97%), apps, SaaS","30% (+62% vs 2022)","N/A","N/A","ADA Title II/III, WCAG 2.1 AA","92% acuerdos, mayoría exitosos"],
    ["2024 (Total Fed.)","Federal (EE.UU.)","3188 (~8.8/día)","Moda, Restaurantes, Belleza, Salud, Fitness, Entretenimiento","Shopify, WP, Magento, Wix, Squarespace","22.65% (722 casos)","Multa FTC $1M a AccessiBe","ADA III / Sec. 508 / WCAG 2.1","En curso / acuerdos privados"],
    ["2024 (Total Estados)","NY, FL, CA, PA, Otros","NY 1600 / FL 629 / CA 485 / PA 121 / Otros 353","Moda, eCommerce, Salud","Shopify, WP, Magento","N/A","Mizrahi Kroub, Gottlieb, Stein Saks, etc.","ADA / estatales","En curso / acuerdos"],
    ["2024 (Mensual Peak)","Federal (EE.UU.)","309 (en octubre)","Varias","N/A","N/A","Ejemplo: Jessica Karim (25 en abril)","ADA","En curso"],
    ["2025 (H1 Total)","Federal + Estatal (EE.UU.)","2019 (ene-jun)","eCommerce 69%, Food 18%, Healthcare 4%, Fitness 3%","Web, apps, video","32% con widgets (659 casos)","N/A","ADA III / WCAG 2.1/2.2","En curso"],
    ["2025 (Proyección)","Federal + Estatal (EE.UU.)","~4187 (estimado anual)","Igual H1 2025","Web, apps, video","N/A","Top 500 eCommerce (20% target)","ADA / WCAG 2.1/2.2","En curso"]
]

cols_panorama = ["Periodo","Jurisdicción","Nº Demandas","Sectores Principales","Plataforma/Tecnología","Widgets (%)","Casos Destacados","Normas","Resultado/Motivo"]

df_panorama = pd.DataFrame(data_panorama, columns=cols_panorama)

# -----------------------------
# 2. DATA POR ESTADO
# -----------------------------
data_estados = [
    ["Nueva York",2024,1600,"eCommerce (69%), Food (18%), Healthcare (4%)","Mizrahi Kroub, Gottlieb, Equal Access, Shaked Law","ADA + estatales NY"],
    ["Nueva York",2025,1011,"eCommerce (69%), Food (18%), Healthcare (4%)","Mizrahi Kroub, Gottlieb, Equal Access, Shaked Law","ADA + estatales NY"],
    ["Florida",2024,629,"Moda, Restaurantes, Healthcare","Gottlieb & Associates, R.V. Hannah","ADA Title III (federal)"],
    ["Florida",2025,544,"Moda, Restaurantes, Healthcare","Gottlieb & Associates, R.V. Hannah","ADA Title III (federal)"],
    ["California",2024,485,"eCommerce, Food, Entertainment, Educación","Firmas locales (migración a CIPA Act)","ADA + Unruh + CIPA Act"],
    ["California",2025,562,"eCommerce, Food, Entertainment, Educación","Firmas locales","ADA + Unruh + CIPA Act"],
    ["Pensilvania",2024,121,"Varias","N/D","ADA"],
    ["Otros",2024,353,"Varias","N/D","ADA"],
    ["Illinois y Minnesota",2024,"En alza","Varias","Nuevos bufetes","ADA estatal/federal"],
    ["Illinois y Minnesota",2025,"En alza","Varias","Nuevos bufetes","ADA estatal/federal"]
]

cols_estados = ["Estado","Año","Nº Demandas","Sectores","Firmas","Normas"]

df_estados = pd.DataFrame(data_estados, columns=cols_estados)

# -----------------------------
# 3. CASOS ESPECIALES
# -----------------------------
data_casos = [
    ["Widgets/Overlays",2024,"722 casos (~22.65%)","N/A","FTC multa $1M a AccessiBe; Stein Saks sancionada","ADA / WCAG","Widgets invalidados como defensa"],
    ["Widgets/Overlays",2025,"659 demandas (H1)","33% de litigios","DOJ/FTC sanción $1M a proveedor IA","ADA / WCAG","En curso"],
    ["Concentración de actores",2024,">50% en 35 demandantes","80% en 10 firmas","Victor Ariza, Nelson Fernandez, Jessica Karim, Julie Dalton, Oscar Herrera","ADA","En curso"],
]

cols_casos = ["Aspecto","Año","Figura Clave","% en Litigios","Actores Destacados","Normas","Resultado"]

df_casos = pd.DataFrame(data_casos, columns=cols_casos)

# -----------------------------
# 4. TENDENCIAS CLAVE
# -----------------------------
data_tendencias = [
    ["Crecimiento sostenido","~4000 casos/año desde 2023"],
    ["Consolidación geográfica","NY + FL + CA = 70% total; IL y MN creciendo"],
    ["Industria expuesta","eCommerce (~70%) + Food + Healthcare"],
    ["Widgets bajo fuego","33% demandas 2025 involucran overlays"],
    ["Shift legal","California suma ADA + CIPA (privacidad)"],
    ["Concentración de actores","80% en 10 firmas; 35 demandantes = >50% del total"],
    ["Evolución normativa","WCAG 2.2 referenciado en 2025 como estándar judicial"]
]

cols_tendencias = ["Aspecto","Detalle"]

df_tendencias = pd.DataFrame(data_tendencias, columns=cols_tendencias)

# -----------------------------
# 5. GUARDAR EN EXCEL
# -----------------------------
with pd.ExcelWriter("dataset_ADA_2023_2025.xlsx", engine="xlsxwriter") as writer:
    df_panorama.to_excel(writer, sheet_name="Panorama", index=False)
    df_estados.to_excel(writer, sheet_name="Estados", index=False)
    df_casos.to_excel(writer, sheet_name="Casos Especiales", index=False)
    df_tendencias.to_excel(writer, sheet_name="Tendencias", index=False)

print("✅ Archivo dataset_ADA_2023_2025.xlsx generado con éxito")
