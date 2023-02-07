from django.db import models


class Phone(models.Model):
    name = models.CharField(max_length= 50, null=False)
    price = models.CharField(max_length=50)
    image = models.FileField()
    release_date = models.DateField()
    lte_exists = models.BooleanField(default=False)
    slug = models.SlugField(max_length = 200, unique=True, db_index=True)
