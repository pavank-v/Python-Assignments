from django.urls import path
from .import views

urlpatterns = [
    path('', views.Base.as_view(), name='home'),
    path('search/',views.SearchBooks.as_view(), name='search'),
    path('favorites/', views.Favorites.as_view(), name='favorites'),
    path('search_history/', views.History.as_view(), name='search_history'),
    path('add_to_favorites/', views.AddToFavorite.as_view(), name='add_to_favorites'),
]