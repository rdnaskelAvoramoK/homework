from django.forms import ModelForm

from catalogue.models import Product, Purchase


class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ('title', 'description', 'price', 'storage')


class PurchaseForm(ModelForm):
    class Meta:
        model = Purchase
        fields = ('quantity',)


class Reclamation(ModelForm):
    class Meta:
        model = Purchase
        fields = '__all__'

