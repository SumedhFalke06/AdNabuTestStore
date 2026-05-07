from page.store_page import StorePage
import logging


# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def test_search_and_add_to_cart(driver):
    """Test to search for a product and add it to cart successfully"""
    # Store driver reference for screenshot capture on failure
    test_search_and_add_to_cart._driver = driver

    logger.info("Starting test: Search and Add to Cart")

    try:
        store = StorePage(driver)

        logger.info("Opening store page")
        store.open_store()

        logger.info("Unlocking store with password")
        store.unlock_store("AdNabuQA")

        logger.info("Searching for product: snowboard")
        store.search_product("snowboard")

        logger.info("Opening first product")
        store.open_first_product()

        logger.info("Adding product to cart")
        store.add_to_cart()

        logger.info("Verifying product was added to cart")
        assert store.is_product_added(), "Product was not successfully added to cart"

        logger.info("Test passed: Product successfully added to cart")

    except Exception as e:
        logger.error(f"Test failed with error: {str(e)}")
        raise
