from django.urls import path
from .views import (
    home_page,
    archive_page,
    contact_page,
)

app_name = 'main'

urlpatterns = [
    path('', home_page, name='home'),
    path('archive/', archive_page, name='archive'),
    path('contact/', contact_page, name='contact'),
]