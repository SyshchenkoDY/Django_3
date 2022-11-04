from django.db import models


class Phone(models.Model):
    # TODO: Добавьте требуемые поля
    objects = None
    name = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.CharField(max_length=1000)
    release_date = models.DateField(auto_now_add=False, auto_now=False)
    lte_exist = models.BooleanField()
    slug = models.CharField(max_length=50)
