from django.urls import path, include
from . import views

# URLconf
urlpatterns=[
    # path("accounts/", include("django.contrib.auth.urls")),
    path("accounts/login/", views.login_user, name='login'),
    path("accounts/logout/", views.logout_user, name='logout'),
    path('', views.add_word, name='add_word'),
    path('add_word/', views.add_word, name='add_word'),
    path('ajax_add_word/', views.ajax_add_word),
]