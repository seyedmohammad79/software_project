from django.urls import path
from . import views

urlpatterns = [
    path('', views.ProductListView.as_view(), name='product_list_page'),
    path('<slug:slug>', views.ProductDetailView.as_view(), name='product_detail_page'),
    # path('category/', '', name='category_page'),
    # path('category/<cat>', '', name='product_category')
]
