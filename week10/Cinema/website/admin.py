from django.contrib import admin
from .models import Movie, Projection, Reservation
from register.models import UserProfile

admin.site.register(Movie)
admin.site.register(Projection)
admin.site.register(Reservation)
admin.site.register(UserProfile)
