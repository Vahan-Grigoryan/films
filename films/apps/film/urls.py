from django.urls import path, include
from . import views

app_name = 'film'
urlpatterns = [
    path('', views.index),
    path('genre/<int:genre_id>/', views.get_genre, name = 'get_genre'),
    path('film/<int:film_id>/', views.get_film, name = 'get_film'),
    path('films_by_search/', views.search, name = 'films_by_search'),
    path('liked_films/<int:film_id>', views.liked_films, name = 'liked_films'),
    path('create_film/', views.create_film, name = 'create_film'),
    path('register/', views.user_register, name = 'register'),
    path('profile/', views.user_profile, name = 'profile'),
    path('login/', views.user_login, name = 'login'),
    path('logout/', views.user_logout, name = 'logout'),
]
