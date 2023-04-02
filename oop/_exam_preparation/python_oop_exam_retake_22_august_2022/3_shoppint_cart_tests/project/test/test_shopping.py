from project.shopping_cart import ShoppingCart
from unittest import TestCase, main


class ShoppingCartTest(TestCase):
    def setUp(self) -> None:
        self.cart1 = ShoppingCart("ShopOne", 100.0)
        self.cart2 = ShoppingCart("ShopTwo", 100.0)

    def test_correct_initialization(self):
        self.assertEqual(self.cart1.shop_name, "ShopOne")
        self.assertEqual(self.cart1.budget, 100.0)
        self.assertIsInstance(self.cart1.products, dict)
        self.assertEqual(self.cart1.products, {})

    def test_shop_name_with_number_raises_value_error(self):
        with self.assertRaises(ValueError) as ex:
            self.cart1.shop_name = "Shop1"
        self.assertEqual(str(ex.exception), "Shop must contain only letters and must start with capital letter!")

    def test_shop_name_with_space_raises_value_error(self):
        with self.assertRaises(ValueError) as ex:
            self.cart1.shop_name = "Shop A"
        self.assertEqual(str(ex.exception), "Shop must contain only letters and must start with capital letter!")

    def test_shop_name_without_first_capital_letter_raises_value_error(self):
        with self.assertRaises(ValueError) as ex:
            self.cart1.shop_name = "shop"
        self.assertEqual(str(ex.exception), "Shop must contain only letters and must start with capital letter!")

    def test_add_to_cart_raises_value_error_if_the_product_costs_100_plus(self):
        with self.assertRaises(ValueError) as ex:
            self.cart1.add_to_cart('Toy', 101.0)
        self.assertEqual(str(ex.exception), "Product Toy cost too much!")

    def test_add_to_cart_raises_value_error_if_the_product_costs_100(self):
        with self.assertRaises(ValueError) as ex:
            self.cart1.add_to_cart('Toy', 100.0)
        self.assertEqual(str(ex.exception), "Product Toy cost too much!")

    def test_add_to_cart_returns_correct_string_and_adds_the_product(self):
        self.cart1.add_to_cart('Doll', 1.0)
        result = self.cart1.add_to_cart('Toy', 99.0)
        self.assertEqual(result, "Toy product was successfully added to the cart!")
        self.assertEqual(self.cart1.products['Toy'], 99.0)
        self.assertEqual(self.cart1.products, {'Doll': 1.0, 'Toy': 99.0})

    def test_remove_from_cart_raises_value_error_for_non_existing_product(self):
        with self.assertRaises(ValueError) as ex:
            self.cart1.remove_from_cart('Doll')
        self.assertEqual(str(ex.exception), "No product with name Doll in the cart!")

    def test_remove_from_cart_returns_corrct_string_and_removes_the_product(self):
        self.cart1.add_to_cart('Toy', 99.0)
        self.cart1.add_to_cart('Doll', 34.0)
        self.assertEqual(self.cart1.products, {'Toy': 99.0, 'Doll': 34.0})
        result = self.cart1.remove_from_cart('Doll')
        self.assertEqual(result, "Product Doll was successfully removed from the cart!")
        self.assertEqual(self.cart1.products, {'Toy': 99.0})

    def test_combining_two_carts_sums_budgets_and_concat_names(self):
        self.cart1.add_to_cart('Toy', 30.0)
        self.cart2.add_to_cart('Doll', 20.0)
        self.cart3 = self.cart1 + self.cart2
        self.assertEqual(self.cart3.shop_name, self.cart1.shop_name + self.cart2.shop_name)
        self.assertEqual(self.cart3.budget, self.cart1.budget + self.cart2.budget)
        self.assertEqual(self.cart3.products, {'Toy': 30.0, 'Doll': 20.0})

    def test_buy_product_raises_value_error_if_we_exceed_the_budget(self):
        self.cart1.add_to_cart('Toy', 99.0)
        self.cart1.add_to_cart('Doll', 20.0)
        with self.assertRaises(ValueError) as ex:
            self.cart1.buy_products()
        self.assertEqual(str(ex.exception), "Not enough money to buy the products! Over budget with 19.00lv!")

    def test_buy_products_below_budget_returns_correct_string(self):
        self.cart1.add_to_cart('Doll', 20.0)
        result = self.cart1.buy_products()
        self.assertEqual(result, 'Products were successfully bought! Total cost: 20.00lv.')

    def test_buy_products_equal_to_budget_returns_correct_string(self):
        self.cart1.add_to_cart('Doll', 50.0)
        self.cart1.add_to_cart('Toy', 50.0)
        result = self.cart1.buy_products()
        self.assertEqual(result, 'Products were successfully bought! Total cost: 100.00lv.')


if __name__ == '__main__':
    main()
