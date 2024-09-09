###Proyecto Importaciones
Descripción
Proyecto Importaciones es una aplicación web diseñada para facilitar la compra de productos importados y permitir la gestión de pedidos para productos no disponibles en la página. El objetivo principal es acercar productos internacionales a los usuarios y permitirles realizar pedidos de artículos que no están actualmente en el catálogo.

Características Principales
Página del Cliente:
Los clientes pueden registrarse, iniciar sesión y gestionar su perfil.

Página del Administrador:
Los administradores pueden aprobar pedidos y compras. (funcionalidad va a ser disponible proximamente)
Actualmente, los administradores pueden ingresar nuevos empleados.

Página All Productos:
Agregar nuevos productos.
Buscar productos mediante su código.
Para buscar, actualmente se pueden usar los códigos 2253 y 3625, que son los únicos presentes en la base de datos.

Página de Requests:
Permite ingresar pedidos para productos que no están en el catálogo.

###Tecnologías Usadas
Python 5.0.3 
Django

###Instalación y Configuración
* Requisitos Previos
Python 5.0.3

###Pasos para Configurar en un Entorno Local
* Clonar el Repositorio:
Abre una nueva carpeta, abre la consola de Git en esa carpeta, y ejecuta el siguiente comando:

```bash
Copiar código
git clone https://github.com/CorreroNerea/Tercera_Pre_entrega-Correro
```

Instalar Dependencias:
Navega al directorio del proyecto y asegúrate de instalar las dependencias necesarias:

```bash

cd Tercera_Pre_entrega-Correro
pip install -r requirements.txt
```

Migraciones y Configuración:
Ejecuta las migraciones para configurar la base de datos:
```bash
python manage.py migrate
```

Iniciar el Servidor:
Finalmente, inicia el servidor de desarrollo:

```bash
Copiar código
python manage.py runserver
```
Puedes acceder a la aplicación en http://127.0.0.1:8000.

Uso
Navegación:
Navega por las distintas pestañas en el menú de navegación. Cada página representa una clase en models y tiene un formulario para cargar datos en la base de datos.

Buscar Productos:
En la página "All Products", en el formulario "Buscar" podes buscar productos usando los códigos 2253 y 3625. Estos códigos devolverán el nombre del producto registrado en la base de datos.

Django Administration:
Solo el administrador con el nombre de usuario: Alejandrino y la contraseña: Alejandrino, tiene acceso a la administración de Django para hacer cambios y gestionar BD en esta aplicación.

Créditos
Desarrollador Principal: Alejandrino

Contacto
Para soporte o más información, contacta a correro.nerea@gmailcom o a través del repositorio de GitHub.

Video explicativo:
https://youtu.be/npB-uXXBcjM

Caso de Prueba:
https://docs.google.com/spreadsheets/d/1o4AUGhL3xZ5s755ZiwGjWF8Eda59424Bg-Ckkj2zeqo/edit?usp=sharing --> Excel.
