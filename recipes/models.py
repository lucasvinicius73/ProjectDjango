from django.db import models


# Create your models here.
class Recipe(models.Model):
    title = models.CharField(max_length =65)
    description = models.CharField(max_length=165)
    slug = models.SlugField()
    preparation_time = models.IntegerField()
    preparation_unit = models.CharField()
    servings = models.IntegerField()
    servings_unit = models.CharField(max_length=65)
    preparation_steps = models.TextField()
    preparation_steps_is_html = models.BooleanField(default=False)
    created_at = models.DateField(auto_now_add=True) #Ele pega a data atual e não muda mais
    updated_at = models.DateField(auto_now=False) #Ele vai atualizando a data sempre que é chamado
    is_published = models.BooleanField(default=False)
    cover = models.ImageField(upload_to='recipes/covers/%Y/%m/%d/')
    