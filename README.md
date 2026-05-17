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

## Despliegue en GitHub Pages (Opcional)

Si deseas mostrar tus cuadernos como una página web en GitHub Pages (sin que los evaluadores tengan que descargar el código), puedes exportarlos a HTML:
```bash
jupyter nbconvert --to html notebooks/01_EDA_and_Preprocessing.ipynb
jupyter nbconvert --to html notebooks/02_Modeling.ipynb
```
Luego, renombra el archivo `01_EDA_and_Preprocessing.html` a `index.html` en la raíz del repositorio y súbelo a la rama `gh-pages` de tu repositorio.

## Autor
Candidato a Machine Learning Engineer.
