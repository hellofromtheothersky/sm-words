from django.urls import path, include
from . import views

# URLconf
urlpatterns=[
    # path("accounts/", include("django.contrib.auth.urls")),
    path("accounts/login/", views.login_user, name='login'),
    path("accounts/logout/", views.logout_user, name='logout'),
    path('word_lists/', views.show_list_word, name="word_lists_words"),
    path('', views.show_list_word, name="word_lists_words"),
    path('ajax_word_crud/', views.ajax_word_crud),
    path('show_list_word/', views.show_list_word),
    path('ajax_crud_list/', views.ajax_crud_list),
]