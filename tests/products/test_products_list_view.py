from django.test import TestCase
from django.urls import reverse
from products.models import Product


class ProductListViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        number_of_products = 14
        for product_id in range(number_of_products):
            Product.objects.create(title=f'Product no {product_id}.',
                                   price=100+product_id)

    def test_product_list_view_url_exists_at_desired_location(self):
        response = self.client.get('/products/')
        self.assertEqual(response.status_code, 200)

    def test_product_list_view_url_accessible_by_name(self):
        response = self.client.get(reverse('products:product_list_view'))
        self.assertEqual(response.status_code, 200)

    def test_product_list_view_uses_correct_template(self):
        response = self.client.get(reverse('products:product_list_view'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'products/product_list.html')

    def test_product_list_view_pagination_by_5(self):
        response = self.client.get(reverse('products:product_list_view'))
        self.assertEqual(response.status_code, 200)
        self.assertTrue('is_paginated' in response.context)
        self.assertTrue(response.context['is_paginated'] is True)
        self.assertEqual(response.context['paginator'].per_page, 5)

    def test_product_list_view_pagination_page_count_validation(self):
        response = self.client.get(reverse('products:product_list_view') + '?page=3')
        self.assertEqual(response.status_code, 200)
        self.assertTrue('is_paginated' in response.context)
        self.assertTrue(response.context['is_paginated'] is True)
        self.assertTrue(len(response.context['object_list']) == 14 % 5)
        self.assertEqual(response.context['paginator'].num_pages, 14//5 + 1)
