from django.db import models

# Create your models here.

class Books(models.Model):

    title = models.CharField(max_length=20)
    body = models.TextField()
    author = models.CharField(max_length=50)
    pages = models.IntegerField()
    year = models.DateField()
    
    class Meta:
        verbose_name = 'Book'
        verbose_name_plural = 'Books'

    def __str__(self):

        name = self.title
        return name 
    

        return super().__str__()