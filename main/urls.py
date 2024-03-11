from django.urls import path, include
from .views import (
    home_page,
    contact_page,
)

app_name = 'main'

urlpatterns = [
    path('', home_page, name='home'),
    path('contact/', contact_page, name='contact'),
    path('api/', include('main.api.urls', namespace='api')),
    # path('category/', category_page, name='category'),
]