# Manual Técnico: PetWorld Manager

## Introducción
El PetWorld Manager es una aplicación de gestión de mascotas virtuales que permite a los usuarios crear y cuidar a sus mascotas. Este manual técnico proporciona información detallada sobre la arquitectura, los componentes y el funcionamiento interno de la aplicación.

## Arquitectura
La aplicación PetWorld Manager sigue una arquitectura modular, con los siguientes componentes principales:

1. **PetManager**: Clase principal que gestiona todas las operaciones relacionadas con las mascotas, como crear mascotas, alimentarlas, jugar con ellas y generar informes.
2. **Interfaz de usuario**: Módulo que interactúa con los usuarios a través de la línea de comandos, proporcionando un menú para realizar acciones como cargar archivos de configuración y realizar operaciones en las mascotas.
3. **Generador de gráficos**: Utiliza la biblioteca Graphviz para generar representaciones visuales de las mascotas y su estado.

## Dependencias
La aplicación PetWorld Manager depende de las siguientes bibliotecas de Python:

- `datetime`: Para el manejo de fechas y horas.
- `re`: Para el análisis de expresiones regulares.
- `graphviz`: Para la generación de gráficos.
- `os`: Para funciones relacionadas con el sistema operativo.

## Instalación
1. Asegúrate de tener Python instalado en tu sistema.
2. Instala las dependencias usando `pip`:

```
pip install graphviz
```

3. Descarga los archivos de la aplicación PetWorld Manager.
4. Ejecuta el programa desde la línea de comandos usando Python:

```
python main.py
```

## Uso
Una vez que la aplicación está en funcionamiento, sigue las instrucciones en pantalla para cargar un archivo de configuración (.petworld) y realizar operaciones en tus mascotas virtuales.

## Contribuciones
¡Las contribuciones son bienvenidas! Si deseas mejorar la aplicación o corregir errores, sigue estos pasos:

1. Haz un fork del repositorio.
2. Realiza tus cambios en una rama separada.
3. Envía una solicitud de extracción (pull request) con tus cambios.

## Soporte
Para obtener ayuda o informar sobre problemas, crea un issue en el repositorio de GitHub o contacta al equipo de desarrollo por correo electrónico.

## Licencia
Este proyecto está bajo la Licencia MIT. Para más detalles, consulta el archivo LICENSE en el repositorio.

