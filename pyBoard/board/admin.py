from django.contrib import admin

# Register your models here.
from .models import Author,Owner,Book
admin.site.register(Author)
admin.site.register(Owner)
admin.site.register(Book)