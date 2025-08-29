import allure
from playwright.sync_api import sync_playwright


@allure.feature("Login")
@allure.story("Login Correcto")
def test_login_correcto():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context(record_video_dir="videos/")
        page = context.new_page()

        with allure.step("Abrir la página de login"):
            page.goto("https://www.saucedemo.com/")

        with allure.step("Introducir credenciales válidas"):
            page.fill('[data-test="username"]', "standard_user")
            page.fill('[data-test="password"]', "secret_sauce")

        with allure.step("Hacer clic en el botón Login"):
            page.click('[data-test="login-button"]')

        with allure.step("Validar que se accede al inventario"):
            assert page.is_visible('[data-test="inventory-container"]')
            screenshot = page.screenshot()
            allure.attach(screenshot, name="Inventario", attachment_type=allure.attachment_type.PNG)

        # Guardar vídeo
        context.close()
        browser.close()


@allure.feature("Login")
@allure.story("Login Incorrecto")
def test_login_incorrecto():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context(record_video_dir="videos/")
        page = context.new_page()

        with allure.step("Abrir la página de login"):
            page.goto("https://www.saucedemo.com/")

        with allure.step("Introducir credenciales inválidas"):
            page.fill('[data-test="username"]', "usuario_malo")
            page.fill('[data-test="password"]', "clave_mala")

        with allure.step("Hacer clic en el botón Login"):
            page.click('[data-test="login-button"]')

        with allure.step("Validar mensaje de error"):
            assert page.is_visible('[data-test="error"]')
            msg = page.inner_text('[data-test="error"]')
            allure.attach(msg, name="Mensaje de Error", attachment_type=allure.attachment_type.TEXT)
            screenshot = page.screenshot()
            allure.attach(screenshot, name="Error_Login", attachment_type=allure.attachment_type.PNG)

        context.close()
        browser.close()


@allure.feature("Carrito")
@allure.story("Añadir productos")
def test_carrito_dos_productos():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context(record_video_dir="videos/")
        page = context.new_page()

        with allure.step("Hacer login válido"):
            page.goto("https://www.saucedemo.com/")
            page.fill('[data-test="username"]', "standard_user")
            page.fill('[data-test="password"]', "secret_sauce")
            page.click('[data-test="login-button"]')

        with allure.step("Añadir 2 productos al carrito"):
            page.click('[data-test="add-to-cart-sauce-labs-backpack"]')
            page.click('[data-test="add-to-cart-sauce-labs-bike-light"]')

        with allure.step("Validar que el contador del carrito es 2"):
            contador = page.inner_text('.shopping_cart_badge')
            assert contador == "2"
            allure.attach(contador, name="Contador Carrito", attachment_type=allure.attachment_type.TEXT)
            screenshot = page.screenshot()
            allure.attach(screenshot, name="Carrito", attachment_type=allure.attachment_type.PNG)
        context.close()
        browser.close()

