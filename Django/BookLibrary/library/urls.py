from django.urls import path
from . import views

urlpatterns = [
    path('', views.base, name='home'),
    path('search/',views.search_books, name='search'),
    path('favourites/', views.favourites, name='favourites'),
    path('search_history/', views.search_history, name='search_history'),
    path('add_to_favorites/', views.add_to_favorites, name='add_to_favorites'),
    path('signup', views.signup, name="signup"),
    path('signin', views.signin, name="signin"),
    path('success', views.success, name="success"),
    path('signout', views.signout, name="signout"),


]