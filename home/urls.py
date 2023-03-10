from django.urls import path
from . import views

# URLconf
urlpatterns=[
    path('add_word/', views.add_word),
    path('ajax_add_word/', views.ajax_add_word),
]