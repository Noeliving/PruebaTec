# 🚀 **Proyecto de Automatización Prueba Técnica**

Proyecto de automatización de pruebas web utilizando **Playwright**, **Pytest**, **Allure**, **GitHub Actions** y **Page Object Model (POM)** para la aplicación [Sauce Demo](https://www.saucedemo.com/). Incluye **CI/CD automatizado**, **reportes visuales avanzados**, **grabación de videos** y **gestión inteligente de evidencias**.


## 📁 **Estructura del Proyecto**

```
PruebaTec/                   # Carpeta raíz del proyecto
│
├── pages/                   # Page Objects (lógica de las páginas)
│   ├── login_page.py        # Lógica de login (abrir página, login, error)
│   └── inventory_page.py    # Lógica del inventario (productos, carrito)
│
├── tests/                   # Carpeta de tests 
│   ├── test_saucedemo2.py   # Tests principales
│   └── tests_forzados_fallo.py # Tests diseñados para fallar 
│
├── videos/                  # Videos de ejecución de tests (solo local)
├── conftest.py              # Configuración común de Pytest (fixtures, setup/teardown)
├── requirements.txt         # Dependencias del proyecto
├── README.md                # Documentación del proyecto
├── .github/                 # Workflows de GitHub Actions
├── .gitignore/              # Archivos y carpetas ignorados por Git
├── allure-results/          # Resultados de Allure (generados automáticamente solo en local)
├── allure-report/           # Reportes HTML generados (solo local)
└── venv/                    # Entorno virtual de Python (solo local)
```

> **💡 Nota:** Los reportes de Allure (`allure-results/` y `allure-report/, videos, venv`) están protegidos en `.gitignore` y solo se generan localmente. No se suben al repositorio para mantenerlo limpio y eficiente.

---

## 🤔 **Decisiones Tomadas**

- **Playwright** frente a Selenium: elegido por su mayor rapidez en la ejecución, soporte multiplataforma.
- **Pytest**: framework ligero y flexible para estructurar los tests, con soporte nativo de fixtures y marcadores.
- **Allure**: seleccionado para generar reportes claros con screenshots, vídeos y trazabilidad de pasos.
- **Patrón Page Object Model (POM)**: permite mantener el código limpio, escalable y fácil de mantener.
- **Evidencias automáticas**: se incluyen screenshots y vídeos en cada test, lo que facilita la validación y el reporte de defectos.
- **-Buenas prácticas con GitHub**:  
  - Creación de un repositorio en GitHub para almacenar el proyecto.  
  - Rama principal (`main`) , trabajando desde  rama secundaria para desarrollar.  
  - Commits incrementales y descriptivos tras cada avance.  
  - Uso de `push` progresivo para mantener la historia trazable.
  
- **Gestión de archivos con `.gitignore`**:  
  - Archivo `.gitignore` incluido en el repositorio para proteger archivos sensibles.  
  - Evita subir automáticamente reportes de Allure, videos y archivos temporales.  
  - Mantiene el repositorio limpio y eficiente, solo con código fuente.  
  - Permite que cada desarrollador genere sus propios reportes localmente.  
## 🛠️ **Configuración del Proyecto**

### 📋 Prerrequisitos
- Python 3.8+
- Navegadores web instalados (Chrome, Firefox, Webkit)
- Allure CLI instalado en el sistema

### 🔧 Instalación

1. **Clonar el repositorio**
   git clone:
2. **Crear y activar entorno virtual**
   ```bash
   python3 -m venv venv
   source venv/bin/activate  
   venv\Scripts\activate      
   ```

3. **Instalar dependencias**
   ```bash
   pip install -r requirements.txt
   playwright install
   ```

---

## 🚀 **Ejecución de Tests**

### 1. Ejecutar todos los tests
```bash
pytest
```

### 2. Ejecutar un archivo concreto
Estos lanzas los tres de una vez
pytest tests/test_saucedemo2.py
pytest tests/tests_forzados_fallo.py
```

### 3. Ejecutar por marcadores

Asi ejecuto el que considere necesario
pytest -m login_correcto
pytest -m login_incorrecto
pytest -m carrito
```

### 4. Generar reporte con Allure(asi me limpia y me genera cada vez)

---

## ⚙️ **Configuración de Pytest**

### Archivo pytest.ini
Se ha configurado un archivo `pytest.ini` para registrar las marcas personalizadas utilizadas en los tests:

```ini
[pytest]
markers =
    login_correcto: Tests relacionados con login exitoso
    login_incorrecto: Tests relacionados con login fallido
    carrito: Tests relacionados con funcionalidad del carrito
    api: Tests de APIs
    ui: Tests de interfaz de usuario
    smoke: Tests de humo (críticos)
    regression: Tests de regresión
```

**Beneficios:**
- ✅ Elimina advertencias de marcas desconocidas
- ✅ Ejecución de tests más limpia y profesional
- ✅ Organización clara de los tipos de tests
- ✅ Permite filtrar tests por categorías específicas

```###Genera el repote solo de un archivo###
rm -rf allure-results allure-report
pytest -v tests/test_saucedemo2.py --alluredir=allure-results
allure generate allure-results -o allure-report --clean
allure open allure-report
```
### . Generar reporte con marcador(asi me limpia y me genera cada vez)

 rm -rf allure-results allure-report && \
pytest -m login_incorrecto --alluredir=allure-results && \
allure generate allure-results -o allure-report --clean && \
allure open allure-report

💡 **NOTA:** Limpia resultados anteriores, ejecuta solo los tests marcados con el marcador en este caso login_correcto, genera el reporte de Allure y lo abre en el navegador.

### 4. Ejecutar tests forzados a fallo con reporte Allure  (para verificar que allure devuelve el error)
rm -rf allure-results allure-report
pytest -v tests/tests_forzados_fallo.py --alluredir=allure-results
allure generate allure-results -o allure-report --clean
allure open allure-report
```



## 🎬 **Tests Implementados**

1. **`test_login_correcto`**  
   - Login válido  
   - Valida acceso al inventario  
   - Adjunta screenshot y vídeo  

2. **`test_login_incorrecto`**  
   - Login inválido  
   - Valida mensaje de error  
   - Adjunta screenshot y vídeo  

3. **`test_carrito_dos_productos`**  
   - Añade 2 productos al carrito  
   - Verifica contador = 2  
   - Adjunta screenshot y vídeo  

4. **Tests forzados a fallo (`tests_forzados_fallo.py`)**  
   - Diseñados para mostrar cómo Allure refleja defectos (ejemplo: esperar 3 productos cuando solo hay 2).  



## 🔍 **Características del `conftest.py`**

El archivo `conftest.py` define un **fixture de Pytest** llamado `page`, que se encarga de:

1. Inicializar el navegador (Chromium, configurable a Firefox o Webkit).  
2. Configurar un contexto con **grabación de vídeo activada**.  
3. Abrir una nueva página y entregarla al test (`yield`).  
4. Cerrar la página, el contexto y el navegador automáticamente al finalizar cada test.  

Esto permite que todos los tests tengan **vídeos y screenshots automáticos** para evitar repetir código.


## 📱 **Page Objects**

El proyecto utiliza el patrón **Page Object Model (POM)** para separar la lógica de las páginas y hacer los tests más mantenibles y escalables.  

### 🔐 `login_page.py`
Contiene la clase `LoginPage`, que abstrae las interacciones con la pantalla de login de SauceDemo:
- **open()** → abre la URL principal de la aplicación.  
- **login(user, pwd)** → introduce usuario y contraseña y hace clic en el botón de login.  
- **get_error()** → devuelve el mensaje de error mostrado en pantalla tras un login inválido.  

👉 Gracias a esta clase, los tests no necesitan repetir selectores ni pasos, solo llaman a `login_page.login(...)`.  

---

### 🛍️ `inventory_page.py`
Contiene la clase `InventoryPage`, que gestiona la página de inventario tras el login:
- **is_loaded()** → verifica que el inventario se cargó correctamente.  
- **add_two_products()** → añade 2 productos concretos al carrito (backpack y bike light).  
- **get_cart_count()** → devuelve el número de productos en el carrito.  

👉 Esto permite validar fácilmente la funcionalidad del carrito sin repetir código en cada test.  


---

## 🔮 **Próximos Mejoras*

- [ ] Mejorar los tiempos en la ejecucion del test en Github
- [ ] Pruebas de regresión mas completas de flujo de negocio
- [ ] Añadir metricas de ejecución 
- [ ] Adaptar los tests de Playwright para que se ejecuten siempre en **modo headless** cuando corren en GitHub Actions.


- [ ] Extender la cobertura en las pruebas de API y realizar pruebas de performance  

---

**¡Seguiremos trabajando! 🚀**
