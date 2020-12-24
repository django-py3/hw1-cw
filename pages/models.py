from django.db import models
from django.urls import reverse

# Create your models here.
class Pages(models.Model):
    title = models.CharField(max_length=250)
    pagebody = models.TextField()
    author = models.ForeignKey(
        'users.RegularUser', # дефолтынй пользователь из django.contrib.auth
        on_delete = models.CASCADE,
    )

    def __str__(self):
        return self.title 
    
    def get_absolute_url(self):
        """
        Хотим перенаправлять на ```DetailView``` данного поста
        """
        return reverse("detail_page", args=[str(self.id)])
