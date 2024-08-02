from django.urls import path
from .views import index_view, blog_view, contact_view, services_view, about_view

urlpatterns = [
    path('', index_view, name='home'),
    path('about/', about_view, name='about'),
    path('blog/', blog_view, name='blog'),
    path('contact/', contact_view, name='contact'),
    path('services/', services_view, name='services'),
]
