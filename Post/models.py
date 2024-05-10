from django.db import models
from Categories.models import Categories
from Author.models import Author
# Create your models here.
class Post(models.Model):
    title=models.CharField(max_length=300)
    content=models.TextField()
    categories=models.ManyToManyField(Categories)
    Author=models.OneToOneField(Author,on_delete=models.CASCADE)
    def __str__(self):
         return f"{self.Author.name} - {self.title}"