from django.urls import path
from .views import (
    home_page,
    contact_page,
    category_page,
)

app_name = 'main'

urlpatterns = [
    path('', home_page, name='home'),
    path('contact/', contact_page, name='contact'),
    path('category/', category_page, name='category'),
]