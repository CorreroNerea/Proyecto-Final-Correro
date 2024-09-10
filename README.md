###Proyecto Importaciones
Descripción
Proyecto Importaciones es una aplicación web diseñada para facilitar la compra de productos importados y permitir la gestión de pedidos para productos no disponibles en la página. El objetivo principal es acercar productos internacionales a los usuarios y permitirles realizar pedidos de artículos que no están actualmente en el catálogo.

Características Principales
Página principal:
Muetra alguno de los proximos productos que seran ingresados.

User:
Desde User --> Register, se puede registrar. Los usuarios pueden registrarse, y luego en la misma tab esta la opcion para iniciar sesión.
Una vez iniciada la sesion, en la misma tab el usuario tiene las opciones de editar su perfil, log out y mirar los detalles de su perfil.

Página del Administrador:
Desde Shop --> Products_adm:
Los administradores pueden crear, borrar, editar y visualizar productos. 
Se esta trabajando para que proximamente puedan revisar y aprobar pedidos. (funcionalidad va a ser disponible proximamente)

Página Productos:
Buscar productos mediante su código.
Para buscar, actualmente se pueden usar los códigos 2116, 2111 y 2253, que son los únicos presentes en la base de datos.
Desde esta tab los diferentes usuarios pueden visualizar el detalle de los productos que quieran, pueden sumar productos a sus carritos de compra.

Pagina Carrito:
Permite a los usuarios aprobar y finalizar sus compras.

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
git clone https://github.com/CorreroNerea/Proyecto-Final-Correro
```

Instalar Dependencias:
Navega al directorio del proyecto y asegúrate de instalar las dependencias necesarias:

```bash

cd Proyecto-Final-Correro
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
En la página "Productos", en el formulario "Buscar" podes buscar productos usando los códigos  2116, 2111 y 2253. Estos códigos devolverán el nombre del producto registrado en la base de datos.

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
