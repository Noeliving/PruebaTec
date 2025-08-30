# 📘 README – Pruebas de API con Postman + Newman (ReqRes API)

## 🔹 1. Objetivo
Validar el comportamiento de la API pública [ReqRes](https://reqres.in) mediante pruebas en **Postman** y su posterior **migración a Python con pytest**, comprobando **casos correctos y de error** (login válido, login inválido y listado de usuarios con emails válidos).  

Como mejora, se integra también la ejecución automática en **GitHub Actions**, permitiendo lanzar los tests al pulsar en el runner.



## 📌 2.Decisiones tomadas

1. **Pruebas en Postman**
   - Inicialmente se cree los tests en **Postman** utilizando scripts en JavaScript en cada request.
   - Los ejecute manualmente para comprobar:
     - Códigos de estado (`200`, `400`).
     - Presencia de `token` en login correcto.
     - Mensaje de error en login incorrecto.
     - Lista de usuarios con emails válidos (regex).

2. **Migración a Python (Pytest)**
   - Posteriormente, estos mismos tests se trasladaron a **Python** utilizando `pytest` y la librería `requests`.
   - Se implementaron las mismas validaciones con asserts (`assert response.status_code == 200`, validación emails, etc.).
   - 👉 En esta migración también se cambió el **lenguaje de implementación**:  
     de **JavaScript** (scripts de Postman) a **Python** (pytest + requests).  
     La lógica de validación se mantuvo igual, pero con un framework más flexible y orientado a la automatización.
   - Esto permite estructurar mejor la integración con reportes pytest-html) y pipelines CI/CD.


## 🔹 3. Cómo ejecutar los tests (flujo completo)
 📂 1. Ir a la ruta del proyecto  
 🛠️ 2. Crear y activar entorno virtual  

# Crear entorno
python3 -m venv venv
# Activar entorno
source venv/bin/activate

### 📦 3. Instalar dependencias necesarias  
pip install requests pytest allure-pytest pytest-html
## 🧪 4. Ejecutar test  
pytest -v tests/api/test_api_tecnico.py

### 📊 Generar reporte HTML de API  
```bash
pytest -v tests/api/test_api_tecnico.py --html=report_api.html --self-contained-html

👉 El archivo `report_api.html` se genera en la carpeta del proyecto y puede abrirse en cualquier navegador.  
## 🔹 4. Resultados esperados
- **Login Correcto** → Devuelve 200 y token.  
- **Login Error** → Devuelve 400 y `"Missing password"`.  
- **Get Users** → Devuelve lista de usuarios con emails válidos.  


🔹### 5. **Casos de prueba realizados y explicados**
```bash

### ✅ Caso 1: Login Correcto – `POST /api/login`
**Request Body**  
```json
{
  "email": "eve.holt@reqres.in",
  "password": "cityslicka"
}
```

**Tests**
```javascript
pm.test("Status code is 200", function () {
    pm.response.to.have.status(200);
});

pm.test("Response has token", function () {
    let jsonData = pm.response.json();
    pm.expect(jsonData).to.have.property("token");
    pm.expect(jsonData.token).to.be.a("string").and.not.empty;
});
```

**✔️ Qué valida**
- Que la API responde con **200 OK**.  
- Que existe un campo `token` en la respuesta y no está vacío.  

**❌ Cómo provoqué un fallo**  
- Cambiando la URL a `/api/logins` (con “s”).  
- Resultado: devolvía `201 Created` con `id` y `createdAt` en lugar de `200 + token`.  
- El test falló al no encontrar el `token`.  

---

### ✅ Caso 2: Login Error – `POST /api/login`
**Request Body**  
```json
{
  "email": "peter@klaven"
}
```

**Tests**
```javascript
pm.test("Status code is 400", function () {
    pm.response.to.have.status(400);
});

pm.test("Response has error message", function () {
    let jsonData = pm.response.json();
    pm.expect(jsonData).to.have.property("error");
    pm.expect(jsonData.error).to.be.a("string").and.not.empty;
    pm.expect(jsonData.error).to.eql("Missing password");
});
```

**✔️ Qué valida**
- Que la API devuelve **400 Bad Request** cuando falta el `password`.  
- Que existe un campo `error` en la respuesta.  
- Que el mensaje es exactamente `"Missing password"`.  

**❌ Cómo provoqué un fallo**  
- Si en vez de quitar el `password` pongo uno incorrecto, la API responde igualmente `200 OK` con token 
- El test falló porque esperaba un `400`.  

---

// ✅ Validar que la respuesta devuelve código 200
pm.test("Status code is 200", function () {
    pm.response.to.have.status(200);
});

// ✅ Validar que la respuesta pertenece a la página 2
pm.test("Response is from page 2", function () {
    let jsonData = pm.response.json();
    pm.expect(jsonData.page).to.eql(2, "The response is not from page 2");
});

// ✅ Validar que la respuesta contiene un array de usuarios y que no está vacío
pm.test("Response has a list of users", function () {
    let jsonData = pm.response.json();
    pm.expect(jsonData.data).to.be.an("array").that.is.not.empty;
});

// ✅ Validar que todos los usuarios tienen emails válidos
pm.test("All users have valid emails", function () {
    let jsonData = pm.response.json();

    // Asegurar que hay usuarios en la lista
    pm.expect(jsonData.data.length).to.be.above(0, "No users found in response");

    // Validar formato de los correos electrónicos con regex
    jsonData.data.forEach(user => {
        pm.expect(user).to.have.property("email");
        pm.expect(user.email).to.match(/^[^@]+@[^@]+\.[^@]+$/);
    });
});


---



---

# 🔮 6. Mejoras Futuras en Automatización

- **Uso de variables y environments**: parametrizar la colección con variables (`{{baseUrl}}`, `{{token}}`, `{{email}}`, `{{password}}`) para reutilizarla en distintos entornos (dev, pre, prod) y evitar modificar las requests manualmente.  

- **Variables dinámicas y pre-request scripts**: generar valores en tiempo de ejecución (ej. `page`, contraseñas aleatorias o tokens de sesión) para validar que la API responde correctamente tanto con datos válidos como inválidos. Estos scripts son compatibles con Postman y también con Newman.  

- **Data-set para login**: usar un dataset (CSV/JSON) con múltiples combinaciones de credenciales para validar de forma masiva los distintos casos de autenticación (login correcto, login sin password, login con email erróneo, etc.) sin duplicar tests.  

- **Encadenar requests en flujo completo**: automatizar un flujo de negocio, por ejemplo: crear un usuario (`POST /users`), consultarlo (`GET /users/{id}`) y eliminarlo (`DELETE /users/{id}`), validando en cada paso que la respuesta es la esperada. También incluir el uso del `token` obtenido en el login correcto como variable en las siguientes peticiones.  

- **Automatización en pipeline**: integrar la colección en un pipeline de CI/CD (ej. GitHub Actions) para que las pruebas se ejecuten automáticamente con cada `push` o `pull request`, generando reportes de forma continua y fáciles de consultar por cualquier miembro del equipo.  

