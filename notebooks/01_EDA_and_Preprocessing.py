# %% [markdown]
# # Alicorp - Caso Práctico Machine Learning Engineer
# ## 01 - Análisis Exploratorio de Datos (EDA) y Preprocesamiento
# 
# **Objetivo:** Explorar los datos de clientes y transaccionales, realizar limpieza, imputación de nulos y generar variables RFM para crear el ABT (Analytical Base Table) final que se utilizará para el modelado.

# %%
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
import os

warnings.filterwarnings('ignore')
sns.set_theme(style="whitegrid")

# %% [markdown]
# ### 1. Carga de Datos

# %%
# Definir rutas
RAW_DIR = '../data/raw'
PROCESSED_DIR = '../data/processed'

# Crear carpeta de procesados si no existe
os.makedirs(PROCESSED_DIR, exist_ok=True)

# Cargar datasets
try:
    df_cliente = pd.read_csv(os.path.join(RAW_DIR, 'data_cliente.csv'))
    df_transaccional = pd.read_csv(os.path.join(RAW_DIR, 'data_transaccional.csv'))
    print("Datos cargados exitosamente.")
except FileNotFoundError:
    print("Error: No se encontraron los archivos en la carpeta data/raw/. Por favor, asegúrate de colocar data_cliente.csv y data_transaccional.csv allí.")
    # Stop execution if data is missing
    raise

# %% [markdown]
# ### 2. Análisis Exploratorio: Datos Cliente

# %%
print(f"Dimensiones Datos Cliente: {df_cliente.shape}")
df_cliente.head()

# %%
# Información general y nulos
df_cliente.info()

# %%
# Resumen de variables numéricas
df_cliente.describe()

# %%
# Distribución de la variable objetivo
plt.figure(figsize=(6,4))
sns.countplot(data=df_cliente, x='target')
plt.title('Distribución de la Variable Objetivo (Target)')
plt.show()

print(df_cliente['target'].value_counts(normalize=True) * 100)

# %% [markdown]
# Como observamos, la variable objetivo está desbalanceada, lo cual era de esperarse según la descripción del caso (~10% de clase positiva).

# %% [markdown]
# ### 3. Limpieza y Preprocesamiento: Datos Cliente

# %%
# Tratamiento de valores nulos
# Vemos si 'age_alicorp' u otras tienen nulos
print("Nulos en datos cliente:")
print(df_cliente.isnull().sum())

# Imputaremos 'age_alicorp' con la mediana ya que es una variable de edad/antigüedad
if df_cliente['age_alicorp'].isnull().sum() > 0:
    median_age = df_cliente['age_alicorp'].median()
    df_cliente['age_alicorp'].fillna(median_age, inplace=True)
    
# Si existen otros nulos en flags numéricos, asumiremos 0 (Falso)
for col in ['has_credit_line', 'has_perfect_customer', 'has_marketing_impulse']:
    if df_cliente[col].isnull().sum() > 0:
        df_cliente[col].fillna(0, inplace=True)

# %% [markdown]
# ### 4. Análisis Exploratorio: Datos Transaccionales

# %%
print(f"Dimensiones Datos Transaccionales: {df_transaccional.shape}")
df_transaccional.head()

# %%
# Información de transaccional
df_transaccional.info()

# %%
# Verificación de nulos
print("Nulos en datos transaccionales:")
print(df_transaccional.isnull().sum())

# %% [markdown]
# Notamos que `date` viene en formato numérico (Excel serial date) u otro formato. Intentaremos convertirlo, aunque no es estrictamente necesario si solo calculamos agregaciones, pero para Recency (Recencia) sí lo es.

# %%
# Convertir date numérico a datetime si está en formato Excel (origen 1899-12-30)
# En el archivo head() vimos: 44026. 44026 en excel es 12/07/2020.
try:
    df_transaccional['date'] = pd.to_datetime(df_transaccional['date'], origin='1899-12-30', unit='D')
except Exception as e:
    print(f"No se pudo convertir fecha numéricamente: {e}. Se intentará directo.")
    df_transaccional['date'] = pd.to_datetime(df_transaccional['date'])

print(f"Rango de fechas: {df_transaccional['date'].min()} a {df_transaccional['date'].max()}")

# %% [markdown]
# ### 5. Ingeniería de Características (RFM + otras)

# %%
# Generar variables por cliente
# Fecha máxima para cálculo de Recency
max_date = df_transaccional['date'].max()

# Agregaciones
rfm = df_transaccional.groupby('customer_id').agg({
    'date': lambda x: (max_date - x.max()).days,  # Recency
    'product_id': 'count',                        # Frequency (número de transacciones/productos)
    'category_product': 'nunique',                # Variedad de categorías
    'amount': ['sum', 'mean'],                    # Monetary total y Ticket promedio
    'discount': 'sum'                             # Total descuento
})

# Renombrar columnas
rfm.columns = ['recency', 'frequency', 'unique_categories', 'total_amount', 'avg_ticket', 'total_discount']
rfm.reset_index(inplace=True)

# Crear feature adicional: Porcentaje de descuento sobre la venta
rfm['discount_rate'] = np.where(rfm['total_amount'] > 0, rfm['total_discount'] / rfm['total_amount'], 0)

rfm.head()

# %% [markdown]
# ### 6. Unión de Tablas (Merge) -> ABT

# %%
# Unir datos demográficos con transaccionales
# Usamos left join desde cliente para mantener a todos (incluso si no transaccionaron)
df_abt = pd.merge(df_cliente, rfm, on='customer_id', how='left')

# Llenar nulos para clientes que no tuvieron transacciones
cols_to_fill = ['recency', 'frequency', 'unique_categories', 'total_amount', 'avg_ticket', 'total_discount', 'discount_rate']
for col in cols_to_fill:
    if col == 'recency':
        # Para recency, si no compró, le ponemos un valor alto (peor recency)
        df_abt[col].fillna(999, inplace=True)
    else:
        df_abt[col].fillna(0, inplace=True)

print(f"Dimensiones ABT: {df_abt.shape}")

# %% [markdown]
# ### 7. Tratamiento de Categóricas

# %%
# Convertiremos territory_id y segment a variables dummy (One-Hot Encoding)
df_abt = pd.get_dummies(df_abt, columns=['territory_id', 'segment'], drop_first=True)

# %%
# Vista final del ABT
df_abt.head()

# %% [markdown]
# ### 8. Exportación del ABT

# %%
# Guardar como CSV
abt_path = os.path.join(PROCESSED_DIR, 'abt_cliente.csv')
df_abt.to_csv(abt_path, index=False)
print(f"Analytical Base Table guardado exitosamente en: {abt_path}")
