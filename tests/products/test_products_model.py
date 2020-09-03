from django.test import TestCase
from products.models import Product


class ProductModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Product.objects.create(title='Test title',
                               description='Test description',
                               price=666.66,
                               featured=True)

    def setUp(self) -> None:
        self.product = Product.objects.get(id=1)

    def test_product_model_title_label(self):
        field_label = self.product._meta.get_field('title').verbose_name
        self.assertEqual(field_label, 'title')

    def test_product_model_description_label(self):
        field_label = self.product._meta.get_field('description').verbose_name
        self.assertEqual(field_label, 'description')

    def test_product_model_price_label(self):
        field_label = self.product._meta.get_field('price').verbose_name
        self.assertEqual(field_label, 'price')

    def test_product_model_featured_label(self):
        field_label = self.product._meta.get_field('featured').verbose_name
        self.assertEqual(field_label, 'featured')

    def test_product_model_summary_label(self):
        field_label = self.product._meta.get_field('summary').verbose_name
        self.assertEqual(field_label, 'summary')

    def test_product_model_title_max_length(self):
        max_length = self.product._meta.get_field('title').max_length
        self.assertEqual(max_length, 128)

    def test_product_model_price_max_digits(self):
        max_digits = self.product._meta.get_field('price').max_digits
        self.assertEqual(max_digits, 10000)

    def test_product_model_price_decimal_places(self):
        max_digits = self.product._meta.get_field('price').decimal_places
        self.assertEqual(max_digits, 2)

    def test_product_model_summary_default(self):
        default_summary_value = self.product._meta.get_field('summary').default
        self.assertEqual(default_summary_value, 'This is great summary')

    def test_product_model_featured_default(self):
        default_featured_value = self.product._meta.get_field('featured').default
        self.assertEqual(default_featured_value, False)

    def test_product_model_get_absolute_url(self):
        # fail if urlconf is not defined
        self.assertEqual(self.product.get_absolute_url(), '/products/1/')


