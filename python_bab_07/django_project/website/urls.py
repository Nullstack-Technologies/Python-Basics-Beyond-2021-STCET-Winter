"""
    test_project URL Configuration
"""
from django.urls import path

from .views import index, contact_us


urlpatterns = [
    # path('', hello_world),
    # path('contact-us/', hello_world_2),

    path('', index),
    path('contact-us/', contact_us),
]