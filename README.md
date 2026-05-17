# Alicorp - Machine Learning Engineer Study Case

Este repositorio contiene la solución a la prueba técnica para la posición de Machine Learning Engineer en Alicorp.
El objetivo del proyecto es estimar la probabilidad de que un cliente tenga un potencial incremental de venta.

## Estructura del Repositorio

- `data/raw/`: Carpeta donde se deben depositar los archivos originales (`data_cliente.csv`, `data_transaccional.csv`). **Importante:** Asegúrate de colocar estos archivos aquí antes de ejecutar los cuadernos.
- `data/processed/`: Contendrá la tabla ABT generada por el script de preprocesamiento.
- `notebooks/`:
  - `01_EDA_and_Preprocessing.ipynb`: Limpieza de datos, imputación, feature engineering (RFM) y creación del ABT.
  - `02_Modeling.ipynb`: Carga del ABT, sobremuestreo (SMOTE), entrenamiento de modelos (RandomForest, GradientBoosting) y evaluación (Curva ROC, Importancia de Variables).
- `presentation/`:
  - `Estructura_Presentacion.md`: Guion y estructura detallada para las 10 diapositivas requeridas en la prueba técnica, con el discurso estratégico y las conclusiones.
- `requirements.txt`: Dependencias de Python necesarias.

## Instalación y Ejecución

1. Clona el repositorio.
2. Asegúrate de tener Python 3.8+ instalado.
3. Instala las dependencias:
   ```bash
   pip install -r requirements.txt
   ```
4. Coloca los archivos `data_cliente.csv` y `data_transaccional.csv` en la carpeta `data/raw/`.
5. Ejecuta los Jupyter Notebooks en orden, desde la carpeta `notebooks/`.

## Despliegue en GitHub Pages (Centro de Control)

El proyecto cuenta con una interfaz web integrada (Single Page Application) pensada para GitHub Pages. Esta página sirve como un **Centro de Control** con pestañas para navegar entre los cuadernos de Jupyter y un simulador interactivo impulsado por PyScript.

Los cuadernos han sido exportados previamente a HTML y alojados en la carpeta `docs/`.
Para visualizar la web interactiva:
1. Sube este repositorio a GitHub.
2. Ve a los **Settings** de tu repositorio.
3. En la sección **Pages** (GitHub Pages), selecciona desplegar desde la rama `master` (o main) apuntando a la carpeta `/docs`.
4. Guarda y abre el link generado para explorar el Análisis, el Modelado y probar las predicciones en tiempo real sin necesidad de un backend.

## Autor
Candidato a Machine Learning Engineer.
