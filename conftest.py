import os
import pytest
from playwright.sync_api import sync_playwright


# 🔹 Fixture para inicializar el navegador y la página en cada test
@pytest.fixture
def page():
    with sync_playwright() as p:
        # Detecta si se está ejecutando en CI/CD (GitHub Actions define CI=true)
        is_ci = os.getenv("CI") == "true"

        # Lanzar navegador Chromium
        browser = p.chromium.launch(
            headless=is_ci  # 👉 True en GitHub Actions, False en local
        )

        # Crear un contexto con grabación de vídeo activada
        context = browser.new_context(record_video_dir="tests/videos/")

        # Abrir nueva página en ese contexto
        page = context.new_page()

        # yield = entrega la página al test, y después ejecuta el bloque de cierre
        yield page

        # Cerrar contexto y navegador al finalizar el test
        context.close()
        browser.close()
