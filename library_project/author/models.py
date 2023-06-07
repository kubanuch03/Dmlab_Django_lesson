from django.db import models


class Author(models.Model):
    full_name = models.CharField(verbose_name="ФИО автора", max_length=100)
    biography = models.TextField(verbose_name="Автобиография")

    def __str__(self):
        return self.full_name