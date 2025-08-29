import pytest
import allure
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage


@pytest.mark.fallo_forzado
@allure.feature("Fallo Forzado")
def test_login_correcto_fallo_forzado(page):
    login = LoginPage(page)
    inventory = InventoryPage(page)

    with allure.step("Abrir página de login"):
        login.open()

    with allure.step("Iniciar sesión con credenciales inválidas (fallo forzado)"):
        login.login("loginforzadomal", "secret_sauce")

    with allure.step("Validar acceso al inventario"):
        try:
            assert inventory.is_loaded(), "El inventario no cargó tras login forzado a fallo"
            screenshot = page.screenshot()
            allure.attach(screenshot, name="Inventario_OK", attachment_type=allure.attachment_type.PNG)
        except AssertionError as e:
            screenshot = page.screenshot()
            allure.attach(screenshot, name="Error_LoginCorrecto", attachment_type=allure.attachment_type.PNG)
            raise e

    # 🎥 Adjuntar video
    video_path = page.video.path()
    allure.attach.file(video_path, name="Video_LoginCorrecto", attachment_type=allure.attachment_type.WEBM)
    page.close()


@pytest.mark.fallo_forzado
@allure.feature("Fallo Forzado")
def test_login_incorrecto_fallo_forzado(page):
    login = LoginPage(page)

    with allure.step("Abrir página de login"):
        login.open()

    with allure.step("Iniciar sesión con credenciales inválidas"):
        login.login("standard_user", "secret_sauce")

    with allure.step("Validar mensaje de error forzado"):
        try:
            error_msg = login.get_error()
            assert "NIIDEA" in error_msg, "El mensaje esperado no apareció (fallo forzado)"
            allure.attach(error_msg, name="Mensaje de Error", attachment_type=allure.attachment_type.TEXT)
            screenshot = page.screenshot()
            allure.attach(screenshot, name="LoginIncorrecto_OK", attachment_type=allure.attachment_type.PNG)
        except AssertionError as e:
            screenshot = page.screenshot()
            allure.attach(screenshot, name="Error_LoginIncorrecto", attachment_type=allure.attachment_type.PNG)
            raise e

    # 🎥 Adjuntar video
    video_path = page.video.path()
    allure.attach.file(video_path, name="Video_LoginIncorrecto", attachment_type=allure.attachment_type.WEBM)
    page.close()


@pytest.mark.fallo_forzado
@allure.feature("Fallo Forzado")
def test_carrito_fallo_forzado(page):
    login = LoginPage(page)
    inventory = InventoryPage(page)

    with allure.step("Login correcto"):
        login.open()
        login.login("standard_user", "secret_sauce")

    with allure.step("Añadir 2 productos al carrito"):
        inventory.add_two_products()

    with allure.step("Validar contador del carrito forzado"):
        try:
            count = inventory.get_cart_count()
            assert count == "3", f"El contador debería ser 3 pero es {count} (fallo forzado)"
            allure.attach(count, name="ContadorCarrito", attachment_type=allure.attachment_type.TEXT)
            screenshot = page.screenshot()
            allure.attach(screenshot, name="Carrito_OK", attachment_type=allure.attachment_type.PNG)
        except AssertionError as e:
            screenshot = page.screenshot()
            allure.attach(screenshot, name="Error_Carrito", attachment_type=allure.attachment_type.PNG)
            raise e

    # 🎥 Adjuntar video
    video_path = page.video.path()
    allure.attach.file(video_path, name="Video_Carrito", attachment_type=allure.attachment_type.WEBM)
    page.close()

