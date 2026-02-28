from django.urls import path, include
from django.http import HttpResponse

def home_page(request):
    return HttpResponse("Welcome to app Home Page!")

urlpatterns = [
    path('sdf', home_page, name='home'),
]
