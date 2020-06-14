from django.db import models

class Phone(models.Model):
    number = models.CharField(
         verbose_name="Phone",
         max_length=20,
    )
    # contact - User
    # type - Catalog
    def __str__(self):
        return self.number

