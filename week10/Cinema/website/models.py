# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin sqlcustom [app_label]'
# into your database.
from __future__ import unicode_literals

from django.db import models


class Movie(models.Model):
    rating = models.FloatField(blank=True, null=True)
    name = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

    def get_name(self):
        return self.__str__().replace(" ","_")

    def __repr__(self):
        return self.__str__().replace(" ", "_")

    class Meta:
        db_table = 'Movies'


class Projection(models.Model):
    movie = models.ForeignKey(Movie, blank=True, null=True)
    type_field = models.TextField(blank=True, null=True)
    date = models.DateField(blank=True, null=True)
    time = models.TimeField(blank=True, null=True)

    def get_movie_name(self):
        return str(self.movie).replace(" ", "_")

    def __str__(self):
        return str(self.movie)

    def __repr__(self):
        return self.__str__()

    class Meta:
        db_table = 'Projections'


class Reservation(models.Model):
    username = models.TextField(blank=True, null=True)
    projection = models.ForeignKey(Projection, blank=True, null=True)
    seat = models.IntegerField(blank=True, null=True)

    class Meta:
        db_table = 'Reservations'
