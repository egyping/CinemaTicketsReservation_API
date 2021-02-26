from django.contrib import admin
from .models import Movie, Guest, Reservation

admin.site.register(Movie)
admin.site.register(Guest)
admin.site.register(Reservation)
