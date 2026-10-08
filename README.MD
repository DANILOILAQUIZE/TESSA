Caso TESSA Corporation:

Necesitamos un pequeño microservicio backend que interactúe con una base de datos y consuma información de un proveedor externo. Para completar se puede realizar en el lenguaje/framework de tu preferencia (Node.js, Python, Java, PHP, etc.).

REQUISITOS INDISPENSABLES:

1. Base de Datos (Configuración Rápida):

Te entregamos adjunto a esta prueba el archivo tessa.db (SQLite) que ya contiene la tabla VariedadFlor y datos de prueba. Te recomendamos usar este archivo para ahorrar tiempo de configuración. (Nota: Si tienes un template rápido, puedes usar Docker para levantar SQL Server o PostgreSQL, pero sugerimos SQLite por tiempo).

Descargar archivo tessa.db aquí

2. Desarrollo de la API (Solo 2 Endpoints):

Endpoint POST /flores: Debe recibir un JSON con los campos nombre, color y precio_tallo, e insertar este nuevo registro en tu base de datos.
Endpoint GET /flores (Con API Externa): Debe listar todas las flores de la base de datos. El Reto: Dentro de este mismo endpoint, tu código debe hacer una petición a https://jsonplaceholder.typicode.com/posts/1 y adjuntar el campo body que devuelve esta API como una nueva propiedad llamada descripcion_agronomica en cada flor de tu respuesta.
3. Contenedores (Docker):

Crea un Dockerfile que empaquete tu aplicación.
Crea un archivo docker-compose.yml que levante el proyecto.
4. Entrega Correcta (Git/GitHub):

El repositorio debe ser público.
Crítico: Debes incluir el archivo de la base de datos SQLite en tu commit (o el script de creación si usas otro motor) para que el proyecto funcione clonando y corriendo un solo comando.
Debe tener un archivo README.md breve explicando cómo levantar el proyecto.
PUNTOS DESEABLES:

Interfaz Gráfica (UI): Un simple archivo index.html servido desde tu backend que consuma tu endpoint GET y muestre las flores en una tabla o tarjetas presentables.
Buenas Prácticas: Código limpio, uso de variables de entorno, manejo de errores (bloques try/catch) y separación de responsabilidades (controladores separados de las rutas).
Tu Entrega: