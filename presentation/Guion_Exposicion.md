# Guion de Exposición: Caso Machine Learning Alicorp
*(Duración estimada: 10 minutos)*

---

**[Diapositiva 1: Título y Presentación]**
"Hola a todos, buenos días/tardes. Mi nombre es [Tu Nombre] y hoy les voy a presentar mi solución analítica para el caso de uso de Alicorp: Estimación de Potencial Incremental de Venta. El objetivo de esta presentación es mostrarles cómo, a través de la ciencia de datos, podemos crear un modelo predictivo que nos permita accionar estrategias comerciales mucho más inteligentes, yendo más allá del simple análisis del ticket de compra."

---

**[Diapositiva 2: Descripción del Caso]**
"Para entender el problema: actualmente Alicorp busca ser más estratégico en sus acciones hacia bodegas y puestos de mercado. Basarnos solamente en quién tiene el 'ticket mayor' no es suficiente para identificar verdaderas oportunidades de crecimiento. 
El objetivo de este proyecto ha sido desarrollar un modelo de Machine Learning que estime la probabilidad de que un cliente tenga un verdadero potencial incremental de venta. ¿El valor agregado? Esto nos va a permitir priorizar a los clientes correctos, optimizando el retorno de inversión en campañas como mercaderismo o ampliaciones de líneas de crédito."

---

**[Diapositiva 3: Análisis de los Datos (EDA)]**
"Para este modelo, partimos de dos fuentes principales: datos demográficos de aproximadamente 5,200 clientes y alrededor de 392 mil transacciones históricas. 
Durante la exploración inicial, el hallazgo más crítico fue que nuestra variable objetivo está altamente desbalanceada: solo cerca del 10% de los clientes en la muestra presentan ese potencial incremental. Este desbalance justificó un enfoque técnico específico que veremos más adelante para evitar que el modelo se sesgue hacia la mayoría que no tiene potencial."

---

**[Diapositiva 4: Preprocesamiento e Ingeniería de Características]**
"Para que los datos sean útiles para el modelo, realizamos un fuerte trabajo de 'Feature Engineering'. Usamos la técnica RFM (Recency, Frequency, Monetary). 
A partir del historial, creé variables como: hace cuántos días fue la última compra, cuántas transacciones hace el cliente, el ticket promedio y qué tanto impacto tienen los descuentos. 
Toda esta información se consolidó en una Tabla Base Analítica. Además, para solucionar el problema del desbalance del 10% que mencioné antes, apliqué la técnica SMOTE, la cual genera datos sintéticos de la clase minoritaria durante el entrenamiento, permitiendo que el algoritmo aprenda a reconocer mejor a los clientes con potencial."

---

**[Diapositiva 5: Desarrollo de la Solución]**
"Abordé este reto como un problema de Clasificación Binaria. 
Evalué modelos basados en árboles, específicamente Random Forest y Gradient Boosting, ya que son excelentes para capturar relaciones complejas y no lineales, y son muy robustos frente a valores atípicos (outliers) en las ventas.
Para garantizar que nuestro modelo generalice bien en el mundo real, separé los datos usando un 80% para entrenar y un 20% exclusivamente para validar su rendimiento con datos que el algoritmo nunca había visto."

---

**[Diapositiva 6: Resultados del Modelo]**
"Los resultados fueron muy positivos. Evaluando el modelo con la curva ROC-AUC obtuvimos un valor sólido (superior a 0.80), lo que indica que el modelo tiene una gran capacidad para separar y ordenar correctamente a los clientes según su verdadera probabilidad de incrementar ventas. 
También monitoreamos métricas como el Recall y el F1-Score para asegurarnos de que estamos capturando la mayor cantidad de clientes verdaderamente potenciales sin generar demasiados falsos positivos que desperdicien el presupuesto."

---

**[Diapositiva 7: Explicabilidad]**
"Pero, ¿qué es lo que realmente impulsa este potencial? Según el análisis de importancia de variables del modelo, descubrimos que la *Recencia* (qué tan reciente es la interacción) y el volumen histórico (*Ticket Total*) son los principales indicadores.
Llevado al negocio, esto confirma que la lealtad y la frecuencia de compra son precursores clave: los clientes que interactúan constantemente están más predispuestos a crecer si les damos el incentivo correcto."

---

**[Diapositiva 8: Estrategia y Uso del Modelo]**
"Sabiendo esto, ¿cómo lo usamos? En lugar de hacer campañas masivas, dividiremos a la cartera en deciles de probabilidad.
Por ejemplo, al Top 10% con mayor probabilidad, podemos ofrecerles inmediatamente la iniciativa de 'Cliente Perfecto' o darles incrementos automáticos en su línea de crédito para concretar su potencial. Al segmento medio (50%-80%), podemos dirigirles acciones de 'Mercaderismo' en su punto de venta para reactivar y empujar a esos clientes que están a un paso de alcanzar su potencial pleno."

---

**[Diapositiva 9: Conclusiones]**
"En conclusión:
1. Hemos demostrado que es posible predecir el potencial incremental basándonos fuertemente en el comportamiento pasado.
2. Esta solución permite a Alicorp evolucionar de una segmentación reactiva y básica a una segmentación completamente proactiva, adelantándonos a la probabilidad futura.
3. Finalmente, logramos una mayor eficiencia, enfocando los recursos y el presupuesto comercial únicamente donde sabemos que existe una alta probabilidad de retorno."

---

**[Diapositiva 10: Siguientes Pasos]**
"Para finalizar, los siguientes pasos naturales serían:
Primero, ejecutar una Fase Piloto (A/B Testing) desplegando el modelo en un canal específico para medir empíricamente la venta incremental contra un grupo de control.
Segundo, enriquecer el modelo incorporando nuevas fuentes, como datos macroeconómicos o la estacionalidad de productos.
Y tercero, orquestar este flujo para su pase a producción, asegurando que el modelo califique a los clientes mensualmente de forma automática.
Muchas gracias. Quedo atento a sus preguntas."
