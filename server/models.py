from django.db import models


class Products(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    price = models.IntegerField(default=0)

    def __str__(self) -> str:
        return self.name
