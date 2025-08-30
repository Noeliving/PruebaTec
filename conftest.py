import pytest
import os
from playwright.sync_api import sync_playwright


# 🔹 Fixture para inicializar el navegador y la página en cada test
@pytest.fixture
def page():
    with sync_playwright() as p:
        # Detectar automáticamente si estamos en CI/CD o entorno local
        is_ci = os.getenv('CI') == 'true' or os.getenv('GITHUB_ACTIONS') == 'true'
        is_headless_env = not os.getenv('DISPLAY') or is_ci
        
        # Configurar navegador según el entorno
        browser_args = []
        if is_headless_env:
            # Argumentos para entornos sin interfaz gráfica (CI/CD, servidores)
            browser_args = [
                '--no-sandbox',
                '--disable-dev-shm-usage',
                '--disable-gpu',
                '--disable-web-security',
                '--disable-features=VizDisplayCompositor'
            ]
        
        # Lanzar navegador Chromium con configuración automática
        browser = p.chromium.launch(
            headless=is_headless_env,  # True en CI/CD, False en local
            args=browser_args
        )

        # Crear un contexto con grabación de vídeo activada
        context = browser.new_context(record_video_dir="videos/")

        # Abrir nueva página en ese contexto
        page = context.new_page()

        # yield = entrega la página al test, y después ejecuta el bloque de cierre
        yield page

        # Cerrar contexto y navegador al finalizar el test
        context.close()
        browser.close()
