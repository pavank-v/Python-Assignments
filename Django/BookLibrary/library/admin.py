from django.contrib import admin
from .models import Book, SearchHistory, Users

admin.site.register(SearchHistory)
admin.site.register(Book)
admin.site.register(Users)