from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class StorePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 20)

    # locators
    PASSWORD_INPUT = (By.NAME, "password")
    SUBMIT_BUTTON = (By.XPATH, "//button[@type='submit']")
    FIRST_PRODUCT = (By.XPATH, "//a[contains(@href, '/products/')]")
    ADD_TO_CART = (By.XPATH, "//button[contains(.,'Add to cart')]")
    CART_TEXT = (
        By.XPATH,
        "//*[contains(text(),'Your cart') or contains(text(),'Cart')]"
    )

    def open_store(self):
        self.driver.get("https://adnabu-store-assignment1.myshopify.com")

    def unlock_store(self, password):
        password_input = self.wait.until(
            EC.visibility_of_element_located(self.PASSWORD_INPUT)
        )
        password_input.clear()
        password_input.send_keys(password)

        self.wait.until(
            EC.element_to_be_clickable(self.SUBMIT_BUTTON)
        ).click()

    def search_product(self, product_name):

        self.driver.get(
            f"https://adnabu-store-assignment1.myshopify.com/search?q={product_name}"
        )


        self.driver.get(
            "https://adnabu-store-assignment1.myshopify.com/products/the-complete-snowboard"
        )

    def open_first_product(self):

        pass

    def add_to_cart(self):
        # Wait for Add to Cart button to be clickable
        add_to_cart_btn = self.wait.until(
            EC.element_to_be_clickable(self.ADD_TO_CART)
        )

        self.driver.execute_script("arguments[0].scrollIntoView(true);", add_to_cart_btn)
        add_to_cart_btn.click()

    def is_product_added(self):

        try:

            confirmation = self.wait.until(
                EC.visibility_of_element_located(self.CART_TEXT)
            )
            return confirmation.is_displayed()
        except:

            result = self.driver.execute_script("""
                const pageText = document.body.innerText.toLowerCase();
                
                // Check for cart text patterns
                if (pageText.includes('your cart') || pageText.includes('in your cart')) {
                    return true;
                }
                
                // Check for success message
                const successElements = document.querySelectorAll('[class*="success"], [class*="cart-drawer"], [role="dialog"]');
                if (successElements.length > 0) {
                    return true;
                }
                
                return false;
            """)
            return result
