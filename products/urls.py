from .views import (product_create_view,
                    ProductDetailView, # product_detail_view,
                    product_delete_view,
                    ProductListView, # product_list_view
                    )
from django.urls import path


app_name = 'products'
urlpatterns = [
    path("", ProductListView.as_view(template_name="products/product_list.html"), name='product_list_view'),     # path("", product_list_view, name='product_list_view'),
    path('create/', product_create_view, name='product_create_view'),
    path("<int:product_id>/", ProductDetailView.as_view(template_name='products/detail.html'), name='product_detail_view'),     # path("<int:product_id>/", product_detail_view, name='product_detail_view'),
    path("<int:product_id>/delete/", product_delete_view, name='product_delete_view'),
]
