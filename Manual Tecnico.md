# Manual Técnico de PetWorld Manager

## Introducción
El **PetWorld Manager** es una aplicación diseñada para gestionar mascotas virtuales, específicamente gatos, permitiendo a los usuarios crear, alimentar, jugar y obtener resúmenes sobre el estado de sus mascotas. Este manual técnico proporciona una visión detallada del funcionamiento interno del sistema, así como las tecnologías y técnicas utilizadas en su desarrollo.

## Estructura del Código Fuente
El código fuente del PetWorld Manager se organiza en un único archivo llamado `petworld_manager.py`. Se divide en varias secciones para una mejor comprensión y mantenibilidad del código.

### 1. Importaciones
En esta sección, se importan los módulos y bibliotecas necesarios para el funcionamiento del programa. En el código proporcionado, se importan los siguientes módulos:

- `datetime`: Para el manejo de fechas y horas.
- `re`: Para el manejo de expresiones regulares.
- `graphviz`: Para la generación de gráficos.

### 2. Clase `PetManager`
La clase `PetManager` es el núcleo del sistema, que gestiona todas las operaciones relacionadas con las mascotas. Esta clase contiene métodos para crear gatos, darles de comer, jugar con ellos, y generar resúmenes tanto individuales como globales. También incluye un método para generar un gráfico que representa visualmente el estado de las mascotas.
![Descripción de la imagen](https://i.ibb.co/VSNMXTJ/image.png)
![Descripción de la imagen](https://i.ibb.co/k0FzX1L/image.png)

### 3. Funciones Auxiliares
Se definen varias funciones auxiliares que son utilizadas por la clase `PetManager` para realizar operaciones específicas, como escribir en un archivo o leer comandos desde un archivo de texto.
![Descripción de la imagen](https://i.ibb.co/xHzgvNP/image.png)


### 4. Funciones de Interfaz de Usuario
Estas funciones son responsables de mostrar los diferentes menús de la aplicación y de interactuar con el usuario para obtener su entrada y ejecutar las acciones correspondientes.

### 5. Función Principal (`main`)
La función `main` es el punto de entrada principal del programa. Utiliza un bucle infinito para mostrar el menú principal y dirigir al usuario a los diferentes módulos de la aplicación según su selección.
![Descripción de la imagen](https://i.ibb.co/dfqTgjY/image.png)
![Descripción de la imagen](https://i.ibb.co/SccCbvX/image.png)


## Tecnologías Utilizadas
El PetWorld Manager está escrito en Python, un lenguaje de programación de alto nivel ampliamente utilizado en el desarrollo de aplicaciones. Además de las bibliotecas estándar de Python, se utiliza la biblioteca `graphviz` para generar gráficos de las mascotas y su estado.



## Requisitos del Sistema
El PetWorld Manager está diseñado para ser ejecutado en cualquier entorno que admita Python 3.x. No tiene requisitos especiales de hardware y se ejecutará en cualquier sistema operativo compatible con Python.

## Instalación y Ejecución
Para ejecutar el PetWorld Manager, simplemente ejecute el archivo `petworld_manager.py` con Python en su entorno de desarrollo preferido o desde la línea de comandos.

```bash
python petworld_manager.py


