from django.db import models

class Articles(models.Model):
    title = models.CharField('Name',max_length=50)
    anons = models.CharField('Anons',max_length=250)
    full_text= models.TextField('Article')
    date = models.DateTimeField('Date of publication')

    def __str__(self):
        return f'Newapp: {self.title}'
    
    def get_absolute_url (self):
        return f'/newapp/{self.id}'
    
    class Meta:
        verbose_name = 'New App'
        verbose_name_plural = 'New Apps'