from django.urls import path
from .views import int_page, srt_page


urlpatterns = [
    path('<int:rand_num>', int_page, name='int_page'),
    path('', srt_page, name="str_page")
]