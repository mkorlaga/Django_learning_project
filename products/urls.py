from .views import (ProductCreateView,  # product_create_view,
                    ProductDetailView,  # product_detail_view,
                    ProductListView,  # product_list_view
                    ProductDeleteView, ProductUpdateView,  # product_delete_view,
                    )
from django.urls import path


app_name = 'products'
urlpatterns = [
    path("", ProductListView.as_view(template_name="products/product_list.html"), name='product_list_view'),                    # path("", product_list_view, name='product_list_view'),
    path('create/', ProductCreateView.as_view(template_name='products/product_create.html'), name='product_create_view'),       # path('create/', product_create_view, name='product_create_view'),
    path("<int:product_id>/", ProductDetailView.as_view(template_name='products/detail.html'), name='product_detail_view'),     # path("<int:product_id>/", product_detail_view, name='product_detail_view'),
    path("<int:product_id>/delete/", ProductDeleteView.as_view(), name='product_delete_view'),                                  # path("<int:product_id>/delete/", product_delete_view, name='product_delete_view'),
    path("<int:product_id>/edit/", ProductUpdateView.as_view(template_name='products/product_update.html'), name='product_update_view'),
]
