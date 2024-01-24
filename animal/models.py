# models.py

from django.db import models
from .utils import get_subclass_name_list


class Animal(models.Model):

    name = models.CharField(max_length=101)

    class_name = models.CharField(max_length=101, choices=[], default='')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Dynamically update choices in case subclasses are added or removed
        self._meta.get_field('class_name').choices = get_subclass_name_list(self.__class__)

    def get_subclass_instance(self):
        subclass_name = self.class_name
        if subclass_name:
            subclass = next((sub for sub in self.__class__.__subclasses__() if sub.__name__ == subclass_name), None)
            if subclass:
                return subclass.objects.get(id=self.id)
        return None


class Cat(Animal):

    CLASS_NAME = 'Cat'

    class Meta:
        proxy = True
    
    def sound_verb(self):
        return "miauler"


class Dog(Animal):

    CLASS_NAME = 'Dog'

    class Meta:
        proxy = True

    def sound_verb(self):
        return "aboyer"