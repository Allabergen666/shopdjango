from django.urls import path
from .views import IndexViev, AddProductViev, ProductViev

urlpatterns = [
    path("", IndexViev),
    path("add/", AddProductViev),
    path("product/", ProductViev),
    path("category/", ProductViev)
    ]