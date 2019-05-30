from django.db import models


class SushiTopping(models.Model):
    """ タコ、サワラ、シメサバなどの具材"""
    name = models.CharField(max_length=255)


class Menu(models.Model):
    """お品書き"""
    name = models.CharField(max_length=255, unique=True)
    price = models.IntegerField(default=0)
    sushi_toppings = models.ManyToManyField(SushiTopping)


class Sale(models.Model):
    sales_date = models.DateTimeField()
    menu = models.ForeignKey(Menu, on_delete=models.PROTECT)
