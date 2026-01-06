from django.db import models
from django.contrib.auth.models import User

class Articles(models.Model):
    title = models.CharField('Name',max_length=50)
    anons = models.CharField('Anons',max_length=250)
    full_text= models.TextField('Article')
    date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="articles",
    )

    def __str__(self):
        return f'Article: {self.title}'
    
    def get_absolute_url (self):
        return f'/article/{self.id}'
    
    class Meta:
        verbose_name = 'Article'
        verbose_name_plural = 'Articles'