from django.db import models

# Create your models here.
class PhoneType(models.Model):
    name = models.CharField(
         verbose_name="Phone Type",
         max_length=10,
    )

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return '/catalogs/list-phone-type/'