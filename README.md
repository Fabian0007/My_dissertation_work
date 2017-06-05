# Modelo de simulación de agentes de las capacidades en investigación en el contexto de la universidad colombiana
El objetivo de este trabajo es estudiar la relación entre la producción de conocimiento de las universidades colombianas y su acumulación de capacidades en investigación, estas capacidades se acumulan de distintas maneras. En el caso de Colombia, los grupos de investigación juegan un rol fundamental, ya que es en ellos donde se institucionaliza el conocimiento. De esta manera, surge una ventaja acumulativa desde y hacia los grupos de investigación, la que produce diferencias significativas en las universidades colombianas. Los resultados muestran que los diferentes tipos de crecimiento de las publicaciones académicas no dependen de la existencia de competencia entre las instituciones y pueden explicarse por un proceso de ventajas acumulativas, también, existen condiciones adicionales para la aparición de un crecimiento exponencial de las publicaciones y, finalmente, que las universidades al aumentar su capacidad en investigación, pierden eficiencia en el uso de esta.

## Navegación por las carpetas
Entrar a la carpeta ModelosPresentados.
### Modelos
En las carpetas, ConCompetencia y SinCompetencia, se encuentran modelos realizados como archivos .nlogo, ademas se encuentran los resultados para cada una de las 100 simulaciones y una carpeta AverageResults, en la cual se encuentran los resultados promedio para las simulaciones realizadas.

### Curvas
En la carpeta Curvas, se encuentran los scripts .nb para la generación de los resultados gráficos de las curvas de producción academica para ambos modelos.

### Relación entre las curvas de producción academica y la probabilidad de éxito
En la carpeta RelaciónCurvas, se encuentran los scripts .nb para la generación de los resultados gráficos de la relación entre producción academica y probabilidad de éxito.

### Distribución
En la carpeta Distribución, se encuentran los scripts .nb para la generación de los resultados gráficos de la distribución para la desviación estandar, la productividad de las universidades y de los grupos de investigación.

### Automatizador de tareas
El archivo automatizador.py es un script realizado en Python, este realiza tareas como:
*	Debido a que se usa la exportación de gráficos de Netlogo como forma de obtener los resultados de la simulación, es necesario a partir de un único archivo de texto, generar las distintas tablas que son objeto de estudio.
*	Creación automática de carpetas para estructurar el directorio
*	Obtener el promedio para los datos obtenidos de repeticiones de una misma prueba.
*	Limpiar los datos de prueba.
*	Ordenar filas de tablas.
*	Calculo de la desviación estándar
