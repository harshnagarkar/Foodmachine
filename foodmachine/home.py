from django.db import models
from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from django.contrib.auth import views
from .views import home


class Cuisines(models.Model):
    name = models.CharField(max_length=100)
    tagline = models.TextField()

    def __str__(self):
        return self.name


class Dishes(models.Model):
    Cuisines = models.ForeignKey(Cuisines, on_delete=models.CASCADE)
    headline = models.CharField(max_length=255)
    body_text = models.TextField()
    rating = models.IntegerField()

    def __str__(self):
        return self.headline
