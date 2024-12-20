# Proyecto Final - CRUD Venta de Autos Usados con FastAPI

## Descripción
Este proyecto tiene como propósito desarrollar una API RESTful para la gestión de la venta de autos usados. Los usuarios pueden realizar operaciones CRUD (crear, leer, actualizar y eliminar) sobre los autos disponibles en la base de datos. Además, la aplicación incluye un sistema de autenticación mediante JWT (JSON Web Tokens) para proteger las rutas de acceso.

## Tecnologías Utilizadas
- **FastAPI**: Framework moderno de Python para crear APIs RESTful rápidas y de alto rendimiento.
- **Uvicorn**: Servidor ASGI para ejecutar la aplicación FastAPI.
- **MySQL**: Base de datos utilizada para almacenar la información de los autos.
- **SQLAlchemy**: ORM utilizado para interactuar con la base de datos (aunque en este caso la conexión se maneja directamente con `mysql.connector`).
- **JWT (JSON Web Tokens)**: Para la autenticación de usuarios mediante tokens.
- **CORS (Cross-Origin Resource Sharing)**: Middleware para permitir solicitudes entre diferentes orígenes.
- **Python**: Lenguaje de programación principal utilizado para el backend.

## Instalación y Ejecución

### 1. Clonar el repositorio
```bash
git clone https://github.com/juan-david-rodriguez/proyecto-crud-venta-autos.git
cd proyecto-crud-venta-autos
2. Crear un entorno virtual (opcional pero recomendado)
bash
Copiar código
python3 -m venv venv
source venv/bin/activate  # En Windows usa `venv\Scripts\activate`

3. Instalar las dependencias


pip install -r requirements.txt

4. Configurar la base de datos:

La base de datos debe tener una tabla cars con los siguientes campos:
id (INT, AUTO_INCREMENT, PRIMARY KEY)
marca (VARCHAR)
modelo (VARCHAR)
color (VARCHAR)
fecha_de_compra (DATE)

5. Ejecutar el servidor

uvicorn main:app --reload
Esto iniciará el servidor de desarrollo de FastAPI, disponible en http://127.0.0.1:8000.

6. Probar la API
Login: Realiza una solicitud POST a /login con el cuerpo JSON:

{
  "email": "juan@gmail.com",
  "password": "1234"
}

Obtendrás un access_token para autenticar futuras solicitudes.

Operaciones CRUD:

GET /users: Obtiene todos los autos en la base de datos.
POST /user: Crea un nuevo auto en la base de datos.
PUT /user/{id}: Actualiza un auto existente con el id especificado.
DELETE /user/{id}: Elimina un auto de la base de datos.
Rutas Disponibles
POST /login: Autenticación de usuario. Requiere un correo y una contraseña.
GET /users: Obtiene la lista de autos.
POST /user: Crea un nuevo auto en la base de datos.
PUT /user/{id}: Actualiza los datos de un auto existente.
DELETE /user/{id}: Elimina un auto de la base de datos.

7. CORS
La API permite solicitudes desde cualquier origen, gracias a la configuración de CORS.
Detalles del Proyecto
Autenticación: El sistema de login utiliza JWT para generar un token de acceso, que se debe incluir en los encabezados de las solicitudes como Authorization: Bearer <token>.
CRUD de Autos: Se pueden agregar, actualizar, obtener y eliminar autos de la base de datos. Los datos de los autos incluyen marca, modelo, color y fecha_de_compra.

## Integrantes del Proyecto
Juan David Rodríguez - Desarrollador principal y encargado de la implementación del backend y creacion y coneccion del frontend con el backend, la conexión a la base de datos y la autenticación con JWT.

Enlaces

API https://github.com/jdu855/backend-FastAPI.git
Frontend https://github.com/jdu855/frontedhtml.git
