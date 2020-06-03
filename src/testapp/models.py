from django.db import models

# Create your models here.

class Genre(models.Model):
    # pk PK + autoincrement not null
    name = models.CharField(
        verbose_name="Название Жанра",
        max_length=100,   
    )
    description = models.TextField(
        verbose_name="Описание Жанра",
        null=True,
        blank=True
    )
    
    def __str__(self):
        return self.name