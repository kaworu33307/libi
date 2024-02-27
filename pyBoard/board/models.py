from django.db import models

class Author(models.Model):
    firstAuthorName = models.CharField(verbose_name="Имя автора", max_length=250)
    lastAuthorName = models.CharField(verbose_name="Фамилия автора", max_length=250)
    def __str__(self):
        return self.lastAuthorName
class Owner(models.Model):
      firstOwnerName = models.CharField(verbose_name="Имя владельца", max_length=250)
      lastOwnerName = models.CharField(verbose_name="Фамилия владельца", max_length=250)

      def __str__(self):
          return self.lastOwnerName
class Book(models.Model):
    title = models.CharField(verbose_name="Название книги", max_length=250)
    description = models.TextField(verbose_name="Описание книги")
    author = models.ForeignKey(Author, verbose_name="Автор книги", on_delete=models.CASCADE, related_name='Author')
    owner = models.ForeignKey(Owner, verbose_name="Владелец книги", on_delete=models.CASCADE, related_name='Owner')
    publishingDate = models.DateField(auto_now_add=True)
    def __str__(self):
        return self.title