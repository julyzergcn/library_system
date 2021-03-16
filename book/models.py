from django.db import models
from django.utils.translation import gettext_lazy as _


class Book(models.Model):
    book_name = models.CharField(_("Book Name"), max_length=50)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    publisher = models.ForeignKey("Publisher", on_delete=models.CASCADE, related_name="books")
    author = models.ManyToManyField("Author", related_name="books")
    is_deleted = models.BooleanField(default=False)

    class Meta:
        db_table = 'tb_book'
        verbose_name = _('Book')
        verbose_name_plural = _('Books')
        ordering = ['price']

    def __str__(self):
        return f"{self.book_name}"  


class Author(models.Model):
    author_name = models.CharField(max_length=30)
    age = models.IntegerField()
    gender = models.BooleanField()

    class Meta:
        db_table = 'book_author'
        verbose_name = _('Author')
        verbose_name_plural = _('Authors')

    def __str__(self):
        return f"{self.author_name}" 


class Publisher(models.Model):
    pub_name = models.CharField(max_length=30, unique=True)

    class Meta:
        db_table = 'book_publisher'
        verbose_name = _('Publisher')
        verbose_name_plural = _('Publishers')

    def __str__(self):
        return f"{self.pub_name}"
