from django.db import models
from datetime import datetime

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=150)
    desc = models.TextField()
    pub_date = models.DateField(default=datetime.now())


    def __str__(self):
        return self.title
