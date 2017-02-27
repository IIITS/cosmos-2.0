from django.contrib import admin

# Register your models here.
from .models import Room,time,books

admin.site.register(Room)
admin.site.register(time)
admin.site.register(books)
