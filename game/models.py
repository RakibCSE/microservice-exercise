from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=60, unique=True)

    def __str__(self):
        return self.name


class Game(models.Model):
    name = models.CharField(max_length=60)
    image = models.ImageField(upload_to="image/")
    category = models.ForeignKey(
        Category, related_name="category", on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.name
