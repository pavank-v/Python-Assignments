from django.contrib import admin
from .models import Book, SearchHistory

admin.site.register(SearchHistory)
admin.site.register(Book)