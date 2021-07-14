from .views import ContactFormView,ContactResultView
from django.urls import path
from . import views

urlpatterns = [
    path('',views.toppage,name = 'toppage'),
    path('contact/', ContactFormView.as_view(), name='contact_form'),
    path('contact/result/', ContactResultView.as_view(), name='contact_result'),
]
