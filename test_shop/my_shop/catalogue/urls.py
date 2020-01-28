from django.urls import path

from catalogue.views import Products, ProductCreate, ProductDelete, PurchaseView


urlpatterns = [
    path('', Products.as_view(), name="list"),
    path('product/create/', ProductCreate.as_view(), name="product_create"),
    path('product/<int:pk>/delete/', ProductDelete.as_view(), name="product_delete"),
    path('product/create/', PurchaseView.as_view(), name='purchase_create'),
]
