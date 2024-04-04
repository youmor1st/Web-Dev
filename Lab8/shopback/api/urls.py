from django.urls import path

from . import views
from .views import MainView, ProductListView, ProductDetailView, CategoryListView, CategoryDetailView

urlpatterns = [
    path("", MainView.as_view()),
    path("products/", ProductListView.as_view(), name="product-list"),
    path("products/<int:pk>", ProductDetailView.as_view(), name="product_detail"),
    path("categories/", CategoryListView.as_view(), name="category-list"),
    path("categories/<int:pk>", CategoryDetailView.as_view(), name="category_detail"),
    # path("categories/<int:pk>/products", )
    # path("products/", views.product_list, name="products"),
    # path("categories/", views.category_list, name="category_list"),
    # path("categories/<int:pk>", views.category_detail, name="category_detail"),
    # path("categories/<int:pk>/products", views.category_products),
]