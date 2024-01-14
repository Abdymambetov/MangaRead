from django.contrib import admin
from .models import Genre, Review, Manga
# Register your models here.

admin.site.register(Manga)
admin.site.register(Genre)
admin.site.register(Review)