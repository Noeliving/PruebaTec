# 🚀 **Proyecto de Automatización Prueba Técnica**

Proyecto de automatización de pruebas web utilizando **Playwright**, **Pytest**, **Allure**, **GitHub Actions** y **Page Object Model (POM)** para la aplicación [Sauce Demo](https://www.saucedemo.com/). Incluye **CI/CD automatizado**, **reportes visuales**, **grabación de vídeos** y **gestión de evidencias**.

---

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
├── Api/                     # Tests de APIs
│   ├── test_api_tecnico.py  # Tests de ReqRes API
│   └── README_APIs.md       # Documentación de APIs
│
├── .github/                 # Workflows de GitHub Actions
│   └── workflows/
│       └── tests.yml        # CI/CD para tests web y API
│
├── conftest.py              # Configuración común de Pytest (fixtures, setup/teardown)
├── pytest.ini               # Configuración de marcas personalizadas
├── requirements.txt         # Dependencias del proyecto
├── README.md                # Documentación del proyecto
├── .gitignore               # Archivos y carpetas ignorados por Git
│
├── videos/                  # Vídeos de ejecución de tests (solo local)
├── allure-results/          # Resultados de Allure web (solo local)
├── allure-results-api/      # Resultados de Allure API (solo local)
├── allure-report/           # Reportes HTML web (solo local)
├── allure-report-api/       # Reportes HTML API (solo local)
└── venv/                    # Entorno virtual de Python (solo local)
```

> **💡 Nota:** Los reportes de Allure (`allure-results/` y `allure-report/`), los vídeos y el entorno virtual (`venv/`) están protegidos en `.gitignore` y solo se generan localmente. No se suben al repositorio para mantenerlo limpio y eficiente.

---

## 🤔 **Decisiones Tomadas**

- **Playwright** frente a Selenium: elegido por su mayor rapidez en la ejecución y soporte multiplataforma.  
- **Pytest**: framework ligero y flexible para estructurar los tests, con soporte nativo de fixtures y marcadores.  
- **Allure**: seleccionado para generar reportes claros con vídeos y trazabilidad de pasos.  
- **Patrón Page Object Model (POM)**: permite mantener el código limpio, escalable y fácil de mantener.  
- **Evidencias automáticas**: se incluyen vídeos en cada test, lo que facilita la validación y el reporte de defectos.

- **Buenas prácticas con GitHub**:  
  - Creación de un repositorio en GitHub para almacenar el proyecto.  
  - Rama principal (`main`), trabajando desde ramas secundarias para desarrollar.  
  - Commits incrementales y descriptivos tras cada avance.  
  - Uso de `push` progresivo para mantener la historia trazable.  

- **Gestión de archivos con `.gitignore`**:  
  - Evita subir automáticamente reportes de Allure, vídeos y archivos temporales.  
  - Mantiene el repositorio limpio y eficiente, solo con código fuente.  
  - Permite que cada desarrollador genere sus propios reportes localmente.  

---

## 🛠️ **Configuración del Proyecto**

### 📋 Prerrequisitos
- Python 3.8+  
- Navegadores web instalados (Chrome, Firefox, Webkit)  
- Allure CLI instalado en el sistema  

### 🔧 Instalación

1. **Clonar el repositorio**
   ```bash
   git clone <url-del-repo>
   cd PruebaTec
   ```

2. **Crear y activar entorno virtual**
   ```bash
   python3 -m venv venv
   source venv/bin/activate  
   ```

3. **Instalar dependencias**
   ```bash
   pip install -r requirements.txt
   playwright install
   ```

---

## 🚀 **Ejecución de Tests**

### 📋 Precondiciones
- Ruta del proyecto (ejemplo en mi caso): `/home/ncodes/Escritorio/PruebaTec`  
- Entorno virtual activado :
  python3 -m venv venv 
  source venv/bin/activate 
- Dependencias instaladas (`pip install -r requirements.txt`)  

---

### 1. Ejecutar todos los tests sin reporte
```bash
pytest
```

### 2. Ejecutar un archivo concreto
```bash
pytest tests/test_saucedemo2.py
pytest tests/tests_forzados_fallo.py
```

### 3. Ejecutar por marcadores
```bash
pytest -m login_correcto
pytest -m login_incorrecto
pytest -m carrito
```

### 4. Generar reporte con Allure (ejemplo sencillo)
```bash
pytest -v tests/test_saucedemo2.py --alluredir=allure-results
allure generate allure-results --clean -o allure-report
allure open allure-report
```

### 5. Generar reporte limpio solo de un archivo
```bash
rm -rf allure-results allure-report
pytest -v tests/test_saucedemo2.py --alluredir=allure-results
allure generate allure-results -o allure-report --clean
allure open allure-report
```

### 6. Generar reporte con marcador
```bash
rm -rf allure-results allure-report
pytest -m login_incorrecto --alluredir=allure-results
allure generate allure-results -o allure-report --clean
allure open allure-report
```

💡 **NOTA:** Limpia resultados anteriores, ejecuta solo los tests marcados con el marcador indicado, genera el reporte de Allure y lo abre en el navegador.

### 7. Ejecutar tests forzados a fallo con Allure
```bash
rm -rf allure-results allure-report
pytest -v tests/tests_forzados_fallo.py --alluredir=allure-results
allure generate allure-results -o allure-report --clean
allure open allure-report
```

---

## ⚙️ **Configuración de Pytest**

### Archivo `pytest.ini`
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

---

## 🎬 **Tests Implementados**

1. **`test_login_correcto`**  
   - Login válido  
   - Valida acceso al inventario  
   - Adjunta vídeo  

2. **`test_login_incorrecto`**  
   - Login inválido  
   - Valida mensaje de error  
   - Adjunta vídeo  

3. **`test_carrito_dos_productos`**  
   - Añade 2 productos al carrito  
   - Verifica contador = 2  
   - Adjunta vídeo  

4. **Tests forzados a fallo (`tests_forzados_fallo.py`)**  
   - Diseñados para mostrar cómo Allure refleja defectos (ejemplo: esperar 3 productos cuando solo hay 2).  

---

## 🔍 **Características del `conftest.py`**

El archivo `conftest.py` define un **fixture de Pytest** llamado `page`, que se encarga de:

1. Inicializar el navegador (Chromium, configurable a Firefox o Webkit).  
2. Configurar un contexto con **grabación de vídeo activada**.  
3. Abrir una nueva página y entregarla al test (`yield`).  
4. Cerrar la página, el contexto y el navegador automáticamente al finalizar cada test.  

👉 Esto permite que todos los tests tengan **vídeos automáticos** de la ejecución, evitando repetir código.

---

## 📱 **Page Objects**

El proyecto utiliza el patrón **Page Object Model (POM)** para separar la lógica de las páginas y hacer los tests más mantenibles y escalables.  

### 🔐 `login_page.py`
- **open()** → abre la URL principal.  
- **login(user, pwd)** → introduce credenciales y hace clic en login.  
- **get_error()** → devuelve el mensaje de error tras un login inválido.  

👉 Evita repetir selectores o pasos en los tests.  

### 🛍️ `inventory_page.py`
- **is_loaded()** → verifica que el inventario se cargó.  
- **add_two_products()** → añade dos productos concretos al carrito.  
- **get_cart_count()** → devuelve el número de productos en el carrito.  

👉 Facilita validar la funcionalidad del carrito de forma reutilizable.  

---

## 🔮 **Próximas Mejoras**

- [ ] Mejorar los tiempos de ejecución en GitHub Actions  
- [ ] Añadir pruebas de regresión más completas de flujo de negocio  
- [ ] Exportar reportes legibles sin necesidad de Allure  
- [ ] Añadir métricas de ejecución  
- [ ] Forzar modo headless en Playwright al ejecutar en GitHub Actions  
- [ ] Realizar pruebas de performance con herramientas como JMeter simulando carga de usuarios  

---

**¡Seguiremos trabajando! 🚀**
