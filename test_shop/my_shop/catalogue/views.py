# Create your views here.
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, CreateView, DeleteView

from catalogue.forms import ProductForm, PurchaseForm
from catalogue.models import Product, Purchase


class Products(ListView):
    model = Product
    template_name = 'list/index.html'
    paginate_by = 10

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)
        context.update({
            'product_form': ProductForm
        })
        return context


class ProductCreate(LoginRequiredMixin, CreateView):
    model = Product
    http_method_names = ['get', 'post']
    success_url = '/create/'
    form_class = ProductForm
    template_name = 'list/create.html'


class ProductDelete(LoginRequiredMixin, DeleteView):
    model = Product
    http_method_names = ['post']
    success_url = '/'


class PurchaseView(LoginRequiredMixin, CreateView):
    model = Purchase
    http_method_names = ['post']
    success_url = '/'
    form_class = PurchaseForm

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.creator = self.request.user
        self.object.save()
        return super().form_valid(form)


#class PurchaseView(CeateView):
#
#         def post (self,request, *args, **kwargs):
#             # product id
#             purchase
#