# MT-Elementos-quimicos
# Máquina de Turing de Elementos

Este proyecto implementa una **Máquina de Turing** que simula reacciones químicas básicas entre elementos de la tabla periódica. Los usuarios pueden ingresar combinaciones de elementos y recibir como resultado el compuesto generado. La interfaz gráfica está construida con HTML, CSS y JavaScript, mientras que el backend está desarrollado en Python utilizando el framework Flask.

## Características

- **Verificación de cadenas válidas**: La máquina acepta solo combinaciones específicas de elementos que producen compuestos conocidos.
- **Historial de entradas**: Muestra las últimas combinaciones ingresadas y si fueron válidas o no.
- **Ventana de ayuda**: Un modal con un `?` muestra las combinaciones válidas que el sistema acepta.
- **Sonidos personalizados**: Cada reacción química tiene un sonido asociado, que se reproduce al generar un compuesto.
- **Animación de reacción**: Al generar un compuesto, se muestra una animación de reacción en la interfaz.

## Tecnologías Utilizadas

- **Frontend**: HTML, CSS, JavaScript
- **Backend**: Python, Flask
- **Gestión de paquetes**: pip
- **Control de versiones**: Git
- **Almacenamiento de sonidos y estilos**: Archivos locales en la carpeta `static`

## Configuración del Proyecto

Sigue estos pasos para configurar y ejecutar el proyecto en tu máquina local:

### Requisitos

- Python 3.x
- pip (instalador de paquetes de Python)
- Git

### Instalación

1. Clona este repositorio en tu máquina local:

   ```bash
   git clone https://github.com/tu_usuario/maquina-de-turing.git
