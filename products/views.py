from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView

from .models import Product
from .forms import ProductForm


def product_create_view(request, *args, **kwargs):
    initial_data = {
        'price': 199.99,
        'description': 'Default description',
        'title': 'Default title'
    }
    # to edit certain object we get the object (hardcoded below) and pass 'obj' as 'instance=obj' parameter to our form
    # obj = Product.objects.get(id=1)
    # form = ProductForm(instance=obj)
    if request.method == 'POST':
        form = ProductForm(request.POST)        # passing the request.POST data stright as form without checking if request.method is POST or GET or other
        if form.is_valid():
            form.save()                                 # ==Product.objects.create(title=request.POST.get('title'),description=request.POST.get('description'), price=request.POST.get('price')) as fields in products/forms.py
            form = ProductForm(initial=initial_data)                        # rerendering the form so it is empty
    else:
        form = ProductForm(initial=initial_data)
    context = {
        'form': form
    }
    return render(request, 'products/product_create.html', context=context)


# def product_detail_view(request, *args, **kwargs):
#     obj = get_object_or_404(Product, id=kwargs.get('product_id'))
#     context = {
#         "object": obj
#     }
#     return render(request, 'products/detail.html', context=context)


class ProductDetailView(DetailView):
    model = Product

    def get(self, request, *args, **kwargs):
        product = get_object_or_404(Product, id=self.kwargs.get('product_id'))
        return render(request, template_name=self.template_name, context={'object': product})


def product_delete_view(request, *args, **kwargs):
    obj = get_object_or_404(Product, id=kwargs.get('product_id'))
    if request.method == 'POST':
        obj.delete()
        redirect('product_create_view')
    context = {
        'object': obj
    }
    return render(request, "products/product_delete.html", context=context)


# def product_list_view(request, *args, **kwargs):
#     queryset = Product.objects.all()
#     context = {
#         'object_list': queryset
#     }
#     return render(request, "products/product_list.html", context=context)


class ProductListView(ListView):
    model = Product
    context_object_name = 'object_list'
    paginate_by = 5


#TODO
# Dokończyć zmianę funkcyjnych na klasy