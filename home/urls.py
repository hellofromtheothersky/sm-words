from django.urls import path, include
from . import views

# URLconf
urlpatterns=[
    # path("accounts/", include("django.contrib.auth.urls")),
    path("accounts/login/", views.login_user, name='login'),
    path("accounts/logout/", views.logout_user, name='logout'),
    path('', views.show_list_word),
    path('ajax_add_word/', views.ajax_add_word),
    path('show_list_word/', views.show_list_word),
    path('ajax_crud_list/', views.ajax_crud_list),
]