from django.db import models

# Create your models here.

class Parsing(models.Model):
    # pk PK + autoincrement not null
    name = models.CharField(
        verbose_name="Название браузера",
        max_length=100,   
    )
    requests17 = models.TextField(
        verbose_name="Запросов 17 мая",
        null=True,
        blank=True
    )
    requests18 = models.TextField(
        verbose_name="Запросов 18 мая",
        null=True,
        blank=True
    )
    requests19 = models.TextField(
        verbose_name="Запросов 19 мая",
        null=True,
        blank=True
    )
    
    requests20 = models.TextField(
        verbose_name="Запросов 20 мая",
        null=True,
        blank=True
    )

    def __str__(self):
        return self.name
