from django.shortcuts import render
from django.views.generic import ListView, DetailView

from product_module.models import Product, ProductVisit, ProductCategory
from utils.http_service import get_client_ip


# Create your views here.

class ProductListView(ListView):
    template_name = ''
    model = Product
    context_object_name = 'products'
    paginate_by = 10
    ordering = ['-create_date']

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(ProductListView, self).get_context_data()

    def get_queryset(self):
        pass


class ProductDetailView(DetailView):
    template_name = ''
    model = Product

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        request = self.request
        current_product = self.object
        user_ip = get_client_ip(request)
        user_id = None
        if request.user.is_authenticated:
            user_id = request.user.id
        has_been_visited = ProductVisit.objects.filter(ip__exact=user_ip, product_id=current_product.id).exists()
        if not has_been_visited:
            product_vist = ProductVisit(ip=user_ip, user_id=user_id, product_id=current_product.id)
            product_vist.save()
        return context


class ProductCategoryView(ListView):
    model = ProductCategory
    template_name = ''

    def get_queryset(self):
        query = super(ProductCategoryView, self).get_queryset()
        query = query.filter(is_active=True)
        return query

