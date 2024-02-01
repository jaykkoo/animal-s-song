# models.py

from django.db import models
from .utils import get_subclass_name_list


class Animal(models.Model):

    name = models.CharField(max_length=101)
    file_sound = models.FileField(upload_to='sounds/', null=True, blank=True)
    picture = models.ImageField(upload_to='images/', null=True, blank=True)
    verb = models.CharField(max_length=101, default='')

    def __str__(self):
        return self.name
