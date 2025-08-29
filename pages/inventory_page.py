class InventoryPage:
    def __init__(self, page):
        self.page = page
        # selectores de la página de inventario
        self.inventory_container = '[data-test="inventory-container"]'
        self.cart_badge = '.shopping_cart_badge'
        self.backpack = '[data-test="add-to-cart-sauce-labs-backpack"]'
        self.bike_light = '[data-test="add-to-cart-sauce-labs-bike-light"]'

    def is_loaded(self):
        # comprueba que el inventario está visible
        return self.page.is_visible(self.inventory_container)

    def add_two_products(self):
        # añade dos productos al carrito
        self.page.click(self.backpack)
        self.page.click(self.bike_light)

    def get_cart_count(self):
        # devuelve el número del carrito
        return self.page.inner_text(self.cart_badge)
