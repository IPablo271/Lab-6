# Redes Neuronales para Recomendación de Libros

Este proyecto implementa dos tipos de redes neuronales para recomendar libros: una red basada en contenido y otra basada en filtros colaborativos.

## Red Neuronal Basada en Contenido

La red neuronal basada en contenido utiliza la información intrínseca de los libros, como el título, el autor, el año de publicación y el editor. Aquí se realiza un proceso de codificación de etiquetas (Label Encoding) para convertir las características no numéricas en representaciones numéricas. Se emplea un modelo de tipo Sequential con las siguientes capas:

1. **Capa de Entrada (Input):** Se configura con un número de neuronas igual al número de características utilizadas (en este caso, 4).
2. **Capas Ocultas (Dense):** Se emplean capas densamente conectadas con funciones de activación 'relu'. Se utilizan capas de 64 y 32 neuronas respectivamente.
3. **Capa de Salida (Dense):** Se utiliza una capa de salida con una sola neurona y función de activación lineal, ya que el objetivo es predecir el rating del libro.

Este modelo se compila con una función de pérdida de error cuadrático medio (mean_squared_error) y se entrena con el optimizador 'adam' durante 10 épocas.

## Red Neuronal Basada en Filtros Colaborativos

La red neuronal basada en filtros colaborativos utiliza la interacción entre usuarios y libros para generar recomendaciones. Se codifican los identificadores de usuario (User-IDs) y los identificadores de libros (ISBNs) utilizando etiquetado. Se construye un modelo más complejo utilizando una arquitectura funcional con las siguientes características:

1. **Capas de Embedding (Embedding Layers):** Se utilizan capas de embedding para usuarios y libros, con una dimensión de 5. Estas capas permiten capturar las relaciones entre usuarios y libros.
2. **Capas Densas (Dense):** Se aplican capas densas con activación 'relu', de 256, 128 y 128 neuronas respectivamente.
3. **Capa de Salida (Dense):** Se usa una capa de salida sin función de activación específica, ya que el objetivo es predecir el rating del libro.

El modelo se compila con la función de pérdida de error cuadrático medio (mean_squared_error) y se entrena utilizando los datos de entrenamiento durante 5 épocas.

Ambos modelos se entrenan con datos distintos y emplean enfoques diferentes para generar recomendaciones de libros. Mientras que la red basada en contenido se enfoca en las características intrínsecas de los libros, la red basada en filtros colaborativos se centra en las interacciones entre usuarios y libros para realizar recomendaciones personalizadas.
