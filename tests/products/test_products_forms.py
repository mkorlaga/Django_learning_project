from django.test import TestCase
from products.forms import ProductForm


class ProductFormTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.form = ProductForm()

    def test_product_form_subtitle_label(self):
        self.assertTrue(self.form.fields['subtitle'].label is None or
                        self.form.fields['subtitle'].label == 'subtitle')

    def test_product_form_subtitle_placeholder(self):
        self.assertEqual(self.form.fields['subtitle'].widget.attrs['placeholder'], "Your Subtitle")

    def test_product_form_subtitle_is_requited(self):
        self.assertFalse(self.form.fields['subtitle'].required)

    def test_product_form_description_widget(self):
        self.assertEqual(self.form.fields['description'].widget.attrs['placeholder'], "Add description here")

    def test_product_form_fields_in_form(self):
        self.assertTrue({'title', 'description', 'price', 'subtitle'} == self.form.fields.keys())

    def test_product_form_clean_title_good(self):
        form = ProductForm(data={'title': 'DUDA',
                                 'price': 1337})
        self.assertFalse(form.is_valid())

    def test_product_form_clean_title_wrong(self):
        form = ProductForm(data={'title': 'Test title',
                                 'price': 1337})
        self.assertTrue(form.is_valid())

    def test_product_form_clean_description_good(self):
        form = ProductForm(data={'title': 'Test title',
                                 'price': 1337,
                                 'description': 'Test description'})
        self.assertTrue(form.is_valid())

    def test_product_form_clean_description_wrong(self):
        form = ProductForm(data={'title': 'Test title',
                                 'price': 1337,
                                 'description': 'DUPA'})
        self.assertFalse(form.is_valid())

    def test_product_form_clean_price_good(self):
        form = ProductForm(data={'title': 'Test title',
                                 'price': 99.99})
        self.assertTrue(form.is_valid())

    def test_product_form_clean_price_wrong(self):
        form = ProductForm(data={'title': 'Test title',
                                 'price': -99.99})
        self.assertFalse(form.is_valid())


