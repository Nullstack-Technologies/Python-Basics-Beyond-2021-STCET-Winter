"""
    test_project URL Configuration
"""
from django.urls import path

from .views import (
    index, contact_us, 
    author_view,
    AuthorAddView
)


urlpatterns = [
    # path('', hello_world),
    # path('contact-us/', hello_world_2),

    path('', index),
    path('contact-us/', contact_us),
    path('authors/', author_view, name="author_add"),

    path('author-add/', AuthorAddView.as_view(), name="author_cbv_add"),

    # path('authors-list')


]
