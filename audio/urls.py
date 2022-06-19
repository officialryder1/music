from unicodedata import name
from django.urls import path
from .views import home, list, search, like_post, login_user, logout_user, register_user, create_music, CategoryView, CountryView, detail

urlpatterns = [
    path('', home, name='home'),
    path('detail/<int:pk>/', detail, name='detail'),
    path('search', search, name='search'),
    path('song_list', list, name='list'),
    path('like/<int:pk>', like_post, name='like' ),
    path('login_user', login_user, name='login'),
    path('logout_user', logout_user, name='logout'),
    path('register_user', register_user, name='register'),
    path('upload', create_music, name='upload'),
    path('category/<str:cats>/', CategoryView, name='categories'),
    path('country/<str:cats>/', CountryView, name='country')
]
