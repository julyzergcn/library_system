from django.db import models

# Create your models here.
class Book(models.Model):
    book_name = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=5,decimal_places=2)
    publisher = models.ForeignKey(to="Publisher",on_delete=models.CASCADE,related_name="book")
    author = models.ManyToManyField(to="Author",related_name="book")

    class Meta:
        db_table = 'tb_book'
        verbose_name = 'book'
        verbose_name_plural = 'books'
        ordering = ['price']

    def __str__(self):
        return f"{self.book_name}"  


class Author(models.Model):
    author_name = models.CharField(max_length=30)
    age = models.IntegerField()
    gender = models.BooleanField()

    class Meta:
        db_table = 'book_author'
        verbose_name = 'author'
        verbose_name_plural = 'authors'

    def __str__(self):
        return f"{self.author_name}" 


class Publisher(models.Model):
    pub_name = models.CharField(max_length=30,unique=True)

    class Meta:
        db_table = 'book_publisher' 
        verbose_name = 'publisher' 
        verbose_name_plural = 'publishers'

    def __str__(self):
        return f"{self.pub_name}"
