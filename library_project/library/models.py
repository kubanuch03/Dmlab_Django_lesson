from django.db import models

from author.models import Author


class Janr(models.Model):
    title = models.CharField("Название жанра", max_length=70)

    def __str__(self):
        return self.title


class Book(models.Model):
    title = models.CharField("Назвние книги", max_length=70)
    description = models.TextField("Описание книги")
    image = models.ImageField("Картинка", upload_to="books", )
    publisher = models.CharField("Издание", max_length=70)
    janr = models.ForeignKey(Janr, on_delete=models.SET_NULL, null=True,
                             related_name="book_janr", verbose_name="Жанр")
    author = models.ForeignKey(Author, on_delete=models.CASCADE,
                               related_name="book_author", verbose_name="Автор")
    isdn = models.CharField(max_length=13, unique=True,
                            verbose_name="Идентификатор книги")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
