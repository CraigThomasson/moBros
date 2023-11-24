from django.db import models


# Create your models here.


# exercise types
# Physical path
# Welness path
# Happiness path (hobbies etc)

# exercise categories

class Categories(models.Model):
    name = models.CharField()

    def __str__(self):
        return self.name
