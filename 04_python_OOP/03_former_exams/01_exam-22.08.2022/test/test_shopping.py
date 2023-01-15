from shopping_cart import ShoppingCart
from unittest import TestCase, main

class ShoppingCartTest(TestCase):
    def setUp(self):
        self.shopping_cart = ShoppingCart("Test", 150)

    def test_correct_initialization(self):
        self.assertEqual("Test", self.shopping_cart.shop_name)
        self.assertEqual(150, self.shopping_cart.budget)
        self.assertEqual({}, self.shopping_cart.products)

    def test_invalid_shop_name_raise_value_error(self):
        with self.assertRaises(ValueError) as ve:
            self.shopping_cart.shop_name = "test"
        self.assertEqual("Shop must contain only letters and must start with capital letter!", str(ve.exception))

        with self.assertRaises(ValueError) as ve:
            self.shopping_cart.shop_name = "Test1"
        self.assertEqual("Shop must contain only letters and must start with capital letter!", str(ve.exception))

    def test_product_price_higher_than_hundred_raise_value_error(self):
        with self.assertRaises(ValueError) as ve:
            self.shopping_cart.add_to_cart("Banana", 101.00)
        self.assertEqual("Product Banana cost too much!", str(ve.exception))

    def test_adding_valid_product_to_cart(self):
        result = self.shopping_cart.add_to_cart("Banana", 75.50)
        self.assertEqual({"Banana": 75.50}, self.shopping_cart.products)
        self.assertEqual("Banana product was successfully added to the cart!", result)

    def test_product_to_remove_not_in_product_dict_raise_value_error(self):
        with self.assertRaises(ValueError) as ve:
            self.shopping_cart.remove_from_cart("Cherry")
        self.assertEqual("No product with name Cherry in the cart!", str(ve.exception))

    def test_valid_product_to_remove_from_cart(self):
        self.shopping_cart.add_to_cart("Banana", 75.50)
        self.shopping_cart.add_to_cart("Cherry", 20.00)
        result = self.shopping_cart.remove_from_cart("Banana")
        self.assertEqual({"Cherry": 20.00}, self.shopping_cart.products)
        self.assertEqual("Product Banana was successfully removed from the cart!", result)

    def test_add_method(self):
        first = ShoppingCart('Test', 200)
        first.add_to_cart('from_first', 1)
        second = ShoppingCart('SecondTest', 100)
        second.add_to_cart('from_second', 2)
        merged = first.__add__(second)
        self.assertEqual('TestSecondTest', merged.shop_name)
        self.assertEqual(300, merged.budget)
        self.assertEqual({'from_first': 1, 'from_second': 2}, merged.products)

    def test_buy_products_raise_value_error(self):
        self.shopping_cart.add_to_cart("Banana", 75.50)
        self.shopping_cart.add_to_cart("Cherry", 85.50)
        with self.assertRaises(ValueError) as ve:
            self.shopping_cart.buy_products()
        expected_result = "Not enough money to buy the products! Over budget with 11.00lv!"
        self.assertEqual(expected_result, str(ve.exception))

    def test_buy_products_works_properly(self):
        self.shopping_cart.add_to_cart("Banana", 50.50)
        self.shopping_cart.add_to_cart("Cherry", 20.50)
        result = self.shopping_cart.buy_products()
        self.assertEqual("Products were successfully bought! Total cost: 71.00lv.", result)

if __name__ == "__main__":
    main()
