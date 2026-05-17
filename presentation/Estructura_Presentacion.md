# Estructura de Presentación: Caso Machine Learning Alicorp
**(Máximo 10 Diapositivas)**

Esta estructura está diseñada para cumplir con los requerimientos de la prueba, asegurando una narrativa clara tanto técnica como de negocio.

---

## Diapositiva 1: Título y Presentación
- **Título:** Estimación de Potencial Incremental de Venta
- **Subtítulo:** Caso de Uso – Data Scientist | Alicorp
- **Presentador:** [Tu Nombre / Candidato]
- **Objetivo Breve:** Mostrar el desarrollo de un modelo predictivo que permita accionar estrategias comerciales más allá del ticket promedio.

---

## Diapositiva 2: Descripción del Caso (Contexto de Negocio)
- **Problema:** Alicorp busca realizar acciones comerciales más estratégicas hacia bodegas y puestos de mercado. Basarse solo en el "ticket mayor" no es suficiente.
- **Objetivo Analítico:** Desarrollar un modelo predictivo para estimar la probabilidad de que un cliente tenga un **potencial incremental de venta**.
- **Valor Agregado:** Permitirá priorizar clientes con alto potencial, optimizando el retorno de inversión (ROI) de campañas de mercaderismo o líneas de crédito.

---

## Diapositiva 3: Análisis de los Datos (EDA)
- **Datos Disponibles:** 
  - *Demográficos:* 5.2k clientes (antigüedad, segmento, flag de crédito).
  - *Transaccionales:* ~392k transacciones (fecha, producto, monto, descuentos).
- **Hallazgo Clave:** La variable objetivo (`target`) se encuentra desbalanceada (~10% de clientes con potencial).
- *Visual sugerida:* Gráfico circular (Pie chart) o barras de la distribución del target para mostrar el desbalance, que justifica el enfoque técnico posterior.

---

## Diapositiva 4: Preprocesamiento e Ingeniería de Características
- **Limpieza:** Imputación de nulos (ej. uso de mediana en antigüedad).
- **Feature Engineering (RFM):** Se extrajeron variables clave a partir de la historia transaccional del cliente:
  - **Recency:** Días desde la última compra.
  - **Frequency:** Cantidad de transacciones.
  - **Monetary:** Ticket promedio y monto total comprado.
  - **Descuentos:** Porcentaje de descuento sobre la venta total.
- **Consolidación:** Unión de datos en una única Tabla Base Analítica (ABT) y técnica SMOTE para balancear la clase minoritaria durante el entrenamiento.

---

## Diapositiva 5: Desarrollo de la Solución (Modelo)
- **Enfoque de Modelado:** Problema de Clasificación Binaria.
- **Modelos Evaluados:** Random Forest y Gradient Boosting. (Se eligen algoritmos basados en árboles por su capacidad de encontrar relaciones no lineales complejas y su robustez ante outliers).
- **Validación:** División estratificada (Train 80% / Test 20%) para evaluar el rendimiento en datos no vistos, evitando el sobreajuste.

---

## Diapositiva 6: Resultados del Modelo (Evaluación)
- **Métricas:** 
  - Curva ROC-AUC: (Destacar el valor, ej. AUC > 0.80) Indica una gran capacidad del modelo para ordenar correctamente a los clientes según su probabilidad real de compra.
  - F1-Score y Recall: (Mencionar la capacidad de capturar verdaderos potenciales).
- *Visual sugerida:* Curva ROC comparando modelos o Matriz de Confusión simple y fácil de leer.

---

## Diapositiva 7: Explicabilidad (Feature Importance)
- **¿Qué impulsa el potencial incremental?**
  - Mostrar gráfico de Importancia de Variables (Feature Importance).
  - **Insights:** Explicar que la Recencia (qué tan reciente compran) y el Ticket Total suelen ser los principales indicadores.
  - *Negocio:* Esto confirma que la lealtad y el volumen histórico son precursores de un mayor potencial de crecimiento si se estimulan correctamente.

---

## Diapositiva 8: Estrategia y Uso del Modelo
- **Segmentación por Probabilidad:** En lugar de campañas masivas, se utilizarán deciles de probabilidad generados por el modelo.
- **Estrategia Comercial (Ejemplo):**
  - **Top 10% (Alta Probabilidad):** Ofrecer la iniciativa "Cliente Perfecto" o incrementos automáticos en la "Línea de Crédito" para concretar el potencial rápidamente.
  - **Segmento Medio (Probabilidad 50-80%):** Acciones de "Mercaderismo" e impulso en punto de venta para reactivar a los que están "a un paso" del potencial pleno.

---

## Diapositiva 9: Conclusiones y Siguientes Pasos
- **Conclusión:** Es posible predecir el potencial incremental basándonos fuertemente en el comportamiento transaccional pasado (RFM), logrando una mayor eficiencia en el gasto comercial.
- **Fase Piloto (A/B Testing):** Desplegar el modelo en un canal específico y comparar la venta incremental contra un grupo de control aleatorio.
- **Nuevas Fuentes de Datos:** Incorporar datos macroeconómicos, ubicación geográfica exacta (lat/lon) y estacionalidad de productos.

---

## Diapositiva 10: Despliegue en Producción (Centro de Control Web)
- **Innovación Tecnológica:** Se ha desarrollado un "Centro de Control" en una Single Page Application (SPA).
- **Tecnologías:** 
  - *GitHub Pages:* Para alojamiento gratuito y de alta disponibilidad.
  - *PyScript (WebAssembly):* Permite ejecutar el modelo de Machine Learning (Random Forest) en el navegador del usuario en tiempo real sin requerir un servidor backend (Edge Computing).
- **Visual:** *[Mostrar captura de pantalla de la página web con el logo de Alicorp y el simulador de predicción probando un cliente]*
- **Impacto:** Entrega de valor inmediata a los equipos de negocio mediante una interfaz amigable y lista para usar.

---
*(Fin de la Presentación - 10 Minutos Máximo, seguido de Ronda de Preguntas)*
