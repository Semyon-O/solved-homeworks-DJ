from django.db import models


class Phone(models.Model):
    # id
    name = models.CharField(max_length=50)
    image = models.URLField()
    price = models.FloatField()
    release_date = models.DateField()
    lte_exists = models.BooleanField()

    slug = models.SlugField(null=True)
